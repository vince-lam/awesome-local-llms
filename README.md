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

*Last Updated: 20/06/2026*

<!-- BEGIN_TABLE -->
|  # | Repo  | Category  | Subcategory  | About  | Stars  | Forks  | Issues  |  Contributors | Releases  | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)  | Agent  | General  | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.  | 185,040 | 46,129  | 448  |  429 | 108  | Other  | 0 days, 2 hrs, 51 mins  |
|  2 | [ollama](https://github.com/ollama/ollama)  | Local LLM  | Inference Backend | Get up and running with Kimi-K2.6, GLM-5.1, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.  | 174,561 | 16,683  | 3,467  |  455 | 226  | MIT License  | 0 days, 8 hrs, 42 mins  |
|  3 | [transformers](https://github.com/huggingface/transformers)  | Local LLM  | Inference Backend | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.  | 161,730 | 33,552  | 2,437  |  438 | 263  | Apache License 2.0  | 0 days, 7 hrs, 53 mins  |
|  4 | [dify](https://github.com/langgenius/dify)  | Agent  | Framework  | Production-ready platform for agentic workflow development.  | 145,854 | 22,935  | 779  |  460 | 164  | Other  | 0 days, 2 hrs, 15 mins  |
|  5 | [open-webui](https://github.com/open-webui/open-webui)  | Local LLM  | Front-end UI  | User-friendly AI Interface (Supports Ollama, OpenAI API, ...)  | 142,294 | 20,453  | 433  |  390 | 163  | Other  | 0 days, 2 hrs, 11 mins  |
|  6 | [langchain](https://github.com/langchain-ai/langchain)  | Agent  | Framework  | The agent engineering platform.  | 139,721 | 23,167  | 462  |  469 | 1,287  | MIT License  | 0 days, 2 hrs, 9 mins  |
|  7 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | Local LLM  | Inference Backend | LLM inference in C/C++  | 117,345 | 19,740  | 1,824  |  445 | 6,411  | MIT License  | 0 days, 1 hrs, 38 mins  |
|  8 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | Local LLM  | Front-end UI  | ✨ Light and Fast AI Assistant. Support: Web | iOS | MacOS | Android |  Linux | Windows  | 88,271  | 59,549  | 838  |  262 | 77  | MIT License  | 36 days, 0 hrs, 37 mins  |
|  9 | [vllm](https://github.com/vllm-project/vllm)  | Local LLM  | Inference Backend | A high-throughput and memory-efficient inference and serving engine for LLMs  | 83,365  | 18,243  | 5,495  |  460 | 97  | Apache License 2.0  | 0 days, 1 hrs, 7 mins  |
|  10 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | Local LLM  | Front-end UI  | 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.  | 78,876  | 15,453  | 453  |  325 | 2,788  | Other  | 0 days, 0 hrs, 46 mins  |
|  11 | [OpenHands](https://github.com/All-Hands-AI/OpenHands)  | Agent  | Coding  | 🙌 OpenHands: AI-Driven Development  | 77,790  | 9,888  | 329  |  463 | 103  | Other  | 0 days, 11 hrs, 31 mins  |
|  12 | [screenshot-to-code](https://github.com/abi/screenshot-to-code)  | Agent  | Coding  | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue)  | 72,966  | 8,981  | 122  |  26 | 0  | MIT License  | 0 days, 1 hrs, 1 mins  |
|  13 | [gpt4free](https://github.com/xtekky/gpt4free)  | Local LLM  | Inference Backend | The official gpt4free repository | various collection of powerful language models | opus 4.6 gpt 5.3 kimi 2.5 deepseek v3.2 gemini 3  | 66,361  | 13,573  | 4  |  261 | 464  | GNU General Public License v3.0  | 0 days, 9 hrs, 32 mins  |
|  14 | [open-interpreter](https://github.com/OpenInterpreter/open-interpreter)  | Agent  | Coding  | A lightweight coding agent for open models like Deepseek, Kimi, and Qwen  | 64,058  | 5,551  | 270  |  477 | 49  | Apache License 2.0  | 0 days, 0 hrs, 30 mins  |
|  15 | [privateGPT](https://github.com/imartinez/privateGPT)  | Local LLM  | Front-end UI  | Interact with your documents using the power of GPT, 100% privately, no data leaks  | 57,286  | 7,608  | 5  |  95 | 14  | Apache License 2.0  | 1 days, 11 hrs, 26 mins  |
|  16 | [crewAI](https://github.com/crewAIInc/crewAI)  | Agent  | Framework  | Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.  | 54,000  | 7,558  | 498  |  297 | 204  | MIT License  | 0 days, 2 hrs, 59 mins  |
|  17 | [Flowise](https://github.com/FlowiseAI/Flowise)  | Agent  | Framework  | Build AI Agents, Visually  | 53,737  | 24,546  | 932  |  317 | 83  | Other  | 3 days, 14 hrs, 55 mins  |
|  18 | [llama_index](https://github.com/run-llama/llama_index)  | Agent  | Framework  | LlamaIndex is the leading document agent and OCR platform  | 50,229  | 7,588  | 483  |  474 | 431  | MIT License  | 0 days, 1 hrs, 48 mins  |
|  19 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | Local LLM  | Front-end UI  | Open-source desktop app for local LLMs. Text, vision, tool-calling, OpenAI/Anthropic-compatible API. 100% private.  | 47,340  | 5,976  | 821  |  381 | 113  | GNU Affero General Public License v3.0  | 17 days, 22 hrs, 45 mins |
|  20 | [LocalAI](https://github.com/mudler/LocalAI)  | Local LLM  | Inference Backend | LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.  | 46,999  | 4,147  | 199  |  206 | 120  | MIT License  | 0 days, 2 hrs, 17 mins  |
|  21 | [aider](https://github.com/Aider-AI/aider)  | Agent  | Coding  | aider is AI pair programming in your terminal  | 46,483  | 4,627  | 1,637  |  172 | 93  | Apache License 2.0  | 28 days, 11 hrs, 57 mins |
|  22 | [exo](https://github.com/exo-explore/exo)  | Local LLM  | Inference Backend | Run frontier AI locally.  | 45,473  | 3,254  | 263  |  97 | 16  | Apache License 2.0  | 4 days, 5 hrs, 14 mins  |
|  23 | [jan](https://github.com/janhq/jan)  | Local LLM  | All-in-one App  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer.  | 43,088  | 2,947  | 456  |  151 | 102  | Other  | 0 days, 12 hrs, 44 mins  |
|  24 | [ColossalAI](https://github.com/hpcaitech/ColossalAI)  | Agent  | Chat  | Making large AI models cheaper, faster and more accessible  | 41,400  | 4,508  | 500  |  189 | 50  | Apache License 2.0  | 25 days, 8 hrs, 20 mins  |
|  25 | [phidata](https://github.com/phidatahq/phidata)  | Agent  | Framework  | Build, run, and manage agent platforms.  | 40,771  | 5,543  | 949  |  445 | 201  | Apache License 2.0  | 0 days, 5 hrs, 16 mins  |
|  26 | [chatbox](https://github.com/Bin-Huang/chatbox)  | Local LLM  | All-in-one App  | Powerful AI Client  | 40,561  | 4,111  | 1,185  |  65 | 57  | GNU General Public License v3.0  | 7 days, 17 hrs, 39 mins  |
|  27 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Local LLM  | Front-end UI  | Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active | 39,492  | 8,091  | 506  |  361 | 92  | MIT License  | 0 days, 5 hrs, 35 mins  |
|  28 | [langgraph](https://github.com/langchain-ai/langgraph)  | Agent  | Framework  | Build resilient agents.  | 35,232  | 5,907  | 587  |  275 | 549  | MIT License  | 0 days, 15 hrs, 54 mins  |
|  29 | [dspy](https://github.com/stanfordnlp/dspy)  | Agent  | Coding  | DSPy: The framework for programming—not prompting—language models  | 35,160  | 2,982  | 526  |  402 | 109  | MIT License  | 1 days, 9 hrs, 1 mins  |
|  30 | [continue](https://github.com/continuedev/continue)  | Agent  | Coding  | open-source coding agent  | 34,140  | 4,740  | 917  |  393 | 827  | Apache License 2.0  | 0 days, 0 hrs, 26 mins  |
|  31 | [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot)  | Agent  | Coding  | The first real AI developer  | 33,738  | 3,485  | 250  |  51 | 0  | Other  | 1 days, 7 hrs, 19 mins  |
|  32 | [ChatDev](https://github.com/OpenBMB/ChatDev)  | Agent  | Coding  | ChatDev 2.0: Dev All through LLM-powered Multi-Agent Collaboration  | 33,498  | 4,172  | 66  |  16 | 12  | Apache License 2.0  | 23 days, 13 hrs, 20 mins |
|  33 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | Local LLM  | Front-end UI  | LLM Frontend for Power Users.  | 29,595  | 5,594  | 500  |  347 | 102  | GNU Affero General Public License v3.0  | 30 days, 15 hrs, 49 mins |
|  34 | [composio](https://github.com/ComposioHQ/composio)  | Agent  | Framework  | Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you build AI agents that turn intent into action.  | 28,866  | 4,630  | 113  |  59 | 828  | MIT License  | 0 days, 1 hrs, 34 mins  |
|  35 | [semantic-kernel](https://github.com/microsoft/semantic-kernel)  | Agent  | Framework  | Integrate cutting-edge LLM technology quickly and easily into your apps  | 28,163  | 4,657  | 267  |  397 | 272  | MIT License  | 0 days, 2 hrs, 15 mins  |
|  36 | [gpt-researcher](https://github.com/assafelovic/gpt-researcher)  | Agent  | Research  | An autonomous agent that conducts deep research on any data using any LLM providers  | 27,794  | 3,750  | 225  |  223 | 70  | Apache License 2.0  | 22 days, 18 hrs, 17 mins |
|  37 | [agentscope](https://github.com/modelscope/agentscope)  | Agent  | Framework  | Build and run agents you can see, understand and trust.  | 27,009  | 3,037  | 289  |  64 | 40  | Apache License 2.0  | 0 days, 23 hrs, 2 mins  |
|  38 | [haystack](https://github.com/deepset-ai/haystack)  | Agent  | Framework  | Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.  | 25,614  | 2,867  | 107  |  368 | 232  | Apache License 2.0  | 0 days, 11 hrs, 6 mins  |
|  39 | [llamafile](https://github.com/Mozilla-Ocho/llamafile)  | Local LLM  | Inference Backend | Distribute and run LLMs with a single file.  | 25,048  | 1,410  | 214  |  71 | 40  | Other  | 10 days, 13 hrs, 39 mins |
|  40 | [letta](https://github.com/letta-ai/letta)  | Agent  | Framework  | Platform for stateful agents: AI with advanced memory that can learn and self-improve over time.  | 23,418  | 2,488  | 66  |  139 | 177  | Apache License 2.0  | 36 days, 8 hrs, 46 mins  |
|  41 | [memgpt](https://github.com/cpacker/memgpt)  | Agent  | Chat  | Platform for stateful agents: AI with advanced memory that can learn and self-improve over time.  | 23,418  | 2,488  | 66  |  139 | 177  | Apache License 2.0  | 36 days, 8 hrs, 45 mins  |
|  42 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Local LLM  | Inference Backend | Universal LLM Deployment Engine with ML Compilation  | 22,825  | 2,066  | 314  |  159 | 1  | Apache License 2.0  | 39 days, 3 hrs, 4 mins  |
|  43 | [swe-agent](https://github.com/princeton-nlp/swe-agent)  | Agent  | Coding  | SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. [NeurIPS 2024]  | 19,567  | 2,139  | 23  |  96 | 10  | MIT License  | 3 days, 0 hrs, 56 mins  |
|  44 | [DB-GPT](https://github.com/csunny/DB-GPT)  | Agent  | Coding  | open-source agentic AI data assistant for the next generation of AI + Data products.  | 19,022  | 2,741  | 412  |  173 | 54  | MIT License  | 0 days, 10 hrs, 26 mins  |
|  45 | [eliza](https://github.com/elizaOS/eliza)  | Agent  | Framework  | Open source agentic operating system  | 18,606  | 5,559  | 14  |  5 | 0  | MIT License  | 0 days, 0 hrs, 2 mins  |
|  46 | [web-llm](https://github.com/mlc-ai/web-llm)  | Local LLM  | Inference Backend | High-performance In-browser LLM Inference Engine  | 18,231  | 1,309  | 146  |  53 | 4  | Apache License 2.0  | 10 days, 22 hrs, 18 mins |
|  47 | [agent-zero](https://github.com/frdel/agent-zero)  | Agent  | Coding  | Agent Zero AI framework  | 18,124  | 3,656  | 356  |  45 | 61  | Other  | 0 days, 11 hrs, 36 mins  |
|  48 | [WrenAI](https://github.com/Canner/WrenAI)  | Agent  | Data Analysis  | Give AI agents the context to query business data correctly through the open context layer that gives AI agents grounded, governed memory, context, SQL across 20+ data sources, that helps you build agentic GenBI, text-to-sql, dashboards, and agentic analytics.  | 15,578  | 1,772  | 329  |  63 | 168  | Other  | 0 days, 14 hrs, 33 mins  |
|  49 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | Local LLM  | Front-end UI  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  | 15,309  | 2,228  | 129  |  54 | 27  | GNU General Public License v3.0  | 50 days, 12 hrs, 2 mins  |
|  50 | [botpress](https://github.com/botpress/botpress)  | Agent  | Framework  | The open-source hub to build & deploy GPT/LLM Agents ⚡️  | 14,748  | 2,268  | 87  |  74 | 126  | MIT License  | 0 days, 8 hrs, 14 mins  |
|  51 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | Local LLM  | Inference Backend | TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in a performant way.  | 13,923  | 2,483  | 1,423  |  403 | 81  | Other  | 0 days, 11 hrs, 6 mins  |
|  52 | [e2b](https://github.com/e2b-dev/e2b)  | Agent  | Runtime  | Open-source, secure environment with real-world tools for enterprise-grade agents.  | 12,654  | 938  | 50  |  51 | 522  | Apache License 2.0  | 0 days, 5 hrs, 15 mins  |
|  53 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Local LLM  | Inference Backend | Run any open-source LLMs, such as DeepSeek and Llama, as OpenAI compatible API endpoint in the cloud.  | 12,360  | 817  | 16  |  32 | 147  | Apache License 2.0  | 4 days, 9 hrs, 1 mins  |
|  54 | [llm](https://github.com/simonw/llm)  | Local LLM  | Front-end UI  | Access large language models from the command-line  | 12,063  | 893  | 624  |  58 | 63  | Apache License 2.0  | 0 days, 1 hrs, 32 mins  |
|  55 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | Local LLM  | Inference Backend | Run GGUF models easily with a KoboldAI UI. One File. Zero Install.  | 10,814  | 717  | 463  |  441 | 128  | GNU Affero General Public License v3.0  | 0 days, 9 hrs, 25 mins  |
|  56 | [chat-ui](https://github.com/huggingface/chat-ui)  | Local LLM  | Front-end UI  | The open source codebase powering HuggingChat  | 10,771  | 1,658  | 247  |  152 | 18  | Apache License 2.0  | 0 days, 12 hrs, 40 mins  |
|  57 | [server](https://github.com/triton-inference-server/server)  | Local LLM  | Inference Backend | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  | 10,765  | 1,796  | 898  |  137 | 91  | BSD 3-Clause "New" or "Revised" License | 0 days, 19 hrs, 47 mins  |
|  58 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Local LLM  | Inference Backend | Python bindings for llama.cpp  | 10,418  | 1,418  | 669  |  183 | 425  | MIT License  | 0 days, 0 hrs, 50 mins  |
|  59 | [inference](https://github.com/xorbitsai/inference)  | Local LLM  | Inference Backend | Swap GPT for any LLM by changing a single line of code. Xinference lets you run open-source, speech, and multimodal models on cloud, on-prem, or your laptop — all through one unified, production-ready inference API.  | 9,368  | 836  | 38  |  146 | 139  | Apache License 2.0  | 0 days, 15 hrs, 2 mins  |
|  60 | [page-assist](https://github.com/n4ze3m/page-assist)  | Local LLM  | Front-end UI  | Use your locally running AI models to assist you in your web browsing  | 8,005  | 757  | 342  |  39 | 104  | MIT License  | 2 days, 16 hrs, 32 mins  |
|  61 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | Local LLM  | Inference Backend | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  | 7,906  | 700  | 590  |  138 | 66  | Apache License 2.0  | 1 days, 15 hrs, 45 mins  |
|  62 | [multi-agent-orchestrator](https://github.com/awslabs/multi-agent-orchestrator) | Agent  | Framework  | Flexible and powerful framework for managing multiple AI agents and handling complex conversations  | 7,660  | 721  | 110  |  26 | 17  | Apache License 2.0  | 2 days, 17 hrs, 19 mins  |
|  63 | [pocketpal-ai](https://github.com/a-ghorbani/pocketpal-ai)  | Local LLM  | All-in-one App  | An app that brings language models directly to your phone.  | 7,314  | 742  | 159  |  20 | 78  | MIT License  | 0 days, 2 hrs, 5 mins  |
|  64 | [big-agi](https://github.com/enricoros/big-agi)  | Local LLM  | Front-end UI  | AI suite powered by state-of-the-art models and providing advanced AI/AGI functions. Includes AI personas, AGI functions, world-class Beam multi-model chats, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy on-prem or in the cloud.  | 7,006  | 1,571  | 278  |  55 | 22  | MIT License  | 0 days, 0 hrs, 47 mins  |
|  65 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Local LLM  | Front-end UI  | Lord of Large Language and Multi modal Systems Web User Interface  | 4,785  | 580  | 178  |  42 | 24  | Apache License 2.0  | 2 days, 6 hrs, 24 mins  |
|  66 | [agency-swarm](https://github.com/VRSEN/agency-swarm)  | Agent  | Framework  | Reliable Multi-Agent Orchestration Framework  | 4,453  | 1,058  | 8  |  22 | 64  | MIT License  | 1 days, 23 hrs, 28 mins  |
|  67 | [gptme](https://github.com/ErikBjare/gptme)  | Agent  | General  | Your agent in your terminal, equipped with local tools: writes code, uses the terminal, browses the web. Make your own persistent autonomous agent on top!  | 4,333  | 389  | 10  |  34 | 100  | MIT License  | 0 days, 15 hrs, 25 mins  |
|  68 | [langroid](https://github.com/langroid/langroid)  | Agent  | Framework  | Harness LLMs with Multi-Agent Programming  | 4,040  | 376  | 68  |  31 | 556  | MIT License  | 4 days, 10 hrs, 9 mins  |
|  69 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | Local LLM  | Inference Backend | A C#/.NET library to run LLM (🦙LLaMA/LLaVA) on your local device efficiently.  | 3,718  | 498  | 22  |  87 | 30  | MIT License  | 18 days, 4 hrs, 57 mins  |
|  70 | [AGiXT](https://github.com/Josh-XT/AGiXT)  | Agent  | Framework  | AGiXT is a dynamic AI Agent Automation Platform that seamlessly orchestrates instruction management and complex task execution across diverse AI providers. Combining adaptive memory, smart features, and a versatile plugin system, AGiXT delivers efficient and comprehensive AI solutions.  | 3,198  | 447  | 2  |  41 | 433  | MIT License  | 3 days, 0 hrs, 51 mins  |
|  71 | [GPT-Agent](https://github.com/SamurAIGPT/GPT-Agent)  | Agent  | Gaming  | A personal knowledge base that builds and maintains itself. Drop in sources — Claude (or Codex/Gemini) reads them, extracts knowledge, and maintains a persistent interlinked wiki. Works with Claude Code, Codex, OpenCode, Gemini CLI. No API key needed.  | 2,989  | 352  | 4  |  6 | 0  | MIT License  | 6 days, 19 hrs, 34 mins  |
|  72 | [ChatterUI](https://github.com/Vali-98/ChatterUI)  | Local LLM  | All-in-one App  | A frontend for running models on mobile or connecting to your preferred API providers.  | 2,510  | 222  | 29  |  8 | 91  | GNU Affero General Public License v3.0  | 4 days, 17 hrs, 47 mins  |
|  73 | [oterm](https://github.com/ggozad/oterm)  | Local LLM  | Front-end UI  | the terminal client for LLMs  | 2,398  | 134  | 8  |  24 | 80  | MIT License  | 11 days, 16 hrs, 54 mins |
|  74 | [lagent](https://github.com/InternLM/lagent)  | Agent  | Framework  | A lightweight framework for building LLM-based agents  | 2,258  | 236  | 23  |  34 | 12  | Apache License 2.0  | 1 days, 16 hrs, 57 mins  |
|  75 | [Adala](https://github.com/HumanSignal/Adala)  | Agent  | Data Analysis  | Adala: Autonomous DAta (Labeling) Agent framework  | 1,605  | 153  | 168  |  18 | 4  | Apache License 2.0  | 0 days, 2 hrs, 3 mins  |
|  76 | [uAgents](https://github.com/fetchai/uAgents)  | Agent  | Automation  | A fast and lightweight framework for creating decentralized agents with ease.  | 1,587  | 348  | 42  |  62 | 110  | Apache License 2.0  | 1 days, 12 hrs, 9 mins  |
|  77 | [Alpaca](https://github.com/Jeffser/Alpaca)  | Local LLM  | All-in-one App  | 🦙 Local and online AI hub  | 1,586  | 142  | 115  |  60 | 113  | GNU General Public License v3.0  | 11 days, 1 hrs, 19 mins  |
|  78 | [dust](https://github.com/dust-tt/dust)  | Agent  | Framework  | Custom AI agent platform to speed up your work.  | 1,389  | 287  | 207  |  101 | 28  | MIT License  | 0 days, 4 hrs, 20 mins  |
|  79 | [aideml](https://github.com/WecoAI/aideml)  | Agent  | Coding  | AIDE: AI-Driven Exploration in the Space of Code. The machine Learning engineering agent that automates AI R&D.  | 1,326  | 194  | 0  |  12 | 4  | MIT License  | 48 days, 9 hrs, 42 mins  |
|  80 | [AgentForge](https://github.com/DataBassGit/AgentForge)  | Agent  | Framework  | Extensible AGI Framework  | 819  | 161  | 4  |  7 | 7  | GNU General Public License v3.0  | 8 days, 4 hrs, 36 mins  |
|  81 | [tenere](https://github.com/pythops/tenere)  | Local LLM  | Front-end UI  | 🤖 TUI for LLMs  | 673  | 34  | 10  |  10 | 14  | GNU General Public License v3.0  | 40 days, 18 hrs, 32 mins |
|  82 | [taskgen](https://github.com/simbianai/taskgen)  | Agent  | Framework  | Task-based Agentic Framework using StrictJSON as the core  | 462  | 46  | 2  |  14 | 0  | MIT License  | 11 days, 12 hrs, 27 mins |
|  83 | [autonomous-hr-chatbot](https://github.com/stepanogil/autonomous-hr-chatbot)  | Agent  | Chat  | An autonomous HR agent that can answer user queries using tools  | 449  | 112  | 5  |  1 | 0  | MIT License  | 51 days, 19 hrs, 24 mins |
|  84 | [AgentRun](https://github.com/Jonathan-Adly/AgentRun)  | Agent  | Coding  | The easiest, and fastest way to run AI-generated Python code safely  | 371  | 41  | 8  |  2 | 9  | Apache License 2.0  | 3 days, 2 hrs, 54 mins  |
|  85 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Local LLM  | All-in-one App  | Local ML voice chat using high-end models.  | 188  | 13  | 0  |  1 | 0  | MIT License  | 15 days, 2 hrs, 32 mins  |
|  86 | [lite.koboldai.net](https://github.com/LostRuins/lite.koboldai.net)  | Local LLM  | Front-end UI  | A zero dependency web UI for any LLM backend, including KoboldCpp, OpenAI and AI Horde  | 183  | 89  | 31  |  39 | 0  | GNU Affero General Public License v3.0  | 4 days, 9 hrs, 50 mins  |
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
