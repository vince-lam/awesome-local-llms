# Turso write optimisation rollout

Deploy independently of the website cache PR. No migration or extra Actions run is required.

- Daily snapshots remain daily, even when all metrics are unchanged.
- Identical same-day upserts skip writes; corrected metrics and NULL transitions still persist.
- Description and owner-type updates use NULL-safe change predicates.
- Latest metrics, snapshot count and rolling deltas are computed from stored history, then applied once per changed repo. This preserves repos missed by partial scrapes and same-day corrections. It avoids two full-table write passes; it still reads history to verify correctness.
- Existing production indexes remain unchanged. New indexes can amplify snapshot writes, so none are added without workload evidence.

## Optional website invalidation

After the website PR is deployed, configure Vercel `REVALIDATE_SECRET`, scraper Actions secret `WEB_REVALIDATE_SECRET` with the same random value, and repository variable `WEB_REVALIDATE_URL=https://llmrepos.com/api/revalidate`.

The callback runs only at the end of successful processing, uses HTTPS, refuses redirects and times out after 15 seconds. Missing configuration or callback failure leaves timed website refresh active. No extra GitHub Actions workflow, job or scheduled run is added. Do not log credentials.

Wait for the next scheduled scrape and check its log for `Website cache invalidated`. Check repository descriptions, snapshot history, counts, ranking and freshness on the deployed website. Compare daily Turso read/write totals before considering Free. Keep Developer until a representative window shows reads comfortably below 500M/month and writes below 10M/month.

Rollback: revert this PR; existing schema and data remain compatible. Remove callback settings to disable invalidation independently. No daily history is deleted or compressed.

## Local evidence

All 57 scraper tests passed, including real SQLite checks for NULL transitions, changed descriptions, same-day corrections, daily history, rolling windows, empty histories, and identical reruns. A 1,000-repository/31-day fixture produced the same denormalised fields as the baseline. Baseline refresh changed 2,000 rows initially and again on a rerun; the optimised refresh changed 1,000 initially and zero on a rerun. These SQLite changed-row measurements do not prove billed Turso write savings or account for all index maintenance.
