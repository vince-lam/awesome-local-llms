"""Fetch GitHub metrics for the curated repos and refresh the README table.

Reads ``repos.json`` (a list of ``{repo, tags}`` entries) and
``categories.json`` (the tag taxonomy), pulls metrics from the GitHub API,
writes a timestamped CSV to ``outputs/`` and injects a filtered, sorted
Markdown table into ``README.md`` between the
``<!-- BEGIN_TABLE -->`` / ``<!-- END_TABLE -->`` markers.
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

API_ROOT = "https://api.github.com"
CONFIG_FILE = "repos.json"
TAXONOMY_FILE = "categories.json"
README_FILE = "README.md"
OUTPUT_DIR = "outputs"

# README table filters
MIN_STARS = 100
MAX_DAYS_SINCE_COMMIT = 60

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
    """Return the GitHub token from the environment (CI or local .env)."""
    # Load a local .env if python-dotenv is available; harmless in CI.
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        pass
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GITHUB_API_TOKEN")
    if not token:
        sys.exit(
            "Error: no GitHub token found. Set GITHUB_TOKEN (CI) or "
            "GITHUB_API_TOKEN in your .env file."
        )
    return token


def make_session(token: str) -> requests.Session:
    """Build a requests session with auth headers and retry/backoff."""
    session = requests.Session()
    session.headers.update(
        {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
    )
    retry = Retry(
        total=5,
        backoff_factor=2,
        # 403 and 429 are GitHub's secondary rate-limit responses; back off and
        # honour any Retry-After header instead of dropping the repo.
        status_forcelist=[403, 429, 500, 502, 503, 504],
        allowed_methods=["GET"],
        respect_retry_after_header=True,
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session


def check_token(session: requests.Session) -> bool:
    """Verify the token works before scraping everything."""
    resp = session.get(f"{API_ROOT}/user")
    if resp.status_code == 401:
        print("Error: invalid or expired GitHub token.")
        return False
    return resp.ok


def count_items(session: requests.Session, url: str) -> int:
    """Count items on a paginated endpoint (contributors, releases) cheaply.

    The GitHub repo object doesn't expose contributor/release counts, so instead
    of walking every page we request a single item and read the ``last`` page
    number from the ``Link`` header. With ``per_page=1`` that page number equals
    the total count, turning N requests into one.
    """
    resp = session.get(url, params={"per_page": 1})
    resp.raise_for_status()
    if not resp.json():
        return 0
    last_url = resp.links.get("last", {}).get("url")
    if not last_url:
        return 1  # only a single item, so no "last" link
    match = re.search(r"[?&]page=(\d+)", last_url)
    return int(match.group(1)) if match else 1


def fetch_repo_info(
    session: requests.Session,
    entry: Dict[str, object],
    taxonomy: Dict[str, Dict[str, str]],
) -> Optional[Dict[str, object]]:
    """Fetch metrics for a single repo entry."""
    repo = entry["repo"]
    slugs: List[str] = entry.get("tags", [])  # type: ignore[assignment]
    tag_names = [taxonomy[s]["name"] for s in slugs if s in taxonomy]
    # Deduplicate parent categories while preserving order.
    cat_names = list(dict.fromkeys(taxonomy[s]["category"] for s in slugs if s in taxonomy))
    platforms: List[str] = entry.get("platforms", [])  # type: ignore[assignment]
    backends: List[str] = entry.get("backends", [])  # type: ignore[assignment]

    base_url = f"{API_ROOT}/repos/{repo}"
    try:
        resp = session.get(base_url)
        resp.raise_for_status()
        data = resp.json()

        contributors = count_items(session, f"{base_url}/contributors")
        releases = count_items(session, f"{base_url}/releases")

        langs_resp = session.get(f"{base_url}/languages")
        langs_resp.raise_for_status()
        languages = ", ".join(langs_resp.json().keys())

        last_commit = datetime.strptime(data["pushed_at"], "%Y-%m-%dT%H:%M:%SZ")
        delta = datetime.now(timezone.utc).replace(tzinfo=None) - last_commit
        days, rem = divmod(delta.total_seconds(), 86400)
        hours, rem = divmod(rem, 3600)
        minutes, _ = divmod(rem, 60)

        license_info = (
            data["license"]["name"]
            if data.get("license")
            else "No license"
        )

        stats = {
            "Owner": repo.split("/")[0],
            "Repository Name": repo.split("/")[1],
            "Categories": ", ".join(cat_names),
            "Tags": ", ".join(tag_names),
            "Platforms": ", ".join(platforms),
            "GPU Backends": ", ".join(backends),
            "About": data.get("description") or "No description available",
            "Stars": data.get("stargazers_count", 0),
            "Forks": data.get("forks_count", 0),
            "Issues": data.get("open_issues_count", 0),
            "Contributors": contributors,
            "Releases": releases,
            "Watchers": data.get("subscribers_count", 0),
            "Time Since Last Commit": (
                f"{int(days)} days, {int(hours)} hrs, {int(minutes)} mins"
            ),
            "License": license_info,
            "Languages": languages,
            "URL": f"https://github.com/{repo}",
            # numeric helpers for sorting/filtering, dropped before output
            "_stars": data.get("stargazers_count", 0),
            "_days": int(days),
        }
        print(f"  ok: {repo} ({stats['Stars']} stars)")
        return stats
    except requests.exceptions.HTTPError as err:
        print(f"  skip: {repo} - HTTP error: {err}")
    except Exception as err:  # noqa: BLE001 - keep going on any single repo
        print(f"  skip: {repo} - error: {err}")
    return None


def fetch_all(
    session: requests.Session,
    entries: List[Dict[str, object]],
    taxonomy: Dict[str, Dict[str, str]],
) -> pd.DataFrame:
    rows = []
    for i, entry in enumerate(entries, 1):
        print(f"[{i}/{len(entries)}] {entry['repo']}")
        info = fetch_repo_info(session, entry, taxonomy)
        if info:
            rows.append(info)
    if not rows:
        sys.exit("Error: no repository data fetched.")
    df = pd.DataFrame(rows).drop_duplicates(subset=["URL"])
    df = df.sort_values(by="_stars", ascending=False).reset_index(drop=True)
    return df


def format_numbers(df: pd.DataFrame) -> pd.DataFrame:
    """Format numeric metric columns with thousands separators (as strings)."""
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
    """Build the condensed, filtered Markdown table for the README."""
    table = df[(df["_stars"] > MIN_STARS) & (df["_days"] <= MAX_DAYS_SINCE_COMMIT)].copy()
    table = table.reset_index(drop=True)
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
    """Inject the table and refresh the Last Updated line in README.md."""
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


def main() -> None:
    start = time.time()
    token = get_token()
    session = make_session(token)
    if not check_token(session):
        sys.exit(1)

    taxonomy = load_taxonomy()

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        entries = json.load(f)

    df = fetch_all(session, entries, taxonomy)
    csv_path = write_csv(df)
    update_readme(build_markdown_table(df))

    mins, secs = divmod(time.time() - start, 60)
    print(f"Done in {int(mins)}m {int(secs)}s. CSV: {csv_path}")


if __name__ == "__main__":
    main()
