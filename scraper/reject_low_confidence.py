"""
Prune weakly-classified repos back off the list — Turso only.

Finds accepted candidates whose classification confidence is below a threshold,
flips their candidate status to 'rejected' (so discovery never re-surfaces them)
and removes them from the tracked `repos` table (and their snapshots). The
inverse of a permissive auto-accept: use it to sweep out borderline / off-topic
matches after the fact.

Usage:
    python reject_low_confidence.py [--max-confidence F] [--dry-run]

    --max-confidence  reject accepted candidates with confidence < F (default 0.6)

Environment variables:
    TURSO_DATABASE_URL, TURSO_AUTH_TOKEN — Turso database
"""

import argparse
import os
import sys

from turso import TursoClient

UPDATE_BATCH = 100   # repos per Turso pipeline


def main() -> None:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-confidence", type=float, default=0.6,
                        help="Reject accepted candidates below this confidence (default 0.6).")
    parser.add_argument("--dry-run", action="store_true",
                        help="Report what would happen without writing anything.")
    args = parser.parse_args()

    url = os.getenv("TURSO_DATABASE_URL")
    token = os.getenv("TURSO_AUTH_TOKEN")
    if not (url and token):
        sys.exit("Error: set TURSO_DATABASE_URL and TURSO_AUTH_TOKEN")
    db = TursoClient(url, token)

    rows = db.query(
        "SELECT full_name, confidence FROM candidates "
        "WHERE status='accepted' AND confidence < ? ORDER BY stars DESC",
        [args.max_confidence],
    )
    if not rows:
        print(f"No accepted candidates below confidence {args.max_confidence}.")
        return

    names = [fn for fn, _ in rows]
    in_repos = {
        r[0] for r in db.query(
            "SELECT full_name FROM repos WHERE full_name IN (%s)"
            % ",".join("?" * len(names)),
            names,
        )
    }

    print(f"Accepted below {args.max_confidence}: {len(names)}")
    print(f"  → currently in repos table: {len(in_repos)}")
    print(f"  → will be marked 'rejected' and removed from the tracked list")

    if args.dry_run:
        print("\n[dry-run] Nothing written.")
        return

    for i in range(0, len(names), UPDATE_BATCH):
        batch = names[i:i + UPDATE_BATCH]
        stmts = []
        for name in batch:
            stmts.append(("DELETE FROM snapshots WHERE repo_id IN "
                          "(SELECT id FROM repos WHERE full_name = ?)", [name]))
            stmts.append(("DELETE FROM repos WHERE full_name = ?", [name]))
            stmts.append(("UPDATE candidates SET status='rejected', "
                          "decided_at=date('now') WHERE full_name = ?", [name]))
        db.executemany(stmts)
        print(f"  pruned: {min(i + UPDATE_BATCH, len(names))}/{len(names)}")

    print("\nDone. These repos are off the list and will not be re-surfaced.")


if __name__ == "__main__":
    main()
