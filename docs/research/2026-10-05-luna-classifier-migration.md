# Luna classifier migration

The daily classifier now uses `gpt-6-luna` through OpenAI Batch. The taxonomy,
4,000-character README excerpts, written reasons, five-subcategory/six-keyword
caps and 0.6 auto-accept threshold are preserved. Reasoning is disabled. Strict
forced function output replaces Anthropic's forced tool output; malformed,
refused and truncated responses are skipped.

## Credentials and deployment

Set `OPENAI_API_KEY` in `scraper/.env` and the repository's Actions secrets.
README fetching still uses `STATS_GH_PAT`, matching discovery. The old Anthropic
secret can remain; the daily workflow no longer uses it.

These changes take effect in scheduled Actions after the commit reaches the
default branch. Local verification does not prove a scheduled run succeeded.

## Batch resume

[OpenAI Batch](https://developers.openai.com/api/docs/guides/batch) uses a
24-hour completion window. Each invocation polls for up to 30 minutes, then
retains the batch ID and requests in `outputs/classifier-state/batch.json`.
The next invocation collects that batch before submitting new repos. Actions
restores the latest state artifact for the same branch and saves state even
when classification fails. A completed run saves an empty state directory with
`.keep`, so older pending artifacts are not restored.

Do not run two local classifiers with the same state directory. An ambiguous
submission retains a guard and stops retries. Inspect the OpenAI Batch dashboard
before resolving that guard. Definitive HTTP rejections clear it. Output IDs
map directly to repo names; database updates only affect candidates still `new`,
preserving later manual decisions and making replay safe.

## Benchmark

The Luna-only runner uses the original frozen 100-repo metadata and README
inputs and reads saved Haiku results. It makes no Anthropic request and writes
no production classifications.

```sh
uv run --python 3.11 --with-requirements scraper/requirements.txt python scraper/benchmark_luna.py --output outputs/classifier-benchmark-luna-2026-10-05
```

Rerun the exact command to collect a pending batch. Input, request and Haiku
checksums prevent accidental changes during resume. Raw responses, token usage,
cost estimates, category disagreements and summary metrics are saved locally.

[GPT-6 Luna rates](https://developers.openai.com/api/docs/models/gpt-6-luna)
are $0.05 input and $0.25 output per million tokens for Batch. Cached input costs
$0.005 and cache writes $0.0625. The benchmark accounts for returned cache read
and write counts; output totals include any reasoning tokens. One successful
standard-rate smoke request is separate from benchmark Batch spend.

Agreement with Haiku is not verified accuracy. Retaining the 0.6 threshold
preserves the existing policy; this benchmark does not calibrate Luna confidence.

## Verification and current benchmark status

All 45 scraper tests pass. Workflow YAML and embedded shell syntax pass local
checks. A live Luna request returned a valid classification with a written
reason and zero reasoning tokens. No production database classifications were
written during verification.

The 100-repo benchmark is submitted as
`batch_6ac3a811bbd48190b4c4614c0c905613`. At this update it is still processing,
with 70 completed requests and zero reported failures. OpenAI has not released
the output file yet, so final cost and label agreement remain unavailable. The
runner saves them when the batch ends; the same command resumes collection if
the local polling timeout is reached. Haiku results remain unchanged, SHA-256
`90772c5945063d75994c0e4e030451bad514bec4ea23b319379158b4cd99dce1`.
