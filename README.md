# 👋 Awesome Local LLMs

There are an overwhelming number of open-source tools for local LLM inference - for both proprietary and open weights LLMs. These tools generally lie within three categories:

1. LLM inference backend engine
2. LLM front end UI
3. All-in-one desktop application

However these tools can overlap in scope with new features are constantly being added so I have chosen not to manually categorize or label features of each project.

GitHub repository metrics, like number of stars, contributors, issues, releases, and time since last commit, have been collected as a proxy for popularity and active maintenance.

**Contributions are welcome!** Feel free to suggest open-source repos that I have missed either in the Issues of this repo or run the script in the [script](https://github.com/vince-lam/awesome-local-llms/tree/script) branch and update the README and make a pull request.

For full table with all metrics go to this [Google Sheet](https://docs.google.com/spreadsheets/d/1Xv38p90V3GiJXjq0a3qc24056Vicn1I5MG6QiFE6nVE/edit?usp=sharing) or [Airtable](https://airtable.com/apparaKqezkq2LECD/shrE26kWFaVU1cvgb).

For my thoughts on local LLM tooling: <https://vinlam.com/posts/local-llm-options/>

Note the condensed table below has two filters applied:

1. Repositories need more than 100 stars
2. Repositories require a commit within the last 60 days

- [guardian-agent-prompts](https://github.com/milkomida77/guardian-agent-prompts) - 49 production-tested AI agent system prompts for multi-agent orchestration. Model-agnostic, works with local and cloud LLMs. MIT licensed.
## Open-Source Local LLM Projects

*Last Updated: 08/09/2025*

|  # | Repo  | About  | Stars  | Forks  | Issues  |  Contributors | Releases  | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [ollama](https://github.com/ollama/ollama)  | Get up and running with OpenAI gpt-oss, DeepSeek-R1, Gemma 3 and other models.  | 151,867 | 13,052  | 2,126  |  461 | 147  | MIT License  | 2 days, 15 hrs, 0 mins  |
|  2 | [transformers](https://github.com/huggingface/transformers)  | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.  | 149,300 | 30,300  | 1,995  |  436 | 227  | Apache License 2.0  | 0 days, 8 hrs, 20 mins  |
|  3 | [open-webui](https://github.com/open-webui/open-webui)  | User-friendly AI Interface (Supports Ollama, OpenAI API, ...)  | 109,207 | 14,926  | 276  |  393 | 123  | Other  | 0 days, 18 hrs, 8 mins  |
|  4 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | LLM inference in C/C++  | 86,200  | 12,958  | 880  |  451 | 4,182  | MIT License  | 0 days, 8 hrs, 23 mins  |
|  5 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | ✨ Light and Fast AI Assistant. Support: Web, iOS, MacOS, Android, Linux, Windows  | 85,783  | 61,027  | 764  |  261 | 77  | MIT License  | 9 days, 1 hrs, 46 mins  |
|  6 | [gpt_academic](https://github.com/binary-husky/gpt_academic)  | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。  | 69,207  | 8,374  | 286  |  102 | 32  | GNU General Public License v3.0  | 15 days, 4 hrs, 2 mins  |
|  7 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | 🤯 Lobe Chat - an open-source, modern design AI chat framework. Supports multiple AI providers (OpenAI / Claude 4 / Gemini / DeepSeek / Ollama / Qwen), Knowledge Base (file upload / RAG ), one click install MCP Marketplace and Artifacts / Thinking. One-click FREE deployment of your private AI Agent application.  | 65,309  | 13,530  | 997  |  262 | 2,019  | Other  | 0 days, 10 hrs, 8 mins  |
|  8 | [gpt4free](https://github.com/xtekky/gpt4free)  | The official gpt4free repository, various collection of powerful language models: o4, o3 and deepseek r1, gpt-4.1, gemini 2.5  | 65,060  | 13,683  | 11  |  247 | 347  | GNU General Public License v3.0  | 0 days, 8 hrs, 54 mins  |
|  9 | [vllm](https://github.com/vllm-project/vllm)  | A high-throughput and memory-efficient inference and serving engine for LLMs  | 57,434  | 9,971  | 2,949  |  458 | 73  | Apache License 2.0  | 0 days, 9 hrs, 27 mins  |
|  10 | [anything-llm](https://github.com/Mintplex-Labs/anything-llm)  | The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.  | 48,752  | 5,031  | 313  |  149 | 20  | MIT License  | 2 days, 15 hrs, 51 mins  |
|  11 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | The definitive Web UI for local AI, with powerful features and easy setup.  | 44,902  | 5,772  | 2,588  |  359 | 81  | GNU Affero General Public License v3.0  | 4 days, 16 hrs, 54 mins  |
|  12 | [jan](https://github.com/janhq/jan)  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer  | 37,712  | 2,229  | 171  |  92 | 88  | Other  | 0 days, 8 hrs, 50 mins  |
|  13 | [chatbox](https://github.com/Bin-Huang/chatbox)  | User-friendly Desktop Client App for AI Models/LLMs (GPT, Claude, Gemini, Ollama...)  | 36,501  | 3,514  | 892  |  55 | 47  | GNU General Public License v3.0  | 19 days, 8 hrs, 22 mins  |
|  14 | [LocalAI](https://github.com/mudler/LocalAI)  | :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement for OpenAI,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. Features: Generate Text, Audio, Video, Images, Voice Cloning, Distributed, P2P inference | 35,118  | 2,751  | 371  |  142 | 84  | MIT License  | 0 days, 8 hrs, 51 mins  |
|  15 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Enhanced ChatGPT Clone: Features Agents, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active project. | 29,816  | 5,617  | 270  |  246 | 59  | MIT License  | 0 days, 14 hrs, 36 mins  |
|  16 | [localGPT](https://github.com/PromtEngineer/localGPT)  | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private.  | 21,841  | 2,428  | 14  |  45 | 0  | MIT License  | 44 days, 13 hrs, 8 mins  |
|  17 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Universal LLM Deployment Engine with ML Compilation  | 21,285  | 1,808  | 321  |  141 | 1  | Apache License 2.0  | 0 days, 12 hrs, 52 mins  |
|  18 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | LLM Frontend for Power Users.  | 18,245  | 3,930  | 344  |  267 | 95  | GNU Affero General Public License v3.0  | 0 days, 10 hrs, 44 mins  |
|  19 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  | 15,436  | 2,273  | 124  |  51 | 27  | GNU General Public License v3.0  | 24 days, 14 hrs, 26 mins |
|  20 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Run any open-source LLMs, such as DeepSeek and Llama, as OpenAI compatible API endpoint in the cloud.  | 11,754  | 764  | 7  |  31 | 147  | Apache License 2.0  | 6 days, 23 hrs, 59 mins  |
|  21 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and support state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in performant way.  | 11,535  | 1,722  | 1,139  |  248 | 39  | Apache License 2.0  | 0 days, 8 hrs, 8 mins  |
|  22 | [text-generation-inference](https://github.com/huggingface/text-generation-inference) | Large Language Model Text Generation Inference  | 10,486  | 1,227  | 312  |  142 | 65  | Apache License 2.0  | 0 days, 22 hrs, 51 mins  |
|  23 | [server](https://github.com/triton-inference-server/server)  | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  | 9,743  | 1,639  | 827  |  132 | 82  | BSD 3-Clause "New" or "Revised" License | 1 days, 3 hrs, 49 mins  |
|  24 | [llm](https://github.com/simonw/llm)  | Access large language models from the command-line  | 9,617  | 600  | 494  |  52 | 55  | Apache License 2.0  | 27 days, 11 hrs, 33 mins |
|  25 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Python bindings for llama.cpp  | 9,548  | 1,220  | 653  |  166 | 307  | MIT License  | 24 days, 10 hrs, 28 mins |
|  26 | [chat-ui](https://github.com/huggingface/chat-ui)  | Open source codebase powering the HuggingChat app  | 9,138  | 1,418  | 339  |  140 | 16  | Apache License 2.0  | 37 days, 21 hrs, 39 mins |
|  27 | [inference](https://github.com/xorbitsai/inference)  | Replace OpenAI GPT with another LLM in your app by changing a single line of code. Xinference gives you the freedom to use any LLM you need. With Xinference, you're empowered to run inference with any open-source language models, speech recognition models, and multimodal models, whether in the cloud, on-premises, or even on your laptop.  | 8,496  | 738  | 166  |  116 | 118  | Apache License 2.0  | 0 days, 13 hrs, 54 mins  |
|  28 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | Run GGUF models easily with a KoboldAI UI. One File. Zero Install.  | 8,168  | 528  | 347  |  447 | 110  | GNU Affero General Public License v3.0  | 0 days, 8 hrs, 47 mins  |
|  29 | [page-assist](https://github.com/n4ze3m/page-assist)  | Use your locally running AI models to assist you in your web browsing  | 7,085  | 632  | 294  |  30 | 64  | MIT License  | 1 days, 1 hrs, 11 mins  |
|  30 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  | 6,981  | 599  | 515  |  124 | 54  | Apache License 2.0  | 0 days, 11 hrs, 4 mins  |
|  31 | [big-agi](https://github.com/enricoros/big-agi)  | AI suite powered by state-of-the-art models and providing advanced AI/AGI functions. It features AI personas, AGI functions, multi-model chats, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy on-prem or in the cloud.  | 6,609  | 1,543  | 266  |  46 | 16  | MIT License  | 3 days, 18 hrs, 39 mins  |
|  32 | [openplayground](https://github.com/nat/openplayground)  | An LLM playground you can run on your laptop  | 6,359  | 491  | 96  |  15 | 0  | MIT License  | 31 days, 9 hrs, 42 mins  |
|  33 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Lord of Large Language and Multi modal Systems Web User Interface  | 4,748  | 581  | 172  |  40 | 24  | Apache License 2.0  | 19 days, 2 hrs, 5 mins  |
|  34 | [pocketpal-ai](https://github.com/a-ghorbani/pocketpal-ai)  | An app that brings language models directly to your phone.  | 4,735  | 441  | 91  |  14 | 48  | MIT License  | 19 days, 1 hrs, 58 mins  |
|  35 | [exllamav2](https://github.com/turboderp/exllamav2)  | A fast inference library for running LLMs locally on modern consumer-class GPUs  | 4,306  | 320  | 153  |  52 | 43  | MIT License  | 22 days, 18 hrs, 48 mins |
|  36 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | A C#/.NET library to run LLM (🦙LLaMA/LLaVA) on your local device efficiently.  | 3,349  | 465  | 30  |  76 | 28  | MIT License  | 7 days, 4 hrs, 30 mins  |
|  37 | [oterm](https://github.com/ggozad/oterm)  | the terminal client for Ollama  | 2,162  | 126  | 9  |  21 | 69  | MIT License  | 1 days, 1 hrs, 10 mins  |
|  38 | [maid](https://github.com/Mobile-Artificial-Intelligence/maid)  | Maid is a cross-platform Flutter app for interfacing with GGUF / llama.cpp models locally, and with Ollama and OpenAI models remotely.  | 2,148  | 218  | 15  |  28 | 38  | MIT License  | 42 days, 3 hrs, 20 mins  |
|  39 | [LLMFarm](https://github.com/guinmoon/LLMFarm)  | llama and other  large language models on iOS and MacOS offline using GGML library.  | 1,861  | 153  | 42  |  1 | 34  | MIT License  | 30 days, 21 hrs, 36 mins |
|  40 | [ChatterUI](https://github.com/Vali-98/ChatterUI)  | Simple frontend for LLMs built in react-native.  | 1,790  | 131  | 23  |  8 | 78  | GNU Affero General Public License v3.0  | 17 days, 3 hrs, 47 mins  |
|  41 | [chatbot-ollama](https://github.com/ivanfioravanti/chatbot-ollama)  | Chatbot Ollama is an open source chat UI for Ollama.  | 1,778  | 313  | 20  |  8 | 3  | Other  | 2 days, 21 hrs, 52 mins  |
|  42 | [Alpaca](https://github.com/Jeffser/Alpaca)  | 🦙 Local and online AI hub  | 1,184  | 104  | 83  |  49 | 87  | GNU General Public License v3.0  | 0 days, 16 hrs, 5 mins  |
|  43 | [amica](https://github.com/semperai/amica)  | Amica is an open source interface for interactive communication with 3D characters with voice synthesis and speech recognition.  | 1,067  | 188  | 15  |  21 | 4  | MIT License  | 46 days, 19 hrs, 48 mins |
|  44 | [web-llm-chat](https://github.com/mlc-ai/web-llm-chat)  | Chat with AI large language models running natively in your browser. Enjoy private, server-free, seamless AI conversations.  | 836  | 149  | 18  |  180 | 0  | Apache License 2.0  | 5 days, 0 hrs, 0 mins  |
|  45 | [tenere](https://github.com/pythops/tenere)  | 🤖 TUI interface for LLMs written in Rust  | 579  | 25  | 12  |  10 | 14  | GNU General Public License v3.0  | 6 days, 21 hrs, 59 mins  |
|  46 | [chat-ui](https://github.com/run-llama/chat-ui)  | Chat UI components for LLM apps  | 497  | 54  | 9  |  15 | 51  | MIT License  | 11 days, 14 hrs, 32 mins |
|  47 | [ava](https://github.com/cztomsik/ava)  | All-in-one desktop app for running LLMs locally.  | 457  | 17  | 4  |  3 | 0  | Other  | 6 days, 2 hrs, 3 mins  |
|  48 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Local ML voice chat using high-end models.  | 175  | 13  | 0  |  1 | 0  | MIT License  | 16 days, 17 hrs, 27 mins |
|  49 | [lite.koboldai.net](https://github.com/LostRuins/lite.koboldai.net)  | A zero dependency web UI for any LLM backend, including KoboldCpp, OpenAI and AI Horde  | 135  | 68  | 15  |  30 | 0  | GNU Affero General Public License v3.0  | 0 days, 8 hrs, 17 mins  |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
