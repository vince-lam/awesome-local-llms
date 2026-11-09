<div align="center">

# 👋 Awesome Local LLMs

### 10,000+ open-source LLM, agent, and local inference repos, tracked daily

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

*Last Updated: 09/11/2026*

<!-- BEGIN_TABLE -->
## Established leaders

The 20 most-starred active projects.

|  # | Repo  |  Stars | 7d growth  | Category  | About  |
|----------|----------|----------|----------|----------|----------|
|  1 | [rea](https://github.com/morluto/rea)  | 445,968 | +24,388 (+5.8%) | AI Engineering | Reverse engineer anything with agents, from app behavior down to native binaries.  |
|  2 | [openclaw](https://github.com/openclaw/openclaw)  | 394,234 | +499 (+0.1%)  | Applications  | The AI that really does things. Any OS. Any Platform. The lobster way. 🦞  |
|  3 | [skills](https://github.com/mattpocock/skills)  | 319,462 | +9,506 (+3.1%)  | AI Engineering | Skills for Real Engineers. Straight from my .agents directory.  |
|  4 | [superpowers](https://github.com/obra/superpowers)  | 314,962 | +3,897 (+1.3%)  | AI Engineering | An agentic skills framework & software development methodology that works.  |
|  5 | [ECC](https://github.com/affaan-m/ECC)  | 300,098 | +4,682 (+1.6%)  | AI Engineering | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.  |
|  6 | [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 277,255 | +7,988 (+3.0%)  | AI Engineering | DeepSeek Harness: Everything is a Plugin.  |
|  7 | [hermes-agent](https://github.com/NousResearch/hermes-agent)  | 262,003 | +2,259 (+0.9%)  | AI Engineering | The agent that grows with you  |
|  8 | [opencode](https://github.com/anomalyco/opencode)  | 225,626 | +1,576 (+0.7%)  | Applications  | The open source coding agent.  |
|  9 | [n8n](https://github.com/n8n-io/n8n)  | 209,918 | +549 (+0.3%)  | AI Engineering | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.  |
|  10 | [firecrawl](https://github.com/firecrawl/firecrawl)  | 200,058 | +2,160 (+1.1%)  | AI Engineering | Supercharge your AI agents with data from the web and beyond. Building the library for superintelligence. 🔥  |
|  11 | [markitdown](https://github.com/microsoft/markitdown)  | 194,580 | +1,038 (+0.5%)  | AI Engineering | Python tool for converting files and office documents to Markdown.  |
|  12 | [skills](https://github.com/anthropics/skills)  | 190,599 | +3,929 (+2.1%)  | AI Engineering | Public repository for Agent Skills  |
|  13 | [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)  | 187,972 | +98 (+0.1%)  | Applications  | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.  |
|  14 | [ponytail](https://github.com/DietrichGebert/ponytail)  | 187,495 | +4,786 (+2.6%)  | AI Engineering | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.  |
|  15 | [ollama](https://github.com/ollama/ollama)  | 186,424 | +739 (+0.4%)  | Infrastructure | Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.  |
|  16 | [prompts.chat](https://github.com/f/prompts.chat)  | 176,717 | +1,110 (+0.6%)  | AI Engineering | f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.  |
|  17 | [transformers](https://github.com/huggingface/transformers)  | 168,690 | +239 (+0.1%)  | Infrastructure | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.  |
|  18 | [agency-agents](https://github.com/msitarzewski/agency-agents)  | 167,472 | +1,385 (+0.8%)  | AI Engineering | A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables. |
|  19 | [dify](https://github.com/langgenius/dify)  | 160,770 | +526 (+0.3%)  | AI Engineering | Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.  |
|  20 | [open-webui](https://github.com/open-webui/open-webui)  | 158,211 | +645 (+0.4%)  | AI Engineering | User-friendly AI Interface (Supports Ollama, OpenAI API, ...)  |

## Trending this week

The 20 largest seven-day star gains, excluding established leaders.

|  # | Repo  |  Stars | 7d growth  | Category  | About  |
|----------|----------|----------|----------|----------|----------|
|  1 | [agent-desktop](https://github.com/vercel-labs/agent-desktop)  |  20,149 | +11,773 (+140.6%)  | AI Engineering | Computer use CLI for AI agents  |
|  2 | [dsh-Go](https://github.com/ccch1mneyyy/dsh-Go)  |  17,323 | +11,738 (+210.2%)  | Applications  | dsh-go — DeepSeek Harness 装进口袋：手机本机运行，也能遥控你的电脑。  |
|  3 | [security-audit-skill](https://github.com/cloudflare/security-audit-skill)  |  67,616 | +10,499 (+18.4%)  | AI Engineering | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings  |
|  4 | [dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model)  |  67,178 | +10,213 (+17.9%)  | AI Engineering | 在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap. |
|  5 | [auto-ontology](https://github.com/NVIDIA/auto-ontology)  |  10,870 | +10,152 (+1413.9%) | AI Engineering | Auto Ontology is a Python framework for building semantic, graph-based reasoning layers over data. It enables deterministic query generation, better context retrieval, and more explainable AI for LLM and agent workflows.  |
|  6 | [dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype) |  21,652 | +9,772 (+82.3%)  | Applications  | Towards a More Autonomous Agent System  |
|  7 | [cactus](https://github.com/cactus-compute/cactus)  |  14,617 | +8,445 (+136.8%)  | AI Engineering | Sub-50mb agentic, voice and vision intelligence for consumer devices.  |
|  8 | [Scrapling](https://github.com/D4Vinci/Scrapling)  | 100,417 | +7,926 (+8.6%)  | AI Engineering | 🕷️ The BEST Web Scraping framework that handles everything from a single request to a full-scale crawl! Don't be shy, join here: https://discord.gg/EMgGbDceNQ and follow here for daily tips and tricks: https://x.com/Scrapling_dev  |
|  9 | [VoiceStudio](https://github.com/debpalash/VoiceStudio)  | 105,771 | +7,096 (+7.2%)  | Applications  | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.  |
|  10 | [orca](https://github.com/stablyai/orca)  | 120,197 | +6,785 (+6.0%)  | AI Engineering | Orca lets you run a fleet of coding agents (e.g. Claude Code, Codex) with your own subscription. Available on desktop, mobile and remote runtime.  |
|  11 | [impeccable](https://github.com/pbakaus/impeccable)  | 106,620 | +6,508 (+6.5%)  | AI Engineering | The design vocabulary for your coding agent. Steer with polish and bolder, review with critique and audit, catch AI slop before it ships.  |
|  12 | [elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)  |  16,054 | +5,841 (+57.2%)  | AI Engineering | Open-source plugin for designing and reviewing software with agents  |
|  13 | [claude-mem](https://github.com/thedotmack/claude-mem)  | 115,297 | +4,808 (+4.4%)  | AI Engineering | Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More  |
|  14 | [magpie](https://github.com/yetone/magpie)  |  33,001 | +4,697 (+16.6%)  | Applications  | Every agent's model. One place. Codex on DeepSeek, Claude Code on Kimi, from the menu bar.  |
|  15 | [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)  |  37,433 | +4,217 (+12.7%)  | Applications  | Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy.  |
|  16 | [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)  | 141,487 | +4,092 (+3.0%)  | Applications  | 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow.  |
|  17 | [graphify](https://github.com/Graphify-Labs/graphify)  | 144,861 | +3,926 (+2.8%)  | AI Engineering | Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.  |
|  18 | [taste-skill](https://github.com/Leonxlnx/taste-skill)  | 112,393 | +3,913 (+3.6%)  | AI Engineering | Agent skills that give coding agents taste: art direction, reference images and a browser check instead of generic AI pages  |
|  19 | [OpenMontage](https://github.com/OpenMontageInc/OpenMontage)  |  79,009 | +3,905 (+5.2%)  | Applications  | World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.  |
|  20 | [spec-kit](https://github.com/github/spec-kit)  | 148,944 | +3,604 (+2.5%)  | AI Engineering | 💫 Toolkit to help you get started with SDD or any other process!  |

## Trending by category

Up to three more weekly movers from each category. Projects already shown above are omitted.

### [AI Engineering](https://llmrepos.com/categories/ai-engineering?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [freellmapi](https://github.com/tashfeenahmed/freellmapi) |  49,613 | +3,419 (+7.4%) | 7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behind one /v1 endpoint, plus any custom OpenAI-compatible endpoint. Smart routing, automatic failover, encrypted keys. Personal experimentation only. |
|  2 | [DeepTutor](https://github.com/HKUDS/DeepTutor)  |  57,531 | +3,311 (+6.1%) | DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.  |
|  3 | [humanizer](https://github.com/blader/humanizer)  |  66,993 | +3,080 (+4.8%) | Agent skill that removes signs of AI-generated writing from text  |

### [Applications](https://llmrepos.com/categories/applications?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) |  13,958 | +3,025 (+27.7%) | A toolbox of film styles made in code for Claude Code: 66 ready to use, and your own. Each style is a style prompt plus a demo film made entirely in code by Claude Opus 5.5, with no video model. By Lemomo. · 一套用代码做片的风格工具箱：66 种现成风格，也能做出你自己的  |
|  2 | [Mika](https://github.com/wangzan101/Mika)  |  7,874 | +2,857 (+56.9%) | An on-device AI agent for Android that operates apps and the web to get things done for you.  |
|  3 | [ppt-master](https://github.com/hugohe3/ppt-master)  |  75,235 | +2,664 (+3.7%)  | AI turns documents or topics into real, native PowerPoint decks—with native shapes, transitions and animations, data-backed charts and tables on demand, audio narration from speaker notes, and support for your own .pptx templates. · by Hugo He |

### [Infrastructure](https://llmrepos.com/categories/infrastructure?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) |  11,402 | +2,099 (+22.6%) | A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB of RAM. Portable C99: no BLAS, no framework, no GPU.  |
|  2 | [OmniRoute](https://github.com/cheaper-inference/OmniRoute)  |  85,874 | +2,034 (+2.4%)  | Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 900+ contributors |
|  3 | [sandstorm](https://github.com/deeplethe/sandstorm)  |  5,954 | +1,943 (+48.4%) | Run thousands of AI agent sandboxes on the cheapest machines.  |

### [Model Development](https://llmrepos.com/categories/model-development?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [agentic-rl-lab](https://github.com/datawhalechina/agentic-rl-lab) |  1,338 | +778 (+138.9%) | Reproducing and studying RL algorithms for LLM agents, including GRPO, GSPO, DAPO, OPD, Search-R1, ReTool, ALFWorld and beyond. |
|  2 | [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)  | 108,092 | +395 (+0.4%)  | Implement a ChatGPT-like LLM in PyTorch from scratch, step by step  |
|  3 | [Soup](https://github.com/MakazhanAlpamys/Soup)  |  10,363 | +369 (+3.7%)  | Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU.  |

### [Models](https://llmrepos.com/categories/models?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [MOSS-Image](https://github.com/OpenMOSS/MOSS-Image) |  2,764 | +278 (+11.2%) | Official repository for MOSS-Image, a 5B-parameter base DiT model with high-quality text rendering, layout generation, and efficient fine-tuning.  |
|  2 | [qwenputer](https://github.com/divagr18/qwenputer)  |  766 | +263 (+52.3%) | A computer, compiled into the weights of a language model. An exact CPU inside Qwen3.5-4B, with Gated DeltaNet state as RAM.  |
|  3 | [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) |  15,842 | +160 (+1.0%)  | Speech-to-text, text-to-speech, speaker diarization, speech enhancement, source separation, and VAD using next-gen Kaldi with onnxruntime without Internet connection. Support embedded systems, Android, iOS, HarmonyOS, Raspberry Pi, RISC-V, RK NPU, Axera NPU, Ascend NPU, x86_64 servers, websocket server/client, support 12 programming languages |

### [Lists](https://llmrepos.com/categories/lists?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [skills](https://github.com/jakubkrehel/skills)  |  11,843 | +1,551 (+15.1%)  | A collection of agent skills that help you build great interfaces.  |
|  2 | [Awesome-REA](https://github.com/reacher-z/Awesome-REA)  |  2,265 | +1,450 (+177.9%) | Curated tools, case studies and papers for reverse engineering websites, games, apps, binaries, firmware and protocols. Source-reviewed, English and Chinese.  |
|  3 | [awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) |  7,976 | +1,420 (+21.7%)  | 77 game-dev skills for AI coding agents — Godot, Unity, Unreal, Phaser, PixiJS, three.js, Bevy, pygame, LÖVE, Roblox. Portable SKILL.md Agent Skills (the format Anthropic launched as Claude Skills), with a router that loads the right skill for your engine and task. Runs in Claude Code, Cursor, Kiro, Codex, Copilot, Gemini CLI and more. |

### [Tutorials](https://llmrepos.com/categories/tutorials?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [figures4papers](https://github.com/ChenLiu-1996/figures4papers) |  10,335 | +874 (+9.2%) | My Python scripts to make high-quality figures for publications in top AI conferences and journals.  |
|  2 | [ai-agent-book](https://github.com/bojieli/ai-agent-book)  |  57,570 | +611 (+1.1%) | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码  |
|  3 | [cs249r_book](https://github.com/harvard-edge/cs249r_book)  |  30,084 | +298 (+1.0%) | Machine Learning Systems: Foundations, Scaling, Agentic AI, and Physical AI (Vols I–IV) • Harvard CS249r \| https://mlsysbook.ai |

### [Misc](https://llmrepos.com/categories/misc?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [PublicFreeSuffix](https://github.com/PublicFreeSuffix/PublicFreeSuffix) |  279 | +31 (+12.5%) | Free Domain Name For Everyone  |
|  2 | [runs-on.dev](https://github.com/zordhalo/runs-on.dev)  |  541 | +28 (+5.5%)  | Grab your own cool 'runs-on.dev' subdomain to use for free forever.  |
|  3 | [OB1](https://github.com/NateBJones-Projects/OB1)  |  4,768 | +16 (+0.3%)  | Open Brain — The infrastructure layer for your thinking. One database, one AI gateway, one chat channel — any AI plugs in. No middleware, no SaaS. |
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
