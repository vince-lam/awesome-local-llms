"""
GitHub repo discovery — finds candidates not yet in the curated list and writes
them to the Turso `candidates` table for triage.

Searches the GitHub Search API across LLM/agent/inference topics and keywords,
filters to >100 stars, deduplicates, drops repos already tracked (in the Turso
`repos` table), then upserts the rest into the candidates table.

A third pass adds a recency dimension: the same API restricted to a rolling
created: window, at a lower star floor, so fast-rising new repos that carry
none of the topics or keywords above still surface.

Repos already tracked in the `repos` table are skipped. Repos already in the
candidates table are refreshed in place via ON CONFLICT — crucially this does
NOT reset their status, so anything previously reviewed and marked 'rejected'
stays rejected and never re-surfaces as new.

Output: rows in the Turso `candidates` table (status='new' for genuinely new repos).

Usage:
    python discover.py [--min-stars N] [--recency-min-stars N] [--recency-days N]

Environment variables:
    STATS_GH_PAT / GITHUB_TOKEN / GITHUB_API_TOKEN  — GitHub token (search)
    TURSO_DATABASE_URL, TURSO_AUTH_TOKEN            — Turso database
"""

import json
import os
import re
import sys
import time
import argparse
from datetime import datetime, timedelta, timezone

import requests

from turso import TursoClient


SEARCH_URL = "https://api.github.com/search/repositories"
MAX_PAGES = 3       # up to 300 results per query (100/page)
REQUEST_DELAY = 2.5 # seconds between requests (search rate limit: 30/min)

# GitHub Search returns at most ~1000 results per query and we only page the top
# 300, so a crowded topic (e.g. topic:llm has 4000+ repos >100 stars) is
# truncated to its highest-starred 300. To page past that, each base query is
# fanned out into star bands — each band returns its own top slice, so the
# mid-tail becomes reachable. Bands are contiguous and non-overlapping.
STAR_BAND_EDGES = [250, 500, 1000, 2500]

# Rolling window and star floor for the recency searches (see RECENCY_SEARCHES).
RECENCY_DAYS = 120
RECENCY_MIN_STARS = 50

_STARS_RE = re.compile(r"\s*stars:(?:>=|>|<=|<)?(\d+)(?:\.\.(?:\d+|\*))?")


def expand_star_bands(query: str, floor: int) -> list[str]:
    """Fan one query out into per-star-band queries.

    If the query already carries a stars: clause, its lower bound is used as the
    band floor (preserving intentionally higher floors on noisy broad topics) and
    that clause is stripped before the band clause is appended.
    """
    m = _STARS_RE.search(query)
    base = query
    if m:
        base = _STARS_RE.sub("", query, count=1).strip()
        floor = max(floor, int(m.group(1)))

    edges = [floor] + [e for e in STAR_BAND_EDGES if e > floor]
    bands = []
    for i, lo in enumerate(edges):
        if i + 1 < len(edges):
            bands.append(f"{base} stars:{lo}..{edges[i + 1] - 1}".strip())
        else:
            bands.append(f"{base} stars:>={lo}".strip())
    return bands

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

# Recency searches close the one gap the topic/keyword sweep has: a repo that
# blows up in a few weeks but carries no matching topic and whose description
# misses every keyword phrase above stays invisible until someone tags it.
# Narrowing to a rolling created: window lets the star floor drop well below
# --min-stars without drowning the run in noise. {since} is filled at runtime.
#
# Two of them re-run sorted by updated: the window's top-300-by-stars slice is
# all a stars-sorted query can reach, so a second ordering exposes the mid-tail
# of the broad topics.
RECENCY_SEARCHES = [
    ("topic:llm created:>{since}", "stars"),
    ("topic:llm created:>{since}", "updated"),
    ("topic:ai-agent created:>{since}", "stars"),
    ("topic:mcp created:>{since}", "stars"),
    ("topic:agentic-ai created:>{since}", "stars"),
    ("topic:generative-ai created:>{since}", "stars"),
    ("ai agent in:name,description created:>{since} is:public", "stars"),
    ("ai agent in:name,description created:>{since} is:public", "updated"),
    ("llm in:name,description created:>{since} is:public", "stars"),
    ("agentic in:name,description created:>{since} is:public", "stars"),
    ("mcp server in:name,description created:>{since} is:public", "stars"),
    ("coding agent in:name,description created:>{since} is:public", "stars"),
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


def _get(session: requests.Session, params: dict):
    """GET the search endpoint, retrying transient network failures.

    A run issues hundreds of queries, so a single read timeout must not abort
    the whole sweep. Returns None once the retries are exhausted, letting the
    caller drop that query and carry on.
    """
    for attempt in range(3):
        try:
            return session.get(SEARCH_URL, params=params, timeout=30)
        except requests.RequestException as e:
            if attempt == 2:
                print(f"    Network error after 3 attempts ({e.__class__.__name__}) — skipping")
                return None
            time.sleep(5 * (attempt + 1))


def search_repos(session: requests.Session, query: str, min_stars: int, max_pages: int,
                 sort: str = "stars") -> list[dict]:
    """Run one search query, paginate up to max_pages, return raw items."""
    # Inject star floor unless the query already has a stars: clause
    if "stars:" not in query:
        query = f"{query} stars:>{min_stars}"

    results = []
    for page in range(1, max_pages + 1):
        params = {
            "q": query,
            "sort": sort,
            "order": "desc",
            "per_page": 100,
            "page": page,
        }
        resp = _get(session, params)
        if resp is None:
            break

        if resp.status_code == 422:
            # Invalid query — skip silently
            break

        if resp.status_code in (403, 429):
            reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
            wait = max(0, reset - time.time()) + 5
            print(f"    Rate limited — sleeping {wait:.0f}s")
            time.sleep(wait)
            resp = _get(session, params)
            if resp is None:
                break

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
    parser.add_argument("--recency-min-stars", type=int, default=RECENCY_MIN_STARS,
                        help="Star floor for the created:-window searches (default 50)")
    parser.add_argument("--recency-days", type=int, default=RECENCY_DAYS,
                        help="Width of the created: window in days (default 120)")
    parser.add_argument("--skip-recency", action="store_true",
                        help="Run only the topic/keyword sweep")
    parser.add_argument("--dry-run", action="store_true",
                        help="Search and report new candidates without writing to Turso")
    parser.add_argument("--max-base", type=int, default=None,
                        help="Only process the first N base queries (for a quick dry run)")
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
    if args.max_base:
        all_queries = all_queries[:args.max_base]

    # Fan each base query out into star bands to page past the per-query cap.
    banded = [(bq, qtype, "stars") for q, qtype in all_queries
              for bq in expand_star_bands(q, min_stars)]

    # Recency queries are not banded: a few months of new repos above a 50-star
    # floor is nowhere near the per-query result cap, so bands would only burn
    # rate limit. The window keeps them narrow instead.
    if not args.skip_recency:
        since = (datetime.now(timezone.utc) - timedelta(days=args.recency_days)).strftime("%Y-%m-%d")
        banded += [
            (f"{tmpl.format(since=since)} stars:>{args.recency_min_stars}", "recency", sort)
            for tmpl, sort in RECENCY_SEARCHES
        ]

    for i, (query, qtype, sort) in enumerate(banded, 1):
        label = query[:70]
        print(f"[{i}/{len(banded)}] {qtype}/{sort}: {label}")
        items = search_repos(session, query, min_stars, MAX_PAGES, sort=sort)
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

    # Filter and shape candidates. Every query already enforces its own floor
    # server-side, so this is only a backstop against stale star counts — it has
    # to use the lowest floor in play or it would discard the recency hits.
    floor = min_stars if args.skip_recency else min(min_stars, args.recency_min_stars)
    candidates = []
    for item in all_items.values():
        stars = item.get("stargazers_count", 0)
        if stars < floor:
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

    new_candidates = [c for c in candidates if c["repo"].lower() not in existing_cand_names]

    if args.dry_run:
        print(f"\n{'='*60}")
        print(f"DRY RUN — no writes. {len(candidates)} not-yet-tracked repos found, "
              f"{len(new_candidates)} of them NEW (not already candidates)")
        print(f"{'='*60}")
    else:
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

    verb = "would upsert" if args.dry_run else "upserted"
    print(f"\nDiscovery complete: {len(new_candidates)} new, "
          f"{len(candidates)} total {verb}, {datetime.now().strftime('%Y-%m-%d %H:%M')}")


if __name__ == "__main__":
    main()
