# Jev refinement: category-first experiment

Prepared 3 October 2026. Live evaluation stopped when OpenRouter returned HTTP 402, insufficient credits. Account credit metadata reports $10 total credits and $10.254051638 total usage, with no per-key spending limit. This account usage includes other activity; it is not the cost of this experiment.

No new successful category responses or reported inference usage were saved. The attempted run is retained in ignored `outputs/classifier-benchmark-jev-tuned-v3/`, including pending markers from the rejected concurrent attempt. Haiku was not rerun. No new comparison scores are available.

## Candidate

- Make a separate primary-category decision, with explicit artifact boundaries and category-specific reference descriptions from the existing 59-repo tuning cohort. Exclude the target's own description from references. No holdout labels enter the prompt.
- Keep the new category prompt only if category matching improves on the tuning cohort; otherwise reuse the previous saved Jev category decisions for the experiment and disclose estimated deployable category-stage cost.
- Score 63 subcategories and 113 keywords in a second request, using Jev's predicted category as context while allowing roles across categories.
- Add concrete role criteria from tuning-set disagreements. Preserve the 1,200-character description cap and frozen README excerpts.
- Fit thresholds on the tuning cohort, then evaluate on the same 41-repo exploratory holdout and compare with the saved Haiku batch and previous Jev variant.

The runner now checks credits before inference, tests one category request before concurrent work, and removes pending markers for confirmed HTTP 402 rejections. Unknown transport failures retain markers to avoid silent repeated billing.

## Resume after adding credits

Use a fresh output directory to preserve the unfunded attempt's uncertain markers:

```sh
uv run --python 3.11 --with requests --with python-dotenv python scraper/refine_jev_benchmark.py --baseline outputs/classifier-benchmark-2026-10-01 --previous outputs/classifier-benchmark-jev-tuned-v2 --output outputs/classifier-benchmark-jev-tuned-v3-funded
```

The command calls only OpenRouter. It reads and hashes the existing Haiku result file. Completed responses in the new directory can be resumed with the same command. Twenty-three local tests pass across the classifier and benchmark runners.
