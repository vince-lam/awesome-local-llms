# Jev versus Haiku: measured repo classification results

Run completed 3 October 2026. Jev was 87.2% cheaper on the 99 shared responses, but its untuned labels differ substantially. Keep Haiku in production pending manual review and threshold calibration.

## Measured results

100 repos, balanced across the eight existing categories with seed 42. Both models received identical public GitHub metadata and 4,000-character README excerpts; all 100 READMEs were fetched. Haiku used the current Batch API request. Jev used 177 typed decisions per repo and a 0.5 tag threshold, with four concurrent workers. Production classifications and Actions secrets were not changed.

| Metric | Haiku 4.5 Batch | Jev 1.13 |
| --- | ---: | ---: |
| Successful model responses | 100/100 | 99/100 |
| Usable classifications with at least one subcategory | 100/100 | 97/100 |
| Cost for all returned responses | $0.316144 | $0.036487 |
| Cost on 99 shared responses | $0.285366 | $0.036487 |
| Cost per 1,000, extrapolated from shared responses | $2.88248 | $0.368556 |
| Completion time | 110.97 seconds, asynchronous batch | 13.78 seconds, four workers |
| Successful request latency P50 / P95 | Not available from Batch API | 0.513 / 0.571 seconds |
| Total reported input / output tokens | 548,512 / 16,755 | 868,740 / 342,794 |

Costs exclude credit purchase/platform fees and tax. Haiku cost is calculated from returned token usage at batch rates; Jev cost is reported by OpenRouter. Jev output tokens are free. Prices checked against [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) and [OpenRouter](https://openrouter.ai/typesafe/jev-1.13) on the run date.

The 99-response comparison is the meaningful cost comparison: the rejected input alone cost Haiku $0.030778. Comparing all submitted inputs gives 88.5% lower Jev spend, but includes a task Jev did not complete. Jev's timing excludes the subsequent diagnostic retry; it ends at the last successful result. Model completion times exclude the shared GitHub input-fetching phase. Batch queue time and synchronous request latency are different metrics.

## Agreement and failures

On the 99 shared responses:

- Primary category agreement: **78/99, or 78.8%**.
- Mean subcategory Jaccard overlap: **47.5%**.
- Mean keyword Jaccard overlap: **32.8%**.
- Every repo differed on at least one category or tag.

Jaccard is shared labels divided by the union of both label sets, averaged per repo. These are agreement metrics, not accuracy: neither model is verified ground truth. The shared response set includes two Jev results without a selected subcategory.

Jev selected no subcategory for `ai4co/reevo` and `Portkey-AI/models` at threshold 0.5. Its other 97 responses met the existing requirement for at least one subcategory.

`cirosantilli/china-dictatroship-7` has a 64,815-character GitHub description. OpenRouter rejected its original input with HTTP 400, `max_tokens_exceeded`. One diagnostic retry reproduced that validation error and returned no usage. No shortened input was substituted. Haiku handled the same original input. A production Jev path would need an explicit input limit or fallback for such cases.

Category disagreements include skill collections, datasets/benchmarks and tools that sit between applications and infrastructure. For example, Haiku chose `lists` and Jev `ai-engineering` for `VoltAgent/awesome-agent-skills`; Haiku chose `lists` and Jev `model-development` for `taoyds/spider`. Manual review should resolve the intended taxonomy rather than automatically preferring Haiku.

## Recommendation and evidence

Keep the current Haiku classifier for now. Review disagreements against the frozen descriptions and README excerpts. Calibrate subcategory/keyword probabilities on a human-labelled subset, then evaluate on a separate held-out sample. Jev's category confidence cannot replace Haiku's overall 0.6 acceptance threshold directly, and Jev provides no written reason.

If quality improves, consider Jev for clear cases with Haiku fallback for ambiguous, overlong or incomplete results. Include fallback cost when estimating savings. At these shared-response rates, 10,000 classifications would save about **$25.14** before platform fees, assuming the same input distribution and no fallback.

Local raw evidence is retained in the ignored `outputs/classifier-benchmark-2026-10-01/` directory: `inputs.json`, `config.json`, `jev-*.json`, `haiku-results.json`, `haiku-batch.json`, `summary.json` and `disagreements.json`. The folder name reflects setup date; the actual measured run occurred on 3 October. Raw files are excluded from Git. [Runner and method](2026-10-01-classifier-benchmark.md).
