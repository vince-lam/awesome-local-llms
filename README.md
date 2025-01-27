# 👋 Awesome Local LLMs

There are an overwhelming number of open-source tools for local LLM inference - for both proprietary and open weights LLMs. These tools generally lie within three categories:

1. LLM inference backend engine
2. LLM front end UI
3. All-in-one desktop application

However these tools can overlap in scope with new features are constantly being added so I have chosen not to manually categorize or label features of each project.

GitHub repository metrics, like number of stars, contributors, issues, releases, and time since last commit, have been collected as a proxy for popularity and active maintenance.

**Contributions are welcome!** Feel ffree to suggest open-source repos that I have missed either in the Issues of this repo or run the script in the [script](https://github.com/vince-lam/awesome-local-llms/tree/script) branch and update the README and make a pull request.

For full table with all metrics go to this [Google Sheet](https://docs.google.com/spreadsheets/d/1Xv38p90V3GiJXjq0a3qc24056Vicn1I5MG6QiFE6nVE/edit?usp=sharing).

For my thoughts on local LLM tooling: <https://vinlam.com/posts/local-llm-options/>

Note the condensed table below has two filters applied:

1. Repositories need more than 100 stars
2. Repositories require a commit within the last 60 days

## Open-Source Local LLM Projects

*Last Updated: 27/01/2025*

|  # | Repo  | About  | Stars  | Forks  | Issues  |  Contributors | Releases  | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [transformers](https://github.com/huggingface/transformers)  | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX.  | 138,058 | 27,674  | 1,538  |  436 | 175  | Apache License 2.0  | 0 days, 9 hrs, 5 mins  |
|  2 | [ollama](https://github.com/ollama/ollama)  | Get up and running with Llama 3.3, Phi 4, Gemma 2, and other large language models.  | 110,705 | 8,829  | 1,364  |  389 | 110  | MIT License  | 1 days, 5 hrs, 29 mins  |
|  3 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | ✨ Local and Fast AI Assistant. Support: Web, iOS, MacOS, Android, Linux, Windows  | 78,974  | 60,174  | 577  |  240 | 75  | MIT License  | 4 days, 18 hrs, 52 mins  |
|  4 | [gpt4all](https://github.com/nomic-ai/gpt4all)  | GPT4All: Run Local LLMs on Any Device. Open-source and available for commercial use.  | 71,930  | 7,813  | 704  |  114 | 35  | MIT License  | 2 days, 13 hrs, 15 mins  |
|  5 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | LLM inference in C/C++  | 71,458  | 10,337  | 624  |  462 | 2,841  | MIT License  | 0 days, 10 hrs, 44 mins  |
|  6 | [gpt_academic](https://github.com/binary-husky/gpt_academic)  | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。  | 67,116  | 8,243  | 419  |  98 | 32  | GNU General Public License v3.0  | 5 days, 14 hrs, 43 mins  |
|  7 | [gpt4free](https://github.com/xtekky/gpt4free)  | The official gpt4free repository, various collection of powerful language models  | 63,216  | 13,517  | 27  |  227 | 226  | GNU General Public License v3.0  | 0 days, 15 hrs, 41 mins  |
|  8 | [open-webui](https://github.com/open-webui/open-webui)  | User-friendly AI Interface (Supports Ollama, OpenAI API, ...)  | 60,041  | 7,315  | 170  |  311 | 83  | BSD 3-Clause "New" or "Revised" License | 2 days, 15 hrs, 49 mins  |
|  9 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | 🤯 Lobe Chat - an open-source, modern-design AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Ollama / Qwen /  DeepSeek), Knowledge Base (file upload / knowledge management / RAG ), Multi-Modals (Vision/TTS/Plugins/Artifacts). One-click FREE deployment of your private ChatGPT/ Claude application.  | 52,225  | 11,307  | 549  |  181 | 1,227  | Other  | 0 days, 8 hrs, 3 mins  |
|  10 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | A Gradio web UI for Large Language Models with support for multiple inference backends.  | 41,814  | 5,441  | 239  |  336 | 56  | GNU Affero General Public License v3.0  | 1 days, 5 hrs, 5 mins  |
|  11 | [vllm](https://github.com/vllm-project/vllm)  | A high-throughput and memory-efficient inference and serving engine for LLMs  | 34,871  | 5,322  | 1,642  |  458 | 46  | Apache License 2.0  | 0 days, 8 hrs, 28 mins  |
|  12 | [anything-llm](https://github.com/Mintplex-Labs/anything-llm)  | The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, and more.  | 30,978  | 3,109  | 217  |  91 | 9  | MIT License  | 2 days, 7 hrs, 38 mins  |
|  13 | [LocalAI](https://github.com/mudler/LocalAI)  | :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement for OpenAI,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. Features: Generate Text, Audio, Video, Images, Voice Cloning, Distributed, P2P inference | 29,764  | 2,240  | 410  |  120 | 68  | MIT License  | 0 days, 10 hrs, 46 mins  |
|  14 | [jan](https://github.com/janhq/jan)  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer  | 26,785  | 1,545  | 135  |  60 | 61  | GNU Affero General Public License v3.0  | 0 days, 16 hrs, 28 mins  |
|  15 | [chatbox](https://github.com/Bin-Huang/chatbox)  | User-friendly Desktop Client App for AI Models/LLMs (GPT, Claude, Gemini, Ollama...)  | 25,590  | 2,518  | 398  |  34 | 47  | GNU General Public License v3.0  | 3 days, 6 hrs, 25 mins  |
|  16 | [llamafile](https://github.com/Mozilla-Ocho/llamafile)  | Distribute and run LLMs with a single file.  | 21,391  | 1,106  | 171  |  47 | 33  | Other  | 21 days, 9 hrs, 42 mins  |
|  17 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Enhanced ChatGPT Clone: Features Agents, Anthropic, AWS, OpenAI, Assistants API, Azure, Groq, o1, GPT-4o, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active project.  | 20,876  | 3,523  | 219  |  176 | 49  | MIT License  | 0 days, 8 hrs, 30 mins  |
|  18 | [exo](https://github.com/exo-explore/exo)  | Run your own AI cluster at home with everyday devices 📱💻 🖥️⌚  | 20,026  | 1,135  | 280  |  48 | 11  | GNU General Public License v3.0  | 0 days, 12 hrs, 1 mins  |
|  19 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Universal LLM Deployment Engine with ML Compilation  | 19,731  | 1,627  | 229  |  134 | 1  | Apache License 2.0  | 2 days, 11 hrs, 43 mins  |
|  20 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  | 15,351  | 2,292  | 126  |  51 | 26  | GNU General Public License v3.0  | 45 days, 17 hrs, 32 mins |
|  21 | [web-llm](https://github.com/mlc-ai/web-llm)  | High-performance In-browser LLM Inference Engine  | 14,397  | 930  | 84  |  45 | 1  | Apache License 2.0  | 6 days, 0 hrs, 15 mins  |
|  22 | [h2ogpt](https://github.com/h2oai/h2ogpt)  | Private chat with local GPT with document, images, video, etc. 100% private, Apache 2.0. Supports oLLaMa, Mixtral, llama.cpp, and more. Demo: https://gpt.h2o.ai/ https://gpt-docs.h2o.ai/  | 11,606  | 1,273  | 304  |  69 | 2  | Apache License 2.0  | 10 days, 23 hrs, 53 mins |
|  23 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Run any open-source LLMs, such as Llama, Mistral, as OpenAI compatible API endpoint in the cloud.  | 10,436  | 661  | 17  |  31 | 134  | Apache License 2.0  | 6 days, 9 hrs, 56 mins  |
|  24 | [text-generation-inference](https://github.com/huggingface/text-generation-inference) | Large Language Model Text Generation Inference  | 9,643  | 1,129  | 201  |  131 | 53  | Apache License 2.0  | 0 days, 18 hrs, 12 mins  |
|  25 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | LLM Frontend for Power Users.  | 9,625  | 2,630  | 221  |  191 | 88  | GNU Affero General Public License v3.0  | 0 days, 10 hrs, 20 mins  |
|  26 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines.  | 9,230  | 1,081  | 441  |  20 | 12  | Apache License 2.0  | 2 days, 12 hrs, 16 mins  |
|  27 | [server](https://github.com/triton-inference-server/server)  | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  | 8,635  | 1,513  | 681  |  123 | 74  | BSD 3-Clause "New" or "Revised" License | 0 days, 8 hrs, 13 mins  |
|  28 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Python bindings for llama.cpp  | 8,471  | 1,022  | 563  |  163 | 284  | MIT License  | 6 days, 11 hrs, 38 mins  |
|  29 | [chat-ui](https://github.com/huggingface/chat-ui)  | Open source codebase powering the HuggingChat app  | 7,951  | 1,174  | 294  |  120 | 15  | Apache License 2.0  | 2 days, 21 hrs, 29 mins  |
|  30 | [openplayground](https://github.com/nat/openplayground)  | An LLM playground you can run on your laptop  | 6,314  | 487  | 90  |  15 | 0  | MIT License  | 10 days, 4 hrs, 4 mins  |
|  31 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | Run GGUF models easily with a KoboldAI UI. One File. Zero Install.  | 6,173  | 395  | 289  |  461 | 94  | GNU Affero General Public License v3.0  | 1 days, 23 hrs, 43 mins  |
|  32 | [inference](https://github.com/xorbitsai/inference)  | Replace OpenAI GPT with another LLM in your app by changing a single line of code. Xinference gives you the freedom to use any LLM you need. With Xinference, you're empowered to run inference with any open-source language models, speech recognition models, and multimodal models, whether in the cloud, on-premises, or even on your laptop.  | 6,054  | 498  | 185  |  89 | 95  | Apache License 2.0  | 1 days, 3 hrs, 13 mins  |
|  33 | [big-agi](https://github.com/enricoros/big-agi)  | AI suite powered by state-of-the-art models and providing advanced AI/AGI functions. It features AI personas, AGI functions, multi-model chats, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy on-prem or in the cloud.  | 5,891  | 1,362  | 218  |  46 | 16  | MIT License  | 1 days, 14 hrs, 18 mins  |
|  34 | [llm](https://github.com/simonw/llm)  | Access large language models from the command-line  | 5,710  | 324  | 280  |  34 | 39  | Apache License 2.0  | 2 days, 13 hrs, 38 mins  |
|  35 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  | 5,305  | 467  | 389  |  89 | 43  | Apache License 2.0  | 0 days, 23 hrs, 57 mins  |
|  36 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Lord of Large Language and Multi modal Systems Web User Interface  | 4,468  | 558  | 163  |  39 | 24  | Apache License 2.0  | 0 days, 9 hrs, 59 mins  |
|  37 | [exllamav2](https://github.com/turboderp/exllamav2)  | A fast inference library for running LLMs locally on modern consumer-class GPUs  | 3,877  | 293  | 108  |  51 | 38  | MIT License  | 17 days, 21 hrs, 55 mins |
|  38 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | A C#/.NET library to run LLM (🦙LLaMA/LLaVA) on your local device efficiently.  | 2,844  | 371  | 144  |  59 | 24  | MIT License  | 5 days, 15 hrs, 32 mins  |
|  39 | [nitro](https://github.com/janhq/nitro)  | Local AI API Platform  | 2,354  | 144  | 115  |  36 | 168  | Apache License 2.0  | 3 days, 20 hrs, 25 mins  |
|  40 | [cortex.cpp](https://github.com/janhq/cortex.cpp)  | Local AI API Platform  | 2,354  | 144  | 115  |  36 | 168  | Apache License 2.0  | 3 days, 20 hrs, 26 mins  |
|  41 | [page-assist](https://github.com/n4ze3m/page-assist)  | Use your locally running AI models to assist you in your web browsing  | 1,859  | 182  | 112  |  16 | 32  | MIT License  | 0 days, 18 hrs, 20 mins  |
|  42 | [pocketpal-ai](https://github.com/a-ghorbani/pocketpal-ai)  | An app that brings language models directly to your phone.  | 1,724  | 136  | 39  |  7 | 9  | MIT License  | 3 days, 12 hrs, 25 mins  |
|  43 | [LLMFarm](https://github.com/guinmoon/LLMFarm)  | llama and other  large language models on iOS and MacOS offline using GGML library.  | 1,521  | 102  | 32  |  1 | 33  | MIT License  | 40 days, 23 hrs, 0 mins  |
|  44 | [oterm](https://github.com/ggozad/oterm)  | a text-based terminal client for Ollama  | 1,220  | 74  | 7  |  15 | 44  | MIT License  | 5 days, 14 hrs, 6 mins  |
|  45 | [amica](https://github.com/semperai/amica)  | Amica is an open source interface for interactive communication with 3D characters with voice synthesis and speech recognition.  | 852  | 135  | 13  |  19 | 4  | MIT License  | 5 days, 12 hrs, 49 mins  |
|  46 | [ChatterUI](https://github.com/Vali-98/ChatterUI)  | Simple frontend for LLMs built in react-native.  | 813  | 47  | 17  |  4 | 54  | GNU Affero General Public License v3.0  | 3 days, 18 hrs, 25 mins  |
|  47 | [web-llm-chat](https://github.com/mlc-ai/web-llm-chat)  | Chat with AI large language models running natively in your browser. Enjoy private, server-free, seamless AI conversations.  | 582  | 81  | 13  |  181 | 0  | Apache License 2.0  | 5 days, 13 hrs, 22 mins  |
|  48 | [exui](https://github.com/turboderp/exui)  | Web UI for ExLlamaV2  | 466  | 44  | 32  |  9 | 0  | MIT License  | 2 days, 13 hrs, 3 mins  |
|  49 | [tenere](https://github.com/pythops/tenere)  | 🤖 TUI interface for LLMs written in Rust  | 443  | 15  | 7  |  10 | 13  | GNU General Public License v3.0  | 19 days, 0 hrs, 19 mins  |
|  50 | [mikupad](https://github.com/lmg-anon/mikupad)  | LLM Frontend in a single html file  | 309  | 32  | 27  |  11 | 64  | Creative Commons Zero v1.0 Universal  | 11 days, 17 hrs, 29 mins |
|  51 | [chat-ui](https://github.com/run-llama/chat-ui)  | Chat UI components for LLM apps  | 167  | 11  | 0  |  5 | 0  | MIT License  | 5 days, 23 hrs, 59 mins  |
|  52 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Local ML voice chat using high-end models.  | 156  | 11  | 1  |  1 | 0  | MIT License  | 19 days, 10 hrs, 16 mins |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
