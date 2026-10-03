"""Rerun Jev only against saved Haiku responses; never submit an Anthropic request."""

import argparse
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import random
import statistics
import time

from dotenv import load_dotenv

try:
    from . import benchmark_classifiers as base
except ImportError:
    import benchmark_classifiers as base


POLICY = """Classify only state.repository. Reference examples illustrate the labelling convention;
do not classify or merge their content into the target. Choose what the repository primarily
delivers, not everything it mentions. Subcategories may span categories. Prefer specific roles
over broad incidental capabilities. Keywords describe essential AI techniques, integrations,
modalities and domains. A keyword is not warranted solely by implementation language, platform,
UI, an incidental dependency, an API, or a passing mention. Empty keyword selections are fine.
For categories: Applications are end-use assistants and tools; AI Engineering comprises reusable
agent frameworks, integrations and building blocks. Infrastructure runs/serves/optimises models.
Model Development covers training/fine-tuning code and research implementations. Models covers
released model weights and model families. Lists includes curated resources, skill/tool/prompt
collections, and datasets/benchmarks distributed as collections. Tutorials includes educational
guides, roadmaps and courses. Misc is a last resort. Match the conventions of the examples.
"""


def split(labels, seed=73):
    groups = defaultdict(list)
    for name, result in labels.items():
        groups[result["category"]].append(name)
    rng = random.Random(seed)
    training, holdout = [], []
    for names in groups.values():
        names = sorted(names)
        rng.shuffle(names)
        cut = max(1, round(len(names) * 0.6)) if len(names) > 1 else 0
        training.extend(names[:cut])
        holdout.extend(names[cut:])
    return sorted(training), sorted(holdout)


def target(repo):
    return {"name": repo["full_name"], "description": (repo.get("description") or "")[:1200],
            "topics": repo.get("topics") or [], "readme": repo.get("readme") or "",
            "implementation_language": repo.get("language")}


def examples(inputs, labels, training, old):
    by_name = {r["full_name"]: r for r in inputs}
    groups = defaultdict(list)
    for name in training:
        groups[labels[name]["category"]].append(name)
    selected = []
    for names in groups.values():
        # Learn category-boundary examples from the tuning cohort only.
        names.sort(key=lambda n: (old.get(n, {}).get("category") == labels[n]["category"], n))
        for name in names[:2]:
            selected.append({"name": name, "description": (by_name[name].get("description") or "")[:400],
                             "readme_excerpt": (by_name[name].get("readme") or "")[:350],
                             "classification": {k: labels[name][k] for k in ("category", "subcategories", "keywords")}})
    return selected


def questions(tax):
    result = base.jev_questions(tax)
    result["category"]["instructions"] = (
        "Classify state.repository only. Which primary category best matches its delivered artifact "
        "under classification_policy and the reference labelling convention?")
    for cat in tax.categories:
        for sub in cat["subcategories"]:
            role = sub["name"] + ". " + sub.get("description", "")
            result["sub_" + sub["slug"]] = {
                "type": "noul", "instructions": f"For state.repository only, is {role} an actual role?",
                "criteria": {"true": f"Its core deliverable implements or supplies {role} under the reference convention.",
                             "false": "Only mentioned, used incidentally, aspirational, or unrelated to its actual role."}}
    for keyword in tax.keywords:
        label = keyword["name"]
        result["keyword_" + keyword["slug"]] = {
            "type": "noul", "instructions": f"For state.repository only, is {label} a central defining facet?",
            "criteria": {"true": f"Clearly and substantially about {label}; the reference convention warrants this tag.",
                         "false": f"{label} is absent, generic, incidental, or only its implementation technology."}}
    return result


def probabilities(body, tax):
    # Validate complete responses and usage, without imposing the final thresholds yet.
    base.parse_jev(body, tax, 0.5)
    return {field: {slug: body["answers"][prefix + slug]["noul"] for slug in slugs}
            for field, prefix, slugs in (
                ("subcategories", "sub_", tax.subcategory_slugs),
                ("keywords", "keyword_", tax.keyword_slugs))}


def decode(body, tax, thresholds):
    ps = probabilities(body, tax)
    result = {"category": body["answers"]["category"]["choice"],
              "confidence": body["answers"]["category"].get("confidence"), "reason": None}
    groups = label_groups(tax)
    for field, cap in (("subcategories", 5), ("keywords", 6)):
        values = ps[field]
        picked = sorted((s for s, p in values.items() if p >= thresholds[field][groups[field][s]]),
                        key=lambda s: (-values[s], s))[:cap]
        # Existing classifier requires a subcategory; use highest-probability role if uncertain.
        if not picked and field == "subcategories":
            picked = [max(values, key=values.get)]
        result[field] = picked
    return result


def label_groups(tax):
    return {"subcategories": tax.sub_to_cat,
            "keywords": {k["slug"]: k["group"] for k in tax.keywords}}


def calibrate(raw, labels, names, tax):
    groups = label_groups(tax)
    thresholds = {f: {g: 0.5 for g in set(mapping.values())} for f, mapping in groups.items()}
    grid = [i / 20 for i in range(2, 20)]
    valid = [n for n in names if raw.get(n, {}).get("answers")]
    if not valid:
        raise RuntimeError("No usable tuning responses for threshold fitting")
    def objective(field):
        return statistics.mean(base.jaccard(decode(raw[n], tax, thresholds)[field], labels[n][field])
                               for n in valid)
    # Coarse field-wide threshold, then group thresholds; no holdout labels used.
    for field in thresholds:
        candidates = []
        for value in grid:
            thresholds[field] = dict.fromkeys(thresholds[field], value)
            candidates.append((objective(field), -abs(value - 0.5), value))
        best = max(candidates)[2]
        thresholds[field] = dict.fromkeys(thresholds[field], best)
        for _ in range(2):
            for group in sorted(thresholds[field]):
                candidates = []
                for value in grid:
                    thresholds[field][group] = value
                    candidates.append((objective(field), -abs(value - best), value))
                thresholds[field][group] = max(candidates)[2]
    return thresholds


def metrics(classifications, labels, names):
    available = [n for n in names if n in classifications]
    if not available:
        return {"responses": 0}
    return {"responses": len(available), "requested": len(names),
            "category_agreement": sum(classifications[n]["category"] == labels[n]["category"]
                                      for n in available) / len(available),
            **{field + "_mean_jaccard": statistics.mean(
                base.jaccard(classifications[n][field], labels[n][field]) for n in available)
               for field in ("subcategories", "keywords")}}


def rerun(repo, index, output, tax, question_set, reference_examples, variant="examples"):
    path = output / f"jev-{index:03d}.json"
    if path.exists():
        return base.read(path)
    pending = output / f"jev-{index:03d}-pending.json"
    if pending.exists():
        raise RuntimeError("Ambiguous Jev call; check provider activity before retrying")
    if variant == "bounded":
        bounded_repo = {**repo, "description": (repo.get("description") or "")[:1200]}
        state = {"repository": base.format_repo_prompt(bounded_repo),
                 "classification_policy": base.build_system_prompt(tax)}
    else:
        state = {"repository": target(repo), "classification_policy": POLICY,
                 "reference_examples": [e for e in reference_examples if e["name"] != repo["full_name"]]}
    base.save(pending, {"full_name": repo["full_name"]})
    started = time.monotonic()
    try:
        body = base.http("POST", base.JEV_URL, {"Authorization": "Bearer " + os.environ["OPENROUTER_API_KEY"]},
                         {"model": base.JEV_MODEL, "state": state, "questions": question_set}).json()
    except base.ProviderHTTPError as error:
        if error.status not in (400, 413):
            raise
        result = {"full_name": repo["full_name"], "status": "rejected", "error": str(error), "raw": {}}
    else:
        result = {"full_name": repo["full_name"], "status": "invalid", "raw": body,
                  "seconds": time.monotonic() - started}
        base.save(path, result)
        probabilities(body, tax)
        result["status"] = "succeeded"
    base.save(path, result)
    pending.unlink()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--variant", choices=("examples", "bounded"), default="bounded")
    args = parser.parse_args()
    if args.baseline.resolve() == args.output.resolve():
        parser.error("Use a separate output directory")
    load_dotenv(Path(__file__).parent / ".env")
    if not os.environ.get("OPENROUTER_API_KEY"):
        raise RuntimeError("Missing OPENROUTER_API_KEY")
    inputs = base.read(args.baseline / "inputs.json")
    saved_haiku_bytes = (args.baseline / "haiku-results.json").read_bytes()
    haiku = json.loads(saved_haiku_bytes)
    labels = {r["full_name"]: r["classification"] for r in haiku}
    old_rows = [base.read(args.baseline / f"jev-{i:03d}.json") for i in range(len(inputs))]
    old = {r["full_name"]: r["classification"] for r in old_rows if r.get("classification")}
    training, holdout = split(labels)
    tax = base.load_taxonomy()
    question_set = questions(tax)
    refs = examples(inputs, labels, training, old) if args.variant == "examples" else []
    if args.variant == "bounded":
        keyword_questions = {k: v for k, v in question_set.items() if k.startswith("keyword_")}
        question_set = {**base.jev_questions(tax), **keyword_questions}
    config = {"model": base.JEV_MODEL, "variant": args.variant,
              "policy": POLICY if args.variant == "examples" else base.build_system_prompt(tax), "examples": refs,
              "questions": question_set, "description_max_chars": 1200,
              "training": training, "holdout": holdout,
              "haiku_sha256": hashlib.sha256(saved_haiku_bytes).hexdigest(),
              "inputs_sha256": hashlib.sha256((args.baseline / "inputs.json").read_bytes()).hexdigest()}
    args.output.mkdir(parents=True, exist_ok=True)
    config_path = args.output / "config.json"
    if config_path.exists() and base.read(config_path) != config:
        raise RuntimeError("Configuration changed; use a new output directory")
    base.save(config_path, config)
    print(f"Tuning {len(training)} repos; holdout {len(holdout)}; {len(refs)} reference examples", flush=True)
    # Also measure what threshold-only calibration achieves on original probabilities.
    old_raw = {r["full_name"]: r["raw"] for r in old_rows}
    old_thresholds = calibrate(old_raw, labels, training, tax)
    old_calibrated = {n: decode(body, tax, old_thresholds) for n, body in old_raw.items() if body.get("answers")}
    base.save(args.output / "baseline-calibrated-thresholds.json", old_thresholds)
    started = time.monotonic()
    by_name = {repo["full_name"]: i for i, repo in enumerate(inputs)}
    rows = {}
    # Fix examples and prompts before examining new holdout responses.
    for cohort in (training, holdout):
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = [pool.submit(rerun, inputs[by_name[n]], by_name[n], args.output, tax, question_set, refs, args.variant)
                       for n in cohort]
            for i, future in enumerate(as_completed(futures), 1):
                result = future.result()
                rows[result["full_name"]] = result
                print(f"Jev {i}/{len(cohort)} complete in cohort", flush=True)
        if cohort == training:
            raw = {n: rows[n]["raw"] for n in training}
            tuned_thresholds = calibrate(raw, labels, training, tax)
            base.save(args.output / "thresholds.json", tuned_thresholds)
    wall = time.monotonic() - started
    raw = {n: r["raw"] for n, r in rows.items()}
    tuned = {n: decode(body, tax, tuned_thresholds) for n, body in raw.items() if body.get("answers")}
    uncalibrated_thresholds = {field: dict.fromkeys(groups.values(), .5)
                               for field, groups in label_groups(tax).items()}
    uncalibrated = {n: decode(body, tax, uncalibrated_thresholds) for n, body in raw.items() if body.get("answers")}
    paired_names = sorted(set(tuned) & set(old))
    paired_holdout = sorted(set(paired_names) & set(holdout))
    jev_cost = sum(body["usage"]["cost"] for body in raw.values() if body.get("usage"))
    comparison = {"variant": args.variant, "training_repos": len(training), "holdout_repos": len(holdout),
                  "haiku_rerun": False, "haiku_sha256": config["haiku_sha256"],
                  "description_truncated_repos": [r["full_name"] for r in inputs if len(r.get("description") or "") > 1200],
                  "reference_example_count": len(refs), "jev_cost_usd": jev_cost,
                  "jev_cost_per_1000": jev_cost / len(inputs) * 1000,
                  "jev_run_wall_seconds": wall,
                  "jev_request_p50_seconds": statistics.median(r["seconds"] for r in rows.values() if r.get("seconds")),
                  "successful_responses": len(tuned),
                  "baseline": {"all": metrics(old, labels, labels), "holdout": metrics(old, labels, holdout)},
                  "baseline_threshold_only": {"all": metrics(old_calibrated, labels, labels),
                                               "holdout": metrics(old_calibrated, labels, holdout)},
                  "tuned_prompt_threshold_0_5": {"all": metrics(uncalibrated, labels, labels),
                                                   "holdout": metrics(uncalibrated, labels, holdout)},
                  "tuned": {"all": metrics(tuned, labels, labels),
                            "training": metrics(tuned, labels, training), "holdout": metrics(tuned, labels, holdout)},
                  "same_99_repos": {"baseline": metrics(old, labels, paired_names),
                                    "tuned": metrics(tuned, labels, paired_names)},
                  "same_holdout_repos": {"baseline": metrics(old, labels, paired_holdout),
                                         "tuned": metrics(tuned, labels, paired_holdout)},
                  "paired_costs": {
                      "haiku_usd": sum(r["cost"] for r in haiku if r["full_name"] in paired_names),
                      "jev_usd": sum(r["raw"]["usage"]["cost"] for r in rows.values()
                                     if r["full_name"] in paired_names)},
                  "haiku_saved_cost_usd": sum(r["cost"] for r in haiku)}
    comparison["savings_percent"] = (1 - jev_cost / comparison["haiku_saved_cost_usd"]) * 100
    comparison["paired_costs"]["savings_percent"] = (
        1 - comparison["paired_costs"]["jev_usd"] / comparison["paired_costs"]["haiku_usd"]) * 100
    if hashlib.sha256((args.baseline / "haiku-results.json").read_bytes()).hexdigest() != config["haiku_sha256"]:
        raise RuntimeError("Saved Haiku baseline changed during run")
    base.save(args.output / "classifications.json", tuned)
    previous = args.output / "summary.json"
    if previous.exists():
        comparison["jev_run_wall_seconds"] = base.read(previous)["jev_run_wall_seconds"]
    base.save(args.output / "summary.json", comparison)
    print(json.dumps(comparison, indent=2))


if __name__ == "__main__":
    main()
