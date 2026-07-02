"""
Edit a tracked repo's metadata directly in Turso (the single source of truth).

Since there is no repos.json, this is how you set the curated fields that the LLM
classifier doesn't produce — chiefly `platforms` / `backends` for local-runtime
tools — and how you hand-correct a repo's category / subcategories / keywords.

The repo must already be tracked (present in the `repos` table). Only the fields
you pass are changed; everything else is left alone.

Usage:
    # Show a repo's current metadata
    python set_metadata.py ggerganov/llama.cpp

    # Set platforms / backends
    python set_metadata.py ggerganov/llama.cpp \
        --platforms Linux macOS Windows Android iOS \
        --backends CPU CUDA ROCm Vulkan Metal SYCL

    # Clear them, or fix taxonomy
    python set_metadata.py owner/name --clear-platforms --clear-backends
    python set_metadata.py owner/name --category infrastructure --subcategories local-runtime

Environment variables:
    TURSO_DATABASE_URL, TURSO_AUTH_TOKEN — Turso database
"""

import argparse
import json
import os
import sys

from turso import TursoClient
from classifier import load_taxonomy

# De-facto canonical values (not enforced — unknown values warn but are allowed).
KNOWN_PLATFORMS = {"Android", "FreeBSD", "Linux", "Web", "Windows", "iOS", "macOS"}
KNOWN_BACKENDS = {"CPU", "CUDA", "MPS", "Metal", "ROCm", "SYCL", "Vulkan", "WebGPU"}


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


def _fmt(value: str | None) -> str:
    try:
        return ", ".join(json.loads(value or "[]")) or "(none)"
    except (json.JSONDecodeError, TypeError):
        return value or "(none)"


def show(db: TursoClient, full_name: str) -> None:
    rows = db.query(
        "SELECT full_name, category, tags, keywords, platforms, backends "
        "FROM repos WHERE full_name = ?",
        [full_name],
    )
    if not rows:
        sys.exit(f"Error: {full_name} is not tracked (not in the repos table).")
    fn, category, tags, keywords, platforms, backends = rows[0]
    print(f"{fn}")
    print(f"  category:      {category or '(none)'}")
    print(f"  subcategories: {_fmt(tags)}")
    print(f"  keywords:      {_fmt(keywords)}")
    print(f"  platforms:     {_fmt(platforms)}")
    print(f"  backends:      {_fmt(backends)}")


def _warn_unknown(values: list[str], known: set[str], label: str) -> None:
    unknown = [v for v in values if v not in known]
    if unknown:
        print(f"  note: non-standard {label}: {', '.join(unknown)} "
              f"(allowed, but check spelling/case)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("repo", help="owner/name (must already be tracked)")
    parser.add_argument("--platforms", nargs="+", metavar="P",
                        help="Set platforms (e.g. Linux macOS Windows)")
    parser.add_argument("--backends", nargs="+", metavar="B",
                        help="Set backends (e.g. CPU CUDA Metal)")
    parser.add_argument("--clear-platforms", action="store_true", help="Set platforms to []")
    parser.add_argument("--clear-backends", action="store_true", help="Set backends to []")
    parser.add_argument("--category", help="Override category slug")
    parser.add_argument("--subcategories", nargs="+", metavar="S",
                        help="Override subcategory slug(s)")
    parser.add_argument("--keywords", nargs="+", metavar="K",
                        help="Override keyword slug(s)")
    args = parser.parse_args()

    db = get_db()

    # No mutation flags → just show current state.
    mutating = any([
        args.platforms, args.backends, args.clear_platforms, args.clear_backends,
        args.category, args.subcategories, args.keywords,
    ])
    if not mutating:
        show(db, args.repo)
        return

    if not db.query("SELECT 1 FROM repos WHERE full_name = ?", [args.repo]):
        sys.exit(f"Error: {args.repo} is not tracked (not in the repos table). "
                 f"Accept it first, or it must be scraped in.")

    tax = load_taxonomy()
    sets: list[tuple[str, str]] = []   # (column, json_value)

    if args.clear_platforms:
        sets.append(("platforms", "[]"))
    elif args.platforms:
        _warn_unknown(args.platforms, KNOWN_PLATFORMS, "platform(s)")
        sets.append(("platforms", json.dumps(args.platforms)))

    if args.clear_backends:
        sets.append(("backends", "[]"))
    elif args.backends:
        _warn_unknown(args.backends, KNOWN_BACKENDS, "backend(s)")
        sets.append(("backends", json.dumps(args.backends)))

    if args.category:
        if args.category not in set(tax.category_slugs):
            sys.exit(f"Error: unknown category slug '{args.category}'")
        sets.append(("category", args.category))

    if args.subcategories:
        bad = [s for s in args.subcategories if s not in set(tax.subcategory_slugs)]
        if bad:
            sys.exit(f"Error: unknown subcategory slug(s): {', '.join(bad)}")
        sets.append(("tags", json.dumps(args.subcategories)))

    if args.keywords:
        bad = [k for k in args.keywords if k not in tax._keyword_set]
        if bad:
            sys.exit(f"Error: unknown keyword slug(s): {', '.join(bad)}")
        sets.append(("keywords", json.dumps(args.keywords)))

    clause = ", ".join(f"{col} = ?" for col, _ in sets)
    db.execute(
        f"UPDATE repos SET {clause} WHERE full_name = ?",
        [val for _, val in sets] + [args.repo],
    )
    print(f"Updated {args.repo}:")
    show(db, args.repo)


if __name__ == "__main__":
    main()
