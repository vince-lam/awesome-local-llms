# 👋 Awesome Local LLMs

A curated list of open-source projects covering all things local LLMs and generative AI — from running models locally to building production applications and autonomous agents. GitHub metrics (stars, forks, issues, contributors, releases, time since last commit) are refreshed automatically every week.

Projects span the full stack:

- **Inference & Runtime** — local engines, production serving, distributed inference, web/edge runtimes, and language bindings
- **Chat Interfaces** — desktop apps, web UIs, mobile apps, CLI tools, and browser extensions
- **Agentic Frameworks** — orchestration libraries, multi-agent systems, workflow builders, and memory/tool layers
- **Coding Assistants** — IDE extensions, terminal agents, code generation tools, and repo automation
- **Research & Knowledge** — research agents, RAG / document Q&A, and prompting optimisation
- **Data & Analytics** — text-to-SQL and data analysis agents
- **Web & Browser Agents** — browser automation and API/REST agents
- **General Autonomous Agents** — task automation and desktop/GUI control
- **Gaming & Simulation** — game agents and social simulations

Each repo carries one or more **tags** mapping to the subcategories above (defined in [`categories.json`](categories.json)). GitHub metrics are refreshed automatically every week by a GitHub Actions workflow.

**Contributions are welcome!** Suggest a repo I've missed by opening an issue, or add it to [`repos.json`](repos.json) (with its `tags` array) and open a pull request. The table below regenerates automatically.

There is also a fuller table of metrics in this [Google Sheet](https://docs.google.com/spreadsheets/d/1Xv38p90V3GiJXjq0a3qc24056Vicn1I5MG6QiFE6nVE/edit?usp=sharing) and [Airtable](https://airtable.com/apparaKqezkq2LECD/shrE26kWFaVU1cvgb) _(no longer updated — kept for reference)_.

For my thoughts on local LLM tooling: <https://vinlam.com/posts/local-llm-options/>

Note the condensed table below has two filters applied:

1. Repositories need more than 100 stars
2. Repositories require a commit within the last 60 days

## Open-Source LLM & Agent Projects

*Last Updated: 20/06/2026*

<!-- BEGIN_TABLE -->
|  # | Repo  | Tags  | About  |  Stars |  Forks |  Issues |  Contributors |  Releases | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)  | Task Automation  | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.  | 185,041 |  46,130 |  448 |  429 |  108 | Other  | 0 days, 4 hrs, 29 mins  |
|  2 | [ollama](https://github.com/ollama/ollama)  | Local Runtime  | Get up and running with Kimi-K2.6, GLM-5.1, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.  | 174,566 |  16,684 |  3,468 |  455 |  226 | MIT License  | 0 days, 10 hrs, 22 mins  |
|  3 | [transformers](https://github.com/huggingface/transformers)  | Bindings & SDKs  | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.  | 161,732 |  33,554 |  2,438 |  438 |  263 | Apache License 2.0  | 0 days, 9 hrs, 33 mins  |
|  4 | [dify](https://github.com/langgenius/dify)  | Workflow / Low-code  | Production-ready platform for agentic workflow development.  | 145,866 |  22,935 |  779 |  460 |  164 | Other  | 0 days, 3 hrs, 52 mins  |
|  5 | [open-webui](https://github.com/open-webui/open-webui)  | Web App  | User-friendly AI Interface (Supports Ollama, OpenAI API, ...)  | 142,300 |  20,454 |  434 |  390 |  163 | Other  | 0 days, 3 hrs, 51 mins  |
|  6 | [langchain](https://github.com/langchain-ai/langchain)  | Orchestration  | The agent engineering platform.  | 139,727 |  23,168 |  413 |  469 |  1,287 | MIT License  | 0 days, 1 hrs, 22 mins  |
|  7 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | Local Runtime  | LLM inference in C/C++  | 117,355 |  19,743 |  1,823 |  445 |  6,411 | MIT License  | 0 days, 3 hrs, 18 mins  |
|  8 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | Web App  | ✨ Light and Fast AI Assistant. Support: Web | iOS | MacOS | Android |  Linux | Windows  |  88,272 |  59,548 |  838 |  262 |  77 | MIT License  | 36 days, 2 hrs, 17 mins  |
|  9 | [vllm](https://github.com/vllm-project/vllm)  | Production Serving  | A high-throughput and memory-efficient inference and serving engine for LLMs  |  83,371 |  18,247 |  5,486 |  460 |  97 | Apache License 2.0  | 0 days, 0 hrs, 8 mins  |
|  10 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | Web App  | 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.  |  78,876 |  15,454 |  456 |  325 |  2,789 | Other  | 0 days, 0 hrs, 2 mins  |
|  11 | [OpenHands](https://github.com/All-Hands-AI/OpenHands)  | Repo & PR Automation, Terminal Agent  | 🙌 OpenHands: AI-Driven Development  |  77,790 |  9,888 |  324 |  463 |  103 | Other  | 0 days, 13 hrs, 9 mins  |
|  12 | [screenshot-to-code](https://github.com/abi/screenshot-to-code)  | Code Generation  | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue)  |  72,967 |  8,981 |  122 |  26 |  0 | MIT License  | 0 days, 2 hrs, 38 mins  |
|  13 | [gpt4free](https://github.com/xtekky/gpt4free)  | Bindings & SDKs  | The official gpt4free repository | various collection of powerful language models | opus 4.6 gpt 5.3 kimi 2.5 deepseek v3.2 gemini 3  |  66,364 |  13,573 |  4 |  261 |  464 | GNU General Public License v3.0  | 0 days, 11 hrs, 12 mins  |
|  14 | [open-interpreter](https://github.com/OpenInterpreter/open-interpreter)  | Terminal Agent  | A lightweight coding agent for open models like Deepseek, Kimi, and Qwen  |  64,057 |  5,551 |  270 |  477 |  50 | Apache License 2.0  | 0 days, 2 hrs, 8 mins  |
|  15 | [anything-llm](https://github.com/Mintplex-Labs/anything-llm)  | Web App, Document Q&A / RAG  | Stop renting your intelligence. Own it with AnythingLLM. Everything you need for a powerful local-first agent experience  |  61,825 |  6,746 |  308 |  204 |  31 | MIT License  | 1 days, 2 hrs, 22 mins  |
|  16 | [privateGPT](https://github.com/imartinez/privateGPT)  | Document Q&A / RAG, Web App  | Interact with your documents using the power of GPT, 100% privately, no data leaks  |  57,286 |  7,608 |  5 |  95 |  14 | Apache License 2.0  | 1 days, 13 hrs, 6 mins  |
|  17 | [crewAI](https://github.com/crewAIInc/crewAI)  | Multi-Agent System  | Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.  |  54,002 |  7,558 |  507 |  297 |  204 | MIT License  | 0 days, 0 hrs, 14 mins  |
|  18 | [Flowise](https://github.com/FlowiseAI/Flowise)  | Workflow / Low-code  | Build AI Agents, Visually  |  53,741 |  24,547 |  932 |  317 |  83 | Other  | 3 days, 16 hrs, 32 mins  |
|  19 | [llama_index](https://github.com/run-llama/llama_index)  | Orchestration  | LlamaIndex is the leading document agent and OCR platform  |  50,229 |  7,588 |  484 |  474 |  431 | MIT License  | 0 days, 3 hrs, 27 mins  |
|  20 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | Web App  | Open-source desktop app for local LLMs. Text, vision, tool-calling, OpenAI/Anthropic-compatible API. 100% private.  |  47,340 |  5,975 |  821 |  381 |  113 | GNU Affero General Public License v3.0  | 18 days, 0 hrs, 24 mins  |
|  21 | [LocalAI](https://github.com/mudler/LocalAI)  | Local Runtime  | LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.  |  47,000 |  4,147 |  199 |  206 |  120 | MIT License  | 0 days, 3 hrs, 57 mins  |
|  22 | [aider](https://github.com/Aider-AI/aider)  | Terminal Agent  | aider is AI pair programming in your terminal  |  46,486 |  4,626 |  1,637 |  172 |  93 | Apache License 2.0  | 28 days, 13 hrs, 35 mins |
|  23 | [exo](https://github.com/exo-explore/exo)  | Distributed Inference  | Run frontier AI locally.  |  45,478 |  3,257 |  264 |  97 |  16 | Apache License 2.0  | 4 days, 6 hrs, 54 mins  |
|  24 | [jan](https://github.com/janhq/jan)  | Desktop App, Local Runtime  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer.  |  43,088 |  2,946 |  456 |  151 |  102 | Other  | 0 days, 14 hrs, 24 mins  |
|  25 | [ColossalAI](https://github.com/hpcaitech/ColossalAI)  | Distributed Inference  | Making large AI models cheaper, faster and more accessible  |  41,400 |  4,508 |  500 |  189 |  50 | Apache License 2.0  | 25 days, 9 hrs, 58 mins  |
|  26 | [phidata](https://github.com/phidatahq/phidata)  | Orchestration  | Build, run, and manage agent platforms.  |  40,772 |  5,543 |  949 |  445 |  201 | Apache License 2.0  | 0 days, 6 hrs, 54 mins  |
|  27 | [chatbox](https://github.com/Bin-Huang/chatbox)  | Desktop App  | Powerful AI Client  |  40,562 |  4,111 |  1,184 |  65 |  57 | GNU General Public License v3.0  | 7 days, 19 hrs, 19 mins  |
|  28 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Web App  | Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active |  39,495 |  8,092 |  507 |  361 |  92 | MIT License  | 0 days, 7 hrs, 15 mins  |
|  29 | [langgraph](https://github.com/langchain-ai/langgraph)  | Orchestration  | Build resilient agents.  |  35,239 |  5,908 |  587 |  275 |  549 | MIT License  | 0 days, 17 hrs, 32 mins  |
|  30 | [dspy](https://github.com/stanfordnlp/dspy)  | Prompting & Optimization, Orchestration | DSPy: The framework for programming—not prompting—language models  |  35,160 |  2,983 |  527 |  402 |  109 | MIT License  | 1 days, 10 hrs, 40 mins  |
|  31 | [continue](https://github.com/continuedev/continue)  | IDE Extension  | open-source coding agent  |  34,141 |  4,741 |  917 |  393 |  827 | Apache License 2.0  | 0 days, 0 hrs, 12 mins  |
|  32 | [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot)  | Code Generation  | The first real AI developer  |  33,738 |  3,485 |  250 |  51 |  0 | Other  | 1 days, 8 hrs, 58 mins  |
|  33 | [ChatDev](https://github.com/OpenBMB/ChatDev)  | Multi-Agent System, Code Generation  | ChatDev 2.0: Dev All through LLM-powered Multi-Agent Collaboration  |  33,497 |  4,172 |  66 |  16 |  12 | Apache License 2.0  | 23 days, 14 hrs, 57 mins |
|  34 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | Web App  | LLM Frontend for Power Users.  |  29,598 |  5,594 |  500 |  347 |  102 | GNU Affero General Public License v3.0  | 30 days, 17 hrs, 29 mins |
|  35 | [composio](https://github.com/ComposioHQ/composio)  | Tool Integration  | Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you build AI agents that turn intent into action.  |  28,867 |  4,630 |  113 |  59 |  828 | MIT License  | 0 days, 3 hrs, 12 mins  |
|  36 | [semantic-kernel](https://github.com/microsoft/semantic-kernel)  | Orchestration  | Integrate cutting-edge LLM technology quickly and easily into your apps  |  28,163 |  4,657 |  265 |  397 |  272 | MIT License  | 0 days, 3 hrs, 54 mins  |
|  37 | [gpt-researcher](https://github.com/assafelovic/gpt-researcher)  | Research Agent  | An autonomous agent that conducts deep research on any data using any LLM providers  |  27,795 |  3,751 |  225 |  223 |  70 | Apache License 2.0  | 22 days, 19 hrs, 56 mins |
|  38 | [agentscope](https://github.com/modelscope/agentscope)  | Orchestration, Multi-Agent System  | Build and run agents you can see, understand and trust.  |  27,010 |  3,037 |  289 |  64 |  40 | Apache License 2.0  | 1 days, 0 hrs, 41 mins  |
|  39 | [haystack](https://github.com/deepset-ai/haystack)  | Orchestration, Document Q&A / RAG  | Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.  |  25,614 |  2,867 |  108 |  368 |  232 | Apache License 2.0  | 0 days, 12 hrs, 45 mins  |
|  40 | [llamafile](https://github.com/Mozilla-Ocho/llamafile)  | Local Runtime  | Distribute and run LLMs with a single file.  |  25,049 |  1,410 |  214 |  71 |  40 | Other  | 10 days, 15 hrs, 19 mins |
|  41 | [letta](https://github.com/letta-ai/letta)  | Memory & State  | Platform for stateful agents: AI with advanced memory that can learn and self-improve over time.  |  23,418 |  2,488 |  66 |  139 |  177 | Apache License 2.0  | 36 days, 10 hrs, 24 mins |
|  42 | [memgpt](https://github.com/cpacker/memgpt)  | Memory & State  | Platform for stateful agents: AI with advanced memory that can learn and self-improve over time.  |  23,418 |  2,488 |  66 |  139 |  177 | Apache License 2.0  | 36 days, 10 hrs, 23 mins |
|  43 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Web / Edge Runtime  | Universal LLM Deployment Engine with ML Compilation  |  22,826 |  2,066 |  315 |  159 |  1 | Apache License 2.0  | 39 days, 4 hrs, 44 mins  |
|  44 | [swe-agent](https://github.com/princeton-nlp/swe-agent)  | Repo & PR Automation, Terminal Agent  | SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. [NeurIPS 2024]  |  19,567 |  2,139 |  23 |  96 |  10 | MIT License  | 3 days, 2 hrs, 34 mins  |
|  45 | [DB-GPT](https://github.com/csunny/DB-GPT)  | Data Analysis Agent, Text-to-SQL  | open-source agentic AI data assistant for the next generation of AI + Data products.  |  19,022 |  2,741 |  412 |  173 |  54 | MIT License  | 0 days, 12 hrs, 5 mins  |
|  46 | [web-llm](https://github.com/mlc-ai/web-llm)  | Web / Edge Runtime  | High-performance In-browser LLM Inference Engine  |  18,232 |  1,309 |  146 |  53 |  4 | Apache License 2.0  | 10 days, 23 hrs, 58 mins |
|  47 | [agent-zero](https://github.com/frdel/agent-zero)  | Terminal Agent  | Agent Zero AI framework  |  18,124 |  3,657 |  356 |  45 |  61 | Other  | 0 days, 13 hrs, 13 mins  |
|  48 | [WrenAI](https://github.com/Canner/WrenAI)  | Text-to-SQL  | Give AI agents the context to query business data correctly through the open context layer that gives AI agents grounded, governed memory, context, SQL across 20+ data sources, that helps you build agentic GenBI, text-to-sql, dashboards, and agentic analytics.  |  15,578 |  1,772 |  329 |  63 |  168 | Other  | 0 days, 16 hrs, 11 mins  |
|  49 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | Web App  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  |  15,309 |  2,228 |  129 |  54 |  27 | GNU General Public License v3.0  | 50 days, 13 hrs, 41 mins |
|  50 | [botpress](https://github.com/botpress/botpress)  | Workflow / Low-code  | The open-source hub to build & deploy GPT/LLM Agents ⚡️  |  14,748 |  2,268 |  87 |  74 |  126 | MIT License  | 0 days, 9 hrs, 53 mins  |
|  51 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | Production Serving  | TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in a performant way.  |  13,923 |  2,483 |  1,423 |  403 |  81 | Other  | 0 days, 0 hrs, 28 mins  |
|  52 | [e2b](https://github.com/e2b-dev/e2b)  | Tool Integration  | Open-source, secure environment with real-world tools for enterprise-grade agents.  |  12,654 |  937 |  50 |  51 |  522 | Apache License 2.0  | 0 days, 6 hrs, 55 mins  |
|  53 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Production Serving  | Run any open-source LLMs, such as DeepSeek and Llama, as OpenAI compatible API endpoint in the cloud.  |  12,360 |  817 |  16 |  32 |  147 | Apache License 2.0  | 4 days, 10 hrs, 40 mins  |
|  54 | [llm](https://github.com/simonw/llm)  | CLI / Terminal  | Access large language models from the command-line  |  12,063 |  893 |  624 |  58 |  63 | Apache License 2.0  | 0 days, 3 hrs, 13 mins  |
|  55 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | Local Runtime  | Run GGUF models easily with a KoboldAI UI. One File. Zero Install.  |  10,815 |  717 |  463 |  441 |  128 | GNU Affero General Public License v3.0  | 0 days, 0 hrs, 16 mins  |
|  56 | [chat-ui](https://github.com/huggingface/chat-ui)  | Web App  | The open source codebase powering HuggingChat  |  10,771 |  1,658 |  247 |  152 |  18 | Apache License 2.0  | 0 days, 0 hrs, 3 mins  |
|  57 | [server](https://github.com/triton-inference-server/server)  | Production Serving  | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  |  10,765 |  1,796 |  898 |  137 |  91 | BSD 3-Clause "New" or "Revised" License | 0 days, 21 hrs, 27 mins  |
|  58 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Bindings & SDKs  | Python bindings for llama.cpp  |  10,418 |  1,418 |  670 |  183 |  425 | MIT License  | 0 days, 1 hrs, 10 mins  |
|  59 | [inference](https://github.com/xorbitsai/inference)  | Production Serving  | Swap GPT for any LLM by changing a single line of code. Xinference lets you run open-source, speech, and multimodal models on cloud, on-prem, or your laptop — all through one unified, production-ready inference API.  |  9,368 |  836 |  38 |  146 |  139 | Apache License 2.0  | 0 days, 16 hrs, 41 mins  |
|  60 | [page-assist](https://github.com/n4ze3m/page-assist)  | Browser Extension  | Use your locally running AI models to assist you in your web browsing  |  8,005 |  757 |  342 |  39 |  104 | MIT License  | 2 days, 18 hrs, 12 mins  |
|  61 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | Production Serving  | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  |  7,906 |  700 |  590 |  138 |  66 | Apache License 2.0  | 1 days, 17 hrs, 25 mins  |
|  62 | [multi-agent-orchestrator](https://github.com/awslabs/multi-agent-orchestrator) | Multi-Agent System  | Flexible and powerful framework for managing multiple AI agents and handling complex conversations  |  7,660 |  721 |  110 |  26 |  17 | Apache License 2.0  | 2 days, 18 hrs, 57 mins  |
|  63 | [pocketpal-ai](https://github.com/a-ghorbani/pocketpal-ai)  | Mobile App  | An app that brings language models directly to your phone.  |  7,314 |  742 |  159 |  20 |  78 | MIT License  | 0 days, 3 hrs, 44 mins  |
|  64 | [big-agi](https://github.com/enricoros/big-agi)  | Web App  | AI suite powered by state-of-the-art models and providing advanced AI/AGI functions. Includes AI personas, AGI functions, world-class Beam multi-model chats, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy on-prem or in the cloud.  |  7,006 |  1,571 |  278 |  55 |  22 | MIT License  | 0 days, 0 hrs, 33 mins  |
|  65 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Web App  | Lord of Large Language and Multi modal Systems Web User Interface  |  4,785 |  580 |  178 |  42 |  24 | Apache License 2.0  | 2 days, 8 hrs, 4 mins  |
|  66 | [agency-swarm](https://github.com/VRSEN/agency-swarm)  | Multi-Agent System  | Reliable Multi-Agent Orchestration Framework  |  4,454 |  1,058 |  8 |  22 |  64 | MIT License  | 2 days, 1 hrs, 7 mins  |
|  67 | [gptme](https://github.com/ErikBjare/gptme)  | Terminal Agent  | Your agent in your terminal, equipped with local tools: writes code, uses the terminal, browses the web. Make your own persistent autonomous agent on top!  |  4,333 |  389 |  8 |  34 |  100 | MIT License  | 0 days, 0 hrs, 28 mins  |
|  68 | [langroid](https://github.com/langroid/langroid)  | Orchestration  | Harness LLMs with Multi-Agent Programming  |  4,040 |  376 |  68 |  31 |  556 | MIT License  | 4 days, 11 hrs, 46 mins  |
|  69 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | Bindings & SDKs  | A C#/.NET library to run LLM (🦙LLaMA/LLaVA) on your local device efficiently.  |  3,718 |  498 |  22 |  87 |  30 | MIT License  | 18 days, 6 hrs, 37 mins  |
|  70 | [AGiXT](https://github.com/Josh-XT/AGiXT)  | Orchestration  | AGiXT is a dynamic AI Agent Automation Platform that seamlessly orchestrates instruction management and complex task execution across diverse AI providers. Combining adaptive memory, smart features, and a versatile plugin system, AGiXT delivers efficient and comprehensive AI solutions.  |  3,198 |  447 |  2 |  41 |  433 | MIT License  | 3 days, 2 hrs, 30 mins  |
|  71 | [core](https://github.com/cheshire-cat-ai/core)  | Orchestration  | AI agent microservice  |  3,046 |  406 |  5 |  76 |  0 | GNU General Public License v3.0  | 0 days, 17 hrs, 33 mins  |
|  72 | [Rapid-MLX](https://github.com/raullenchai/Rapid-MLX)  | Local Runtime  | The fastest local AI engine for Apple Silicon. 4.2x faster than Ollama, 0.08s cached TTFT, 100% tool calling. 17 tool parsers, prompt cache, reasoning separation, cloud routing. Drop-in OpenAI replacement. Works with Claude Code, Cursor, Aider.  |  2,992 |  350 |  31 |  30 |  127 | Apache License 2.0  | 0 days, 0 hrs, 39 mins  |
|  73 | [GPT-Agent](https://github.com/SamurAIGPT/GPT-Agent)  | Game Agent  | A personal knowledge base that builds and maintains itself. Drop in sources — Claude (or Codex/Gemini) reads them, extracts knowledge, and maintains a persistent interlinked wiki. Works with Claude Code, Codex, OpenCode, Gemini CLI. No API key needed.  |  2,990 |  352 |  4 |  6 |  0 | MIT License  | 6 days, 21 hrs, 12 mins  |
|  74 | [ChatterUI](https://github.com/Vali-98/ChatterUI)  | Mobile App  | A frontend for running models on mobile or connecting to your preferred API providers.  |  2,510 |  222 |  29 |  8 |  91 | GNU Affero General Public License v3.0  | 4 days, 19 hrs, 27 mins  |
|  75 | [oterm](https://github.com/ggozad/oterm)  | CLI / Terminal  | the terminal client for LLMs  |  2,398 |  134 |  8 |  24 |  80 | MIT License  | 11 days, 18 hrs, 34 mins |
|  76 | [lagent](https://github.com/InternLM/lagent)  | Orchestration  | A lightweight framework for building LLM-based agents  |  2,258 |  236 |  23 |  34 |  12 | Apache License 2.0  | 1 days, 18 hrs, 36 mins  |
|  77 | [Adala](https://github.com/HumanSignal/Adala)  | Data Analysis Agent  | Adala: Autonomous DAta (Labeling) Agent framework  |  1,605 |  153 |  168 |  18 |  4 | Apache License 2.0  | 0 days, 3 hrs, 41 mins  |
|  78 | [uAgents](https://github.com/fetchai/uAgents)  | API / REST Agent  | A fast and lightweight framework for creating decentralized agents with ease.  |  1,587 |  348 |  42 |  62 |  110 | Apache License 2.0  | 1 days, 13 hrs, 47 mins  |
|  79 | [Alpaca](https://github.com/Jeffser/Alpaca)  | Desktop App  | 🦙 Local and online AI hub  |  1,586 |  142 |  115 |  60 |  113 | GNU General Public License v3.0  | 11 days, 2 hrs, 59 mins  |
|  80 | [dust](https://github.com/dust-tt/dust)  | Orchestration, Workflow / Low-code  | Custom AI agent platform to speed up your work.  |  1,389 |  287 |  207 |  101 |  28 | MIT License  | 0 days, 6 hrs, 0 mins  |
|  81 | [aideml](https://github.com/WecoAI/aideml)  | Code Generation  | AIDE: AI-Driven Exploration in the Space of Code. The machine Learning engineering agent that automates AI R&D.  |  1,326 |  194 |  0 |  12 |  4 | MIT License  | 48 days, 11 hrs, 20 mins |
|  82 | [Atomic-Chat](https://github.com/AtomicBot-ai/Atomic-Chat)  | Desktop App, Local Runtime  | Local AI app and inference engine for agents. Run open-weight LLMs locally — private, 100% offline on your computer.  |  928 |  87 |  21 |  145 |  35 | Other  | 0 days, 9 hrs, 50 mins  |
|  83 | [AgentForge](https://github.com/DataBassGit/AgentForge)  | Orchestration  | Extensible AGI Framework  |  819 |  161 |  4 |  7 |  7 | GNU General Public License v3.0  | 8 days, 6 hrs, 13 mins  |
|  84 | [tenere](https://github.com/pythops/tenere)  | CLI / Terminal  | 🤖 TUI for LLMs  |  673 |  34 |  10 |  10 |  14 | GNU General Public License v3.0  | 40 days, 20 hrs, 12 mins |
|  85 | [taskgen](https://github.com/simbianai/taskgen)  | Orchestration  | Task-based Agentic Framework using StrictJSON as the core  |  462 |  46 |  2 |  14 |  0 | MIT License  | 11 days, 14 hrs, 6 mins  |
|  86 | [autonomous-hr-chatbot](https://github.com/stepanogil/autonomous-hr-chatbot)  | Orchestration  | An autonomous HR agent that can answer user queries using tools  |  449 |  112 |  5 |  1 |  0 | MIT License  | 51 days, 21 hrs, 2 mins  |
|  87 | [AgentRun](https://github.com/Jonathan-Adly/AgentRun)  | Code Generation, Tool Integration  | The easiest, and fastest way to run AI-generated Python code safely  |  371 |  41 |  8 |  2 |  9 | Apache License 2.0  | 3 days, 4 hrs, 32 mins  |
|  88 | [qvac](https://github.com/tetherto/qvac)  | Bindings & SDKs  | QVAC - Local AI SDK and libraries for building private, cross-platform, peer-to-peer AI applications. Run LLMs, speech-to-text, translation, and more locally on Linux, macOS, Windows, Android, and iOS.  |  260 |  72 |  90 |  59 |  192 | Apache License 2.0  | 0 days, 6 hrs, 3 mins  |
|  89 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Desktop App  | Local ML voice chat using high-end models.  |  188 |  13 |  0 |  1 |  0 | MIT License  | 15 days, 4 hrs, 11 mins  |
|  90 | [lite.koboldai.net](https://github.com/LostRuins/lite.koboldai.net)  | Web App  | A zero dependency web UI for any LLM backend, including KoboldCpp, OpenAI and AI Horde  |  183 |  89 |  31 |  39 |  0 | GNU Affero General Public License v3.0  | 0 days, 0 hrs, 35 mins  |
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
