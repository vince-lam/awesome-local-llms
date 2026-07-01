"""
Batch re-classify the curated repos.json into the 3-tier taxonomy.

Reads data/repos.json, fetches fresh GitHub metadata (description, topics,
language, stars) for each repo, runs the shared classifier, and rewrites each
entry into the new shape:

    { "repo": "...", "category": "<slug>", "subcategories": [...],
      "keywords": [...], "platforms": [...], "backends": [...] }

The original file is backed up to repos.json.bak before anything is written,
and results are checkpointed to disk every few repos so a crash is resumable.
After running, spot-check the result with `git diff data/repos.json`.

Usage:
    python reclassify.py [--limit N] [--only-missing]

    --limit N        classify only the first N entries (leave the rest as-is);
                     use this to eyeball a small slice before the full run.
    --only-missing   skip entries that already have a `category` field (resume).

Environment variables:
    ANTHROPIC_API_KEY                               — Claude API key
    STATS_GH_PAT / GITHUB_TOKEN / GITHUB_API_TOKEN  — GitHub token (metadata)
"""

import argparse
import json
import os
import shutil
import sys
import time

import anthropic
import requests

from classifier import (
    MODEL, load_taxonomy, build_system_prompt, build_tool,
    classify_one, normalise_result,
    github_token, make_github_session, fetch_readme,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
REPOS_FILE = os.path.join(DATA_DIR, "repos.json")
BACKUP_FILE = os.path.join(DATA_DIR, "repos.json.bak")

CHECKPOINT_EVERY = 10


def fetch_metadata(session: requests.Session, full_name: str) -> dict:
    """Best-effort GitHub metadata; returns {} on any failure."""
    try:
        resp = session.get(f"https://api.github.com/repos/{full_name}", timeout=30)
    except requests.RequestException:
        return {}

    if resp.status_code in (403, 429):
        reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
        wait = max(0, reset - time.time()) + 5
        print(f"    Rate limited — sleeping {wait:.0f}s")
        time.sleep(wait)
        try:
            resp = session.get(f"https://api.github.com/repos/{full_name}", timeout=30)
        except requests.RequestException:
            return {}

    if not resp.ok:
        return {}

    data = resp.json()
    return {
        "description": data.get("description"),
        "topics": data.get("topics") or [],
        "language": data.get("language"),
        "stars": data.get("stargazers_count") or 0,
    }


def save_repos(repos: list[dict]) -> None:
    with open(REPOS_FILE, "w", encoding="utf-8") as f:
        json.dump(repos, f, indent=2, ensure_ascii=False)
        f.write("\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None,
                        help="Classify only the first N entries (leave rest as-is)")
    parser.add_argument("--only-missing", action="store_true",
                        help="Skip entries that already have a `category` field")
    args = parser.parse_args()

    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("Error: set ANTHROPIC_API_KEY")

    gh_token = github_token()
    if not gh_token:
        print("Warning: no GitHub token found — classifying from repo names only "
              "(descriptions/topics/README unavailable, quality will be lower).")

    with open(REPOS_FILE, encoding="utf-8") as f:
        repos = json.load(f)

    # Back up once (don't clobber an existing backup from an interrupted run).
    if not os.path.exists(BACKUP_FILE):
        shutil.copy2(REPOS_FILE, BACKUP_FILE)
        print(f"Backed up original to {BACKUP_FILE}")

    tax = load_taxonomy()
    system = build_system_prompt(tax)
    tool = build_tool(tax)
    client = anthropic.Anthropic()
    session = make_github_session(gh_token)

    targets = repos if args.limit is None else repos[:args.limit]
    print(f"Re-classifying {len(targets)} of {len(repos)} repos with {MODEL}\n")

    done = 0
    for i, entry in enumerate(targets):
        full_name = entry["repo"]
        if args.only_missing and entry.get("category"):
            continue

        meta = fetch_metadata(session, full_name) if gh_token else {}
        repo = {"full_name": full_name, **meta}
        if gh_token:
            repo["readme"] = fetch_readme(session, full_name)

        try:
            raw = classify_one(client, tool, system, repo)
        except (anthropic.AuthenticationError, anthropic.PermissionDeniedError) as e:
            save_repos(repos)
            sys.exit(f"\nAborting: {e.__class__.__name__} — {e}\n"
                     f"{done} re-classified and saved so far; re-run with "
                     f"--only-missing to resume.")
        except anthropic.APIConnectionError as e:
            save_repos(repos)
            sys.exit(f"\nAborting: connection error — {e}\n"
                     f"{done} re-classified and saved so far; re-run with "
                     f"--only-missing to resume.")
        except anthropic.APIStatusError as e:
            print(f"  API error on {full_name}: {e} — leaving unchanged")
            continue

        if not raw:
            print(f"  No classification returned for {full_name} — leaving unchanged")
            continue

        result = normalise_result(raw, tax)
        if not result["subcategories"]:
            print(f"  No valid subcategory for {full_name} — leaving unchanged")
            continue

        # Rewrite the entry in the new shape, preserving curated platforms/backends.
        new_entry = {
            "repo": full_name,
            "category": result["category"],
            "subcategories": result["subcategories"],
            "keywords": result["keywords"],
        }
        if entry.get("platforms"):
            new_entry["platforms"] = entry["platforms"]
        if entry.get("backends"):
            new_entry["backends"] = entry["backends"]
        repos[i] = new_entry

        done += 1
        subs = ",".join(result["subcategories"])
        print(f"  [{result['confidence']:.2f}] {result['category']:<18} {subs:<28} {full_name}")

        if done % CHECKPOINT_EVERY == 0:
            save_repos(repos)

    save_repos(repos)
    print(f"\nRe-classified {done} repos → {REPOS_FILE}")
    print("Spot-check with:  git diff scraper/data/repos.json")


if __name__ == "__main__":
    main()
