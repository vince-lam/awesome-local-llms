"""Fetch GitHub metrics for the curated repos and refresh the README table.

Reads ``repos.json`` (a list of ``{repo, tags}`` entries) and
``categories.json`` (the tag taxonomy), pulls metrics from the GitHub GraphQL
API in batches of 25 repos per request, writes a timestamped CSV to
``outputs/`` and injects a filtered, sorted Markdown table into ``README.md``
between the ``<!-- BEGIN_TABLE -->`` / ``<!-- END_TABLE -->`` markers.
"""

import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from typing import Dict, List, Optional

import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from tabulate import tabulate
from urllib3.util.retry import Retry

GRAPHQL_URL = "https://api.github.com/graphql"
BATCH_SIZE = 50

# This script lives in scraper/; data sits in scraper/data/ and the README and
# CSV outputs live at the repo root (the parent directory).
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

# Full column order for the CSV.
FULL_COLUMNS = [
    "Owner",
    "Repository Name",
    "Categories",
    "Tags",
    "Platforms",
    "GPU Backends",
    "About",
    "Stars",
    "Forks",
    "Issues",
    "Contributors",
    "Releases",
    "Watchers",
    "Time Since Last Commit",
    "License",
    "Languages",
    "URL",
]

# Column order for the condensed README table.
README_COLUMNS = [
    "#",
    "Repo",
    "Tags",
    "About",
    "Stars",
    "Forks",
    "Issues",
    "Contributors",
    "Releases",
    "License",
    "Time Since Last Commit",
]

# GraphQL fragment fetched for every repo in a batch.
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
  mentionableUsers { totalCount }
}"""


# ---------------------------------------------------------------------------
# Config / auth
# ---------------------------------------------------------------------------

def load_taxonomy() -> Dict[str, Dict[str, str]]:
    """Return a slug→{name, category} mapping from categories.json."""
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
        total=5,
        backoff_factor=2,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["POST"],
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session


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
) -> List[Dict]:
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
            "Categories": ", ".join(cat_names),
            "Tags": ", ".join(tag_names),
            "Platforms": ", ".join(platforms),
            "GPU Backends": ", ".join(backends),
            "About": node.get("description") or "No description available",
            "Stars": node.get("stargazerCount", 0),
            "Forks": node.get("forkCount", 0),
            "Issues": (node.get("openIssues") or {}).get("totalCount", 0),
            "Contributors": (node.get("mentionableUsers") or {}).get("totalCount", 0),
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

    # Back off if running low on GraphQL point budget
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
    batches = [entries[i: i + BATCH_SIZE] for i in range(0, len(entries), BATCH_SIZE)]
    total = len(batches)
    rows: List[Dict] = []

    for idx, batch in enumerate(batches, 1):
        names = ", ".join(e["repo"].split("/")[1] for e in batch[:3])
        suffix = "..." if len(batch) > 3 else ""
        print(f"\n[Batch {idx}/{total}] {names}{suffix}")
        rows.extend(fetch_batch(session, batch, taxonomy))
        if idx < total:
            time.sleep(0.5)

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
    """Build the condensed Markdown table for the README (top N by stars)."""
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

    taxonomy = load_taxonomy()

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        entries = json.load(f)

    print(f"Fetching {len(entries)} repos in batches of {BATCH_SIZE} "
          f"({-(-len(entries) // BATCH_SIZE)} GraphQL requests)...")

    df = fetch_all(session, entries, taxonomy)
    csv_path = write_csv(df)
    update_readme(build_markdown_table(df))

    mins, secs = divmod(time.time() - start, 60)
    print(f"\nDone: {len(df)} repos in {int(mins)}m {int(secs)}s. CSV: {csv_path}")


if __name__ == "__main__":
    main()
