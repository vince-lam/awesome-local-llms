"""Benchmark Luna Batch on frozen repos; reuse Haiku results without calling it.

uv run --python 3.11 --with openai --with requests --with python-dotenv python \
  scraper/benchmark_luna.py --output outputs/classifier-benchmark-luna
Rerun the same command to collect a pending batch.
"""

import argparse
import hashlib
import json
from pathlib import Path
import statistics

from dotenv import load_dotenv

try:
    from .classifier import (MODEL, build_system_prompt, build_tool, build_luna_params,
                             load_taxonomy, normalise_result, parse_luna_message)
    from . import luna_batch
except ImportError:
    from classifier import (MODEL, build_system_prompt, build_tool, build_luna_params,
                            load_taxonomy, normalise_result, parse_luna_message)
    import luna_batch


def cost(usage):
    """USD at GPT-6 Luna Batch rates, including cache reads/writes and reasoning.

    prompt_tokens includes cached and cache-write tokens. completion_tokens
    includes reasoning tokens. Rates checked against official docs 2026-10-05.
    """
    details = usage.get("prompt_tokens_details") or {}
    cached = details.get("cached_tokens") or 0
    writes = details.get("cache_write_tokens") or 0
    uncached = usage["prompt_tokens"] - cached - writes
    return (uncached * .05 + cached * .005 + writes * .0625
            + usage["completion_tokens"] * .25) / 1_000_000


def jaccard(a, b):
    union = set(a) | set(b)
    return len(set(a) & set(b)) / len(union) if union else 1.0


def compare(results, haiku, state):
    h_by_name = {r["full_name"]: r for r in haiku if r.get("classification")}
    pairs = [(r, h_by_name[r["full_name"]]) for r in results
             if r.get("classification") and r["full_name"] in h_by_name]
    luna_cost = sum(r.get("cost", 0) for r in results)
    haiku_cost = sum(h.get("cost", 0) for _, h in pairs)
    paired_luna_cost = sum(r.get("cost", 0) for r, _ in pairs)
    batch = state["batch"]
    ended = next((batch.get(k) for k in ("completed_at", "expired_at", "cancelled_at", "failed_at") if batch.get(k)), None)
    n = len(pairs)
    return {
        "model": MODEL, "haiku_rerun": False, "submitted": len(state["requests"]),
        "valid_results": sum(bool(r.get("classification")) for r in results),
        "paired_results": n, "batch_status": batch["status"],
        "batch_completion_seconds": ended - batch["created_at"] if ended else None,
        "cost_usd_from_usage_at_batch_rates": luna_cost,
        "cost_per_1000_submitted": luna_cost / len(state["requests"]) * 1000,
        "input_tokens": sum(r.get("usage", {}).get("prompt_tokens", 0) for r in results),
        "output_tokens": sum(r.get("usage", {}).get("completion_tokens", 0) for r in results),
        "paired_costs": {"haiku_usd": haiku_cost, "luna_usd": paired_luna_cost,
                         "savings_percent": (1 - paired_luna_cost / haiku_cost) * 100 if haiku_cost else None},
        "category_agreement": sum(r["classification"]["category"] == h["classification"]["category"] for r, h in pairs) / n if n else None,
        **{field + "_mean_jaccard": statistics.mean(jaccard(r["classification"][field], h["classification"][field]) for r, h in pairs) if n else None
           for field in ("subcategories", "keywords")},
        "limitations": ["Agreement with Haiku is not verified accuracy.",
                        "Costs calculated from provider usage and documented rates; exclude tax and purchase fees.",
                        "Batch completion includes provider queue time.",
                        "One standard-rate smoke request is separate from this Batch cost."],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, default=Path("outputs/classifier-benchmark-2026-10-01"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--batch-timeout", type=int, default=1800)
    args = parser.parse_args()
    load_dotenv(Path(__file__).parent / ".env")
    baseline_bytes = (args.baseline / "haiku-results.json").read_bytes()
    inputs_bytes = (args.baseline / "inputs.json").read_bytes()
    inputs = json.loads(inputs_bytes)
    haiku = json.loads(baseline_bytes)
    tax = load_taxonomy()
    requests = [{"custom_id": str(i), "method": "POST", "url": "/v1/chat/completions",
                 "body": build_luna_params(build_tool(tax), build_system_prompt(tax), repo)}
                for i, repo in enumerate(inputs)]
    config = {"model": MODEL, "haiku_sha256": hashlib.sha256(baseline_bytes).hexdigest(),
              "inputs_sha256": hashlib.sha256(inputs_bytes).hexdigest(),
              "requests_sha256": hashlib.sha256(json.dumps(requests, sort_keys=True).encode()).hexdigest(),
              "haiku_rerun": False}
    args.output.mkdir(parents=True, exist_ok=True)
    config_path = args.output / "config.json"
    if config_path.exists() and json.loads(config_path.read_text()) != config:
        raise RuntimeError("Benchmark inputs/config changed; use a new output directory")
    luna_batch.save(config_path, config)
    api = luna_batch.client()
    path = args.output / "luna-batch.json"
    state = luna_batch.submit(api, requests, path)
    rows = luna_batch.collect(api, state, path, timeout=args.batch_timeout)
    if rows is None:
        return
    results = []
    seen = set()
    for item in rows:
        index = int(item["custom_id"])
        if index in seen or not 0 <= index < len(inputs):
            raise RuntimeError("Invalid or duplicate response id")
        seen.add(index)
        response = item.get("response") or {}
        body = response.get("body") or {}
        raw = parse_luna_message(body) if response.get("status_code") == 200 else None
        result = {"full_name": inputs[index]["full_name"], "raw": item}
        if body.get("usage"):
            result["usage"] = body["usage"]
            result["cost"] = cost(body["usage"])
        if raw:
            normalised = normalise_result(raw, tax)
            if normalised["category"] and normalised["subcategories"]:
                result["classification"] = normalised
        results.append(result)
    luna_batch.save(args.output / "luna-results.json", results)
    summary = compare(results, haiku, state)
    luna_batch.save(args.output / "summary.json", summary)
    disagreements = [{"full_name": r["full_name"], "luna": r["classification"], "haiku": h["classification"]}
                     for r in results if r.get("classification")
                     for h in haiku if h["full_name"] == r["full_name"] and h.get("classification")
                     if r["classification"]["category"] != h["classification"]["category"]]
    luna_batch.save(args.output / "disagreements.json", disagreements)
    if (args.baseline / "haiku-results.json").read_bytes() != baseline_bytes:
        raise RuntimeError("Saved Haiku baseline changed")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
