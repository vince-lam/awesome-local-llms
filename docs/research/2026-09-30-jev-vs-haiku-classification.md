# Jev versus Haiku for repository classification

Checked 30 September 2026. USD, before tax. Research only; no classifier change or paid inference.

Jev has a much lower token rate than the current Haiku Batch implementation. It is worth benchmarking, but exact savings and classification quality remain unmeasured.

## Current implementation

- [`scraper/classifier.py`](../../scraper/classifier.py) selects `claude-haiku-4-5`. Each repository returns one category, up to five subcategories, up to six keywords, confidence and a short reason through a forced tool call. Output is capped at 512 tokens; that cap is not actual usage.
- [`scraper/classify.py`](../../scraper/classify.py) submits Anthropic Message Batches in chunks of 300. Each request repeats the system prompt and tool schema. No prompt caching is configured. Results with confidence at least 0.6 are automatically accepted.
- The taxonomy contains 8 categories, 63 subcategories and 113 keywords. The system prompt plus serialised tool definition occupies 9,736 characters. This is a character count, not a measured token count; tools also incur input overhead.
- README context is capped at 4,000 characters when a GitHub token exists. The classification step in [the daily workflow](../../.github/workflows/discover.yml) passes no GitHub token. Under that checked-in configuration, classification normally uses metadata without README context.
- The scripts do not record response token usage or cost. This research therefore cannot establish the current bill per repository.

## Prices and illustrative costs

| Service | Input per million tokens | Output per million tokens |
| --- | ---: | ---: |
| Current Haiku 4.5 Batch | $0.50 | $2.50 |
| Jev 1.13 through OpenRouter | $0.042 | $0 |

Sources: [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), [Jev model pricing](https://openrouter.ai/typesafe/jev-1.13). Haiku's batch discount is already included. Jev input is approximately 11.9 times cheaper per billed token.

Illustrative scenarios, not measured workload costs:

| Per-repository usage assumption | Cost per 1,000 repositories |
| --- | ---: |
| Haiku Batch: 3,000 input + 150 output tokens | $1.875 |
| Jev: 3,000 input tokens | $0.126 |
| Jev: 6,000 input tokens | $0.252 |

That represents 93.3% savings with equal input counts, or 86.6% if Jev uses twice as many input tokens. Different tokenisers and question formats mean equal input counts are an assumption. At this illustrative Haiku baseline, Jev breaks even at about 44,643 billed input tokens across all requests per repo, before platform fees or Haiku fallback costs.

[OpenRouter Standard pricing](https://openrouter.ai/pricing) lists a 5.5% platform fee. Credit purchases can also have a $0.80 minimum fee, according to [OpenRouter's billing explanation](https://openrouter.ai/blog/insights/openrouter-vs-litellm/). Allocate purchase fees across consumed credits; do not treat a new credit balance as entirely spent on this task.

## Fit and migration implications

[Jev documentation](https://openrouter.ai/docs/guides/community/jev) describes typed Choice, Noul and Score decisions through its Decisions or System One APIs. It does not generate free text or explanations. Changing only the model name in the Anthropic client would not work. Preserving the existing written reason requires another source, a template, or a generative model with additional cost.

The [official classification cookbook](https://openrouter.ai/docs/cookbook/evaluate-and-optimize/jev-classification) uses one Choice for the category and one Noul probability per overlapping tag, grouped in one request. Applied directly here, that means 177 questions: one category plus 63 subcategory checks and 113 keyword checks. Application code would select tags using calibrated thresholds, enforce the existing caps and construct arrays. Preserve cross-category subcategories; restricting checks to the chosen category changes existing behaviour.

The cookbook supports multiple judgments in one request, so 177 judgments need not mean 177 HTTP calls. The docs publish no maximum question count; acceptance and cost of this full taxonomy need validation. Measure returned `usage.input_tokens` and `usage.cost`; do not assume the existing prompt size transfers unchanged. OpenRouter's [Batch API](https://openrouter.ai/docs/batch-quickstart) lists supported endpoints without Decisions or System One. Budget Jev at its listed rate using concurrent requests, without assuming an additional batch discount.

Jev's category confidence and tag probabilities differ from Haiku's self-reported overall confidence. The current 0.6 auto-accept threshold cannot be reused without calibration, especially where the category looks certain but tags remain ambiguous.

## Recommendation

Benchmark Jev before switching production. Use 100-200 manually reviewed repositories spanning categories, overlapping roles, sparse descriptions and missing READMEs. Match current inputs for the first comparison. Measure primary-category accuracy, subcategory and keyword precision/recall, incorrect automatic acceptance, request failures and total cost including retries and fallback.

Jev is likely cheaper for labels alone. If its quality passes, use it for clear cases and retain Haiku for ambiguous cases or cases needing a written reason. Requiring Haiku to explain every Jev result could consume much of the saving. At the illustrative baseline, even 10,000 classifications save only about $16-$17 before fees, so migration effort matters alongside the percentage reduction.
