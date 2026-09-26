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

*Last Updated: 21/09/2026*

<!-- BEGIN_TABLE -->
## Established leaders

The 20 most-starred active projects.

|  # | Repo  |  Stars | 7d growth  | Category  | About  |
|----------|----------|----------|----------|----------|----------|
|  1 | [openclaw](https://github.com/openclaw/openclaw)  | 390,192 | +537 (+0.1%)  | Applications  | The AI that really does things. Any OS. Any Platform. The lobster way. 🦞  |
|  2 | [superpowers](https://github.com/obra/superpowers)  | 289,561 | +3,067 (+1.1%) | AI Engineering | An agentic skills framework & software development methodology that works.  |
|  3 | [skills](https://github.com/mattpocock/skills)  | 266,887 | +5,113 (+2.0%) | AI Engineering | Skills for Real Engineers. Straight from my .agents directory.  |
|  4 | [ECC](https://github.com/affaan-m/ECC)  | 264,432 | +6,307 (+2.4%) | AI Engineering | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.  |
|  5 | [hermes-agent](https://github.com/NousResearch/hermes-agent)  | 247,677 | +2,307 (+0.9%) | AI Engineering | The agent that grows with you  |
|  6 | [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 231,972 | +8,536 (+3.8%) | AI Engineering | DeepSeek Harness: Everything is a Plugin.  |
|  7 | [opencode](https://github.com/anomalyco/opencode)  | 209,064 | +1,772 (+0.9%) | Applications  | The open source coding agent.  |
|  8 | [n8n](https://github.com/n8n-io/n8n)  | 205,545 | +1,286 (+0.6%) | AI Engineering | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.  |
|  9 | [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)  | 187,475 | +155 (+0.1%)  | Applications  | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.  |
|  10 | [markitdown](https://github.com/microsoft/markitdown)  | 186,108 | +2,235 (+1.2%) | AI Engineering | Python tool for converting files and office documents to Markdown.  |
|  11 | [firecrawl](https://github.com/firecrawl/firecrawl)  | 182,813 | +2,553 (+1.4%) | AI Engineering | The web data API to search, scrape, and interact at scale. 🔥  |
|  12 | [ollama](https://github.com/ollama/ollama)  | 181,358 | +458 (+0.3%)  | Infrastructure | Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.  |
|  13 | [skills](https://github.com/anthropics/skills)  | 177,427 | +1,189 (+0.7%) | AI Engineering | Public repository for Agent Skills  |
|  14 | [prompts.chat](https://github.com/f/prompts.chat)  | 170,885 | +577 (+0.3%)  | AI Engineering | f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.  |
|  15 | [transformers](https://github.com/huggingface/transformers)  | 166,466 | +634 (+0.4%)  | Infrastructure | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.  |
|  16 | [dify](https://github.com/langgenius/dify)  | 156,731 | +1,048 (+0.7%) | AI Engineering | Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.  |
|  17 | [langflow](https://github.com/langflow-ai/langflow)  | 155,093 | +303 (+0.2%)  | AI Engineering | Langflow is a powerful tool for building and deploying AI-powered agents and workflows.  |
|  18 | [agency-agents](https://github.com/msitarzewski/agency-agents)  | 153,902 | +1,659 (+1.1%) | AI Engineering | A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.  |
|  19 | [open-webui](https://github.com/open-webui/open-webui)  | 152,699 | +716 (+0.5%)  | AI Engineering | User-friendly AI Interface (Supports Ollama, OpenAI API, ...)  |
|  20 | [claude-code](https://github.com/anthropics/claude-code)  | 147,414 | +2,426 (+1.7%) | AI Engineering | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |

## Trending this week

The 20 largest seven-day star gains, excluding established leaders.

|  # | Repo  |  Stars | 7d growth  | Category  | About  |
|----------|----------|----------|----------|----------|----------|
|  1 | [security-audit-skill](https://github.com/cloudflare/security-audit-skill) |  18,602 | +15,314 (+465.8%)  | AI Engineering | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings  |
|  2 | [open-code-review](https://github.com/alibaba/open-code-review)  |  38,977 | +14,246 (+57.6%)  | Applications  | Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible. |
|  3 | [hypit](https://github.com/hypit-ai/hypit)  |  12,390 | +12,015 (+3204.0%) | Applications  | Clone any viral video with AI agents. Not just a script, the whole workflow: swap the face, the words, the B-roll, ship 100 variants in one command, and get your 100M views.  |
|  4 | [archify](https://github.com/tt-a1i/archify)  |  68,796 | +7,157 (+11.6%)  | AI Engineering | Agent skill for beautiful, verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams—self-contained HTML with motion and crisp export.  |
|  5 | [orca](https://github.com/stablyai/orca)  |  74,353 | +5,971 (+8.7%)  | AI Engineering | Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and remote runtime.  |
|  6 | [VoiceStudio](https://github.com/debpalash/VoiceStudio)  |  33,748 | +5,614 (+20.0%)  | Applications  | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.  |
|  7 | [OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio)  |  33,760 | +5,556 (+19.7%)  | Applications  | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.  |
|  8 | [ponytail](https://github.com/DietrichGebert/ponytail)  | 143,541 | +5,522 (+4.0%)  | AI Engineering | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.  |
|  9 | [WeKnora](https://github.com/Tencent/WeKnora)  |  28,393 | +5,305 (+23.0%)  | AI Engineering | Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.  |
|  10 | [i-have-adhd](https://github.com/ayghri/i-have-adhd)  |  49,558 | +4,600 (+10.2%)  | AI Engineering | A skill to stop your coding agent from burying the answer. ADHD-friendly output.  |
|  11 | [BrowserSkill](https://github.com/Tencent/BrowserSkill)  |  6,234 | +4,253 (+214.7%)  | AI Engineering | Let AI agents use your real, logged-in browser without interrupting your work. CLI + extension for browser automation across any shell-capable AI agent.  |
|  12 | [agent-skills](https://github.com/addyosmani/agent-skills)  |  98,019 | +3,785 (+4.0%)  | Applications  | Production-grade engineering skills for AI coding agents.  |
|  13 | [graphify](https://github.com/safishamsi/graphify)  | 120,097 | +3,477 (+3.0%)  | AI Engineering | Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.  |
|  14 | [graphify](https://github.com/Graphify-Labs/graphify)  | 120,068 | +3,469 (+3.0%)  | AI Engineering | Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.  |
|  15 | [Agent-Reach](https://github.com/Panniantong/Agent-Reach)  |  84,220 | +3,339 (+4.1%)  | Applications  | Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.  |
|  16 | [codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)  |  10,195 | +3,195 (+45.6%)  | AI Engineering | Use ChatGPT Web (including Pro) as a native model in Codex — with context, tools, streaming and images, without using Codex quota.  |
|  17 | [OpenResearch](https://github.com/alphaXiv/OpenResearch)  |  5,496 | +3,129 (+132.2%)  | AI Engineering | Turn your coding agents into research agents  |
|  18 | [ai-infra-book](https://github.com/bojieli/ai-infra-book)  |  4,840 | +3,105 (+179.0%)  | Tutorials  | 《深入理解 AI Infra：量化分析与系统设计》（李博杰 著）开源书稿：从硬件约束和模型架构出发，量化推导 LLM 推理与训练系统设计。含全书正文、PDF、配套计算工具与实验  |
|  19 | [pi](https://github.com/earendil-works/pi)  | 108,053 | +3,050 (+2.9%)  | AI Engineering | AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI  |
|  20 | [humanizer](https://github.com/blader/humanizer)  |  50,906 | +2,940 (+6.1%)  | AI Engineering | Agent skill that removes signs of AI-generated writing from text  |

## Trending by category

Up to three more weekly movers from each category. Projects already shown above are omitted.

### [AI Engineering](https://llmrepos.com/categories/ai-engineering?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [cua](https://github.com/trycua/cua)  |  25,535 | +2,909 (+12.9%)  | Scale computer-use 2.0 with open-source drivers, cross-OS fleets, and benchmarks for training, evaluation, and data generation. |
|  2 | [Octop](https://github.com/TencentCloud/Octop)  |  4,483 | +2,838 (+172.5%) | A smarter, self-hosted AI assistant — multi-user, multi-agent.  |
|  3 | [reef](https://github.com/Human-Agent-Society/reef) |  3,884 | +2,490 (+178.6%) | Continual learning infra for self-improving agents  |

### [Applications](https://llmrepos.com/categories/applications?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [OpenMontage](https://github.com/calesthio/OpenMontage) |  60,643 | +1,673 (+2.8%) | World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.  |
|  2 | [codex](https://github.com/openai/codex)  | 125,705 | +1,657 (+1.3%) | Lightweight coding agent that runs in your terminal  |
|  3 | [ppt-master](https://github.com/hugohe3/ppt-master)  |  55,752 | +1,475 (+2.7%) | AI turns documents or topics into real, native PowerPoint decks—with native shapes, transitions and animations, data-backed charts and tables on demand, audio narration from speaker notes, and support for your own .pptx templates. · by Hugo He |

### [Infrastructure](https://llmrepos.com/categories/infrastructure?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) |  68,766 | +2,825 (+4.3%)  | Never stop coding. Free MIT AI gateway: one endpoint, 352 providers (150+ free), 1200+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 550+ contributors |
|  2 | [utopia](https://github.com/deeplethe/utopia)  |  9,585 | +2,142 (+28.8%) | World's first open-source enterprise world model.  |
|  3 | [ComfyUI](https://github.com/Comfy-Org/ComfyUI)  | 134,250 | +1,198 (+0.9%)  | The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface.  |

### [Model Development](https://llmrepos.com/categories/model-development?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [Soup](https://github.com/MakazhanAlpamys/Soup)  |  6,939 | +537 (+8.4%)  | Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU.  |
|  2 | [NeoHorse](https://github.com/TokenRhythm/NeoHorse)  |  723 | +435 (+151.0%) | NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness. |
|  3 | [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 105,336 | +390 (+0.4%)  | Implement a ChatGPT-like LLM in PyTorch from scratch, step by step  |

### [Models](https://llmrepos.com/categories/models?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [needle](https://github.com/cactus-compute/needle)  |  12,003 | +1,002 (+9.1%) | Automation foundation model for tiny devices: 2-bit, 8-29 MB, tool calls, structured extraction and embeddings on phones, wearables, smart homes, robots, cars and microcontrollers. |
|  2 | [AuK](https://github.com/Tencent-Hunyuan/AuK)  |  1,186 | +346 (+41.2%)  | AuK: An Open-Source Foundational Model for Speech Generation and Editing  |
|  3 | [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) |  62,009 | +209 (+0.3%)  | 1 min voice data can also be used to train a good TTS model! (few shot voice cloning)  |

### [Lists](https://llmrepos.com/categories/lists?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) |  33,120 | +1,312 (+4.1%) | Prompt as Code \| GPT Image 2 / 2.5 提示词与案例库，530+ 个案例、20+ 套工业级模板与可复用 Skills，新增 2.5 同提示词对比专区，附完整提示词与生成记录，持续更新。 |
|  2 | [skills](https://github.com/jakubkrehel/skills)  |  6,958 | +462 (+7.1%)  | A collection of agent skills that help you build great interfaces.  |
|  3 | [awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis)  |  7,992 | +391 (+5.1%)  | List of Permanent Free LLM API (API Keys)  |

### [Tutorials](https://llmrepos.com/categories/tutorials?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [ai-agent-book](https://github.com/bojieli/ai-agent-book)  |  49,596 | +2,820 (+6.0%) | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码  |
|  2 | [zero-to-sglang](https://github.com/datawhalechina/zero-to-sglang) |  1,209 | +330 (+37.5%)  | Official SGLang x Datawhale course on LLM inference: understand inference, build a mini-sglang from scratch, then read the real SGLang source and land your first PR. Available in English and Chinese. |
|  3 | [WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)  |  3,138 | +183 (+6.2%)  | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。  |

### [Misc](https://llmrepos.com/categories/misc?utm_source=github&utm_medium=readme&utm_campaign=readme_funnel)

|  # | Repo  |  Stars | 7d growth  | About  |
|----------|----------|----------|----------|----------|
|  1 | [OB1](https://github.com/NateBJones-Projects/OB1)  |  4,631 | +16 (+0.3%) | Open Brain — The infrastructure layer for your thinking. One database, one AI gateway, one chat channel — any AI plugs in. No middleware, no SaaS. |
|  2 | [WhisperLive](https://github.com/collabora/WhisperLive)  |  4,290 | +16 (+0.4%) | A nearly-live implementation of OpenAI's Whisper.  |
|  3 | [specification.website](https://github.com/jdevalk/specification.website) |  863 | +10 (+1.2%) | Website specification — HTML, accessibility, security, SEO, agent-readiness. Platform-agnostic, sourced, MIT.  |
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
