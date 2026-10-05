"""Resumable OpenAI Batch transport shared by production and the benchmark."""

import json
import time
from pathlib import Path

from openai import APIStatusError, OpenAI

TERMINAL = {"completed", "failed", "expired", "cancelled"}


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(path)


def client():
    # Never automatically retry a potentially accepted batch submission.
    return OpenAI(max_retries=0, timeout=60)


def submit(api, requests, path):
    """Persist a guard before submitting; preserve ambiguous network failures."""
    path = Path(path)
    if path.exists():
        state = json.loads(path.read_text())
        if not state.get("id"):
            raise RuntimeError("Ambiguous batch submission: inspect OpenAI Batches before retrying")
        return state
    content = "\n".join(json.dumps(r) for r in requests).encode()
    upload = api.files.create(file=("classifications.jsonl", content, "application/jsonl"), purpose="batch")
    save(path, {"input_file_id": upload.id, "requests": requests})
    try:
        batch = api.batches.create(input_file_id=upload.id,
                                  endpoint="/v1/chat/completions", completion_window="24h")
    except APIStatusError as exc:
        # A definite rejection cannot have created a chargeable batch.
        if 400 <= exc.status_code < 500 and exc.status_code not in (408, 409):
            path.unlink()
        raise
    state = {"id": batch.id, "input_file_id": upload.id, "requests": requests,
             "created_at": batch.created_at}
    save(path, state)
    return state


def collect(api, state, path, timeout=1800, poll_interval=30):
    """Return unordered result lines, or None while the saved batch is running."""
    deadline = time.monotonic() + timeout
    while True:
        batch = api.batches.retrieve(state["id"])
        state["batch"] = batch.model_dump()
        save(path, state)
        print(f"Luna batch {batch.id}: {batch.status} {batch.request_counts}", flush=True)
        if batch.status in TERMINAL:
            break
        if time.monotonic() >= deadline:
            print("Batch still running; rerun to collect the same batch.", flush=True)
            return None
        time.sleep(poll_interval)
    if batch.status == "failed":
        raise RuntimeError(f"Batch {batch.id} failed validation; inspect saved batch state")
    rows = []
    for file_id in (batch.output_file_id, batch.error_file_id):
        if file_id:
            rows.extend(json.loads(line) for line in api.files.content(file_id).text.splitlines() if line.strip())
    return rows
