"""Apply the curated Agent Skills repository-subcategory backfill.

Dry-run by default. Pass ``--apply`` to update Turso. Existing subcategory tags
are preserved, because ``agent-skills`` describes a repository role and can
coexist with task-oriented tags from any primary category.
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    from .turso import TursoClient
except ImportError:
    from turso import TursoClient


MANIFEST = Path(__file__).parent / "migrations" / "2026-09-20-agent-skills.json"


def get_db() -> TursoClient:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass
    url = os.getenv("TURSO_DATABASE_URL")
    token = os.getenv("TURSO_AUTH_TOKEN")
    if not (url and token):
        sys.exit("Error: set TURSO_DATABASE_URL and TURSO_AUTH_TOKEN")
    return TursoClient(url, token)


def add_tag(value: str | None, tag: str) -> tuple[str, bool]:
    try:
        parsed = json.loads(value or "[]")
    except (json.JSONDecodeError, TypeError) as exc:
        raise ValueError("tags must be a JSON array") from exc
    if not isinstance(parsed, list) or not all(isinstance(item, str) for item in parsed):
        raise ValueError("tags must be a JSON string array")
    if tag in parsed:
        return json.dumps(parsed), False
    return json.dumps([*parsed, tag]), True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write updates to Turso")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text())
    tag = manifest["subcategory"]
    selected = manifest["repositories"]
    if len(selected) != len(set(selected)):
        raise SystemExit("Error: duplicate repository in backfill manifest")

    db = get_db()
    tracked = {name: tags for name, tags in db.query("SELECT full_name, tags FROM repos")}
    missing = [name for name in selected if name not in tracked]
    if missing:
        shown = ", ".join(missing[:10])
        raise SystemExit(f"Error: {len(missing)} selected repositories are not tracked: {shown}")

    updates = []
    unchanged = 0
    for name in selected:
        tags, changed = add_tag(tracked[name], tag)
        if changed:
            updates.append(("UPDATE repos SET tags = ? WHERE full_name = ?", [tags, name]))
        else:
            unchanged += 1

    action = "Applying" if args.apply else "Would apply"
    print(f"{action} '{tag}' to {len(updates)} repositories; {unchanged} already tagged.")
    if args.apply and updates:
        db.executemany(updates)
        print(f"Updated {len(updates)} repositories.")
    elif not args.apply:
        print("Dry run only. Pass --apply to write changes.")


if __name__ == "__main__":
    main()
