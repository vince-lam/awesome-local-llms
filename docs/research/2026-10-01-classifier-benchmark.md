# Classifier benchmark

## Status

Completed on 3 October 2026 after replacing the local GitHub token. See [measured results](2026-10-03-classifier-benchmark-results.md). The Actions secret was left unchanged. The earlier blocked runs below describe setup history.

Runner prepared; live comparison blocked on 1 October 2026. The key names in `scraper/.env` are present and nonempty, including `OPENROUTER_API_KEY`. Authentication and credit balance remain unverified. This agent session cannot resolve OpenRouter, Anthropic or GitHub. No inference was submitted and no production classifications were changed.

On 2 October, a terminal run reached GitHub but failed with `GitHub metadata HTTP 401`, before model inference. GitHub rejected the token selected by the runner. Replace the corresponding token in `scraper/.env` and check for a stale exported value overriding it. The runner now names the selected environment variable on this error without printing its value.

Fifteen local tests pass, covering the existing classifier and benchmark. A test compares the benchmark's Haiku request directly with the production batch request builder. Other checks cover full taxonomy decisions, cross-category tags, caps, usage validation, pricing, summary calculations, rejected GitHub credentials, rejected model inputs and avoiding repeated completed or ambiguous calls.

## Run

From the repository root, in a terminal with network access:

```sh
uv run --python 3.11 --with requests --with python-dotenv python scraper/benchmark_classifiers.py --output outputs/classifier-benchmark-2026-10-01
```

Rerun the same command to resume. Inputs, settings, raw responses and the Anthropic batch ID are saved. Completed results are reused. A transport failure with uncertain billing leaves a pending marker; check provider activity before removing that marker or retrying. Do not start two processes with the same output directory.

## Method

- Read-only sample of 100 curated repos from Turso, selected round-robin across existing categories with seed 42. This balanced sample is not an estimate of the production category distribution.
- Fetch public GitHub metadata and the first 4,000 README characters once. Save this input snapshot and use it for both models. Missing READMEs remain missing for both.
- Haiku uses the current model, prompt, forced tool and 512-token output limit through Anthropic's Message Batches API. One batch of 100 fits within the existing 300-repo chunk size. Poll every 30 seconds, with a 30-minute timeout; a later run collects the same batch.
- Jev uses one primary-category Choice and 176 independent Noul tag decisions in each request. Validate the full question set on one repo before processing the rest with four workers. Tag probability threshold is initially 0.5, capped at five subcategories and six keywords. This threshold is uncalibrated. Jev cannot produce the Haiku written reason.
- Haiku cost comes from returned usage at current batch rates. Jev cost comes from returned `usage.cost`. Costs exclude platform purchase fees and tax. No automatic paid-request retries run.
- Compare category agreement and mean Jaccard overlap for subcategories and keywords. Agreement is not accuracy. Existing labels guide sampling; they are not independently verified ground truth. Report costs separately for the shared response set when one model rejects an input.
- Report Jev request P50/P95 and wall completion time, plus Haiku batch completion time. Haiku batch queue time and Jev request latency are different metrics. Jev wall time includes any interruption before resuming.

## Outputs

The ignored `outputs/classifier-benchmark-2026-10-01/` directory contains frozen inputs, config, raw model responses, usage and timing. When both providers finish, `summary.json` contains costs, token counts, valid-result counts and agreement. `disagreements.json` contains repo names and both classifications for manual review. Early failures retain any saved responses for investigation rather than presenting an incomplete comparison as a result.

Sources: [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), [Jev Decisions API](https://openrouter.ai/docs/api/api-reference/alphadecisions/submit-a-decisions-request), [Jev classification cookbook](https://openrouter.ai/docs/cookbook/evaluate-and-optimize/jev-classification).
