"""Fetch GitHub metrics for curated repos → Turso database + README + CSV.

Reads ``data/repos.json`` and ``data/categories.json``, fetches metrics via
the GitHub GraphQL API (batches of 50 repos per request), then:

  • Upserts daily snapshots into Turso (always)
  • Refreshes the README table between <!-- BEGIN_TABLE --> markers (always)
  • Writes a timestamped CSV to outputs/ (local runs only — skipped in CI)

Environment variables:
  STATS_GH_PAT or GITHUB_TOKEN or GITHUB_API_TOKEN
  TURSO_DATABASE_URL   — libsql://... URL from Turso dashboard
  TURSO_AUTH_TOKEN     — Turso auth token
"""

import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timezone
from typing import Dict, List, Optional

import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from tabulate import tabulate
from urllib3.util.retry import Retry

GRAPHQL_URL = "https://api.github.com/graphql"
BATCH_SIZE = 50

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
CONFIG_FILE = os.path.join(DATA_DIR, "repos.json")
TAXONOMY_FILE = os.path.join(DATA_DIR, "categories.json")
README_FILE = os.path.join(REPO_ROOT, "README.md")
OUTPUT_DIR = os.path.join(REPO_ROOT, "outputs")

# README table filters
MIN_STARS = 100
MAX_DAYS_SINCE_COMMIT = 60
README_TOP_N = 100

FULL_COLUMNS = [
    "Owner", "Repository Name", "Categories", "Tags", "Platforms",
    "GPU Backends", "About", "Stars", "Forks", "Issues", "Contributors",
    "Releases", "Watchers", "Time Since Last Commit", "License", "Languages", "URL",
]

README_COLUMNS = [
    "#", "Repo", "Tags", "About", "Stars", "Forks", "Issues",
    "Contributors", "Releases", "License", "Time Since Last Commit",
]

REPO_FIELDS = """{
  stargazerCount
  forkCount
  description
  pushedAt
  isArchived
  owner { __typename }
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
        self.base_url = url.replace("libsql://", "https://").rstrip("/")
        self._headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def _pipeline(self, stmts: list) -> list:
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

    def executemany(self, statements: list) -> list:
        stmts = []
        for sql, args in statements:
            stmt: dict = {"sql": sql}
            if args:
                stmt["args"] = [_arg(a) for a in args]
            stmts.append(stmt)
        return self._pipeline(stmts)


_INIT_REPO_SQL = """
INSERT INTO repos (full_name, owner, name, url, tags, platforms, backends)
VALUES (?, ?, ?, ?, ?, ?, ?)
ON CONFLICT(full_name) DO UPDATE SET
  tags      = excluded.tags,
  platforms = excluded.platforms,
  backends  = excluded.backends
"""

_UPDATE_DESC_SQL = "UPDATE repos SET description = ? WHERE full_name = ?"
_UPDATE_OWNER_TYPE_SQL = "UPDATE repos SET owner_type = ? WHERE full_name = ?"

_UPSERT_SNAPSHOT_SQL = """
INSERT INTO snapshots
  (repo_id, scraped_date, stars, forks, issues, releases,
   watchers, days_since_commit, license, primary_language, contributors)
SELECT id, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
FROM   repos WHERE full_name = ?
ON CONFLICT(repo_id, scraped_date) DO UPDATE SET
  stars             = excluded.stars,
  forks             = excluded.forks,
  issues            = excluded.issues,
  releases          = excluded.releases,
  watchers          = excluded.watchers,
  days_since_commit = excluded.days_since_commit,
  license           = excluded.license,
  primary_language  = excluded.primary_language,
  contributors      = excluded.contributors
"""


def _flush(db: TursoClient, stmts: list) -> list:
    if stmts:
        db.executemany(stmts)
    return []


def init_repos(db: TursoClient, entries: List[Dict]) -> None:
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
    print(f"Initialised {len(entries)} repos in Turso")


def write_snapshots_to_db(
    db: TursoClient,
    df: pd.DataFrame,
    contributor_counts: Dict[str, int],
) -> None:
    today = date.today().isoformat()
    desc_stmts, snap_stmts = [], []

    for _, row in df.iterrows():
        full_name = f"{row['Owner']}/{row['Repository Name']}"
        description = row.get("About")
        if description == "No description available":
            description = None
        license_val = row.get("License")
        if license_val == "No license":
            license_val = None

        desc_stmts.append((_UPDATE_DESC_SQL, [description, full_name]))
        owner_type = row.get("owner_type")
        if owner_type:
            desc_stmts.append((_UPDATE_OWNER_TYPE_SQL, [owner_type, full_name]))
        snap_stmts.append((_UPSERT_SNAPSHOT_SQL, [
            today,
            int(row["Stars"]), int(row["Forks"]), int(row["Issues"]),
            int(row.get("Releases", 0)),
            int(row.get("Watchers", 0)),
            int(row["_days"]),
            license_val,
            row.get("Languages") or None,
            contributor_counts.get(full_name),
            full_name,
        ]))

        if len(snap_stmts) >= 50:
            _flush(db, desc_stmts)
            _flush(db, snap_stmts)
            desc_stmts, snap_stmts = [], []

    _flush(db, desc_stmts)
    _flush(db, snap_stmts)
    print(f"Wrote {len(df)} snapshots to Turso")


# ---------------------------------------------------------------------------
# Contributor counts (REST API — cheap, one call per repo)
# ---------------------------------------------------------------------------

def _fetch_one_contributor_count(
    session: requests.Session,
    full_name: str,
) -> tuple[str, Optional[int]]:
    try:
        resp = session.get(
            f"https://api.github.com/repos/{full_name}/contributors",
            params={"per_page": 1, "anon": 1},
            timeout=15,
        )
        # Sleep if rate limit is low
        remaining = int(resp.headers.get("X-RateLimit-Remaining", 1000))
        if remaining < 100:
            reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
            wait = max(0, reset - time.time()) + 5
            print(f"  Rate limit low ({remaining}) — sleeping {wait:.0f}s")
            time.sleep(wait)

        if resp.status_code in (204, 404):
            return full_name, 0
        if not resp.ok:
            return full_name, None

        link = resp.headers.get("Link", "")
        m = re.search(r'[?&]page=(\d+)>;\s*rel="last"', link)
        if m:
            return full_name, int(m.group(1))
        body = resp.json()
        return full_name, len(body) if isinstance(body, list) else 0
    except Exception as exc:
        print(f"  contributor error {full_name}: {exc}")
        return full_name, None


def fetch_all_contributor_counts(
    session: requests.Session,
    full_names: List[str],
    workers: int = 4,
) -> Dict[str, int]:
    print(f"\nFetching contributor counts for {len(full_names)} repos ({workers} workers)...")
    counts: Dict[str, int] = {}
    done = 0
    total = len(full_names)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(_fetch_one_contributor_count, session, fn): fn
            for fn in full_names
        }
        for fut in as_completed(futures):
            fn, count = fut.result()
            if count is not None:
                counts[fn] = count
            done += 1
            if done % 200 == 0 or done == total:
                print(f"  {done}/{total} contributor counts fetched")

    print(f"  Done — got counts for {len(counts)}/{total} repos")
    return counts


# ---------------------------------------------------------------------------
# Config / auth
# ---------------------------------------------------------------------------

def load_taxonomy() -> Dict[str, Dict[str, str]]:
    with open(TAXONOMY_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    lookup: Dict[str, Dict[str, str]] = {}
    for cat in data:
        for sub in cat["subcategories"]:
            lookup[sub["slug"]] = {"name": sub["name"], "category": cat["category"]}
    return lookup


def get_token() -> str:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass
    token = (
        os.getenv("STATS_GH_PAT")
        or os.getenv("GITHUB_TOKEN")
        or os.getenv("GITHUB_API_TOKEN")
    )
    if not token:
        sys.exit(
            "Error: no GitHub token found. Set STATS_GH_PAT / GITHUB_TOKEN / "
            "GITHUB_API_TOKEN in your environment or .env file."
        )
    return token


def make_session(token: str) -> requests.Session:
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    })
    retry = Retry(
        total=3,
        backoff_factor=2,
        backoff_max=5,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["POST"],
        respect_retry_after_header=True,
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session


def _post(session: requests.Session, query: str) -> Optional[requests.Response]:
    """POST a GraphQL query. Returns None on failure so the caller can queue a retry."""
    try:
        return session.post(GRAPHQL_URL, json={"query": query}, timeout=30)
    except requests.exceptions.RequestException as exc:
        print(f"  API error (will retry later): {exc}")
        return None


# ---------------------------------------------------------------------------
# GraphQL helpers
# ---------------------------------------------------------------------------

def build_query(batch: List[Dict]) -> str:
    parts = []
    for i, entry in enumerate(batch):
        owner, name = entry["repo"].split("/", 1)
        owner = owner.replace('"', "")
        name = name.replace('"', "")
        parts.append(f'  r{i}: repository(owner: "{owner}", name: "{name}") {REPO_FIELDS}')
    return "query {\n" + "\n".join(parts) + "\n}"


def fetch_batch(
    session: requests.Session,
    batch: List[Dict],
    taxonomy: Dict[str, Dict[str, str]],
) -> Optional[List[Dict]]:
    """Returns a list of rows on success, or None if the API was unreachable."""
    query = build_query(batch)
    resp = _post(session, query)
    if resp is None:
        return None

    if resp.status_code in (403, 429):
        reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
        wait = max(0, reset - time.time()) + 5
        print(f"  Rate limited — sleeping {wait:.0f}s")
        time.sleep(wait)
        resp = _post(session, query)
        if resp is None:
            return None

    if not resp.ok:
        print(f"  HTTP {resp.status_code} — queuing for retry")
        return None

    try:
        payload = resp.json()
    except requests.exceptions.JSONDecodeError:
        print(f"  Empty/invalid JSON response (status {resp.status_code}) — queuing for retry")
        return None
    for err in payload.get("errors", []):
        print(f"  GraphQL error: {err.get('message', err)}")

    data = payload.get("data") or {}
    rows = []

    for i, entry in enumerate(batch):
        node = data.get(f"r{i}")
        if node is None:
            print(f"  skip: {entry['repo']} — null (private/deleted/renamed?)")
            continue

        repo = entry["repo"]
        slugs: List[str] = entry.get("tags", [])
        tag_names = [taxonomy[s]["name"] for s in slugs if s in taxonomy]
        cat_names = list(dict.fromkeys(
            taxonomy[s]["category"] for s in slugs if s in taxonomy
        ))
        platforms: List[str] = entry.get("platforms", [])
        backends: List[str] = entry.get("backends", [])

        pushed = node.get("pushedAt") or ""
        days = hours = minutes = 0
        if pushed:
            dt = datetime.strptime(pushed, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            delta = datetime.now(timezone.utc) - dt
            days, rem = divmod(delta.total_seconds(), 86400)
            hours, rem = divmod(rem, 3600)
            minutes, _ = divmod(rem, 60)

        row = {
            "Owner": repo.split("/")[0],
            "Repository Name": repo.split("/")[1],
            "owner_type": (node.get("owner") or {}).get("__typename"),
            "Categories": ", ".join(cat_names),
            "Tags": ", ".join(tag_names),
            "Platforms": ", ".join(platforms),
            "GPU Backends": ", ".join(backends),
            "About": node.get("description") or "No description available",
            "Stars": node.get("stargazerCount", 0),
            "Forks": node.get("forkCount", 0),
            "Issues": (node.get("openIssues") or {}).get("totalCount", 0),
            "Contributors": 0,
            "Releases": (node.get("releases") or {}).get("totalCount", 0),
            "Watchers": (node.get("watchers") or {}).get("totalCount", 0),
            "Time Since Last Commit": (
                f"{int(days)} days, {int(hours)} hrs, {int(minutes)} mins"
            ),
            "License": (node.get("licenseInfo") or {}).get("name") or "No license",
            "Languages": (node.get("primaryLanguage") or {}).get("name") or "",
            "URL": f"https://github.com/{repo}",
            "_stars": node.get("stargazerCount", 0),
            "_days": int(days),
        }
        print(f"  ok: {repo} ({row['Stars']:,} ★)")
        rows.append(row)

    remaining = int(resp.headers.get("X-RateLimit-Remaining", 100))
    if remaining < 20:
        reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
        wait = max(0, reset - time.time()) + 5
        print(f"  Rate limit low ({remaining} left) — sleeping {wait:.0f}s")
        time.sleep(wait)

    return rows


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def fetch_all(
    session: requests.Session,
    entries: List[Dict],
    taxonomy: Dict[str, Dict[str, str]],
) -> pd.DataFrame:
    # Reverse so low-star repos are processed first; high-star repos land at the
    # end and benefit from any mid-run recovery from GitHub 502 storms.
    ordered = list(reversed(entries))
    batches = [ordered[i: i + BATCH_SIZE] for i in range(0, len(ordered), BATCH_SIZE)]
    total = len(batches)
    rows: List[Dict] = []
    failed: List[List[Dict]] = []

    for idx, batch in enumerate(batches, 1):
        names = ", ".join(e["repo"].split("/")[1] for e in batch[:3])
        suffix = "..." if len(batch) > 3 else ""
        print(f"\n[Batch {idx}/{total}] {names}{suffix}")
        result = fetch_batch(session, batch, taxonomy)
        if result is None:
            failed.append(batch)
        else:
            rows.extend(result)
        if idx < total:
            time.sleep(0.5)

    for attempt in range(1, 3):
        if not failed:
            break
        print(f"\n{len(failed)} batch(es) failed — waiting 5 min then retrying (attempt {attempt}/2)...")
        time.sleep(300)
        still_failed = []
        for batch in failed:
            names = ", ".join(e["repo"].split("/")[1] for e in batch[:3])
            print(f"\n[Retry {attempt}] {names}...")
            result = fetch_batch(session, batch, taxonomy)
            if result is None:
                still_failed.append(batch)
                print(f"  Still failing")
            else:
                rows.extend(result)
            time.sleep(0.5)
        failed = still_failed

    if failed:
        # Retry each repo individually so transient 502s don't strand an
        # entire batch — only truly broken repos end up skipped.
        individual_failed: List[Dict] = [e for batch in failed for e in batch]
        print(f"\n{len(individual_failed)} repos from failed batches — retrying individually...")
        still_individual_failed: List[Dict] = []
        for entry in individual_failed:
            result = fetch_batch(session, [entry], taxonomy)
            if result is None:
                print(f"  permanently skipped: {entry['repo']}")
                still_individual_failed.append(entry)
            else:
                rows.extend(result)
            time.sleep(0.5)
        if still_individual_failed:
            print(f"  {len(still_individual_failed)} repo(s) permanently skipped after individual retry")

    if not rows:
        sys.exit("Error: no repository data fetched.")

    df = pd.DataFrame(rows).drop_duplicates(subset=["URL"])
    df = df.sort_values(by="_stars", ascending=False).reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def format_numbers(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in ["Stars", "Forks", "Issues", "Contributors", "Releases", "Watchers"]:
        df[col] = df[col].apply(lambda x: f"{int(x):,}")
    return df


def write_csv(df: pd.DataFrame) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    path = os.path.join(OUTPUT_DIR, f"{stamp}_repo_stats.csv")
    df[FULL_COLUMNS].to_csv(path, index=False)
    print(f"Wrote {path}")
    return path


def build_markdown_table(df: pd.DataFrame) -> str:
    table = df[(df["_stars"] > MIN_STARS) & (df["_days"] <= MAX_DAYS_SINCE_COMMIT)].copy()
    table = table.head(README_TOP_N).reset_index(drop=True)
    table["#"] = table.index + 1
    table["Repo"] = table.apply(
        lambda r: f'[{r["Repository Name"]}]({r["URL"]})', axis=1
    )
    table = format_numbers(table)[README_COLUMNS]
    md = tabulate(table, headers="keys", tablefmt="github", showindex=False)
    md = re.sub(r" {3,}", "  ", md)
    md = re.sub(r"-{4,}", "----------", md)
    return md


def update_readme(markdown_table: str) -> None:
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    today = datetime.now().strftime("%d/%m/%Y")
    content = re.sub(
        r"\*Last Updated:.*?\*",
        f"*Last Updated: {today}*",
        content,
        count=1,
    )

    block = f"<!-- BEGIN_TABLE -->\n{markdown_table}\n<!-- END_TABLE -->"
    if "<!-- BEGIN_TABLE -->" not in content:
        sys.exit(
            "Error: README.md is missing the <!-- BEGIN_TABLE --> / "
            "<!-- END_TABLE --> markers."
        )
    content = re.sub(
        r"<!-- BEGIN_TABLE -->.*?<!-- END_TABLE -->",
        block,
        content,
        flags=re.DOTALL,
    )

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {README_FILE}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    start = time.time()
    token = get_token()
    session = make_session(token)

    turso_url = os.getenv("TURSO_DATABASE_URL")
    turso_token = os.getenv("TURSO_AUTH_TOKEN")
    use_db = bool(turso_url and turso_token)
    db = TursoClient(turso_url, turso_token) if use_db else None  # type: ignore[arg-type]
    if not use_db:
        print("Warning: TURSO_DATABASE_URL / TURSO_AUTH_TOKEN not set — skipping DB writes")

    taxonomy = load_taxonomy()

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        entries = json.load(f)

    print(f"Fetching {len(entries)} repos in batches of {BATCH_SIZE} "
          f"({-(-len(entries) // BATCH_SIZE)} GraphQL requests)...")

    df = fetch_all(session, entries, taxonomy)

    contributor_counts = fetch_all_contributor_counts(
        session, [e["repo"] for e in entries]
    )

    if db:
        init_repos(db, entries)
        write_snapshots_to_db(db, df, contributor_counts)

    # Skip CSV in CI — it's gitignored and not useful in the action runner
    if not os.getenv("CI"):
        write_csv(df)

    # README update: weekly in CI (controlled by UPDATE_README env var),
    # always when running locally
    if not os.getenv("CI") or os.getenv("UPDATE_README"):
        update_readme(build_markdown_table(df))
    else:
        print("Skipping README update (daily CI run)")

    mins, secs = divmod(time.time() - start, 60)
    print(f"\nDone: {len(df)} repos in {int(mins)}m {int(secs)}s")


if __name__ == "__main__":
    main()
