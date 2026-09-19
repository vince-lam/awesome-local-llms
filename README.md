<div align="center">

# 👋 Awesome Local LLMs

### 10,000+ open-source LLM, agent, and local inference repos, tracked daily

[**llmrepos.com**](https://llmrepos.com) sorts them by how fast they are gaining stars, not by how many they have.

[![Browse llmrepos.com](https://img.shields.io/badge/browse-llmrepos.com-2ea44f?style=for-the-badge)](https://llmrepos.com)
[![Stars](https://img.shields.io/github/stars/vince-lam/awesome-local-llms?style=for-the-badge)](https://github.com/vince-lam/awesome-local-llms/stargazers)
[![Daily refresh](https://img.shields.io/github/actions/workflow/status/vince-lam/awesome-local-llms/update-stats.yml?style=for-the-badge&label=daily%20refresh)](https://github.com/vince-lam/awesome-local-llms/actions/workflows/update-stats.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)

<a href="https://llmrepos.com"><img src="assets/llmrepos-demo.gif" alt="llmrepos.com: a searchable, sortable table of 8,600+ open-source LLM and AI agent repos with 1d/7d/30d star growth and category, subcategory, language and license filters" width="100%"></a>

</div>

---

## What this is

A curated list of open-source projects for building with LLMs, covering the whole stack: model weights, training code, inference runtimes, agent frameworks, end-user apps, and the lists and tutorials that help you learn.

Each repo is checked once a day for stars, 1d/7d/30d star growth, forks, contributors, open issues, language, license, creation date, and time since last commit.

Two ways to use it:

- [**llmrepos.com**](https://llmrepos.com) has all 8,600+ repos, with search, growth sorting, and filters by category, subcategory, language, and license.
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

**Contributions are welcome!** Suggest a repo I've missed by [opening an issue](https://github.com/vince-lam/awesome-local-llms/issues/new).

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

*Last Updated: 19/09/2026*

<!-- BEGIN_TABLE -->
## Established leaders

The 20 most-starred active projects.

|  # | Repo  |  Stars | 7d growth  | Category  | About  |
|----------|----------|----------|----------|----------|----------|
|  1 | [openclaw](https://github.com/openclaw/openclaw)  | 390,027 | +610 (+0.2%)  | Applications  | The AI that really does things. Any OS. Any Platform. The lobster way. 🦞  |
|  2 | [superpowers](https://github.com/obra/superpowers)  | 288,225 | +3,359 (+1.2%) | AI Engineering | An agentic skills framework & software development methodology that works.  |
|  3 | [skills](https://github.com/mattpocock/skills)  | 264,742 | +5,642 (+2.2%) | AI Engineering | Skills for Real Engineers. Straight from my .agents directory.  |
|  4 | [ECC](https://github.com/affaan-m/ECC)  | 261,395 | +5,337 (+2.1%) | AI Engineering | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.  |
|  5 | [hermes-agent](https://github.com/NousResearch/hermes-agent)  | 246,656 | +2,319 (+0.9%) | AI Engineering | The agent that grows with you  |
|  6 | [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 228,283 | +8,731 (+4.0%) | AI Engineering | DeepSeek Harness: Everything is a Plugin.  |
|  7 | [opencode](https://github.com/anomalyco/opencode)  | 208,275 | +1,703 (+0.8%) | Applications  | The open source coding agent.  |
|  8 | [n8n](https://github.com/n8n-io/n8n)  | 205,139 | +1,163 (+0.6%) | AI Engineering | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.  |
|  9 | [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)  | 187,424 | +173 (+0.1%)  | Applications  | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.  |
|  10 | [markitdown](https://github.com/microsoft/markitdown)  | 185,223 | +2,722 (+1.5%) | AI Engineering | Python tool for converting files and office documents to Markdown.  |
|  11 | [firecrawl](https://github.com/firecrawl/firecrawl)  | 181,778 | +2,853 (+1.6%) | AI Engineering | The web data API to search, scrape, and interact at scale. 🔥  |
|  12 | [ollama](https://github.com/ollama/ollama)  | 181,189 | +556 (+0.3%)  | Infrastructure | Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.  |
|  13 | [skills](https://github.com/anthropics/skills)  | 176,945 | +1,225 (+0.7%) | AI Engineering | Public repository for Agent Skills  |
|  14 | [prompts.chat](https://github.com/f/prompts.chat)  | 170,618 | +691 (+0.4%)  | AI Engineering | f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.  |
|  15 | [transformers](https://github.com/huggingface/transformers)  | 166,275 | +1,171 (+0.7%) | Infrastructure | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.  |
|  16 | [dify](https://github.com/langgenius/dify)  | 156,236 | +846 (+0.5%)  | AI Engineering | Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.  |
|  17 | [langflow](https://github.com/langflow-ai/langflow)  | 154,960 | +396 (+0.3%)  | AI Engineering | Langflow is a powerful tool for building and deploying AI-powered agents and workflows.  |
|  18 | [agency-agents](https://github.com/msitarzewski/agency-agents)  | 153,228 | +1,619 (+1.1%) | AI Engineering | A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables. |
|  19 | [open-webui](https://github.com/open-webui/open-webui)  | 152,438 | +844 (+0.6%)  | AI Engineering | User-friendly AI Interface (Supports Ollama, OpenAI API, ...)  |
|  20 | [langchain](https://github.com/langchain-ai/langchain)  | 146,574 | +464 (+0.3%)  | AI Engineering | The agent engineering platform.  |

## Trending this week

The 20 largest seven-day star gains, excluding established leaders.

|  # | Repo  |  Stars | 7d growth  | Category  | About  |
|----------|----------|----------|----------|----------|----------|
|  1 | [open-code-review](https://github.com/alibaba/open-code-review)  |  35,640 | +13,407 (+60.3%) | Applications  | Fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible.  |
|  2 | [OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio)  |  32,584 | +10,246 (+45.9%) | Applications  | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.  |
|  3 | [VoiceStudio](https://github.com/debpalash/VoiceStudio)  |  32,570 | +10,238 (+45.8%) | Applications  | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.  |
|  4 | [i-have-adhd](https://github.com/ayghri/i-have-adhd)  |  47,591 | +8,617 (+22.1%)  | AI Engineering | A skill to stop your coding agent from burying the answer. ADHD-friendly output.  |
|  5 | [archify](https://github.com/tt-a1i/archify)  |  66,109 | +8,412 (+14.6%)  | AI Engineering | Agent skill for beautiful, verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams—self-contained HTML with motion and crisp export.  |
|  6 | [security-audit-skill](https://github.com/cloudflare/security-audit-skill) |  11,092 | +7,822 (+239.2%) | AI Engineering | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings  |
|  7 | [ponytail](https://github.com/DietrichGebert/ponytail)  | 141,563 | +6,439 (+4.8%)  | AI Engineering | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.  |
|  8 | [orca](https://github.com/stablyai/orca)  |  71,347 | +5,138 (+7.8%)  | AI Engineering | Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and remote runtime.  |
|  9 | [WeKnora](https://github.com/Tencent/WeKnora)  |  26,594 | +4,404 (+19.8%)  | AI Engineering | Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.  |
|  10 | [OpenResearch](https://github.com/alphaXiv/OpenResearch)  |  5,081 | +4,079 (+407.1%) | AI Engineering | Turn your coding agents into research agents  |
|  11 | [Agent-Reach](https://github.com/Panniantong/Agent-Reach)  |  82,912 | +3,560 (+4.5%)  | Applications  | Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.  |
|  12 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute)  |  67,560 | +3,131 (+4.9%)  | Infrastructure | Never stop coding. Free MIT AI gateway: one endpoint, 352 providers (150+ free), 1200+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 550+ contributors |
|  13 | [humanizer](https://github.com/blader/humanizer)  |  49,672 | +3,047 (+6.5%)  | AI Engineering | Agent skill that removes signs of AI-generated writing from text  |
|  14 | [TradingAgents](https://github.com/TauricResearch/TradingAgents)  | 107,371 | +2,801 (+2.7%)  | AI Engineering | TradingAgents: Multi-Agents LLM Financial Trading Framework  |
|  15 | [pi](https://github.com/earendil-works/pi)  | 106,759 | +2,782 (+2.7%)  | AI Engineering | AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI  |
|  16 | [OpenMontage](https://github.com/calesthio/OpenMontage)  |  59,817 | +2,716 (+4.8%)  | Applications  | World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.  |
|  17 | [codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)  |  9,053 | +2,704 (+42.6%)  | AI Engineering | Use ChatGPT Web (including Pro) as a native model in Codex — with context, tools, streaming and images, without using Codex quota.  |
|  18 | [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks)  |  67,395 | +2,633 (+4.1%)  | AI Engineering | Extracted system prompts from Anthropic - Claude Fable 5.1, Opus 5, Claude Design, Claude Code. OpenAI - ChatGPT GPT-6-Astra, Codex. Google - Gemini 3.8 Flash, 3.1 Pro, Antigravity. xAI - Grok, Grok Bot, Cursor, Kimi and more! Updated regularly.  |
|  19 | [ai-agent-book](https://github.com/bojieli/ai-agent-book)  |  48,382 | +2,615 (+5.7%)  | Tutorials  | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码  |
|  20 | [agent-skills](https://github.com/addyosmani/agent-skills)  |  96,029 | +2,578 (+2.8%)  | Applications  | Production-grade engineering skills for AI coding agents.  |

## Trending by category

Up to three more weekly movers from each category. Projects already shown above are omitted.

### [AI Engineering](https://llmrepos.com/categories/ai-engineering?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [BrowserSkill](https://github.com/Tencent/BrowserSkill) |  4,492 | +2,565 (+133.1%) | Let AI agents use your real, logged-in browser without interrupting your work. CLI + extension for browser automation across any shell-capable AI agent. |
|  2 | [reef](https://github.com/Human-Agent-Society/reef)  |  3,395 | +2,461 (+263.5%) | Continual learning infra for self-improving agents  |
|  3 | [spec-kit](https://github.com/github/spec-kit)  | 137,681 | +2,344 (+1.7%)  | 💫 Toolkit to help you get started with Spec-Driven Development  |

### [Applications](https://llmrepos.com/categories/applications?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 124,491 | +2,152 (+1.8%)  | 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow.  |
|  2 | [DeskcommCRM](https://github.com/melgarafael/DeskcommCRM)  |  3,098 | +2,065 (+199.9%) | Open-source AI sales OS — self-hosted CRM with native AI agents + WhatsApp (WAHA). Open alternative to Kommo, Octadesk & Intercom for any business that sells by chat. MCP-ready, multi-tenant, LGPD. |
|  3 | [codex](https://github.com/openai/codex)  | 125,006 | +1,808 (+1.5%)  | Lightweight coding agent that runs in your terminal  |

### [Infrastructure](https://llmrepos.com/categories/infrastructure?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [ComfyUI](https://github.com/Comfy-Org/ComfyUI)  | 133,717 | +1,249 (+0.9%)  | The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface.  |
|  2 | [utopia](https://github.com/deeplethe/utopia)  |  7,983 | +1,202 (+17.7%) | World's first open-source enterprise world model.  |
|  3 | [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) |  52,357 | +1,008 (+2.0%)  | Wrap Antigravity, ChatGPT Codex, Claude Code, Grok Build as an OpenAI/Gemini/Claude/Codex compatible API service, allowing you to enjoy the free Gemini 3.1 Pro, GPT 5.6 Series, Grok 4.5, Claude model through API |

### [Model Development](https://llmrepos.com/categories/model-development?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [Soup](https://github.com/MakazhanAlpamys/Soup)  |  6,775 | +713 (+11.8%)  | Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU.  |
|  2 | [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 105,175 | +434 (+0.4%)  | Implement a ChatGPT-like LLM in PyTorch from scratch, step by step  |
|  3 | [NeoHorse](https://github.com/TokenRhythm/NeoHorse)  |  535 | +412 (+335.0%) | NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness. |

### [Models](https://llmrepos.com/categories/models?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [needle](https://github.com/cactus-compute/needle)  |  11,155 | +372 (+3.4%) | Automation foundation model for tiny devices: 2-bit, 8-29 MB, tool calls, structured extraction and embeddings on phones, wearables, smart homes, robots, cars and microcontrollers. |
|  2 | [index-tts](https://github.com/index-tts/index-tts)  |  24,053 | +172 (+0.7%) | An Industrial-Level Controllable and Efficient Zero-Shot Text-To-Speech System  |
|  3 | [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) |  61,878 | +161 (+0.3%) | 1 min voice data can also be used to train a good TTS model! (few shot voice cloning)  |

### [Lists](https://llmrepos.com/categories/lists?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) |  32,564 | +1,508 (+4.9%) | Prompt as Code \| GPT Image 2 / 2.5 提示词与案例库，530+ 个案例、20+ 套工业级模板与可复用 Skills，新增 2.5 同提示词对比专区，附完整提示词与生成记录，持续更新。  |
|  2 | [skills](https://github.com/jakubkrehel/skills)  |  6,854 | +750 (+12.3%)  | A collection of agent skills that help you build great interfaces.  |
|  3 | [skill](https://github.com/anbeime/skill)  |  6,887 | +371 (+5.7%)  | 收录最全、更新最快的技能Skills商店：精选原创技能包（涵盖文档处理、内容创作、编程开发、机器学习、自动化工作流），全部打包好可直接安装使用！同时自动抓取GitHub上万个Skills项目，按分类、更新时间、Star数量整理。The most comprehensive and frequently updated AI Agent skill library, featuring curated skill packs across document processing, content creation, programming, machine learning, automated workflows, and many more domains. |

### [Tutorials](https://llmrepos.com/categories/tutorials?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [deepagents-in-action](https://github.com/datawhalechina/deepagents-in-action) |  2,449 | +453 (+22.7%) | 📚 《Deep Agents 实战》—— LangChain 官方大使出品，基于 LangChain / LangGraph 生态，从零构建生产级 AI Agent 的完整指南  |
|  2 | [zero-to-sglang](https://github.com/datawhalechina/zero-to-sglang)  |  955 | +250 (+35.5%) | Official SGLang x Datawhale course on LLM inference: understand inference, build a mini-sglang from scratch, then read the real SGLang source and land your first PR. Available in English and Chinese. |
|  3 | [WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)  |  3,065 | +155 (+5.3%)  | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。  |

### [Misc](https://llmrepos.com/categories/misc?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [WhisperLive](https://github.com/collabora/WhisperLive)  |  4,286 | +28 (+0.7%) | A nearly-live implementation of OpenAI's Whisper.  |
|  2 | [OB1](https://github.com/NateBJones-Projects/OB1)  |  4,625 | +19 (+0.4%) | Open Brain — The infrastructure layer for your thinking. One database, one AI gateway, one chat channel — any AI plugs in. No middleware, no SaaS.  |
|  3 | [OpenDeepWiki](https://github.com/AIDotNet/OpenDeepWiki) |  3,594 | +12 (+0.3%) | OpenDeepWiki is the open-source version of the DeepWiki project, aiming to provide a powerful knowledge management and collaboration platform. The project is mainly developed using C# and TypeScript, supporting modular design, and is easy to expand and customize. |
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
