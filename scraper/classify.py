"""
LLM categorisation of discovered candidates via Anthropic Batch API.

Processes candidates in chunks: fetches READMEs for CHUNK_SIZE repos, submits
a batch, polls until done, writes results, then moves to the next chunk.
This gives progressive results and limits memory use vs. loading everything
at once.

Usage:
    python classify.py [--limit N] [--chunk-size N]

Environment variables:
    ANTHROPIC_API_KEY                    — Claude API key
    TURSO_DATABASE_URL, TURSO_AUTH_TOKEN — Turso database
"""

import argparse
import json
import os
import sys
import time
from datetime import date

import anthropic

from turso import TursoClient
from classifier import (
    MODEL, load_taxonomy, build_system_prompt, build_tool,
    format_repo_prompt, normalise_result,
    github_token, make_github_session, fetch_readme,
)


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
WHERE  full_name = ?
"""


def _today() -> str:
    return date.today().isoformat()


def _build_request(custom_id: str, tool: dict, system: str, repo: dict) -> dict:
    # Anthropic custom_id: ^[a-zA-Z0-9_-]{1,64}$  — repo full_names contain
    # "/" and "." so we use a plain integer index as the id instead.
    return {
        "custom_id": custom_id,
        "params": {
            "model": MODEL,
            "max_tokens": 512,
            "system": system,
            "tools": [tool],
            "tool_choice": {"type": "tool", "name": "classify_repo"},
            "messages": [{"role": "user", "content": format_repo_prompt(repo)}],
        },
    }


def _run_chunk(chunk: list[dict], chunk_num: int, total_chunks: int,
               tool: dict, system: str, tax, db, client) -> int:
    """Fetch READMEs, submit batch, poll, write results. Returns count classified."""
    n = len(chunk)
    print(f"\n── Chunk {chunk_num}/{total_chunks}  ({n} repos) ──────────────────")

    # Fetch READMEs for this chunk only.
    session = make_github_session(github_token())
    for cand in chunk:
        if cand.get("_needs_readme"):
            cand["readme"] = fetch_readme(session, cand["full_name"])

    # Submit batch (retry up to 3 times on transient server errors).
    idx_to_name = {str(i): c["full_name"] for i, c in enumerate(chunk)}
    batch = None
    for attempt in range(1, 4):
        try:
            batch = client.messages.batches.create(
                requests=[_build_request(str(i), tool, system, c)
                          for i, c in enumerate(chunk)]
            )
            break
        except (anthropic.AuthenticationError, anthropic.PermissionDeniedError) as e:
            sys.exit(f"\nAborting: {e.__class__.__name__} — {e}")
        except (anthropic.APIConnectionError, anthropic.InternalServerError) as e:
            if attempt == 3:
                sys.exit(f"\nAborting after 3 attempts: {e}")
            wait = 30 * attempt
            print(f"  Transient error (attempt {attempt}/3), retrying in {wait}s: {e}")
            time.sleep(wait)

    print(f"Submitted batch {batch.id}  requests={n}")

    # Poll until done.
    deadline = time.time() + POLL_TIMEOUT
    while True:
        batch = client.messages.batches.retrieve(batch.id)
        c = batch.request_counts
        print(f"  {batch.processing_status}  "
              f"processing={c.processing}  succeeded={c.succeeded}  "
              f"errored={c.errored}")
        if batch.processing_status == "ended":
            break
        if time.time() > deadline:
            print(f"\nTimed out waiting for batch {batch.id} — "
                  f"chunk skipped, candidates remain 'new'.")
            return 0
        time.sleep(POLL_INTERVAL)

    # Write results.
    done = 0
    for item in client.messages.batches.results(batch.id):
        full_name = idx_to_name.get(item.custom_id, item.custom_id)
        if item.result.type != "succeeded":
            print(f"  {full_name}: {item.result.type} — skipping")
            continue

        raw = None
        for block in item.result.message.content:
            if block.type == "tool_use" and block.name == "classify_repo":
                raw = block.input
                break

        if not raw:
            print(f"  No classification returned for {full_name} — skipping")
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

    print(f"  → {done}/{n} classified")
    return done


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None,
                        help="Max candidates to classify this run")
    parser.add_argument("--chunk-size", type=int, default=CHUNK_SIZE,
                        help=f"Repos per batch (default {CHUNK_SIZE})")
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

    tax = load_taxonomy()
    system = build_system_prompt(tax)
    tool = build_tool(tax)
    client = anthropic.Anthropic()

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
        total_done += _run_chunk(chunk, i, total_chunks, tool, system, tax, db, client)

    print(f"\n{'═'*60}")
    print(f"Done. Classified {total_done}/{len(candidates)} candidates total.")


if __name__ == "__main__":
    main()
