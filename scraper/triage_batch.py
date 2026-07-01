"""
Manual batched triage of discovered candidates.

Lets a human (or Claude) classify candidates in stars-descending batches without
the API classifier. Two modes:

    pull  — print the next N unclassified candidates (status='new'), highest
            stars first, as compact JSON. Entries whose description is too thin
            to classify from are flagged "needs_readme": true.

    write — read a JSON array of classifications from a file and write them back
            to the candidates table (validated + normalised against the
            taxonomy), flipping status 'new' → 'classified'.

Because status flips on write, `pull` naturally pages forward — the process is
resumable. Classifications are proposals; a human still accepts/rejects via
review.py.

Usage:
    python triage_batch.py pull  [--limit N] [--min-stars S]
    python triage_batch.py write batch.json

Write-file shape (one object per repo):
    [{"repo": "owner/name", "category": "<slug>",
      "subcategories": ["<slug>", ...], "keywords": ["<slug>", ...],
      "confidence": 0.0-1.0, "reason": "<= 120 chars"}]

Environment variables:
    TURSO_DATABASE_URL, TURSO_AUTH_TOKEN — Turso database
"""

import argparse
import json
import os
import sys

from turso import TursoClient
from classifier import load_taxonomy, normalise_result

DESC_MIN_CHARS = 30   # below this, flag needs_readme


def get_db() -> TursoClient:
    try:
        from dotenv import load_dotenv
        load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))
    except ImportError:
        pass
    url = os.getenv("TURSO_DATABASE_URL")
    token = os.getenv("TURSO_AUTH_TOKEN")
    if not (url and token):
        sys.exit("Error: set TURSO_DATABASE_URL and TURSO_AUTH_TOKEN")
    return TursoClient(url, token)


def cmd_pull(db: TursoClient, args) -> None:
    sql = """
        SELECT full_name, description, topics, language, stars, url
        FROM   candidates
        WHERE  status = 'new' AND stars >= ?
        ORDER BY stars DESC
        LIMIT  ?
    """
    rows = db.query(sql, [args.min_stars, args.limit])
    out = []
    for full_name, description, topics_json, language, stars, url in rows:
        desc = (description or "").strip()
        out.append({
            "repo": full_name,
            "description": desc or None,
            "topics": json.loads(topics_json) if topics_json else [],
            "language": language,
            "stars": stars or 0,
            "url": url,
            "needs_readme": len(desc) < DESC_MIN_CHARS,
        })
    remaining = db.query("SELECT COUNT(*) FROM candidates WHERE status='new'")[0][0]
    if args.compact:
        for e in out:
            flag = " [needs_readme]" if e["needs_readme"] else ""
            topics = ",".join(e["topics"][:10])
            desc = (e["description"] or "").replace("\n", " ")
            print(f"{e['repo']} | {e['stars']}★ | {e['language'] or '?'}{flag} | "
                  f"{desc} | topics: {topics}")
        print(f"\n# remaining_new: {remaining}")
    else:
        print(json.dumps({"batch": out, "remaining_new": remaining},
                         ensure_ascii=False, indent=2))


# Refine 'new' or already-'classified' rows, but never overwrite a human
# accept/reject decision.
_WRITE_SQL = """
UPDATE candidates
SET    suggested_category = ?, suggested_subcategory = ?,
       suggested_keywords = ?, confidence = ?, reason = ?, status = 'classified'
WHERE  full_name = ? AND status IN ('new', 'classified')
"""


def cmd_write(db: TursoClient, args) -> None:
    with open(args.file, encoding="utf-8") as f:
        items = json.load(f)

    tax = load_taxonomy()
    stmts, written, problems = [], 0, []
    for it in items:
        repo = it.get("repo")
        # Reuse the classifier's reconciliation: keep subs that match the
        # category, correct the category from the first sub on mismatch, and
        # drop any keyword outside the vocabulary.
        result = normalise_result({
            "category_slug": it.get("category"),
            "subcategory_slugs": it.get("subcategories") or [],
            "keyword_slugs": it.get("keywords") or [],
            "confidence": it.get("confidence"),
            "reason": it.get("reason"),
        }, tax)
        if not result["category"] or not result["subcategories"]:
            problems.append(f"{repo}: missing valid category/subcategory")
            continue
        stmts.append((_WRITE_SQL, [
            result["category"],
            json.dumps(result["subcategories"]),
            json.dumps(result["keywords"]),
            result["confidence"],
            result["reason"],
            repo,
        ]))
        written += 1

    for i in range(0, len(stmts), 50):
        db.executemany(stmts[i:i + 50])

    print(f"Wrote {written} classification(s) → status='classified'.")
    if problems:
        print(f"{len(problems)} skipped:")
        for p in problems:
            print(f"  - {p}")
    remaining = db.query("SELECT COUNT(*) FROM candidates WHERE status='new'")[0][0]
    print(f"{remaining} candidates still 'new'.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_pull = sub.add_parser("pull", help="Print next N unclassified candidates")
    p_pull.add_argument("--limit", type=int, default=50)
    p_pull.add_argument("--min-stars", type=int, default=100)
    p_pull.add_argument("--compact", action="store_true",
                        help="Terse one-line-per-repo output instead of JSON")

    p_write = sub.add_parser("write", help="Write classifications from a JSON file")
    p_write.add_argument("file", help="Path to classifications JSON array")

    args = parser.parse_args()
    db = get_db()
    if args.command == "pull":
        cmd_pull(db, args)
    elif args.command == "write":
        cmd_write(db, args)


if __name__ == "__main__":
    main()
