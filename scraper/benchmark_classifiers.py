"""Compare Haiku Batch and Jev on identical frozen inputs, without database writes.

python scraper/benchmark_classifiers.py --output outputs/classifier-benchmark
Uses scraper/.env; rerun the same command to resume saved inputs and results.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import random
import socket
import statistics
import time
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

try:
    from .classifier import (MODEL, build_system_prompt, build_tool, fetch_readme,
                             format_repo_prompt, github_token, load_taxonomy,
                             make_github_session, normalise_result)
    from .turso import TursoClient
except ImportError:
    from classifier import (MODEL, build_system_prompt, build_tool, fetch_readme,
                            format_repo_prompt, github_token, load_taxonomy,
                            make_github_session, normalise_result)
    from turso import TursoClient

JEV_MODEL = "typesafe/jev-1.13"
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages/batches"
JEV_URL = "https://openrouter.ai/api/alpha/decisions"


def save(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    temporary.replace(path)


def read(path):
    return json.loads(path.read_text())


def haiku_params(repo, tax):
    # Match classify.py:_build_request; transport only differs (HTTP vs SDK).
    return {"model": MODEL, "max_tokens": 512,
            "system": build_system_prompt(tax), "tools": [build_tool(tax)],
            "tool_choice": {"type": "tool", "name": "classify_repo"},
            "messages": [{"role": "user", "content": format_repo_prompt(repo)}]}


def jev_questions(tax):
    questions = {"category": {
        "type": "choice", "instructions": "Choose the single best-fitting primary category.",
        "criteria": {c["slug"]: c["category"] + ": " + c.get("description", "")
                     for c in tax.categories}}}
    for cat in tax.categories:
        for sub in cat["subcategories"]:
            questions["sub_" + sub["slug"]] = {
                "type": "noul", "instructions": (
                    f"Does this repository genuinely fulfil this role: {sub['name']} "
                    f"({cat['category']})? {sub.get('description', '')} "
                    "Roles may span categories; incidental mentions do not count.")}
    for keyword in tax.keywords:
        questions["keyword_" + keyword["slug"]] = {
            "type": "noul", "instructions": (
                f"Is this repository clearly about {keyword['name']} "
                f"({keyword.get('group', '')})? Incidental mentions do not count.")}
    return questions


def numeric(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError("Missing or invalid numeric response value")
    return value


def parse_jev(body, tax, threshold):
    answers = body["answers"]
    category = answers["category"]
    if category["type"] != "choice" or category["choice"] not in tax.category_slugs:
        raise ValueError("Invalid Jev category")
    confidence = category.get("confidence")
    if confidence is not None and not 0 <= numeric(confidence) <= 1:
        raise ValueError("Invalid Jev confidence")
    selected = {}
    for field, prefix, slugs, cap in [
        ("subcategories", "sub_", tax.subcategory_slugs, 5),
        ("keywords", "keyword_", tax.keyword_slugs, 6),
    ]:
        probabilities = {}
        for slug in slugs:
            answer = answers[prefix + slug]
            p = numeric(answer["noul"])
            if answer["type"] != "noul" or not 0 <= p <= 1:
                raise ValueError("Invalid Jev tag probability")
            probabilities[slug] = p
        selected[field] = sorted(
            (s for s in slugs if probabilities[s] >= threshold),
            key=lambda s: (-probabilities[s], s))[:cap]
    usage = body["usage"]
    for key in ("input_tokens", "output_tokens", "cost"):
        if numeric(usage[key]) < 0:
            raise ValueError("Invalid Jev usage")
    return {"category": category["choice"], **selected,
            "confidence": confidence, "reason": None}


def haiku_cost(usage):
    # USD: Haiku 4.5 Batch rates checked 2026-10-01. No caching configured.
    return (usage["input_tokens"] * 0.50 + usage["output_tokens"] * 2.50
            + usage.get("cache_read_input_tokens", 0) * 0.05
            + usage.get("cache_creation_input_tokens", 0) * 0.625) / 1_000_000


class ProviderHTTPError(RuntimeError):
    def __init__(self, response):
        self.status = response.status_code
        try:
            message = str(response.json().get("error", {}).get("message", ""))
        except (ValueError, AttributeError):
            message = ""
        for name in ("OPENROUTER_API_KEY", "ANTHROPIC_API_KEY", "STATS_GH_PAT", "TURSO_AUTH_TOKEN"):
            secret = os.environ.get(name)
            if secret:
                message = message.replace(secret, "[redacted]")
        super().__init__(f"{urlparse(response.url).hostname}: HTTP {self.status} {message[:800]}")


def http(method, url, headers, payload=None):
    response = requests.request(method, url, headers=headers, json=payload, timeout=120)
    if not response.ok:
        # Avoid logging request headers, credentials or provider error bodies.
        raise ProviderHTTPError(response)
    return response


def prepare_inputs(args, output, tax):
    path = output / "inputs.json"
    if path.exists():
        return read(path)
    db = TursoClient(os.environ["TURSO_DATABASE_URL"], os.environ["TURSO_AUTH_TOKEN"])
    rows = db.query("""
        SELECT r.full_name, r.description, COALESCE(c.topics, '[]'),
               COALESCE(r.latest_language, c.language), COALESCE(r.latest_stars, c.stars, 0),
               r.category, r.tags, r.keywords
        FROM repos r LEFT JOIN candidates c ON c.full_name = r.full_name
        WHERE r.category IS NOT NULL ORDER BY r.full_name
    """)
    groups = {slug: [] for slug in tax.category_slugs}
    for name, description, topics, language, stars, cat, tags, keywords in rows:
        if cat in groups:
            groups[cat].append({"full_name": name, "description": description,
                                "topics": json.loads(topics), "language": language,
                                "stars": stars, "existing_labels": {
                                    "category": cat, "subcategories": json.loads(tags),
                                    "keywords": json.loads(keywords)}})
    rng = random.Random(args.seed)
    for group in groups.values():
        rng.shuffle(group)
    selected = []
    while len(selected) < args.limit and any(groups.values()):
        for group in groups.values():
            if group and len(selected) < args.limit:
                selected.append(group.pop())
    if len(selected) < args.limit:
        raise RuntimeError(f"Only {len(selected)} eligible repos; requested {args.limit}")
    session = make_github_session(github_token())
    for i, repo in enumerate(selected):
        # Capture public metadata to include GitHub topics even for curated-only rows.
        response = session.get(f"https://api.github.com/repos/{repo['full_name']}", timeout=30)
        if response.status_code == 401:
            source = next(key for key in ("STATS_GH_PAT", "GITHUB_TOKEN", "GITHUB_API_TOKEN")
                          if os.environ.get(key))
            raise RuntimeError(
                f"GitHub rejected {source} (HTTP 401). Replace its token in scraper/.env; "
                "also check for a stale exported value, which overrides the file. "
                "No model inference was submitted.")
        if not response.ok:
            raise RuntimeError(f"GitHub metadata HTTP {response.status_code}")
        metadata = response.json()
        repo.update(description=metadata.get("description"), topics=metadata.get("topics", []),
                    language=metadata.get("language"), stars=metadata.get("stargazers_count", 0))
        repo["readme"] = fetch_readme(session, repo["full_name"])
        print(f"Inputs {i + 1}/{len(selected)}: {repo['full_name']}", flush=True)
    save(path, selected)
    return selected


def run_jev(repo, index, args, output, tax, questions):
    path = output / f"jev-{index:03d}.json"
    if path.exists():
        return
    pending = output / f"jev-{index:03d}-pending.json"
    if pending.exists():
        raise RuntimeError("Ambiguous prior Jev call: check OpenRouter activity before retrying")
    headers = {"Authorization": "Bearer " + os.environ["OPENROUTER_API_KEY"]}
    started = time.monotonic()
    payload = {"model": JEV_MODEL, "state": {
        "repository": format_repo_prompt(repo), "classification_policy": build_system_prompt(tax)},
        "questions": questions}
    # No automatic inference retries: an ambiguous transport failure may be billed.
    save(pending, {"full_name": repo["full_name"]})
    try:
        body = http("POST", JEV_URL, headers, payload).json()
    except ProviderHTTPError as error:
        if error.status not in (400, 413):
            raise
        # Definitive input rejection, not an ambiguous transport failure.
        save(path, {"full_name": repo["full_name"], "seconds": time.monotonic() - started,
                    "status": "rejected", "http_status": error.status,
                    "error": str(error), "raw": {}})
        pending.unlink()
        return
    # Save usage before validating labels, retaining any billed malformed response.
    result = {"full_name": repo["full_name"], "seconds": time.monotonic() - started,
              "raw": body, "status": "invalid"}
    save(path, result)
    pending.unlink()
    result.update(classification=parse_jev(body, tax, args.threshold), status="succeeded")
    save(path, result)


def run_haiku(inputs, args, output, tax):
    path = output / "haiku-batch.json"
    headers = {"x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01"}
    if not path.exists():
        pending = output / "haiku-submission-pending.json"
        if pending.exists():
            raise RuntimeError("Ambiguous prior batch submission: check Anthropic before resubmitting")
        submitted_at = datetime.now(timezone.utc).isoformat()
        save(pending, {"submitted_at": submitted_at})
        batch = http("POST", ANTHROPIC_URL, headers, {"requests": [
            {"custom_id": str(i), "params": haiku_params(repo, tax)}
            for i, repo in enumerate(inputs)]}).json()
        save(path, {"id": batch["id"], "submitted_at": submitted_at})
        pending.unlink()
    saved = read(path)
    if (output / "haiku-results.json").exists():
        return
    deadline = time.monotonic() + args.batch_timeout
    while True:
        batch = http("GET", ANTHROPIC_URL + "/" + saved["id"], headers).json()
        print("Haiku batch:", batch["processing_status"], batch["request_counts"], flush=True)
        if batch["processing_status"] == "ended":
            break
        if time.monotonic() >= deadline:
            raise RuntimeError("Batch still running; rerun to collect the same batch")
        time.sleep(30)
    saved["ended_at"] = batch["ended_at"]
    save(path, saved)
    response = http("GET", ANTHROPIC_URL + "/" + saved["id"] + "/results", headers)
    results = []
    for line in response.text.splitlines():
        item = json.loads(line)
        index = int(item["custom_id"])
        result = {"full_name": inputs[index]["full_name"], "raw": item,
                  "status": item["result"]["type"]}
        if result["status"] == "succeeded":
            message = item["result"]["message"]
            result["usage"] = message["usage"]
            result["cost"] = haiku_cost(message["usage"])
            tool = next((b["input"] for b in message["content"]
                         if b["type"] == "tool_use" and b["name"] == "classify_repo"), None)
            if tool:
                result["classification"] = normalise_result(tool, tax)
            else:
                result["status"] = "invalid"
        results.append(result)
    save(output / "haiku-results.json", results)


def jaccard(a, b):
    union = set(a) | set(b)
    return len(set(a) & set(b)) / len(union) if union else 1.0


def summarise(output, inputs):
    haiku = read(output / "haiku-results.json")
    jev = [read(output / f"jev-{i:03d}.json") for i in range(len(inputs))]
    h_by_name = {r["full_name"]: r for r in haiku}
    pairs = [(h_by_name[j["full_name"]], j) for j in jev
             if j["full_name"] in h_by_name
             and h_by_name[j["full_name"]].get("classification") and j.get("classification")]
    h_cost = sum(r.get("cost", 0) for r in haiku)
    billed_jev = [r for r in jev if "usage" in r["raw"]]
    j_cost = sum(numeric(r["raw"]["usage"]["cost"]) for r in billed_jev)
    times = sorted(r["seconds"] for r in jev if r.get("status") == "succeeded")
    paired_h_cost = sum(h.get("cost", 0) for h, j in pairs)
    paired_j_cost = sum(j["raw"]["usage"]["cost"] for h, j in pairs)
    batch = read(output / "haiku-batch.json")
    seconds = (datetime.fromisoformat(batch["ended_at"].replace("Z", "+00:00"))
               - datetime.fromisoformat(batch["submitted_at"])).total_seconds()
    summary = {"repos": len(inputs), "readmes_present": sum(bool(r["readme"]) for r in inputs),
               "paired_results": len(pairs), "haiku": {
                   "cost_usd_from_usage_at_batch_rates": h_cost,
                   "cost_per_1000_submitted": h_cost / len(inputs) * 1000,
                   "input_tokens": sum(r.get("usage", {}).get("input_tokens", 0) for r in haiku),
                   "output_tokens": sum(r.get("usage", {}).get("output_tokens", 0) for r in haiku),
                   "batch_completion_seconds": seconds,
                   "valid_results": sum(bool(r.get("classification", {}).get("subcategories")) for r in haiku)},
               "jev": {"cost_usd_reported": j_cost,
                       "cost_per_1000_submitted": j_cost / len(inputs) * 1000,
                       "input_tokens": sum(r["raw"]["usage"]["input_tokens"] for r in billed_jev),
                       "output_tokens": sum(r["raw"]["usage"]["output_tokens"] for r in billed_jev),
                       "rejected_inputs": sum(r.get("status") == "rejected" for r in jev),
                       "request_p50_seconds": statistics.median(times) if times else None,
                       "request_p95_seconds": times[max(0, math.ceil(len(times) * 0.95) - 1)] if times else None,
                       "valid_results": sum(bool(r.get("classification", {}).get("subcategories")) for r in jev)},
               "savings_percent_before_platform_fees": (1 - j_cost / h_cost) * 100 if h_cost else None,
               "paired_cost_comparison": {"repos": len(pairs),
                   "haiku_usd": paired_h_cost, "jev_usd": paired_j_cost,
                   "haiku_per_1000": paired_h_cost / len(pairs) * 1000 if pairs else None,
                   "jev_per_1000": paired_j_cost / len(pairs) * 1000 if pairs else None,
                   "savings_percent": (1 - paired_j_cost / paired_h_cost) * 100 if paired_h_cost else None},
               "limitations": ["Agreement is not accuracy; existing labels are not verified ground truth.",
                               "Jev threshold is uncalibrated; reason is unavailable.",
                               "Haiku batch completion and Jev per-request latency measure different things.",
                               "Provider usage costs exclude platform purchase fees and tax."]}
    jev_run = read(output / "jev-run.json")
    summary["jev"]["wall_completion_seconds"] = (
        datetime.fromisoformat(jev_run["ended_at"]) - datetime.fromisoformat(jev_run["started_at"])
    ).total_seconds()
    summary["limitations"].append("Jev wall time includes any interruption/resume gap.")
    disagreements = []
    if pairs:
        summary["category_agreement"] = sum(h["classification"]["category"] == j["classification"]["category"]
                                            for h, j in pairs) / len(pairs)
        for field in ("subcategories", "keywords"):
            summary[field + "_mean_jaccard"] = statistics.mean(
                jaccard(h["classification"][field], j["classification"][field]) for h, j in pairs)
        for h, j in pairs:
            a, b = h["classification"], j["classification"]
            if a["category"] != b["category"] or any(set(a[f]) != set(b[f]) for f in ("subcategories", "keywords")):
                disagreements.append({"full_name": h["full_name"], "haiku": a, "jev": b})
    save(output / "summary.json", summary)
    save(output / "disagreements.json", disagreements)
    print(json.dumps(summary, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--threshold", type=float, default=0.5)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--batch-timeout", type=int, default=1800)
    args = parser.parse_args()
    if not 1 <= args.limit <= 100 or not 0 <= args.threshold <= 1 or not 1 <= args.workers <= 8:
        parser.error("limit must be 1-100, threshold 0-1, workers 1-8")
    load_dotenv(Path(__file__).parent / ".env")
    required = ("ANTHROPIC_API_KEY", "OPENROUTER_API_KEY", "TURSO_DATABASE_URL", "TURSO_AUTH_TOKEN")
    missing = [k for k in required if not os.environ.get(k)]
    if missing or not github_token():
        raise RuntimeError("Missing credentials: " + ", ".join(missing + ([] if github_token() else ["GitHub token"])))
    for host in ("api.anthropic.com", "openrouter.ai", "api.github.com",
                 urlparse(os.environ["TURSO_DATABASE_URL"].replace("libsql://", "https://")).hostname):
        try:
            socket.getaddrinfo(host, 443)
        except OSError:
            # Do not print the private database hostname.
            raise RuntimeError("Network preflight failed: DNS unavailable; no inference submitted") from None
    tax = load_taxonomy()
    questions = jev_questions(tax)
    config = {"limit": args.limit, "seed": args.seed, "threshold": args.threshold,
              "haiku_model": MODEL, "jev_model": JEV_MODEL, "workers": args.workers,
              "taxonomy_hash": hashlib.sha256(json.dumps({"system": build_system_prompt(tax),
                  "tool": build_tool(tax), "questions": questions}, sort_keys=True).encode()).hexdigest()}
    output = args.output
    output.mkdir(parents=True, exist_ok=True)
    manifest = output / "config.json"
    if manifest.exists() and read(manifest) != config:
        raise RuntimeError("Config changed; use a new output directory")
    save(manifest, config)
    inputs = prepare_inputs(args, output, tax)
    print(f"Testing {len(inputs)} repos; {len(questions)} Jev decisions per repo", flush=True)
    jev_run_path = output / "jev-run.json"
    jev_run = read(jev_run_path) if jev_run_path.exists() else {
        "started_at": datetime.now(timezone.utc).isoformat()}
    save(jev_run_path, jev_run)
    # Validate full question set on one repo before submitting more paid work.
    run_jev(inputs[0], 0, args, output, tax, questions)
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(run_jev, repo, i, args, output, tax, questions)
                   for i, repo in enumerate(inputs[1:], start=1)]
        for count, future in enumerate(as_completed(futures), start=2):
            future.result()
            print(f"Jev {count}/{len(inputs)} complete", flush=True)
    if "ended_at" not in jev_run:
        jev_run["ended_at"] = datetime.now(timezone.utc).isoformat()
        save(jev_run_path, jev_run)
    run_haiku(inputs, args, output, tax)
    summarise(output, inputs)


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, requests.RequestException) as error:
        # Exception messages from requests may contain private endpoints.
        message = str(error) if isinstance(error, RuntimeError) else type(error).__name__
        raise SystemExit(message) from None
