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

*Last Updated: 02/11/2026*

<!-- BEGIN_TABLE -->
## Established leaders

The 20 most-starred active projects.

|  # | Repo  |  Stars | 7d growth  | Category  | About  |
|----------|----------|----------|----------|----------|----------|
|  1 | [rea](https://github.com/morluto/rea)  | 421,580 | +33,070 (+8.5%) | AI Engineering | Reverse engineer anything with agents, from app behavior down to native binaries.  |
|  2 | [openclaw](https://github.com/openclaw/openclaw)  | 393,735 | +608 (+0.2%)  | Applications  | The AI that really does things. Any OS. Any Platform. The lobster way. 🦞  |
|  3 | [superpowers](https://github.com/obra/superpowers)  | 311,065 | +5,685 (+1.9%)  | AI Engineering | An agentic skills framework & software development methodology that works.  |
|  4 | [skills](https://github.com/mattpocock/skills)  | 309,956 | +6,231 (+2.1%)  | AI Engineering | Skills for Real Engineers. Straight from my .agents directory.  |
|  5 | [ECC](https://github.com/affaan-m/ECC)  | 295,416 | +6,039 (+2.1%)  | AI Engineering | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.  |
|  6 | [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 269,267 | +7,101 (+2.7%)  | AI Engineering | DeepSeek Harness: Everything is a Plugin.  |
|  7 | [hermes-agent](https://github.com/NousResearch/hermes-agent)  | 259,744 | +2,465 (+1.0%)  | AI Engineering | The agent that grows with you  |
|  8 | [opencode](https://github.com/anomalyco/opencode)  | 224,050 | +2,251 (+1.0%)  | Applications  | The open source coding agent.  |
|  9 | [n8n](https://github.com/n8n-io/n8n)  | 209,369 | +726 (+0.3%)  | AI Engineering | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.  |
|  10 | [firecrawl](https://github.com/firecrawl/firecrawl)  | 197,898 | +2,353 (+1.2%)  | AI Engineering | Supercharge your AI agents with data from the web and beyond. Building the library for superintelligence. 🔥  |
|  11 | [markitdown](https://github.com/microsoft/markitdown)  | 193,542 | +1,242 (+0.6%)  | AI Engineering | Python tool for converting files and office documents to Markdown.  |
|  12 | [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)  | 187,874 | +112 (+0.1%)  | Applications  | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.  |
|  13 | [skills](https://github.com/anthropics/skills)  | 186,670 | +2,771 (+1.5%)  | AI Engineering | Public repository for Agent Skills  |
|  14 | [ollama](https://github.com/ollama/ollama)  | 185,685 | +837 (+0.5%)  | Infrastructure | Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.  |
|  15 | [ponytail](https://github.com/DietrichGebert/ponytail)  | 182,709 | +5,943 (+3.4%)  | AI Engineering | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.  |
|  16 | [prompts.chat](https://github.com/f/prompts.chat)  | 175,607 | +967 (+0.6%)  | AI Engineering | f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.  |
|  17 | [transformers](https://github.com/huggingface/transformers)  | 168,451 | +259 (+0.2%)  | Infrastructure | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.  |
|  18 | [agency-agents](https://github.com/msitarzewski/agency-agents)  | 166,087 | +1,930 (+1.2%)  | AI Engineering | A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables. |
|  19 | [dify](https://github.com/langgenius/dify)  | 160,244 | +648 (+0.4%)  | AI Engineering | Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.  |
|  20 | [open-webui](https://github.com/open-webui/open-webui)  | 157,566 | +754 (+0.5%)  | AI Engineering | User-friendly AI Interface (Supports Ollama, OpenAI API, ...)  |

## Trending this week

The 20 largest seven-day star gains, excluding established leaders.

|  # | Repo  |  Stars | 7d growth  | Category  | About  |
|----------|----------|----------|----------|----------|----------|
|  1 | [dsh-our-free-model](https://github.com/zouyuxuan122/dsh-our-free-model)  |  56,966 | +12,815 (+29.0%) | AI Engineering | 在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.  |
|  2 | [dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model)  |  56,965 | +12,815 (+29.0%) | AI Engineering | 在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.  |
|  3 | [DeepTutor](https://github.com/HKUDS/DeepTutor)  |  54,220 | +10,797 (+24.9%) | AI Engineering | DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.  |
|  4 | [VoiceStudio](https://github.com/debpalash/VoiceStudio)  |  98,675 | +10,698 (+12.2%) | Applications  | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.  |
|  5 | [security-audit-skill](https://github.com/cloudflare/security-audit-skill)  |  57,117 | +9,268 (+19.4%)  | AI Engineering | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings  |
|  6 | [elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)  |  10,213 | +8,816 (+631.1%) | AI Engineering | Open-source skills for designing and reviewing software with AI agents  |
|  7 | [iFixAi](https://github.com/ifixai-ai/iFixAi)  |  43,006 | +8,255 (+23.8%)  | AI Engineering | Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most crucial question in the AI Agent Economy. Is the agent doing what is supposed to do? With iFixAi you can have this answer in less than 120 seconds.  |
|  8 | [claude-mem](https://github.com/thedotmack/claude-mem)  | 110,489 | +7,193 (+7.0%)  | AI Engineering | Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More  |
|  9 | [agent-desktop](https://github.com/lahfir/agent-desktop)  |  8,698 | +6,875 (+377.1%) | AI Engineering | Agent Desktop gives any agent reliable computer use on the desktop. Built with Rust, it sees any app's real UI structure through OS accessibility trees and operates it — refs stay stable and actions stay safe to retry, instead of guessing from pixels.  |
|  10 | [orca](https://github.com/stablyai/orca)  | 113,412 | +6,765 (+6.3%)  | AI Engineering | Orca is the place for working with a fleet of agents (e.g. Grok Bot, Claude Code). Run any coding agent with your own subscription. Available on desktop, mobile and remote runtime.  |
|  11 | [magpie](https://github.com/yetone/magpie)  |  28,304 | +6,074 (+27.3%)  | Applications  | Every agent's model. One place. Codex on DeepSeek, Claude Code on Kimi, from the menu bar.  |
|  12 | [taste-skill](https://github.com/Leonxlnx/taste-skill)  | 108,480 | +5,718 (+5.6%)  | AI Engineering | Agent skills that give coding agents taste: art direction, reference images and a browser check instead of generic AI pages  |
|  13 | [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) |  33,216 | +5,567 (+20.1%)  | Applications  | Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy.  |
|  14 | [Orkas](https://github.com/Orkas-AI/Orkas)  |  7,719 | +5,546 (+255.2%) | AI Engineering | Orkas is an open-source (MIT), local-first AI team for your desktop: a Commander turns your goal into to-dos and coordinates 16 built-in specialist agents plus Claude Code, Codex, OpenCode, OpenClaw and Hermes, with projects, scheduled automations and connectors. Free app for macOS & Windows; built-in models or your own keys. |
|  15 | [graphify](https://github.com/Graphify-Labs/graphify)  | 140,935 | +5,168 (+3.8%)  | AI Engineering | Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.  |
|  16 | [Agent-Reach](https://github.com/Panniantong/Agent-Reach)  | 107,985 | +4,917 (+4.8%)  | Applications  | Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.  |
|  17 | [thinkrail](https://github.com/JetBrains/thinkrail)  |  7,137 | +4,816 (+207.5%) | Applications  | Vibe code with pi in a lightweight, real IDE that customises itself around the way you work — The Vibe You Need  |
|  18 | [TradingAgents](https://github.com/TauricResearch/TradingAgents)  | 119,888 | +4,395 (+3.8%)  | AI Engineering | TradingAgents: Multi-Agents LLM Financial Trading Framework  |
|  19 | [android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)  |  5,866 | +4,383 (+295.5%) | Applications  | 关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。  |
|  20 | [freellmapi](https://github.com/tashfeenahmed/freellmapi)  |  46,194 | +4,260 (+10.2%)  | AI Engineering | 7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behind one /v1 endpoint, plus any custom OpenAI-compatible endpoint. Smart routing, automatic failover, encrypted keys. Personal experimentation only.  |

## Trending by category

Up to three more weekly movers from each category. Projects already shown above are omitted.

### [AI Engineering](https://llmrepos.com/categories/ai-engineering?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [TokenEconomizer](https://github.com/microsoft/TokenEconomizer) |  4,380 | +4,151 (+1812.7%) | Experience-Driven Black-Box Cost Control for Coding Agents  |
|  2 | [hindsight](https://github.com/vectorize-io/hindsight)  |  58,025 | +4,007 (+7.4%)  | Hindsight: Agent Memory That Learns  |
|  3 | [openbot](https://github.com/nightly-labs/openbot)  |  4,628 | +3,530 (+321.5%)  | A local-first desktop workspace for persistent AI teammates. Run Codex, Claude, and Grok with dedicated workspaces, task queues, file sharing, browser control, and agent-to-agent collaboration. |

### [Applications](https://llmrepos.com/categories/applications?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [claude-seo](https://github.com/AgriciDaniel/claude-seo) |  25,898 | +4,080 (+18.7%)  | Universal SEO skill for Claude Code. 26 sub-skills + 19 sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, agent readiness (Lighthouse Agentic Browsing, WebMCP, llms.txt), backlinks, local SEO, e-commerce, international SEO, Google APIs, and PDF/Excel reporting. 9 optional extensions for live SEO data. |
|  2 | [ppt-master](https://github.com/hugohe3/ppt-master)  |  72,571 | +3,792 (+5.5%)  | AI turns documents or topics into real, native PowerPoint decks—with native shapes, transitions and animations, data-backed charts and tables on demand, audio narration from speaker notes, and support for your own .pptx templates. · by Hugo He  |
|  3 | [dossier](https://github.com/AienTech/dossier)  |  3,961 | +3,437 (+655.9%) | A self-hosted job search app that writes tailored resumes and cover letters from your profile.  |

### [Infrastructure](https://llmrepos.com/categories/infrastructure?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [xerj](https://github.com/xerj-org/xerj)  |  18,799 | +3,050 (+19.4%) | AI search engine and MCP server for bots and agents. One Rust binary indexes code, docs, logs, JSONL/CSV and PDFs for BM25 full-text, vector and hybrid search, code search without grep, agent memory and RAG. Elasticsearch-compatible API; Corpus Hub serves hundreds of reference memory corpora.  |
|  2 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute)  |  83,864 | +2,526 (+3.1%)  | Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 900+ contributors |
|  3 | [OmniRoute](https://github.com/cheaper-inference/OmniRoute) |  83,840 | +2,519 (+3.1%)  | Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 900+ contributors |

### [Model Development](https://llmrepos.com/categories/model-development?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [unsloth](https://github.com/unslothai/unsloth)  |  78,961 | +374 (+0.5%) | Local UI to run and train LLMs and diffusion models. Supports GGUF, MLX, Qwen3.8, DeepSeek-V4.1, MiniMax-H3, Gemma 4, FLUX and more. |
|  2 | [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 107,697 | +369 (+0.3%) | Implement a ChatGPT-like LLM in PyTorch from scratch, step by step  |
|  3 | [Soup](https://github.com/MakazhanAlpamys/Soup)  |  9,994 | +309 (+3.2%) | Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU.  |

### [Models](https://llmrepos.com/categories/models?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) |  64,612 | +813 (+1.3%)  | 1 min voice data can also be used to train a good TTS model! (few shot voice cloning)  |
|  2 | [MOSS-Image](https://github.com/OpenMOSS/MOSS-Image) |  2,486 | +569 (+29.7%) | Official repository for MOSS-Image, a 5B-parameter base DiT model with high-quality text rendering, layout generation, and efficient fine-tuning.  |
|  3 | [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) |  15,682 | +156 (+1.0%)  | Speech-to-text, text-to-speech, speaker diarization, speech enhancement, source separation, and VAD using next-gen Kaldi with onnxruntime without Internet connection. Support embedded systems, Android, iOS, HarmonyOS, Raspberry Pi, RISC-V, RK NPU, Axera NPU, Ascend NPU, x86_64 servers, websocket server/client, support 12 programming languages |

### [Lists](https://llmrepos.com/categories/lists?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) |  6,556 | +1,934 (+41.8%) | 77 game-dev skills for AI coding agents — Godot, Unity, Unreal, Phaser, PixiJS, three.js, Bevy, pygame, LÖVE, Roblox. Portable SKILL.md Agent Skills (the format Anthropic launched as Claude Skills), with a router that loads the right skill for your engine and task. Runs in Claude Code, Cursor, Kiro, Codex, Copilot, Gemini CLI and more. |
|  2 | [awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos)  |  13,171 | +1,840 (+16.2%) | A growing collection of viral videos made with Claude Opus 5.5 and the prompts behind them. Watch each original next to a live remake on Skillry. Updated regularly.  |
|  3 | [skills](https://github.com/jakubkrehel/skills)  |  10,292 | +1,738 (+20.3%) | A collection of agent skills that help you build great interfaces.  |

### [Tutorials](https://llmrepos.com/categories/tutorials?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [ai-agent-book](https://github.com/bojieli/ai-agent-book)  |  56,959 | +1,005 (+1.8%) | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码  |
|  2 | [diy-llm](https://github.com/datawhalechina/diy-llm)  |  2,696 | +824 (+44.0%)  | Covers pre-training data, Tokenizer, Transformer, MoE,distributed training, Scaling Laws, inference & alignment .6 progressive code assignments for full-stack LLM learning \| 涵盖预训练数据、分词器、Transformer、MoE、分布式训练、缩放定律、推理与对齐，6 项渐进代码作业，掌握 LLM 全栈知识 |
|  3 | [figures4papers](https://github.com/ChenLiu-1996/figures4papers) |  9,461 | +486 (+5.4%)  | My Python scripts to make high-quality figures for publications in top AI conferences and journals.  |

### [Misc](https://llmrepos.com/categories/misc?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [OpenDeepWiki](https://github.com/AIDotNet/OpenDeepWiki)  |  3,655 | +15 (+0.4%) | OpenDeepWiki is the open-source version of the DeepWiki project, aiming to provide a powerful knowledge management and collaboration platform. The project is mainly developed using C# and TypeScript, supporting modular design, and is easy to expand and customize. |
|  2 | [specification.website](https://github.com/jdevalk/specification.website) |  923 | +11 (+1.2%) | Website specification — HTML, accessibility, security, SEO, agent-readiness. Platform-agnostic, sourced, MIT.  |
|  3 | [OB1](https://github.com/NateBJones-Projects/OB1)  |  4,752 | +10 (+0.2%) | Open Brain — The infrastructure layer for your thinking. One database, one AI gateway, one chat channel — any AI plugs in. No middleware, no SaaS.  |
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
