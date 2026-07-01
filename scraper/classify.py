"""
LLM categorisation of discovered candidates.

For every candidate with status='new', asks Claude to pick the best-fitting
subcategory from the taxonomy in data/categories.json, then writes the
suggestion (category, subcategory, confidence, one-line reason) back to the
candidates table and flips status to 'classified'.

The model is constrained via a strict tool whose `subcategory_slug` is an enum
of the real taxonomy slugs — it cannot invent a category. Suggestions are
proposals only; a human accepts/rejects via review.py before promotion.

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


MODEL = "claude-haiku-4-5"   # cheap + fast; classification is an easy task

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
CATEGORIES_FILE = os.path.join(DATA_DIR, "categories.json")


_SELECT_NEW_SQL = """
SELECT full_name, description, topics, language, stars
FROM   candidates
WHERE  status = 'new'
ORDER BY stars DESC
"""

_UPDATE_CLASSIFICATION_SQL = """
UPDATE candidates
SET    suggested_category = ?, suggested_subcategory = ?,
       confidence = ?, reason = ?, status = 'classified'
WHERE  full_name = ?
"""


def load_taxonomy() -> tuple[list[dict], dict[str, str]]:
    """Return (subcategories, subcategory_slug → category_slug)."""
    with open(CATEGORIES_FILE, encoding="utf-8") as f:
        categories = json.load(f)

    subcats = []          # {category, category_slug, name, slug}
    sub_to_cat = {}       # subcategory slug → category slug
    for cat in categories:
        for sub in cat["subcategories"]:
            subcats.append({
                "category": cat["category"],
                "category_slug": cat["slug"],
                "name": sub["name"],
                "slug": sub["slug"],
            })
            sub_to_cat[sub["slug"]] = cat["slug"]
    return subcats, sub_to_cat


def build_system_prompt(subcats: list[dict]) -> str:
    lines = [
        "You classify open-source LLM/AI GitHub repositories into a fixed taxonomy.",
        "Pick the single best-fitting subcategory for the repo described by the user.",
        "Use the repo's name, description, and topics. If genuinely unsure, still pick",
        "the closest fit but lower your confidence. Valid subcategories:",
        "",
    ]
    current = None
    for s in subcats:
        if s["category"] != current:
            current = s["category"]
            lines.append(f"{s['category']}:")
        lines.append(f"  - {s['name']} (slug: {s['slug']})")
    return "\n".join(lines)


def build_tool(subcats: list[dict]) -> dict:
    slugs = [s["slug"] for s in subcats]
    return {
        "name": "classify_repo",
        "description": "Record the best-fitting subcategory for this repository.",
        "strict": True,
        "input_schema": {
            "type": "object",
            "properties": {
                "subcategory_slug": {
                    "type": "string",
                    "enum": slugs,
                    "description": "Slug of the single best-fitting subcategory.",
                },
                "confidence": {
                    "type": "number",
                    "description": "Confidence in this classification, 0.0 to 1.0.",
                },
                "reason": {
                    "type": "string",
                    "description": "One-line justification (<= 120 characters).",
                },
            },
            "required": ["subcategory_slug", "confidence", "reason"],
            "additionalProperties": False,
        },
    }


def classify_one(client, tool, system, cand: dict) -> dict | None:
    """Return {subcategory_slug, confidence, reason} or None on failure."""
    topics = ", ".join(cand["topics"]) if cand["topics"] else "(none)"
    user = (
        f"Repository: {cand['full_name']}\n"
        f"Description: {cand['description'] or '(none)'}\n"
        f"Primary language: {cand['language'] or '(unknown)'}\n"
        f"GitHub topics: {topics}\n"
        f"Stars: {cand['stars']:,}"
    )
    resp = client.messages.create(
        model=MODEL,
        max_tokens=512,
        system=system,
        tools=[tool],
        tool_choice={"type": "tool", "name": "classify_repo"},
        messages=[{"role": "user", "content": user}],
    )
    for block in resp.content:
        if block.type == "tool_use" and block.name == "classify_repo":
            return block.input
    return None


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

    subcats, sub_to_cat = load_taxonomy()
    system = build_system_prompt(subcats)
    tool = build_tool(subcats)
    client = anthropic.Anthropic()

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
        }
        try:
            result = classify_one(client, tool, system, cand)
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

        if not result:
            print(f"  No classification returned for {full_name} — skipping")
            continue

        sub_slug = result["subcategory_slug"]
        cat_slug = sub_to_cat.get(sub_slug, "")
        confidence = float(result["confidence"])
        reason = result["reason"]

        # Checkpoint per row so a crash resumes cleanly.
        db.execute(_UPDATE_CLASSIFICATION_SQL,
                   [cat_slug, sub_slug, confidence, reason, full_name])
        done += 1
        print(f"  [{confidence:.2f}] {sub_slug:<22} {full_name}")

    print(f"\nClassified {done}/{len(rows)} candidates → status='classified'")


if __name__ == "__main__":
    main()
