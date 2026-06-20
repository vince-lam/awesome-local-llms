# 👋 Awesome Local LLMs

There are an overwhelming number of open-source tools for running LLMs locally and for building on top of them. This repo curates two families of projects and tracks their GitHub metrics as a proxy for popularity and active maintenance:

- **Local LLM** projects — split into *Inference Backend* engines, *Front-end UI* clients, and *All-in-one App* desktop/mobile apps.
- **Agent** projects — frameworks, coding agents, research agents, and more.

Each repo is tagged with a **Category** and **Subcategory** so you can tell the types apart at a glance. GitHub metrics (stars, forks, issues, contributors, releases, time since last commit) are refreshed automatically every week by a GitHub Actions workflow.

**Contributions are welcome!** Suggest a repo I've missed by opening an issue, or add it to [`repos.json`](repos.json) (with its `category` and `subcategory`) and open a pull request. The table below regenerates automatically.

There is also a fuller table of metrics in this [Google Sheet](https://docs.google.com/spreadsheets/d/1Xv38p90V3GiJXjq0a3qc24056Vicn1I5MG6QiFE6nVE/edit?usp=sharing) and [Airtable](https://airtable.com/apparaKqezkq2LECD/shrE26kWFaVU1cvgb) _(no longer updated — kept for reference)_.

For my thoughts on local LLM tooling: <https://vinlam.com/posts/local-llm-options/>

Note the condensed table below has two filters applied:

1. Repositories need more than 100 stars
2. Repositories require a commit within the last 60 days

## Open-Source LLM & Agent Projects

*Last Updated: (pending first automated run)*

<!-- BEGIN_TABLE -->
_The table is generated automatically by `update_stats.py`. Run it locally or trigger the "Update repo stats" workflow to populate this section._
<!-- END_TABLE -->

## How it works

[`update_stats.py`](update_stats.py) reads [`repos.json`](repos.json), pulls metrics from the GitHub API, writes a full timestamped CSV to `outputs/`, and injects the filtered table above between the `BEGIN_TABLE` / `END_TABLE` markers.

The condensed table above is filtered to repos with **more than 100 stars** and a **commit within the last 60 days**. The full, unfiltered dataset (every tracked repo, all columns) is produced as the `outputs/` CSV, which the weekly workflow also uploads as a build artifact.

### Run it yourself

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add your GitHub token
python update_stats.py
```

### Automated weekly updates

The [`Update repo stats`](.github/workflows/update-stats.yml) GitHub Actions workflow runs every Monday (and on demand via *Run workflow*), regenerates the table, and commits the refreshed README back to `main`. It needs one repository secret (Settings → Secrets and variables → Actions):

| Secret | Purpose |
|--------|---------|
| `STATS_GH_PAT` | GitHub read-only PAT (5,000 req/hour; the built-in token's 1,000/hour isn't enough for ~190 repos) |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
