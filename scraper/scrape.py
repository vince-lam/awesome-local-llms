"""
GraphQL-based GitHub scraper → Turso database + CSV.

Batches up to 25 repos per GraphQL query (vs 4 REST calls per repo in the
legacy update_stats.py), upserts daily snapshots into Turso, and writes a
timestamped CSV for backwards-compatible README updates.

Environment variables:
  STATS_GH_PAT or GITHUB_TOKEN or GITHUB_API_TOKEN
  TURSO_DATABASE_URL   — libsql://... URL from Turso dashboard
  TURSO_AUTH_TOKEN     — Turso auth token
"""

import json
import os
import sys
import time
import csv
from datetime import date, datetime, timezone
from typing import Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

GRAPHQL_URL = "https://api.github.com/graphql"
BATCH_SIZE = 25

# This script lives in scraper/; data sits in scraper/data/ and CSV outputs
# live at the repo root (the parent directory).
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(REPO_ROOT, "outputs")
REPOS_FILE = os.path.join(DATA_DIR, "repos.json")

REPO_FIELDS = """{
  stargazerCount
  forkCount
  description
  pushedAt
  isArchived
  primaryLanguage { name }
  licenseInfo { name }
  openIssues: issues(states: OPEN) { totalCount }
  watchers { totalCount }
  releases { totalCount }
}"""


# ---------------------------------------------------------------------------
# Turso HTTP client
# ---------------------------------------------------------------------------

def _arg(v) -> dict:
    if v is None:
        return {"type": "null"}
    if isinstance(v, bool):
        return {"type": "integer", "value": str(int(v))}
    if isinstance(v, int):
        return {"type": "integer", "value": str(v)}
    if isinstance(v, float):
        return {"type": "float", "value": str(v)}
    return {"type": "text", "value": str(v)}


class TursoClient:
    def __init__(self, url: str, token: str) -> None:
        # Accept libsql:// or https://
        self.base_url = url.replace("libsql://", "https://").rstrip("/")
        self._headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def _pipeline(self, stmts: list[dict]) -> list[dict]:
        payload = {
            "requests": [{"type": "execute", "stmt": s} for s in stmts]
            + [{"type": "close"}]
        }
        r = requests.post(
            f"{self.base_url}/v2/pipeline",
            json=payload,
            headers=self._headers,
            timeout=30,
        )
        r.raise_for_status()
        results = r.json().get("results", [])
        for res in results:
            if res.get("type") == "error":
                raise RuntimeError(f"Turso: {res['error']['message']}")
        return results

    def execute(self, sql: str, args: Optional[list] = None) -> dict:
        stmt: dict = {"sql": sql}
        if args:
            stmt["args"] = [_arg(a) for a in args]
        return self._pipeline([stmt])[0]

    def executemany(self, statements: list[tuple[str, list]]) -> list[dict]:
        stmts = []
        for sql, args in statements:
            stmt: dict = {"sql": sql}
            if args:
                stmt["args"] = [_arg(a) for a in args]
            stmts.append(stmt)
        return self._pipeline(stmts)


# ---------------------------------------------------------------------------
# GitHub session
# ---------------------------------------------------------------------------

def make_session(token: str) -> requests.Session:
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    })
    retry = Retry(
        total=3,
        backoff_factor=2,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["POST"],
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session


# ---------------------------------------------------------------------------
# GraphQL helpers
# ---------------------------------------------------------------------------

def build_query(batch: list[dict]) -> str:
    parts = []
    for i, entry in enumerate(batch):
        owner, name = entry["repo"].split("/", 1)
        owner = owner.replace('"', "")
        name = name.replace('"', "")
        parts.append(f'  r{i}: repository(owner: "{owner}", name: "{name}") {REPO_FIELDS}')
    return "query {\n" + "\n".join(parts) + "\n}"


def fetch_batch(session: requests.Session, batch: list[dict]) -> list[dict]:
    query = build_query(batch)
    resp = session.post(GRAPHQL_URL, json={"query": query}, timeout=30)

    if resp.status_code in (403, 429):
        reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
        wait = max(0, reset - time.time()) + 5
        print(f"  Rate limited — sleeping {wait:.0f}s")
        time.sleep(wait)
        resp = session.post(GRAPHQL_URL, json={"query": query}, timeout=30)

    if not resp.ok:
        print(f"  HTTP {resp.status_code} — skipping batch")
        return []

    payload = resp.json()
    for err in payload.get("errors", []):
        print(f"  GraphQL error: {err.get('message', err)}")

    data = payload.get("data") or {}
    results = []

    for i, entry in enumerate(batch):
        node = data.get(f"r{i}")
        if node is None:
            print(f"  skip: {entry['repo']} — null (private/deleted/renamed?)")
            continue

        pushed = node.get("pushedAt") or ""
        days_since = None
        if pushed:
            dt = datetime.strptime(pushed, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            days_since = int((datetime.now(timezone.utc) - dt).total_seconds() / 86400)

        row = {
            "repo": entry["repo"],
            "tags": entry.get("tags", []),
            "platforms": entry.get("platforms", []),
            "backends": entry.get("backends", []),
            "description": node.get("description"),
            "stars": node.get("stargazerCount", 0),
            "forks": node.get("forkCount", 0),
            "issues": (node.get("openIssues") or {}).get("totalCount", 0),
            "watchers": (node.get("watchers") or {}).get("totalCount", 0),
            "releases": (node.get("releases") or {}).get("totalCount", 0),
            "days_since_commit": days_since,
            "license": (node.get("licenseInfo") or {}).get("name"),
            "primary_language": (node.get("primaryLanguage") or {}).get("name"),
            "is_archived": node.get("isArchived", False),
        }
        results.append(row)
        print(f"  ok: {entry['repo']} ({row['stars']:,} ★)")

    # Slow down if running low on rate limit budget
    remaining = int(resp.headers.get("X-RateLimit-Remaining", 100))
    if remaining < 20:
        reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
        wait = max(0, reset - time.time()) + 5
        print(f"  Rate limit low ({remaining} left) — sleeping {wait:.0f}s")
        time.sleep(wait)

    return results


# ---------------------------------------------------------------------------
# Database writes
# ---------------------------------------------------------------------------

_INIT_REPO_SQL = """
INSERT INTO repos (full_name, owner, name, url, tags, platforms, backends)
VALUES (?, ?, ?, ?, ?, ?, ?)
ON CONFLICT(full_name) DO UPDATE SET
  tags      = excluded.tags,
  platforms = excluded.platforms,
  backends  = excluded.backends
"""

_UPDATE_DESC_SQL = "UPDATE repos SET description = ? WHERE full_name = ?"

_UPSERT_SNAPSHOT_SQL = """
INSERT INTO snapshots
  (repo_id, scraped_date, stars, forks, issues, releases,
   watchers, days_since_commit, license, primary_language)
SELECT id, ?, ?, ?, ?, ?, ?, ?, ?, ?
FROM   repos WHERE full_name = ?
ON CONFLICT(repo_id, scraped_date) DO UPDATE SET
  stars             = excluded.stars,
  forks             = excluded.forks,
  issues            = excluded.issues,
  releases          = excluded.releases,
  watchers          = excluded.watchers,
  days_since_commit = excluded.days_since_commit,
  license           = excluded.license,
  primary_language  = excluded.primary_language
"""


def _flush(db: TursoClient, stmts: list) -> list:
    if stmts:
        db.executemany(stmts)
    return []


def init_repos(db: TursoClient, entries: list[dict]) -> None:
    """Ensure every repo from repos.json exists in the repos table."""
    stmts = []
    for e in entries:
        owner, name = e["repo"].split("/", 1)
        stmts.append((_INIT_REPO_SQL, [
            e["repo"], owner, name,
            f"https://github.com/{e['repo']}",
            json.dumps(e.get("tags", [])),
            json.dumps(e.get("platforms", [])),
            json.dumps(e.get("backends", [])),
        ]))
        if len(stmts) >= 50:
            stmts = _flush(db, stmts)
    _flush(db, stmts)
    print(f"Initialised {len(entries)} repos in repos table")


def write_batch_to_db(db: TursoClient, rows: list[dict]) -> None:
    today = date.today().isoformat()
    desc_stmts, snap_stmts = [], []

    for r in rows:
        desc_stmts.append((_UPDATE_DESC_SQL, [r.get("description"), r["repo"]]))
        snap_stmts.append((_UPSERT_SNAPSHOT_SQL, [
            today,
            r["stars"], r["forks"], r["issues"],
            r.get("releases"), r["watchers"],
            r.get("days_since_commit"), r.get("license"),
            r.get("primary_language"),
            r["repo"],
        ]))
        if len(snap_stmts) >= 50:
            _flush(db, desc_stmts)
            _flush(db, snap_stmts)
            desc_stmts, snap_stmts = [], []

    _flush(db, desc_stmts)
    _flush(db, snap_stmts)


# ---------------------------------------------------------------------------
# CSV output (keeps existing outputs/ convention)
# ---------------------------------------------------------------------------

_CSV_FIELDS = [
    "repo", "description", "stars", "forks", "issues", "watchers",
    "releases", "days_since_commit", "license", "primary_language",
    "tags", "platforms", "backends",
]


def write_csv(rows: list[dict]) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    path = os.path.join(OUTPUT_DIR, f"{stamp}_repo_stats.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=_CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in sorted(rows, key=lambda r: r["stars"], reverse=True):
            writer.writerow({
                **row,
                "tags": ", ".join(row.get("tags", [])),
                "platforms": ", ".join(row.get("platforms", [])),
                "backends": ", ".join(row.get("backends", [])),
            })
    print(f"Wrote {path}")
    return path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    start = time.time()

    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    gh_token = (
        os.getenv("STATS_GH_PAT")
        or os.getenv("GITHUB_TOKEN")
        or os.getenv("GITHUB_API_TOKEN")
    )
    if not gh_token:
        sys.exit("Error: set STATS_GH_PAT, GITHUB_TOKEN, or GITHUB_API_TOKEN")

    turso_url = os.getenv("TURSO_DATABASE_URL")
    turso_token = os.getenv("TURSO_AUTH_TOKEN")
    use_db = bool(turso_url and turso_token)
    if not use_db:
        print("Warning: TURSO_DATABASE_URL / TURSO_AUTH_TOKEN not set — skipping DB writes")

    with open(REPOS_FILE, encoding="utf-8") as f:
        entries = json.load(f)

    session = make_session(gh_token)
    db = TursoClient(turso_url, turso_token) if use_db else None  # type: ignore[arg-type]

    if db:
        init_repos(db, entries)

    batches = [entries[i : i + BATCH_SIZE] for i in range(0, len(entries), BATCH_SIZE)]
    all_rows: list[dict] = []

    for idx, batch in enumerate(batches, 1):
        print(f"\n[Batch {idx}/{len(batches)}] {', '.join(e['repo'].split('/')[1] for e in batch[:3])}{'...' if len(batch) > 3 else ''}")
        rows = fetch_batch(session, batch)
        all_rows.extend(rows)

        if db and rows:
            write_batch_to_db(db, rows)

        if idx < len(batches):
            time.sleep(0.5)

    write_csv(all_rows)

    mins, secs = divmod(time.time() - start, 60)
    print(f"\nDone: {len(all_rows)}/{len(entries)} repos in {int(mins)}m {int(secs)}s")


if __name__ == "__main__":
    main()
