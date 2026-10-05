"""
LLM categorisation of discovered candidates via OpenAI Batch API.

Processes candidates in chunks: fetches READMEs for CHUNK_SIZE repos, submits
a batch, polls until done, writes results, then moves to the next chunk.
This gives progressive results and limits memory use vs. loading everything
at once.

Usage:
    python classify.py [--limit N] [--chunk-size N]

Environment variables:
    OPENAI_API_KEY                       — OpenAI API key
    TURSO_DATABASE_URL, TURSO_AUTH_TOKEN — Turso database
"""

import argparse
import json
import os
import sys
from datetime import date

from pathlib import Path

try:
    from . import luna_batch
    from .turso import TursoClient
    from .classifier import (MODEL, load_taxonomy, build_system_prompt, build_tool,
                             build_luna_params, parse_luna_message, normalise_result,
                             github_token, make_github_session, fetch_readme)
except ImportError:
    import luna_batch
    from turso import TursoClient
    from classifier import (MODEL, load_taxonomy, build_system_prompt, build_tool,
                            build_luna_params, parse_luna_message, normalise_result,
                            github_token, make_github_session, fetch_readme)


CHUNK_SIZE    = 300   # repos per batch submission
POLL_INTERVAL = 30    # seconds between batch status checks
POLL_TIMEOUT  = 1800  # 30-minute ceiling per chunk (chunks are small)

# Classifications at or above this confidence are auto-accepted: they go live on
# the next update_stats.py run (which merges status='accepted' candidates straight
# from Turso — no human review, no repos.json commit needed). Below it they stay
# 'classified' as an optional manual-review bucket rather than being auto-rejected.
AUTO_ACCEPT_CONFIDENCE = 0.6

_SELECT_NEW_SQL = """
SELECT full_name, description, topics, language, stars
FROM   candidates
WHERE  status = 'new'
ORDER BY stars DESC
"""

_UPDATE_CLASSIFICATION_SQL = """
UPDATE candidates
SET    suggested_category = ?, suggested_subcategory = ?,
       suggested_keywords = ?, confidence = ?, reason = ?,
       status = ?, decided_at = ?
WHERE  full_name = ? AND status = 'new'
"""


def _today() -> str:
    return date.today().isoformat()


def _build_request(custom_id: str, tool: dict, system: str, repo: dict) -> dict:
    return {"custom_id": custom_id, "method": "POST", "url": "/v1/chat/completions",
            "body": build_luna_params(tool, system, repo)}


def _run_chunk(chunk, chunk_num, total_chunks, tool, system, tax, db, client, state_path):
    """Resume a saved batch before submitting new candidates. None means pending."""
    if not state_path.exists():
        session = make_github_session(github_token())
        for cand in chunk:
            if cand.get("_needs_readme"):
                cand["readme"] = fetch_readme(session, cand["full_name"])
        requests = [_build_request(c["full_name"], tool, system, c) for c in chunk]
        state = luna_batch.submit(client, requests, state_path)
    else:
        state = json.loads(state_path.read_text())
        if not state.get("id"):
            raise RuntimeError("Ambiguous batch submission: inspect OpenAI Batches before retrying")
    names = {r["custom_id"] for r in state["requests"]}
    n = len(names)
    print(f"Chunk {chunk_num}/{total_chunks}: {n} repos, batch={state['id']}")
    items = luna_batch.collect(client, state, state_path, POLL_TIMEOUT, POLL_INTERVAL)
    if items is None:
        return None

    # Write results.
    done = 0
    for item in items:
        full_name = item.get("custom_id")
        if full_name not in names:
            print("  Unknown response id - skipping")
            continue
        response = item.get("response") or {}
        if item.get("error") or response.get("status_code") != 200:
            print(f"  {full_name}: provider error - skipping")
            continue
        raw = parse_luna_message(response.get("body") or {})
        if raw is None:
            print(f"  No complete classification for {full_name} - skipping")
            continue

        result = normalise_result(raw, tax)
        if not result["subcategories"]:
            print(f"  No valid subcategory for {full_name} — skipping")
            continue

        # Auto-accept confident classifications straight to 'accepted' (they go
        # live via update_stats.py — no human review). Park the rest as
        # 'classified' for an optional manual look.
        accepted = result["confidence"] >= AUTO_ACCEPT_CONFIDENCE
        status = "accepted" if accepted else "classified"
        decided_at = _today() if accepted else None

        db.execute(_UPDATE_CLASSIFICATION_SQL, [
            result["category"],
            json.dumps(result["subcategories"]),
            json.dumps(result["keywords"]),
            result["confidence"],
            result["reason"],
            status,
            decided_at,
            full_name,
        ])
        done += 1
        subs = ",".join(result["subcategories"])
        mark = "✓ accept" if accepted else "· park  "
        print(f"  {mark} [{result['confidence']:.2f}] {result['category']:<18} {subs:<28} {full_name}")

    state_path.unlink()
    print(f"  → {done}/{n} classified")
    return done


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None,
                        help="Max candidates to classify this run")
    parser.add_argument("--chunk-size", type=int, default=CHUNK_SIZE,
                        help=f"Repos per batch (default {CHUNK_SIZE})")
    parser.add_argument("--state-dir", type=Path, default=Path("outputs/classifier-state"),
                        help="Saved batch state; retain between runs")
    args = parser.parse_args()
    if args.chunk_size < 1 or (args.limit is not None and args.limit < 1):
        parser.error("limit and chunk-size must be positive")
    args.state_dir.mkdir(parents=True, exist_ok=True)
    (args.state_dir / ".keep").touch()
    state_path = args.state_dir / "batch.json"

    try:
        from dotenv import load_dotenv
        load_dotenv(Path(__file__).parent / ".env")
    except ImportError:
        pass

    if not os.getenv("OPENAI_API_KEY"):
        sys.exit("Error: set OPENAI_API_KEY")

    turso_url = os.getenv("TURSO_DATABASE_URL")
    turso_token = os.getenv("TURSO_AUTH_TOKEN")
    if not (turso_url and turso_token):
        sys.exit("Error: set TURSO_DATABASE_URL and TURSO_AUTH_TOKEN")
    db = TursoClient(turso_url, turso_token)

    tax = load_taxonomy()
    system = build_system_prompt(tax)
    tool = build_tool(tax)
    client = luna_batch.client()

    if state_path.exists():
        done = _run_chunk([], 1, 1, tool, system, tax, db, client, state_path)
        if done is None:
            return

    gh_token = github_token()
    if not gh_token:
        print("Warning: no GitHub token — classifying without README context.")

    sql = _SELECT_NEW_SQL
    if args.limit:
        sql += f"\nLIMIT {int(args.limit)}"
    rows = db.query(sql)
    if not rows:
        print("No candidates with status='new' to classify.")
        return

    # Build candidate list (READMEs fetched per-chunk below).
    candidates = [
        {
            "full_name": full_name,
            "description": description,
            "topics": json.loads(topics_json) if topics_json else [],
            "language": language,
            "stars": stars or 0,
            "readme": None,
            "_needs_readme": bool(gh_token),
        }
        for full_name, description, topics_json, language, stars in rows
    ]

    chunk_size = args.chunk_size
    chunks = [candidates[i:i + chunk_size]
              for i in range(0, len(candidates), chunk_size)]
    total_chunks = len(chunks)

    print(f"{len(candidates)} candidates  •  {total_chunks} chunk(s) of ≤{chunk_size}  •  model={MODEL}")

    total_done = 0
    for i, chunk in enumerate(chunks, 1):
        done = _run_chunk(chunk, i, total_chunks, tool, system, tax, db, client, state_path)
        if done is None:
            break
        total_done += done

    print(f"\n{'═'*60}")
    print(f"Done. Classified {total_done}/{len(candidates)} candidates total.")


if __name__ == "__main__":
    main()
