"""Test category-first Jev classification using frozen inputs and saved Haiku labels."""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import os
from pathlib import Path
import time

from dotenv import load_dotenv

try:
    from . import benchmark_classifiers as base
    from . import tune_jev_benchmark as tuning
except ImportError:
    import benchmark_classifiers as base
    import tune_jev_benchmark as tuning


CATEGORY_HINTS = {
    "applications": "Finished tools for end users: assistants, productivity, QA/mobile testing, Minecraft modding, specialised domain applications.",
    "ai-engineering": "Reusable agent SDKs, multi-agent systems, MCP integrations/clients, agent frontends, IDE integrations, installable Agent Skills and reusable agent prompting.",
    "infrastructure": "Model runtime/serving, embedding and vector retrieval libraries, gateways, operational data and model-pricing/configuration databases that power gateways.",
    "model-development": "Research/training implementations and frameworks, fine-tuning workflows, NLP training/data processing, reflective evolution and learning algorithms. Fine-tuning projects can belong here even when they publish a model.",
    "models": "The main delivered artifact is a model or model-family release, weights, audio/speech/image models or specialised pretrained models.",
    "lists": "Collections of resources, tools, skills, prompts, icons, papers, datasets or benchmark data. Dataset/benchmark releases with scripts and baselines are collections, unless operational infrastructure is their purpose.",
    "tutorials": "Guides, courses, roadmaps, learning labs and educational walkthroughs. A reusable example prompt does not by itself make an educational guide a framework.",
    "misc": "Last resort when no other role fits. Do not use merely because a concrete application/resource lacks an LLM or has an unfamiliar name.",
}

ROLE_HINTS = {
    "productivity": "End-use help with work, study, documentation, team QA or knowledge management, rather than a generic reusable library.",
    "domain-specific": "End-use application specialised for a domain such as course revision, legal documents, database work, QA/mobile testing or Minecraft modding.",
    "research-assistant": "An end-use research/knowledge analysis or repository understanding and wiki tool.",
    "automation": "Actually automates repeated user workflows or testing, beyond merely exposing a callable API.",
    "coding": "Helps an end user create, understand or modify code; coding assistant, IDE/code-review or screen-guided coding tool.",
    "agent-sdk": "Provides a reusable agent framework or multi-agent implementation/integration with agent-facing tools, not merely a chatbot UI.",
    "agent-ui": "Frontend or companion interface for agents: conversations, diffs, workspace/task management.",
    "deploy-to-users": "Helps run, integrate or distribute agent workflows to users, including an agent-facing CLI integration.",
    "prompting-scaffolding": "Reusable prompting, structured workflows/methodologies or agent scaffolding; can coexist with an educational role.",
    "training-toolkits": "Research or training implementation/framework including optimisation, hyper-heuristic evolution, backdoor research, or NLP learning pipelines.",
    "training": "Implements a learning/training procedure or research optimisation method.",
    "interpretability": "Investigates model behaviour, recognition limits, backdoors, robustness or alignment through research implementations.",
    "dataset-engineering": "Data preparation, tokenisation, NLP pipelines or code/data supporting model research; not a dataset/benchmark collection alone.",
    "dataset-collections": "A released dataset or benchmark-data collection with associated evaluation scripts/baselines, rather than primarily a data-processing toolkit.",
    "tool-collections": "Curated reusable resources, tools, skills or icon assets, rather than a single application's dependencies.",
    "tool-tutorials": "Teaching a concrete AI tool, coding agent, workflow or implementation technique.",
    "getting-started": "Introductions, courses or hands-on learning materials helping learners start using or building AI.",
    "vector-search": "Libraries for producing, finding or consuming vector embeddings and vector retrieval/indexing.",
    "data-systems": "Operational databases or structured data/configuration pipelines used by model/LLM infrastructure.",
    "gateway": "LLM gateway/routing infrastructure, including operational model metadata/pricing that powers a gateway.",
    "local-runtime": "Executes model inference locally or in a self-hosted inference process, including transcription inference.",
    "serving": "Serves model inference to clients, including real-time self-hosted transcription servers.",
    "inference-optimization": "Explicit inference backends or acceleration such as TensorRT, OpenVINO, quantisation or optimised runtimes.",
    "memory-knowledge": "Reusable agent retrieval/knowledge/memory component, not every app which happens to store data.",
}


def category_question(tax, references, target_name):
    criteria = {}
    for cat in tax.categories:
        examples = [e["description"] for e in references if e["name"] != target_name
                    and e["classification"]["category"] == cat["slug"]]
        criteria[cat["slug"]] = CATEGORY_HINTS[cat["slug"]]
        if examples:
            criteria[cat["slug"]] += " Examples of this category: " + " | ".join(examples)
    return {"category": {"type": "choice", "criteria": criteria,
                         "instructions": "Classify state.repository only by its primary delivered artifact. Choose the closest role under these category conventions, not its incidental dependencies."}}


def role_questions(tax):
    questions = tuning.questions(tax)
    questions.pop("category")
    for cat in tax.categories:
        for sub in cat["subcategories"]:
            hint = ROLE_HINTS.get(sub["slug"], sub.get("description") or sub["name"])
            questions["sub_" + sub["slug"]] = {
                "type": "noul", "instructions": f"Does state.repository actually deliver the role {sub['name']}?",
                "criteria": {"true": hint + " Its documented implemented role warrants this label.",
                             "false": "Merely mentioned, an incidental dependency, an unrealised plan or unrelated capability."}}
    return questions


def call(stage, repo, index, output, questions, category=None):
    path = output / f"{stage}-{index:03d}.json"
    if path.exists():
        return base.read(path)
    pending = output / f"{stage}-{index:03d}-pending.json"
    if pending.exists():
        raise RuntimeError("Ambiguous Jev call; check provider activity before retrying")
    state = {"repository": tuning.target(repo)}
    if category:
        state["predicted_primary_category"] = category
        state["policy"] = (
            "The predicted primary category is a useful hint, not a hard constraint. "
            "Roles may span categories. Evaluate only the target repository. "
            "Select implemented defining roles and substantive AI facets; ignore incidental technologies.")
    base.save(pending, {"full_name": repo["full_name"]})
    started = time.monotonic()
    try:
        body = base.http("POST", base.JEV_URL, {"Authorization": "Bearer " + os.environ["OPENROUTER_API_KEY"]},
                         {"model": base.JEV_MODEL, "state": state, "questions": questions}).json()
    except base.ProviderHTTPError as error:
        if error.status == 402:
            # A definitive rejected request can be retried after credits are restored.
            base.save(output / f"{stage}-{index:03d}-error.json",
                      {"full_name": repo["full_name"], "http_status": 402, "error": str(error)})
            pending.unlink()
        raise
    result = {"full_name": repo["full_name"], "raw": body, "seconds": time.monotonic() - started}
    base.save(path, result)
    pending.unlink()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--previous", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() in (args.baseline.resolve(), args.previous.resolve()):
        parser.error("Use a separate experiment directory")
    load_dotenv(Path(__file__).parent / ".env")
    if not os.environ.get("OPENROUTER_API_KEY"):
        raise RuntimeError("Missing OPENROUTER_API_KEY")
    credits = base.http("GET", "https://openrouter.ai/api/v1/credits",
                        {"Authorization": "Bearer " + os.environ["OPENROUTER_API_KEY"]}).json()["data"]
    if credits["total_credits"] <= credits["total_usage"]:
        raise RuntimeError("OpenRouter credits exhausted; add credits before resuming")
    inputs = base.read(args.baseline / "inputs.json")
    by_name = {r["full_name"]: i for i, r in enumerate(inputs)}
    haiku_bytes = (args.baseline / "haiku-results.json").read_bytes()
    haiku = json.loads(haiku_bytes)
    labels = {r["full_name"]: r["classification"] for r in haiku}
    previous = base.read(args.previous / "classifications.json")
    split = base.read(args.previous / "config.json")
    training, holdout = split["training"], split["holdout"]
    tax = base.load_taxonomy()
    refs = tuning.examples(inputs, labels, training, previous)
    config = {"haiku_sha256": hashlib.sha256(haiku_bytes).hexdigest(),
              "training": training, "holdout": holdout, "references": refs,
              "category_hints": CATEGORY_HINTS, "role_hints": ROLE_HINTS,
              "tag_questions": role_questions(tax), "description_max_chars": 1200}
    args.output.mkdir(parents=True, exist_ok=True)
    path = args.output / "config.json"
    if path.exists() and base.read(path) != config:
        raise RuntimeError("Configuration changed; use a new output directory")
    base.save(path, config)
    rows, categories = {}, {}
    started = time.monotonic()
    # Choose whether to retain this category prompt using only tuning labels.
    def category_phase(names):
        # Check one request before submitting the rest of a cohort.
        first = names[0]
        row = call("category", inputs[by_name[first]], by_name[first], args.output,
                   category_question(tax, refs, first))
        categories[first] = row["raw"]["answers"]["category"]
        rows["category_" + first] = row
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = {pool.submit(call, "category", inputs[by_name[n]], by_name[n], args.output,
                                   category_question(tax, refs, n)): n for n in names[1:]}
            for future in as_completed(futures):
                n = futures[future]
                row = future.result()
                answer = row["raw"]["answers"]["category"]
                if answer["type"] != "choice" or answer["choice"] not in tax.category_slugs:
                    raise RuntimeError("Invalid category response")
                categories[n] = answer
                rows["category_" + n] = row
    category_phase(training)
    new_correct = sum(categories[n]["choice"] == labels[n]["category"] for n in training)
    old_correct = sum(previous[n]["category"] == labels[n]["category"] for n in training)
    selected = new_correct > old_correct
    print(f"Category tuning set: previous={old_correct}/{len(training)}, candidate={new_correct}/{len(training)}; selected={selected}", flush=True)
    if selected:
        category_phase(holdout)
    else:
        # Reuse paid previous Jev choices rather than rerunning a losing prompt.
        categories = {n: {"type": "choice", "choice": r["category"], "confidence": r.get("confidence")}
                      for n, r in previous.items()}
    raw = {}
    for cohort in (training, holdout):
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = {pool.submit(call, "tags", inputs[by_name[n]], by_name[n], args.output,
                                   role_questions(tax), categories[n]["choice"]): n for n in cohort}
            for i, future in enumerate(as_completed(futures), 1):
                n = futures[future]
                row = future.result()
                rows["tags_" + n] = row
                body = {**row["raw"], "answers": {**row["raw"]["answers"], "category": categories[n]}}
                tuning.probabilities(body, tax)
                raw[n] = body
                print(f"Tags {i}/{len(cohort)} complete", flush=True)
        if cohort == training:
            thresholds = tuning.calibrate(raw, labels, training, tax)
            base.save(args.output / "thresholds.json", thresholds)
    classifications = {n: tuning.decode(body, tax, thresholds) for n, body in raw.items()}
    base.save(args.output / "classifications.json", classifications)
    direct_cost = sum(r["raw"]["usage"]["cost"] for r in rows.values())
    # If categories were reused, estimate deployable category-stage cost using this tuning-set run.
    category_cost = sum(r["raw"]["usage"]["cost"] for k, r in rows.items() if k.startswith("category_"))
    tags_cost = direct_cost - category_cost
    projected_cost = direct_cost if selected else tags_cost + category_cost / len(training) * len(inputs)
    summary = {"category_prompt_selected_on_training": selected,
               "category_training_correct": {"previous": old_correct, "candidate": new_correct},
               "haiku_rerun": False, "haiku_sha256": config["haiku_sha256"],
               "jev_experiment_cost_usd": direct_cost, "jev_pipeline_cost_for_100": projected_cost,
               "pipeline_cost_is_estimated": not selected,
               "wall_seconds": time.monotonic() - started,
               "previous": {"all": tuning.metrics(previous, labels, labels),
                            "training": tuning.metrics(previous, labels, training),
                            "holdout": tuning.metrics(previous, labels, holdout)},
               "candidate": {"all": tuning.metrics(classifications, labels, labels),
                             "training": tuning.metrics(classifications, labels, training),
                             "holdout": tuning.metrics(classifications, labels, holdout)}}
    summary["haiku_saved_cost_usd"] = sum(r["cost"] for r in haiku)
    summary["pipeline_savings_percent"] = (1 - projected_cost / summary["haiku_saved_cost_usd"]) * 100
    if hashlib.sha256((args.baseline / "haiku-results.json").read_bytes()).hexdigest() != config["haiku_sha256"]:
        raise RuntimeError("Haiku baseline changed")
    base.save(args.output / "summary.json", summary)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
