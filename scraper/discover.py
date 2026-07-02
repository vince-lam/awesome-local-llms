"""
GitHub repo discovery — finds candidates not yet in the curated list and writes
them to the Turso `candidates` table for triage.

Searches the GitHub Search API across LLM/agent/inference topics and keywords,
filters to >100 stars, deduplicates, drops repos already tracked (in the Turso
`repos` table), then upserts the rest into the candidates table.

Repos already tracked in the `repos` table are skipped. Repos already in the
candidates table are refreshed in place via ON CONFLICT — crucially this does
NOT reset their status, so anything previously reviewed and marked 'rejected'
stays rejected and never re-surfaces as new.

Output: rows in the Turso `candidates` table (status='new' for genuinely new repos).

Usage:
    python discover.py [--min-stars N]  (default 100)

Environment variables:
    STATS_GH_PAT / GITHUB_TOKEN / GITHUB_API_TOKEN  — GitHub token (search)
    TURSO_DATABASE_URL, TURSO_AUTH_TOKEN            — Turso database
"""

import json
import os
import sys
import time
import argparse
from datetime import datetime

import requests

from turso import TursoClient


SEARCH_URL = "https://api.github.com/search/repositories"
MAX_PAGES = 3       # up to 300 results per query (100/page)
REQUEST_DELAY = 2.5 # seconds between requests (search rate limit: 30/min)

# This script lives in scraper/; data sits in scraper/data/.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")


# ---------------------------------------------------------------------------
# Search queries
# ---------------------------------------------------------------------------

# Topic searches are low-noise: repos self-identify with these tags.
TOPIC_SEARCHES = [
    # AI Engineering / agents
    "topic:llm-agent",
    "topic:ai-agent",
    "topic:autonomous-agent",
    "topic:agentic-ai",
    "topic:llm-framework",
    "topic:multi-agent",
    "topic:mcp",
    "topic:mcp-server",
    "topic:model-context-protocol",
    "topic:retrieval-augmented-generation",
    "topic:rag",
    "topic:vector-database",
    "topic:llm-observability",
    "topic:llmops",
    "topic:code-assistant",
    "topic:coding-assistant",
    "topic:ai-coding-assistant",
    # Infrastructure / runtime
    "topic:local-llm",
    "topic:llm-inference",
    "topic:local-inference",
    "topic:llm-serving",
    "topic:llm-gateway",
    # Model Development
    "topic:fine-tuning",
    "topic:llm-training",
    "topic:reinforcement-learning-from-human-feedback",
    "topic:llm-evaluation",
    # Models
    "topic:llm stars:>500",           # broad tag, raise star floor
    "topic:large-language-model stars:>500",
    "topic:generative-ai stars:>500",
    "topic:text-to-image stars:>500",
    "topic:text-to-speech stars:>500",
    "topic:embeddings stars:>300",
    # Lists / awesome (AI-qualified only — bare topic:awesome-list is too noisy)
    "topic:awesome-llm",
    "topic:awesome-ai",
    # Prompts
    "topic:prompt-engineering stars:>500",
    "topic:system-prompts",
    "topic:awesome-chatgpt-prompts",
    "topic:chatgpt-prompts",
    # Tutorials / learning
    "topic:llm-course",
    "topic:generative-ai-course",
    "topic:machine-learning-roadmap",
]

# Name/description keyword searches for known gap areas.
KEYWORD_SEARCHES = [
    # AI Engineering / agents
    "ai agent framework in:name,description stars:>300 is:public",
    "multi agent in:name stars:>300 is:public",
    "agentic workflow in:name,description stars:>100 is:public",
    "agent harness in:name,description stars:>100 is:public",
    "context engineering in:name,description stars:>100 is:public",
    "model context protocol in:name,description stars:>100 is:public",
    "mcp server in:name,description stars:>200 is:public",
    "function calling llm in:name,description stars:>100 is:public",
    "rag framework in:name,description stars:>200 is:public",
    "document qa in:name,description stars:>100 is:public",
    "personal ai assistant in:name,description stars:>200 is:public",
    "open source claude in:name stars:>100 is:public",
    # Applications
    "ai coding agent in:name,description stars:>200 is:public",
    "code interpreter llm in:name,description stars:>100 is:public",
    "deep research in:name,description stars:>200 is:public",
    "text to sql in:name,description stars:>200 is:public",
    # Infrastructure
    "llm inference server in:name,description stars:>200 is:public",
    "local llm in:name stars:>200 is:public",
    "llm observability in:name,description stars:>100 is:public",
    "llm tracing in:name,description stars:>100 is:public",
    "llm router in:name,description stars:>100 is:public",
    "llm gateway in:name,description stars:>100 is:public",
    # Model Development
    "llm fine tuning in:name,description stars:>300 is:public",
    "llm finetuning in:name,description stars:>300 is:public",
    "llm evaluation in:name,description stars:>200 is:public",
    "llm benchmark in:name,description stars:>200 is:public",
    "training toolkit llm in:name,description stars:>100 is:public",
    "synthetic data generation in:name,description stars:>200 is:public",
    # Lists
    "awesome llm in:name stars:>500 is:public",
    "awesome generative ai in:name stars:>300 is:public",
    "awesome mcp in:name stars:>300 is:public",
    "awesome agents in:name stars:>300 is:public",
    # Prompts
    "prompt engineering in:name,description stars:>500 is:public",
    "system prompts in:name,description stars:>300 is:public",
    "prompt collection in:name,description stars:>300 is:public",
    # Tutorials
    "llm course in:name,description stars:>300 is:public",
    "generative ai course in:name,description stars:>300 is:public",
    "llm tutorial in:name,description stars:>300 is:public",
    "llm roadmap in:name,description stars:>300 is:public",
    "llm from scratch in:name,description stars:>500 is:public",
]


# ---------------------------------------------------------------------------
# Candidate upsert
# ---------------------------------------------------------------------------

# Refreshes an existing candidate's stats without touching status/classification,
# so a rejected repo stays rejected and a classified one keeps its category.
_UPSERT_CANDIDATE_SQL = """
INSERT INTO candidates (full_name, description, topics, language, stars, archived, url)
VALUES (?, ?, ?, ?, ?, ?, ?)
ON CONFLICT(full_name) DO UPDATE SET
  stars       = excluded.stars,
  description = excluded.description,
  topics      = excluded.topics,
  language    = excluded.language,
  archived    = excluded.archived,
  url         = excluded.url
"""


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

    turso_url = os.getenv("TURSO_DATABASE_URL")
    turso_token = os.getenv("TURSO_AUTH_TOKEN")
    if not (turso_url and turso_token):
        sys.exit("Error: set TURSO_DATABASE_URL and TURSO_AUTH_TOKEN")
    db = TursoClient(turso_url, turso_token)

    # Repos already tracked (in the repos table) — never surface these as candidates.
    curated_names = {
        row[0].lower() for row in db.query("SELECT full_name FROM repos")
    }

    # Candidates already tracked (any status) — used only to report which repos
    # are genuinely new this run; the upsert refreshes the rest in place.
    existing_cand_names = {
        row[0].lower() for row in db.query("SELECT full_name FROM candidates")
    }

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
            if name.lower() in curated_names:
                continue  # already in the curated list
            if name not in all_items:
                all_items[name] = item
                new_count += 1
        print(f"    → {len(items)} results, {new_count} not-yet-curated")
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

    # Upsert into the candidates table.
    stmts = [
        (_UPSERT_CANDIDATE_SQL, [
            c["repo"], c["description"], json.dumps(c["topics"]),
            c["language"], c["stars"], int(c["archived"]), c["url"],
        ])
        for c in candidates
    ]
    for i in range(0, len(stmts), 50):
        db.executemany(stmts[i:i + 50])

    new_candidates = [c for c in candidates if c["repo"].lower() not in existing_cand_names]

    print(f"\n{'='*60}")
    print(f"Upserted {len(candidates)} candidates ({len(new_candidates)} new this run)")
    print(f"{'='*60}")
    print(f"\n{'Stars':>7}  {'Archived':>8}  Repo")
    print("-" * 70)
    for c in new_candidates[:80]:
        archived = "[archived]" if c["archived"] else ""
        print(f"{c['stars']:>7,}  {archived:>10}  {c['repo']}")
        if c["description"]:
            desc = c["description"][:80]
            print(f"           {'':>10}  {desc}")
        if c["topics"]:
            print(f"           {'':>10}  topics: {', '.join(c['topics'][:6])}")
        print()

    if len(new_candidates) > 80:
        print(f"... and {len(new_candidates) - 80} more new candidates in the DB")

    print(f"\nDiscovery complete: {len(new_candidates)} new, "
          f"{len(candidates)} total upserted, {datetime.now().strftime('%Y-%m-%d %H:%M')}")


if __name__ == "__main__":
    main()
