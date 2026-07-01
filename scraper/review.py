"""
Triage classified candidates: list them, then accept or reject.

- list                       Show classified candidates (highest stars first).
- accept <repo> [slug ...]   Add repo to repos.json with the given (or suggested)
                             subcategory tag; mark candidate 'accepted'.
- reject <repo> ...          Mark candidate(s) 'rejected' so discovery never
                             re-surfaces them.

Accepting appends to data/repos.json (the curated source scrape.py scrapes from),
so the repo starts getting daily snapshots on the next scrape run. platforms /
backends are left empty for you to fill in manually.

Usage:
    python review.py list [--min-confidence F]
    python review.py accept owner/name [subcategory-slug]
    python review.py reject owner/name [owner/name ...]

Environment variables:
    TURSO_DATABASE_URL, TURSO_AUTH_TOKEN — Turso database
"""

import argparse
import json
import os
import sys

from turso import TursoClient


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
REPOS_FILE = os.path.join(DATA_DIR, "repos.json")
CATEGORIES_FILE = os.path.join(DATA_DIR, "categories.json")


def get_db() -> TursoClient:
    url = os.getenv("TURSO_DATABASE_URL")
    token = os.getenv("TURSO_AUTH_TOKEN")
    if not (url and token):
        sys.exit("Error: set TURSO_DATABASE_URL and TURSO_AUTH_TOKEN")
    return TursoClient(url, token)


def valid_slugs() -> set[str]:
    with open(CATEGORIES_FILE, encoding="utf-8") as f:
        categories = json.load(f)
    return {sub["slug"] for cat in categories for sub in cat["subcategories"]}


def load_repos() -> list[dict]:
    with open(REPOS_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_repos(repos: list[dict]) -> None:
    with open(REPOS_FILE, "w", encoding="utf-8") as f:
        json.dump(repos, f, indent=2, ensure_ascii=False)
        f.write("\n")


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_list(db: TursoClient, args) -> None:
    rows = db.query("""
        SELECT full_name, stars, confidence, suggested_subcategory, reason
        FROM   candidates
        WHERE  status = 'classified'
        ORDER BY stars DESC
    """)
    min_conf = args.min_confidence
    shown = 0
    print(f"{'Stars':>7}  {'Conf':>4}  {'Subcategory':<22}  Repo")
    print("-" * 78)
    for full_name, stars, confidence, sub, reason in rows:
        if min_conf is not None and (confidence or 0) < min_conf:
            continue
        shown += 1
        print(f"{stars or 0:>7,}  {confidence or 0:>4.2f}  {sub or '':<22}  {full_name}")
        if reason:
            print(f"{'':>7}  {'':>4}  {'':<22}  ↳ {reason}")
    print("-" * 78)
    print(f"{shown} classified candidate(s) awaiting review.")


def cmd_accept(db: TursoClient, args) -> None:
    full_name = args.repo
    rows = db.query(
        "SELECT suggested_subcategory, status FROM candidates WHERE full_name = ?",
        [full_name],
    )
    if not rows:
        sys.exit(f"Error: {full_name} is not a candidate.")
    suggested, status = rows[0]

    slug = args.slug or suggested
    if not slug:
        sys.exit(f"Error: {full_name} has no suggested subcategory — pass one explicitly.")
    if slug not in valid_slugs():
        sys.exit(f"Error: '{slug}' is not a valid subcategory slug.")

    repos = load_repos()
    if any(r["repo"].lower() == full_name.lower() for r in repos):
        print(f"{full_name} already in repos.json — marking accepted only.")
    else:
        repos.append({"repo": full_name, "tags": [slug]})
        save_repos(repos)
        print(f"Added {full_name} to repos.json with tag '{slug}'.")

    db.execute(
        "UPDATE candidates SET status='accepted', decided_at=date('now') WHERE full_name = ?",
        [full_name],
    )
    print(f"Marked {full_name} accepted. It will be scraped on the next run.")


def cmd_reject(db: TursoClient, args) -> None:
    for full_name in args.repos:
        res = db.execute(
            "UPDATE candidates SET status='rejected', decided_at=date('now') WHERE full_name = ?",
            [full_name],
        )
        affected = res.get("response", {}).get("result", {}).get("affected_row_count", 0)
        if affected:
            print(f"Rejected {full_name}.")
        else:
            print(f"Not a candidate: {full_name}")


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

    p_accept = sub.add_parser("accept", help="Accept a candidate into repos.json")
    p_accept.add_argument("repo", help="owner/name")
    p_accept.add_argument("slug", nargs="?", default=None,
                          help="Subcategory slug (defaults to the LLM suggestion)")

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
