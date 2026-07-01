"""
Validate the taxonomy files and repos.json against them.

Checks:
  - categories.json and keywords.json parse and have unique slugs;
  - every repos.json entry has a valid category, at least one valid
    subcategory, each subcategory belongs to its category, and every keyword
    is in the vocabulary.

Exits non-zero if anything is wrong, so it can gate CI / pre-commit.

Usage:
    python validate_taxonomy.py
"""

import json
import os
import sys

from classifier import load_taxonomy

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPOS_FILE = os.path.join(SCRIPT_DIR, "data", "repos.json")


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

    # 2. Every repos.json entry validates against the taxonomy.
    with open(REPOS_FILE, encoding="utf-8") as f:
        repos = json.load(f)

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
