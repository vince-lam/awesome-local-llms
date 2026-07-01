"""
LLM categorisation of discovered candidates.

For every candidate with status='new', asks Claude to classify it into the
3-tier taxonomy (data/categories.json + data/keywords.json): one category,
one-or-more subcategories, and zero-or-more keywords. The suggestion (category,
subcategories JSON, keywords JSON, confidence, one-line reason) is written back
to the candidates table and status is flipped to 'classified'.

The model is constrained via a strict tool whose slugs are enums of the real
taxonomy — it cannot invent a category. Suggestions are proposals only; a human
accepts/rejects via review.py before promotion.

Usage:
    python classify.py [--limit N]   (default: all status='new')

Environment variables:
    ANTHROPIC_API_KEY                    — Claude API key
    TURSO_DATABASE_URL, TURSO_AUTH_TOKEN — Turso database
"""

import argparse
import json
import os
import sys

import anthropic

from turso import TursoClient
from classifier import (
    MODEL, load_taxonomy, build_system_prompt, build_tool,
    classify_one, normalise_result,
    github_token, make_github_session, fetch_readme,
)


_SELECT_NEW_SQL = """
SELECT full_name, description, topics, language, stars
FROM   candidates
WHERE  status = 'new'
ORDER BY stars DESC
"""

_UPDATE_CLASSIFICATION_SQL = """
UPDATE candidates
SET    suggested_category = ?, suggested_subcategory = ?,
       suggested_keywords = ?, confidence = ?, reason = ?, status = 'classified'
WHERE  full_name = ?
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None,
                        help="Max candidates to classify this run")
    args = parser.parse_args()

    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("Error: set ANTHROPIC_API_KEY")

    turso_url = os.getenv("TURSO_DATABASE_URL")
    turso_token = os.getenv("TURSO_AUTH_TOKEN")
    if not (turso_url and turso_token):
        sys.exit("Error: set TURSO_DATABASE_URL and TURSO_AUTH_TOKEN")
    db = TursoClient(turso_url, turso_token)

    tax = load_taxonomy()
    system = build_system_prompt(tax)
    tool = build_tool(tax)
    client = anthropic.Anthropic()

    gh_token = github_token()
    if not gh_token:
        print("Warning: no GitHub token — classifying without README context.")
    session = make_github_session(gh_token)

    sql = _SELECT_NEW_SQL
    if args.limit:
        sql += f"\nLIMIT {int(args.limit)}"
    rows = db.query(sql)
    if not rows:
        print("No candidates with status='new' to classify.")
        return

    print(f"Classifying {len(rows)} candidate(s) with {MODEL}\n")

    done = 0
    for full_name, description, topics_json, language, stars in rows:
        cand = {
            "full_name": full_name,
            "description": description,
            "topics": json.loads(topics_json) if topics_json else [],
            "language": language,
            "stars": stars or 0,
            "readme": fetch_readme(session, full_name) if gh_token else None,
        }
        try:
            raw = classify_one(client, tool, system, cand)
        except (anthropic.AuthenticationError, anthropic.PermissionDeniedError) as e:
            # Bad/expired key or exhausted credit — every remaining call would
            # fail the same way. Stop now; candidates stay 'new' for next run.
            sys.exit(f"\nAborting: {e.__class__.__name__} — {e}\n"
                     f"Fix the API key / billing, then re-run. "
                     f"{done} classified so far; the rest remain 'new'.")
        except anthropic.APIConnectionError as e:
            # Network/timeout — unlikely to recover within this run.
            sys.exit(f"\nAborting: connection error — {e}\n"
                     f"{done} classified so far; the rest remain 'new'.")
        except anthropic.APIStatusError as e:
            # Other per-request errors (e.g. a one-off 400/500) — skip this one.
            print(f"  API error on {full_name}: {e}")
            continue

        if not raw:
            print(f"  No classification returned for {full_name} — skipping")
            continue

        result = normalise_result(raw, tax)
        if not result["subcategories"]:
            print(f"  No valid subcategory for {full_name} — skipping")
            continue

        # Checkpoint per row so a crash resumes cleanly.
        db.execute(_UPDATE_CLASSIFICATION_SQL, [
            result["category"],
            json.dumps(result["subcategories"]),
            json.dumps(result["keywords"]),
            result["confidence"],
            result["reason"],
            full_name,
        ])
        done += 1
        subs = ",".join(result["subcategories"])
        print(f"  [{result['confidence']:.2f}] {result['category']:<18} {subs:<28} {full_name}")

    print(f"\nClassified {done}/{len(rows)} candidates → status='classified'")


if __name__ == "__main__":
    main()
