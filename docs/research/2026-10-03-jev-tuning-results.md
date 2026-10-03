# Jev tuning against the saved Haiku batch

Completed 3 October 2026. Reran only Jev, in two 100-repo variants. The saved Haiku results were reused and their SHA-256 remained unchanged: `90772c5945063d75994c0e4e030451bad514bec4ea23b319379158b4cd99dce1`.

The narrower second variant improves overall agreement, mainly keywords, and handles the previously rejected input. It remains materially different from Haiku. No production classifier or database rows were changed.

## Changes and method

- Freeze the original 100 metadata/README snapshots; no GitHub refresh or Haiku requests.
- Stratify by saved Haiku category with seed 73: 59 tuning repos and 41 holdout repos. Threshold fitting uses tuning labels only.
- First variant: structured inputs, clearer artifact/category guidance, positive/negative tag criteria, and 14 labelled examples selected solely from the tuning cohort. Exclude the target's own example when classifying tuning repos. This reduced category agreement, so it was not selected.
- Second variant: preserve the original category/subcategory questions and system policy. Add positive/negative criteria only to keywords, rejecting incidental implementation technology, dependencies and passing mentions. Remove examples.
- Cap descriptions at 1,200 characters. Only `cirosantilli/china-dictatroship-7` changes; its original description has 64,815 characters. README excerpts stay unchanged at 4,000 characters.
- Fit subcategory thresholds by parent category and keyword thresholds by taxonomy group. Search 0.10-0.95 in 0.05 steps, maximising mean tuning-set Jaccard. Keep caps of five subcategories and six keywords. If no subcategory passes, choose the highest-probability role. This fallback enforces the existing nonempty-subcategory contract; it does not prove that role is correct.

The same holdout was evaluated for both variants. These are exploratory results, not an untouched final acceptance test. Haiku is the requested matching target, not independently verified ground truth.

## Agreement on the same 99 originally comparable repos

| Variant | Category agreement | Subcategory overlap | Keyword overlap |
| --- | ---: | ---: | ---: |
| Original Jev | 78.8% | 47.5% | 32.8% |
| Original probabilities, threshold fitting only | 78.8% | 51.0% | 42.5% |
| First prompt variant, fitted thresholds | 73.7% | 48.2% | 43.0% |
| Selected second variant, fitted thresholds | **79.8%** | **51.5%** | **46.1%** |

Overlap is mean per-repo Jaccard: shared labels divided by the union of both label sets. Category matching improves by one repo on this comparison. The largest improvement is keyword overlap, up 13.3 percentage points.

## Holdout check on the same 40 comparable repos

| Metric | Original Jev | Selected variant |
| --- | ---: | ---: |
| Category agreement | 87.5% | 87.5% |
| Subcategory overlap | 52.61% | 52.58% |
| Keyword overlap | 34.18% | **47.23%** |

The keyword gain survives the holdout check. Category/subcategory agreement does not materially improve there. The 41st holdout repo is the overlong description rejected by original Jev; it now returns successfully but is excluded from the matched holdout table.

## Price, timing and response coverage

The selected variant returns 100/100 responses, versus original Jev's 99/100. Decoding produces a subcategory for all 100, including the explicit highest-probability fallback where needed.

| Cost comparison | Saved Haiku Batch | Selected Jev variant |
| --- | ---: | ---: |
| Same 99 responses | $0.285366 | $0.054957 |
| Per 1,000, extrapolated from those 99 | $2.88248 | $0.55512 |
| All 100 responses | $0.316144 | $0.055551 |

The fair matched comparison is **80.7% cheaper than Haiku**. Jev's new keyword criteria increase its cost relative to the original Jev run. Costs exclude platform credit-purchase fees and tax. Jev costs are returned `usage.cost`; Haiku costs use its existing saved usage at batch rates.

The selected run took 15.99 seconds including threshold fitting between cohorts, with 0.512-second median request latency. It used four workers. Both new Jev experiments together cost **$0.132253**. No new Haiku cost was incurred.

## Files and rerunning

The selected experiment is in ignored `outputs/classifier-benchmark-jev-tuned-v2/`: raw responses, config, split, fitted thresholds, final classifications and summary. The first variant is retained in `outputs/classifier-benchmark-jev-tuned-v1/`. Existing baseline evidence stays in `outputs/classifier-benchmark-2026-10-01/`.

```sh
uv run --python 3.11 --with requests --with python-dotenv python scraper/tune_jev_benchmark.py --baseline outputs/classifier-benchmark-2026-10-01 --output outputs/classifier-benchmark-jev-tuned-v2 --variant bounded
```

Completed responses are reused; the command has no Anthropic submission path. Use a new output directory for changed experiment settings. Twenty local tests pass, including checking the split, excluding holdout labels from examples, bounding the input and verifying the rerun transport targets only Jev.

Recommendation: retain this variant for further evaluation, but keep Haiku in production until disagreement review and a fresh evaluation set establish acceptable label quality. [Original measured benchmark](2026-10-03-classifier-benchmark-results.md).
