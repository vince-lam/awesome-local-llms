<div align="center">

# 👋 Awesome Local LLMs

### 10,000+ open-source LLM, agent, and local inference repos, tracked daily
- [Continuum-AI-Corp/OrcaReplay](https://github.com/Continuum-AI-Corp/OrcaReplay) — drop-in recorder that sits between your agent and the model provider.

[**llmrepos.com**](https://llmrepos.com) sorts them by how fast they are gaining stars, not by how many they have.

[![Browse llmrepos.com](https://img.shields.io/badge/browse-llmrepos.com-2ea44f?style=for-the-badge)](https://llmrepos.com)
[![Stars](https://img.shields.io/github/stars/vince-lam/awesome-local-llms?style=for-the-badge)](https://github.com/vince-lam/awesome-local-llms/stargazers)
[![Daily refresh](https://img.shields.io/github/actions/workflow/status/vince-lam/awesome-local-llms/update-stats.yml?style=for-the-badge&label=daily%20refresh)](https://github.com/vince-lam/awesome-local-llms/actions/workflows/update-stats.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)

<a href="https://llmrepos.com"><img src="assets/llmrepos-demo.gif" alt="Animated demo of llmrepos.com filtering trending AI repos, browsing Skills and MCP, and searching repositories" width="100%"></a>

</div>

---

## What this is

A curated list of open-source projects for building with LLMs, covering the whole stack: model weights, training code, inference runtimes, agent frameworks, end-user apps, and the lists and tutorials that help you learn.

Each repo is checked once a day for stars, 1d/7d/30d star growth, forks, contributors, open issues, language, license, creation date, and time since last commit.

Two ways to use it:

- [**llmrepos.com**](https://llmrepos.com) has all 11,000+ repos, with search, growth sorting, and filters by category, subcategory, language, and license.
- **This README** mixes established leaders with projects gaining stars this week, regenerated every Monday.

Projects are organised into eight categories:

- **AI Engineering**: agent SDKs, orchestration, prompting & scaffolding, memory/RAG, tools & integrations, MCP, evaluation, and guardrails
- **Applications**: coding assistants, personal agents, productivity, content creation, research, data analytics, and automation
- **Infrastructure**: local runtimes, production serving, distributed & edge inference, optimisation, gateways, observability, and vector search
- **Model Development**: fine-tuning, training, RLHF, deep learning frameworks, dataset engineering, and interpretability
- **Models**: foundation, vision, audio/speech, embedding, on-device, and domain-specific model releases
- **Lists**: curated collections of prompts, tools, models, papers, and datasets
- **Tutorials**: getting-started guides, courses, roadmaps, and interview prep
- **Misc**: everything else

Each repo is tagged with one **category**, one or more **subcategories**, and a set of cross-cutting **keywords** (techniques, integrations, modalities, and domains such as `RAG`, `MCP`, or `Context engineering`).

**Contributions are welcome!** [Open an issue](https://github.com/vince-lam/awesome-local-llms/issues/new/choose) to suggest a missing repo, correct a listing, or improve the site.

## How the project has changed

This started in 2024 as a markdown list of local LLM tools that I edited by hand and kept in sync with a Google Sheet. It went out of date faster than I could edit it, so it became a pipeline instead.

| | 2024 | 2026 |
|---|---|---|
| Repos tracked | ~40, picked by hand | 8,600+, found via the GitHub API and classified automatically |
| Refresh | Manual, later weekly | Daily, via GitHub Actions into a [Turso](https://turso.tech) (libSQL) database |
| Ranking | Total stars | 1d/7d/30d star growth, so a repo shows up within days of taking off |
| Scope | Local inference and chat UIs | Agents, RAG, coding assistants, serving, model development, evals |
| Surface | This README | [llmrepos.com](https://llmrepos.com), plus this README |

## Elsewhere

- My write-up on local LLM tooling: <https://vinlam.com/posts/local-llm-options/>
- Older exports, no longer updated: [Google Sheet](https://docs.google.com/spreadsheets/d/1Xv38p90V3GiJXjq0a3qc24056Vicn1I5MG6QiFE6nVE/edit?usp=sharing) and [Airtable](https://airtable.com/apparaKqezkq2LECD/shrE26kWFaVU1cvgb)

## Weekly Open-Source LLM & Agent Rankings

These generated rankings combine the 20 most-starred active projects, the 20 largest seven-day movers outside that group, and up to three more movers from each category. Each project appears once. For the complete daily index, search, filters, and longer growth windows, use [llmrepos.com](https://llmrepos.com/?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel).

*Last Updated: 12/10/2026*

<!-- BEGIN_TABLE -->
## Established leaders

The 20 most-starred active projects.

|  # | Repo  |  Stars | 7d growth  | Category  | About  |
|----------|----------|----------|----------|----------|----------|
|  1 | [openclaw](https://github.com/openclaw/openclaw)  | 391,774 | +369 (+0.1%)  | Applications  | The AI that really does things. Any OS. Any Platform. The lobster way. 🦞  |
|  2 | [superpowers](https://github.com/obra/superpowers)  | 298,056 | +2,680 (+0.9%)  | AI Engineering | An agentic skills framework & software development methodology that works.  |
|  3 | [skills](https://github.com/mattpocock/skills)  | 287,467 | +11,060 (+4.0%) | AI Engineering | Skills for Real Engineers. Straight from my .agents directory.  |
|  4 | [ECC](https://github.com/affaan-m/ECC)  | 277,714 | +4,536 (+1.7%)  | AI Engineering | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.  |
|  5 | [hermes-agent](https://github.com/NousResearch/hermes-agent)  | 253,052 | +1,766 (+0.7%)  | AI Engineering | The agent that grows with you  |
|  6 | [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 248,081 | +4,538 (+1.9%)  | AI Engineering | DeepSeek Harness: Everything is a Plugin.  |
|  7 | [opencode](https://github.com/anomalyco/opencode)  | 212,905 | +1,111 (+0.5%)  | Applications  | The open source coding agent.  |
|  8 | [n8n](https://github.com/n8n-io/n8n)  | 207,115 | +423 (+0.2%)  | AI Engineering | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.  |
|  9 | [firecrawl](https://github.com/firecrawl/firecrawl)  | 190,769 | +2,051 (+1.1%)  | AI Engineering | Supercharge your AI agents with data from the web and beyond. Building the library for superintelligence. 🔥  |
|  10 | [markitdown](https://github.com/microsoft/markitdown)  | 189,752 | +1,233 (+0.7%)  | AI Engineering | Python tool for converting files and office documents to Markdown.  |
|  11 | [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)  | 187,532 | +-124 (+-0.1%)  | Applications  | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.  |
|  12 | [ollama](https://github.com/ollama/ollama)  | 182,864 | +649 (+0.4%)  | Infrastructure | Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.  |
|  13 | [skills](https://github.com/anthropics/skills)  | 180,679 | +987 (+0.5%)  | AI Engineering | Public repository for Agent Skills  |
|  14 | [prompts.chat](https://github.com/f/prompts.chat)  | 172,710 | +657 (+0.4%)  | AI Engineering | f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.  |
|  15 | [transformers](https://github.com/huggingface/transformers)  | 167,585 | +622 (+0.4%)  | Infrastructure | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.  |
|  16 | [ponytail](https://github.com/DietrichGebert/ponytail)  | 161,707 | +6,366 (+4.1%)  | AI Engineering | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.  |
|  17 | [agency-agents](https://github.com/msitarzewski/agency-agents)  | 159,381 | +2,497 (+1.6%)  | AI Engineering | A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables. |
|  18 | [dify](https://github.com/langgenius/dify)  | 158,260 | +395 (+0.3%)  | AI Engineering | Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.  |
|  19 | [langflow](https://github.com/langflow-ai/langflow)  | 155,544 | +42 (+0.0%)  | AI Engineering | Langflow is a powerful tool for building and deploying AI-powered agents and workflows.  |
|  20 | [open-webui](https://github.com/open-webui/open-webui)  | 154,712 | +733 (+0.5%)  | AI Engineering | User-friendly AI Interface (Supports Ollama, OpenAI API, ...)  |

## Trending this week

The 20 largest seven-day star gains, excluding established leaders.

|  # | Repo  |  Stars | 7d growth  | Category  | About  |
|----------|----------|----------|----------|----------|----------|
|  1 | [rea](https://github.com/morluto/rea)  | 138,494 | +135,465 (+4472.3%) | AI Engineering | Reverse engineer anything with agents, from app behavior down to native binaries.  |
|  2 | [dots](https://github.com/feder-cr/dots)  |  31,981 | +29,375 (+1127.2%)  | AI Engineering | Open-source, self-hosted alternative to OpenAI Dots, Grok Bot. Built to be undetectable by anti-bot systems.  |
|  3 | [dsh-our-free-model](https://github.com/zouyuxuan122/dsh-our-free-model)  |  11,339 | +10,049 (+779.0%)  | AI Engineering | 在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap. |
|  4 | [moli](https://github.com/lexmount/moli)  |  17,008 | +9,070 (+114.3%)  | Infrastructure | Best headless browser for AI agents. Lite, Fast, High-Compatibility. Built in Rust  |
|  5 | [openGym](https://github.com/DuarteSantos8/openGym)  |  10,169 | +6,927 (+213.7%)  | Applications  | Self-hosted gym & body-weight tracker — plan routines, log workouts (supersets, warm-ups, cardio), see which muscles are trained, fatigued or detrained, import from FitNotes/Strong/Hevy, passkey login. Your data, your server.  |
|  6 | [VoiceStudio](https://github.com/debpalash/VoiceStudio)  |  59,818 | +6,504 (+12.2%)  | Applications  | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.  |
|  7 | [magpie](https://github.com/yetone/magpie)  |  10,210 | +5,279 (+107.1%)  | Applications  | Every agent's model. One place. Codex on DeepSeek, Claude Code on Kimi, from the menu bar.  |
|  8 | [Agent-Reach](https://github.com/Panniantong/Agent-Reach)  |  96,500 | +5,237 (+5.7%)  | Applications  | Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.  |
|  9 | [orca](https://github.com/stablyai/orca)  |  90,494 | +5,217 (+6.1%)  | AI Engineering | Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and remote runtime.  |
|  10 | [archify](https://github.com/tt-a1i/archify)  |  82,455 | +4,789 (+6.2%)  | AI Engineering | Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more.  |
|  11 | [security-audit-skill](https://github.com/cloudflare/security-audit-skill)  |  28,603 | +4,161 (+17.0%)  | AI Engineering | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings  |
|  12 | [agent-skills](https://github.com/addyosmani/agent-skills)  | 105,467 | +4,128 (+4.1%)  | Applications  | Production-grade engineering skills for AI coding agents.  |
|  13 | [OpenMontage](https://github.com/calesthio/OpenMontage)  |  67,431 | +3,996 (+6.3%)  | Applications  | World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.  |
|  14 | [ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) |  67,958 | +3,823 (+6.0%)  | AI Engineering | Learn AI Engineering! Learn it. Build it. Ship it for others.  |
|  15 | [claude-mem](https://github.com/thedotmack/claude-mem)  | 100,017 | +3,721 (+3.9%)  | AI Engineering | Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More  |
|  16 | [universal-modder](https://github.com/rehan-remade/universal-modder)  |  6,924 | +3,558 (+105.7%)  | Applications  | Point Claude at any game. Skills, tools and the fal MCP that let Claude Code mod almost any PC game you own: recon, reverse engineering, fal-generated art/3D/audio, in-game testing, showcase videos.  |
|  17 | [paperclip](https://github.com/paperclipai/paperclip)  | 100,764 | +3,443 (+3.5%)  | AI Engineering | The open-source app everyone uses to manage agents at work  |
|  18 | [iFixAi](https://github.com/ifixai-ai/iFixAi)  |  24,053 | +3,443 (+16.7%)  | AI Engineering | Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most crucial question in the AI Agent Economy. Is the agent doing what is supposed to do? With iFixAi you can have this answer in less than 120 seconds.  |
|  19 | [ppt-master](https://github.com/hugohe3/ppt-master)  |  61,019 | +3,357 (+5.8%)  | Applications  | AI turns documents or topics into real, native PowerPoint decks—with native shapes, transitions and animations, data-backed charts and tables on demand, audio narration from speaker notes, and support for your own .pptx templates. · by Hugo He  |
|  20 | [autoharness](https://github.com/tigerless-labs/autoharness)  |  11,018 | +3,195 (+40.8%)  | AI Engineering | Autoharness — a self-learning skill layer for Claude Code — distills skills from your real sessions, updates them as you work, and prunes the ones that stop getting used. No daemon, no benchmark.  |

## Trending by category

Up to three more weekly movers from each category. Projects already shown above are omitted.

### [AI Engineering](https://llmrepos.com/categories/ai-engineering?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [cc-switch](https://github.com/farion1231/cc-switch)  | 143,241 | +3,137 (+2.2%) | A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io  |
|  2 | [hindsight](https://github.com/vectorize-io/hindsight)  |  48,736 | +3,092 (+6.8%) | Hindsight: Agent Memory That Learns  |
|  3 | [freellmapi](https://github.com/tashfeenahmed/freellmapi) |  33,790 | +3,049 (+9.9%) | 7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behind one /v1 endpoint, plus any custom OpenAI-compatible endpoint. Smart routing, automatic failover, encrypted keys. Personal experimentation only. |

### [Applications](https://llmrepos.com/categories/applications?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [open-code-review](https://github.com/alibaba/open-code-review)  |  46,467 | +2,689 (+6.1%)  | Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible.  |
|  2 | [hypit](https://github.com/hypit-ai/hypit)  |  21,504 | +2,200 (+11.4%) | Clone any viral video with AI agents. Not just a script, the whole workflow: swap the face, the words, the B-roll, ship 100 variants in one command, and get your 100M views.  |
|  3 | [free-claude-code](https://github.com/Alishahryar1/free-claude-code) |  58,683 | +1,996 (+3.5%)  | Use Claude Code, Codex, VSCode, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly) |

### [Infrastructure](https://llmrepos.com/categories/infrastructure?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) |  75,574 | +2,486 (+3.4%)  | Never stop coding. Free MIT AI gateway: one endpoint, 359 providers (150+ free), 1200+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by hundreds of contributors |
|  2 | [airllm](https://github.com/lyogavin/airllm)  |  37,280 | +1,880 (+5.3%)  | AirLLM 70B inference with single 4GB GPU  |
|  3 | [xerj](https://github.com/xerj-org/xerj)  |  3,658 | +1,015 (+38.4%) | XERJ is the new way for AI to search data. Its autoindex capability activates agents to know your data without the token waste of grep and sed. One command indexes code, docs, logs and PDFs for search, RAG, security audits and agent memory, using 40x fewer tokens than grep. Elasticsearch compatible, so existing clients just work.  |

### [Model Development](https://llmrepos.com/categories/model-development?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [unsloth](https://github.com/unslothai/unsloth)  |  77,870 | +662 (+0.9%) | Local UI to run and train LLMs and diffusion models. Supports GGUF, MLX, Qwen3.8, DeepSeek-V4, MiniMax-H3, Gemma 4, FLUX and more. |
|  2 | [Soup](https://github.com/MakazhanAlpamys/Soup)  |  8,606 | +459 (+5.6%) | Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU.  |
|  3 | [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 106,421 | +393 (+0.4%) | Implement a ChatGPT-like LLM in PyTorch from scratch, step by step  |

### [Models](https://llmrepos.com/categories/models?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [Index-Translate](https://github.com/bilibili/Index-Translate) |  1,407 | +775 (+122.6%) | A Multilingual, Multimodal Translation Model Family  |
|  2 | [needle](https://github.com/cactus-compute/needle)  |  13,876 | +637 (+4.8%)  | Automation foundation model for tiny devices: 2-bit, 8-29 MB, tool calls, ASR, structured extraction and embeddings on phones, wearables, smart homes, robots, cars and microcontrollers. |
|  3 | [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)  |  62,723 | +364 (+0.6%)  | 1 min voice data can also be used to train a good TTS model! (few shot voice cloning)  |

### [Lists](https://llmrepos.com/categories/lists?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) |  4,476 | +2,498 (+126.3%) | A growing collection of viral videos made with Claude Opus 5.5 and the prompts behind them. Watch each original next to a live remake on Skillry. Updated regularly.  |
|  2 | [AISafetyHot-Hub](https://github.com/wuyoscar/AISafetyHot-Hub)  |  1,045 | +895 (+596.7%)  | 每天的 AI 安全精选和论文清单（md / bib / json），附 Agent 接入说明 · AI Safety HOT  |
|  3 | [marketing-skills](https://github.com/irinabuht12-oss/marketing-skills)  |  4,293 | +856 (+24.9%)  | Claude skills for marketing: 49 free marketing skills for Claude Code and claude.ai (Google Ads, Meta Ads, SEO, AI visibility) + the Ryze Google Ads MCP / Meta Ads MCP: claude mcp add ryze --transport http https://connector.get-ryze.ai/mcp |

### [Tutorials](https://llmrepos.com/categories/tutorials?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [ai-agent-book](https://github.com/bojieli/ai-agent-book)  |  53,700 | +1,298 (+2.5%) | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码  |
|  2 | [ai-infra-book](https://github.com/bojieli/ai-infra-book)  |  6,292 | +409 (+7.0%)  | 《深入理解 AI Infra：量化分析与系统设计》（李博杰 著）开源书稿：从硬件约束和模型架构出发，量化推导 LLM 推理与训练系统设计。含全书正文、PDF、配套计算工具与实验  |
|  3 | [figures4papers](https://github.com/ChenLiu-1996/figures4papers) |  8,413 | +385 (+4.8%)  | My Python scripts to make high-quality figures for publications in top AI conferences and journals. |

### [Misc](https://llmrepos.com/categories/misc?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [OB1](https://github.com/NateBJones-Projects/OB1)  |  4,719 | +41 (+0.9%) | Open Brain — The infrastructure layer for your thinking. One database, one AI gateway, one chat channel — any AI plugs in. No middleware, no SaaS. |
|  2 | [keyline-icons](https://github.com/keyline-icons/keyline-icons) |  160 | +14 (+9.6%) | 1,435 free MIT icons in stroke, two-tone, duotone and fill, rounded or sharp: 11,480 SVGs on one 24×24 grid. Built for shadcn/ui.  |
|  3 | [WhisperLive](https://github.com/collabora/WhisperLive)  |  4,318 | +12 (+0.3%) | A nearly-live implementation of OpenAI's Whisper.  |
<!-- END_TABLE -->

The rankings above require more than 100 stars and a commit within the last 60 days. Weekly movers need a complete seven-day history. [llmrepos.com](https://llmrepos.com/?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel) has the full index, refreshed daily.

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
