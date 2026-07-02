"""
Triage classified candidates: list them, then accept or reject. Turso only —
there is no repos.json; the `repos` table is the single source of truth.

- list                       Show classified candidates (highest stars first).
- accept <repo> [slug ...]   Mark candidate 'accepted' (with the given or
                             suggested subcategory slug(s)). update_stats.py
                             promotes accepted candidates into the repos table on
                             its next run, so the repo starts getting snapshots.
- reject <repo> ...          Mark candidate(s) 'rejected' so discovery never
                             re-surfaces them, and remove them from the tracked
                             `repos` table (and their snapshots) if present.

The category is derived from the subcategory; keywords come from the LLM
suggestion. platforms / backends default to empty and can be set in Turso.

Usage:
    python review.py list [--min-confidence F]
    python review.py accept owner/name [subcategory-slug ...]
    python review.py reject owner/name [owner/name ...]

Environment variables:
    TURSO_DATABASE_URL, TURSO_AUTH_TOKEN — Turso database
"""

import argparse
import json
import os
import sys

from turso import TursoClient
from classifier import load_taxonomy


def get_db() -> TursoClient:
    url = os.getenv("TURSO_DATABASE_URL")
    token = os.getenv("TURSO_AUTH_TOKEN")
    if not (url and token):
        sys.exit("Error: set TURSO_DATABASE_URL and TURSO_AUTH_TOKEN")
    return TursoClient(url, token)


def _parse_json_list(value) -> list[str]:
    """suggested_subcategory / suggested_keywords are JSON arrays (older rows
    may hold a bare slug string)."""
    if not value:
        return []
    try:
        parsed = json.loads(value)
        return parsed if isinstance(parsed, list) else [parsed]
    except (json.JSONDecodeError, TypeError):
        return [value]


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_list(db: TursoClient, args) -> None:
    rows = db.query("""
        SELECT full_name, stars, confidence, suggested_category,
               suggested_subcategory, reason
        FROM   candidates
        WHERE  status = 'classified'
        ORDER BY stars DESC
    """)
    min_conf = args.min_confidence
    shown = 0
    print(f"{'Stars':>7}  {'Conf':>4}  {'Category':<16}  {'Subcategories':<26}  Repo")
    print("-" * 96)
    for full_name, stars, confidence, category, sub, reason in rows:
        if min_conf is not None and (confidence or 0) < min_conf:
            continue
        shown += 1
        subs = ", ".join(_parse_json_list(sub))
        print(f"{stars or 0:>7,}  {confidence or 0:>4.2f}  {category or '':<16}  {subs:<26}  {full_name}")
        if reason:
            print(f"{'':>7}  {'':>4}  {'':<16}  ↳ {reason}")
    print("-" * 96)
    print(f"{shown} classified candidate(s) awaiting review.")


def cmd_accept(db: TursoClient, args) -> None:
    full_name = args.repo
    rows = db.query(
        "SELECT suggested_category, suggested_subcategory, suggested_keywords, status "
        "FROM candidates WHERE full_name = ?",
        [full_name],
    )
    if not rows:
        sys.exit(f"Error: {full_name} is not a candidate.")
    sug_category, sug_sub, sug_keywords, status = rows[0]

    tax = load_taxonomy()
    valid_subs = set(tax.subcategory_slugs)

    subcategories = args.slugs or _parse_json_list(sug_sub)
    if not subcategories:
        sys.exit(f"Error: {full_name} has no suggested subcategory — pass one explicitly.")
    bad = [s for s in subcategories if s not in valid_subs]
    if bad:
        sys.exit(f"Error: invalid subcategory slug(s): {', '.join(bad)}")

    # Use the stored primary category (subcategories may span categories, so we
    # can't derive it from the first subcategory). Fall back to the first
    # subcategory's parent only if the stored category is missing/invalid.
    category = sug_category if sug_category in set(tax.category_slugs) \
        else tax.sub_to_cat[subcategories[0]]

    # Persist any slug override on the candidate so update_stats.py promotes the
    # repo with the accepted taxonomy, then flip it to 'accepted'.
    db.execute(
        "UPDATE candidates SET suggested_category = ?, suggested_subcategory = ?, "
        "status = 'accepted', decided_at = date('now') WHERE full_name = ?",
        [category, json.dumps(subcategories), full_name],
    )
    print(f"Accepted {full_name} [{category}] {', '.join(subcategories)}. "
          f"update_stats.py will promote it into the repos table on its next run.")


def cmd_reject(db: TursoClient, args) -> None:
    for full_name in args.repos:
        # Remove from the tracked list (and its snapshots) if present, then mark
        # the candidate rejected so discovery never re-surfaces it.
        db.executemany([
            ("DELETE FROM snapshots WHERE repo_id IN "
             "(SELECT id FROM repos WHERE full_name = ?)", [full_name]),
            ("DELETE FROM repos WHERE full_name = ?", [full_name]),
        ])
        res = db.execute(
            "UPDATE candidates SET status='rejected', decided_at=date('now') WHERE full_name = ?",
            [full_name],
        )
        affected = res.get("response", {}).get("result", {}).get("affected_row_count", 0)
        if affected:
            print(f"Rejected {full_name} (removed from tracked list).")
        else:
            print(f"Not a candidate: {full_name} (also removed from repos table if it was there).")


def main() -> None:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="Show classified candidates")
    p_list.add_argument("--min-confidence", type=float, default=None)

    p_accept = sub.add_parser("accept", help="Accept a candidate (mark 'accepted' in Turso)")
    p_accept.add_argument("repo", help="owner/name")
    p_accept.add_argument("slugs", nargs="*", default=None,
                          help="Subcategory slug(s) (defaults to the LLM suggestion)")

    p_reject = sub.add_parser("reject", help="Reject candidate(s)")
    p_reject.add_argument("repos", nargs="+", help="one or more owner/name")

    args = parser.parse_args()
    db = get_db()

    if args.command == "list":
        cmd_list(db, args)
    elif args.command == "accept":
        cmd_accept(db, args)
    elif args.command == "reject":
        cmd_reject(db, args)


if __name__ == "__main__":
    main()
