"""
Validate the taxonomy files and the tracked repos (Turso) against them.

Checks:
  - categories.json and keywords.json parse and have unique slugs;
  - every repo in the Turso `repos` table has a valid category, at least one
    valid subcategory, and every keyword is in the vocabulary.

Exits non-zero if anything is wrong, so it can gate CI / pre-commit.

Usage:
    python validate_taxonomy.py

Environment variables:
    TURSO_DATABASE_URL, TURSO_AUTH_TOKEN — Turso database
"""

import json
import os
import sys

from turso import TursoClient
from classifier import load_taxonomy


def _json_list(value) -> list[str]:
    if not value:
        return []
    try:
        parsed = json.loads(value)
        return parsed if isinstance(parsed, list) else [parsed]
    except (json.JSONDecodeError, TypeError):
        return [value]


def load_tracked_repos() -> list[dict]:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass
    url = os.getenv("TURSO_DATABASE_URL")
    token = os.getenv("TURSO_AUTH_TOKEN")
    if not (url and token):
        sys.exit("Error: set TURSO_DATABASE_URL and TURSO_AUTH_TOKEN")
    db = TursoClient(url, token)
    rows = db.query("SELECT full_name, category, tags, keywords FROM repos")
    return [
        {"repo": fn, "category": cat,
         "subcategories": _json_list(tags), "keywords": _json_list(kw)}
        for fn, cat, tags, kw in rows
    ]


def main() -> None:
    tax = load_taxonomy()
    errors: list[str] = []

    # 1. Slug uniqueness within each vocabulary.
    for label, slugs in (
        ("category", tax.category_slugs),
        ("subcategory", tax.subcategory_slugs),
        ("keyword", tax.keyword_slugs),
    ):
        dupes = {s for s in slugs if slugs.count(s) > 1}
        if dupes:
            errors.append(f"Duplicate {label} slug(s): {', '.join(sorted(dupes))}")

    cat_set = set(tax.category_slugs)
    sub_set = set(tax.subcategory_slugs)

    # 2. Every tracked repo validates against the taxonomy.
    repos = load_tracked_repos()

    checked = 0
    for e in repos:
        repo = e.get("repo", "?")
        category = e.get("category")
        subs = e.get("subcategories") or e.get("tags") or []
        keywords = e.get("keywords") or []

        # Legacy entries (no category yet) are skipped from the strict check but
        # still have their subcategory slugs validated.
        if category is not None:
            checked += 1
            if category not in cat_set:
                errors.append(f"{repo}: unknown category '{category}'")
            if not subs:
                errors.append(f"{repo}: no subcategories")
            # Subcategories may span categories (a repo can wear more than one
            # hat), so we only check the slug is real — not that it belongs to
            # the primary category.
            for s in subs:
                if s not in sub_set:
                    errors.append(f"{repo}: unknown subcategory '{s}'")
            for k in keywords:
                if k not in tax._keyword_set:
                    errors.append(f"{repo}: unknown keyword '{k}'")
        else:
            for s in subs:
                if s not in sub_set:
                    errors.append(f"{repo}: unknown subcategory '{s}'")

    if errors:
        print(f"✗ {len(errors)} validation error(s):")
        for msg in errors[:100]:
            print(f"  - {msg}")
        if len(errors) > 100:
            print(f"  ... and {len(errors) - 100} more")
        sys.exit(1)

    print(
        f"✓ Taxonomy valid: {len(tax.category_slugs)} categories, "
        f"{len(tax.subcategory_slugs)} subcategories, {len(tax.keyword_slugs)} keywords. "
        f"{len(repos)} repos checked ({checked} fully classified)."
    )


if __name__ == "__main__":
    main()
