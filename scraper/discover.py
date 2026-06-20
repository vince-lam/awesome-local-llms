"""
GitHub repo discovery — finds candidates not yet in repos.json.

Searches GitHub Search API across LLM/agent/inference topics and keywords,
filters to >100 stars, deduplicates, then diffs against repos.json.

Output: discover_candidates.json  (sorted by stars desc)

Usage:
    python discover.py [--min-stars N]  (default 100)
"""

import json
import os
import sys
import time
import argparse
from datetime import datetime

import requests


SEARCH_URL = "https://api.github.com/search/repositories"
MAX_PAGES = 3       # up to 300 results per query (100/page)
REQUEST_DELAY = 2.5 # seconds between requests (search rate limit: 30/min)

# This script lives in scraper/; data sits in scraper/data/ and the raw
# candidate dump is written to the repo root (the parent directory).
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
REPOS_FILE = os.path.join(DATA_DIR, "repos.json")
CANDIDATES_FILE = os.path.join(REPO_ROOT, "discover_candidates.json")


# ---------------------------------------------------------------------------
# Search queries
# ---------------------------------------------------------------------------

# Topic searches are low-noise: repos self-identify with these tags.
TOPIC_SEARCHES = [
    "topic:local-llm",
    "topic:llm-inference",
    "topic:llm-framework",
    "topic:llm-agent",
    "topic:ai-agent",
    "topic:llm-observability",
    "topic:llmops",
    "topic:autonomous-agent",
    "topic:agentic-ai",
    "topic:local-inference",
    "topic:retrieval-augmented-generation",
    "topic:rag",
    "topic:vector-database",
    "topic:code-assistant",
    "topic:coding-assistant",
    "topic:ai-coding-assistant",
    "topic:llm stars:>500",           # broad tag, raise star floor
    "topic:large-language-model stars:>500",
    "topic:generative-ai stars:>500",
]

# Name/description keyword searches for known gap areas.
KEYWORD_SEARCHES = [
    "llm inference server in:name,description stars:>200 is:public",
    "local llm in:name stars:>200 is:public",
    "llm observability in:name,description stars:>100 is:public",
    "llm tracing in:name,description stars:>100 is:public",
    "llm evaluation in:name,description stars:>200 is:public",
    "llm benchmark in:name,description stars:>200 is:public",
    "llm router in:name,description stars:>100 is:public",
    "llm gateway in:name,description stars:>100 is:public",
    "ai coding agent in:name,description stars:>200 is:public",
    "code interpreter llm in:name,description stars:>100 is:public",
    "open source claude in:name stars:>100 is:public",
    "model context protocol in:name,description stars:>100 is:public",
    "mcp server in:name,description stars:>200 is:public",
    "function calling llm in:name,description stars:>100 is:public",
    "llm fine tuning in:name,description stars:>300 is:public",
    "llm finetuning in:name,description stars:>300 is:public",
    "prompt engineering in:name,description stars:>500 is:public",
    "ai agent framework in:name,description stars:>300 is:public",
    "multi agent in:name stars:>300 is:public",
    "agentic workflow in:name,description stars:>100 is:public",
    "rag framework in:name,description stars:>200 is:public",
    "document qa in:name,description stars:>100 is:public",
]


# ---------------------------------------------------------------------------
# GitHub REST search
# ---------------------------------------------------------------------------

def make_session(token: str) -> requests.Session:
    s = requests.Session()
    s.headers.update({
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    return s


def search_repos(session: requests.Session, query: str, min_stars: int, max_pages: int) -> list[dict]:
    """Run one search query, paginate up to max_pages, return raw items."""
    # Inject star floor unless the query already has a stars: clause
    if "stars:" not in query:
        query = f"{query} stars:>{min_stars}"

    results = []
    for page in range(1, max_pages + 1):
        params = {
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": 100,
            "page": page,
        }
        resp = session.get(SEARCH_URL, params=params, timeout=30)

        if resp.status_code == 422:
            # Invalid query — skip silently
            break

        if resp.status_code in (403, 429):
            reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
            wait = max(0, reset - time.time()) + 5
            print(f"    Rate limited — sleeping {wait:.0f}s")
            time.sleep(wait)
            resp = session.get(SEARCH_URL, params=params, timeout=30)

        if not resp.ok:
            print(f"    HTTP {resp.status_code} for query: {query[:60]}")
            break

        data = resp.json()
        items = data.get("items", [])
        results.extend(items)

        remaining = int(resp.headers.get("X-RateLimit-Remaining", 30))
        if remaining < 5:
            reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
            wait = max(0, reset - time.time()) + 5
            print(f"    Rate limit low ({remaining}) — sleeping {wait:.0f}s")
            time.sleep(wait)

        if len(items) < 100:
            break  # last page

        time.sleep(REQUEST_DELAY)

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-stars", type=int, default=100)
    args = parser.parse_args()
    min_stars = args.min_stars

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
        sys.exit("Error: set STATS_GH_PAT, GITHUB_TOKEN, or GITHUB_API_TOKEN")

    with open(REPOS_FILE, encoding="utf-8") as f:
        existing = json.load(f)
    existing_names = {e["repo"].lower() for e in existing}

    session = make_session(token)
    all_items: dict[str, dict] = {}  # full_name → item

    all_queries = [(q, "topic") for q in TOPIC_SEARCHES] + \
                  [(q, "keyword") for q in KEYWORD_SEARCHES]

    for i, (query, qtype) in enumerate(all_queries, 1):
        label = query[:70]
        print(f"[{i}/{len(all_queries)}] {qtype}: {label}")
        items = search_repos(session, query, min_stars, MAX_PAGES)
        new_count = 0
        for item in items:
            name = item["full_name"]
            if name.lower() not in existing_names and name not in all_items:
                all_items[name] = item
                new_count += 1
        print(f"    → {len(items)} results, {new_count} new candidates")
        time.sleep(REQUEST_DELAY)

    # Filter and shape candidates
    candidates = []
    for item in all_items.values():
        stars = item.get("stargazers_count", 0)
        if stars < min_stars:
            continue
        candidates.append({
            "repo": item["full_name"],
            "stars": stars,
            "description": item.get("description", ""),
            "topics": item.get("topics", []),
            "language": item.get("language", ""),
            "archived": item.get("archived", False),
            "url": item.get("html_url", ""),
        })

    candidates.sort(key=lambda x: x["stars"], reverse=True)

    out_path = CANDIDATES_FILE
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(candidates, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"Found {len(candidates)} candidates not in repos.json")
    print(f"Saved to {out_path}")
    print(f"{'='*60}")
    print(f"\n{'Stars':>7}  {'Archived':>8}  Repo")
    print("-" * 70)
    for c in candidates[:80]:
        archived = "[archived]" if c["archived"] else ""
        print(f"{c['stars']:>7,}  {archived:>10}  {c['repo']}")
        if c["description"]:
            desc = c["description"][:80]
            print(f"           {'':>10}  {desc}")
        if c["topics"]:
            print(f"           {'':>10}  topics: {', '.join(c['topics'][:6])}")
        print()

    if len(candidates) > 80:
        print(f"... and {len(candidates) - 80} more in {out_path}")

    print(f"\nDiscovery complete: {len(candidates)} candidates, {datetime.now().strftime('%Y-%m-%d %H:%M')}")


if __name__ == "__main__":
    main()
