# 👋 Awesome Local LLMs

There are an overwhelming number of open-source tools for local LLM inference - for both proprietary and open weights LLMs. These tools generally lie within three categories:

1. LLM inference backend engine
2. LLM front end UI
3. All-in-one desktop application

However these tools can overlap in scope with new features are constantly being added so I have chosen not to manually categorize or label features of each project.

GitHub repository metrics, like number of stars, contributors, issues, releases, and time since last commit, have been collected as a proxy for popularity and active maintenance.

**Contributions are welcome!** Feel free to suggest open-source repos that I have missed either in the Issues of this repo or run the script in the [script](https://github.com/vince-lam/awesome-local-llms/tree/script) branch and update the README and make a pull request.

For full table with all metrics go to this [Google Sheet](https://docs.google.com/spreadsheets/d/1Xv38p90V3GiJXjq0a3qc24056Vicn1I5MG6QiFE6nVE/edit?usp=sharing).

For my thoughts on local LLM tooling: <https://vinlam.com/posts/local-llm-options/>

Note the condensed table below has two filters applied:

1. Repositories need more than 100 stars
2. Repositories require a commit within the last 60 days

## Open-Source Local LLM Projects

*Last Updated: 01/11/2024*

|  # | Repo  | About  | Stars  | Forks  | Issues  |  Contributors | Releases  | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [transformers](https://github.com/huggingface/transformers)  | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX.  | 134,277 | 26,847  | 1,426  |  431 | 169  | Apache License 2.0  | 0 days, 15 hrs, 45 mins  |
|  2 | [ollama](https://github.com/ollama/ollama)  | Get up and running with Llama 3.2, Mistral, Gemma 2, and other large language models.  | 95,775  | 7,600  | 1,437  |  308 | 95  | MIT License  | 0 days, 14 hrs, 28 mins  |
|  3 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS). 一键拥有你自己的跨平台 ChatGPT/Gemini 应用。  | 76,177  | 59,025  | 455  |  228 | 73  | MIT License  | 0 days, 8 hrs, 40 mins  |
|  4 | [gpt4all](https://github.com/nomic-ai/gpt4all)  | GPT4All: Run Local LLMs on Any Device. Open-source and available for commercial use.  | 70,365  | 7,683  | 615  |  114 | 28  | MIT License  | 0 days, 15 hrs, 20 mins  |
|  5 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | LLM inference in C/C++  | 67,172  | 9,639  | 554  |  465 | 2,494  | MIT License  | 0 days, 10 hrs, 41 mins  |
|  6 | [gpt_academic](https://github.com/binary-husky/gpt_academic)  | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。  | 65,299  | 8,038  | 372  |  90 | 31  | GNU General Public License v3.0  | 2 days, 1 hrs, 15 mins  |
|  7 | [gpt4free](https://github.com/xtekky/gpt4free)  | The official gpt4free repository, various collection of powerful language models  | 60,953  | 13,292  | 22  |  218 | 153  | GNU General Public License v3.0  | 2 days, 5 hrs, 57 mins  |
|  8 | [privateGPT](https://github.com/imartinez/privateGPT)  | Interact with your documents using the power of GPT, 100% privately, no data leaks  | 54,049  | 7,264  | 239  |  90 | 10  | Apache License 2.0  | 15 days, 4 hrs, 9 mins  |
|  9 | [open-webui](https://github.com/open-webui/open-webui)  | User-friendly AI Interface (Supports Ollama, OpenAI API, ...)  | 44,894  | 5,466  | 139  |  238 | 66  | MIT License  | 0 days, 11 hrs, 37 mins  |
|  10 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | 🤯 Lobe Chat - an open-source, modern-design AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Ollama / Azure /  DeepSeek), Knowledge Base (file upload / knowledge management / RAG ), Multi-Modals (Vision/TTS) and plugin system. One-click FREE deployment of your private ChatGPT/ Claude application.  | 44,029  | 9,845  | 396  |  159 | 1,020  | Other  | 0 days, 14 hrs, 22 mins  |
|  11 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | A Gradio web UI for Large Language Models.  | 40,391  | 5,295  | 287  |  329 | 52  | GNU Affero General Public License v3.0  | 3 days, 17 hrs, 59 mins  |
|  12 | [vllm](https://github.com/vllm-project/vllm)  | A high-throughput and memory-efficient inference and serving engine for LLMs  | 29,451  | 4,415  | 2,218  |  454 | 41  | Apache License 2.0  | 0 days, 8 hrs, 58 mins  |
|  13 | [anything-llm](https://github.com/Mintplex-Labs/anything-llm)  | The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, and more.  | 25,386  | 2,566  | 185  |  78 | 8  | MIT License  | 0 days, 21 hrs, 57 mins  |
|  14 | [LocalAI](https://github.com/mudler/LocalAI)  | :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement for OpenAI,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. Features: Generate Text, Audio, Video, Images, Voice Cloning, Distributed inference  | 24,305  | 1,863  | 385  |  109 | 63  | MIT License  | 0 days, 17 hrs, 14 mins  |
|  15 | [jan](https://github.com/janhq/jan)  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer. Multiple engine support (llama.cpp, TensorRT-LLM)  | 23,063  | 1,336  | 174  |  55 | 33  | GNU Affero General Public License v3.0  | 0 days, 9 hrs, 14 mins  |
|  16 | [chatbox](https://github.com/Bin-Huang/chatbox)  | User-friendly Desktop Client App for AI Models/LLMs (GPT, Claude, Gemini, Ollama...)  | 21,472  | 2,169  | 375  |  29 | 44  | GNU General Public License v3.0  | 9 days, 2 hrs, 7 mins  |
|  17 | [llamafile](https://github.com/Mozilla-Ocho/llamafile)  | Distribute and run LLMs with a single file.  | 20,070  | 1,006  | 134  |  46 | 30  | Other  | 1 days, 2 hrs, 1 mins  |
|  18 | [localGPT](https://github.com/PromtEngineer/localGPT)  | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private.  | 20,039  | 2,238  | 476  |  44 | 0  | Apache License 2.0  | 4 days, 11 hrs, 25 mins  |
|  19 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Universal LLM Deployment Engine with ML Compilation  | 19,086  | 1,563  | 200  |  127 | 1  | Apache License 2.0  | 1 days, 12 hrs, 14 mins  |
|  20 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Enhanced ChatGPT Clone: Features Anthropic, AWS, OpenAI, Assistants API, Azure, Groq, o1, GPT-4o, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, langchain, DALL-E-3, ChatGPT Plugins, OpenAI Functions, Secure Multi-User System, Presets, completely open-source for self-hosting. Actively in public development. | 18,507  | 3,112  | 176  |  163 | 47  | MIT License  | 1 days, 0 hrs, 59 mins  |
|  21 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  | 15,233  | 2,294  | 122  |  51 | 25  | GNU General Public License v3.0  | 10 days, 7 hrs, 54 mins  |
|  22 | [web-llm](https://github.com/mlc-ai/web-llm)  | High-performance In-browser LLM Inference Engine  | 13,504  | 870  | 71  |  42 | 1  | Apache License 2.0  | 10 days, 20 hrs, 22 mins |
|  23 | [h2ogpt](https://github.com/h2oai/h2ogpt)  | Private chat with local GPT with document, images, video, etc. 100% private, Apache 2.0. Supports oLLaMa, Mixtral, llama.cpp, and more. Demo: https://gpt.h2o.ai/ https://gpt-docs.h2o.ai/  | 11,388  | 1,248  | 281  |  69 | 2  | Apache License 2.0  | 0 days, 10 hrs, 36 mins  |
|  24 | [chathub](https://github.com/chathub-dev/chathub)  | All-in-one chatbot client  | 10,016  | 1,022  | 281  |  12 | 0  | GNU General Public License v3.0  | 14 days, 8 hrs, 53 mins  |
|  25 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Run any open-source LLMs, such as Llama 3.1, Gemma, as OpenAI compatible API endpoint in the cloud.  | 9,961  | 635  | 21  |  31 | 131  | Apache License 2.0  | 3 days, 8 hrs, 51 mins  |
|  26 | [FlexGen](https://github.com/FMInference/FlexGen)  | Running large language models on a single GPU for throughput-oriented scenarios.  | 9,180  | 548  | 57  |  19 | 0  | Apache License 2.0  | 4 days, 11 hrs, 51 mins  |
|  27 | [text-generation-inference](https://github.com/huggingface/text-generation-inference) | Large Language Model Text Generation Inference  | 8,979  | 1,059  | 124  |  117 | 49  | Apache License 2.0  | 0 days, 12 hrs, 52 mins  |
|  28 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines.  | 8,543  | 969  | 790  |  16 | 9  | Apache License 2.0  | 2 days, 23 hrs, 33 mins  |
|  29 | [server](https://github.com/triton-inference-server/server)  | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  | 8,269  | 1,473  | 624  |  120 | 72  | BSD 3-Clause "New" or "Revised" License | 0 days, 14 hrs, 46 mins  |
|  30 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | LLM Frontend for Power Users.  | 8,072  | 2,386  | 246  |  166 | 84  | GNU Affero General Public License v3.0  | 0 days, 19 hrs, 50 mins  |
|  31 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Python bindings for llama.cpp  | 8,027  | 951  | 525  |  156 | 276  | MIT License  | 0 days, 21 hrs, 6 mins  |
|  32 | [chat-ui](https://github.com/huggingface/chat-ui)  | Open source codebase powering the HuggingChat app  | 7,528  | 1,105  | 274  |  108 | 14  | Apache License 2.0  | 1 days, 17 hrs, 47 mins  |
|  33 | [openplayground](https://github.com/nat/openplayground)  | An LLM playground you can run on your laptop  | 6,243  | 486  | 88  |  15 | 0  | MIT License  | 4 days, 8 hrs, 53 mins  |
|  34 | [big-agi](https://github.com/enricoros/big-agi)  | Generative AI suite powered by state-of-the-art models and providing advanced AI/AGI functions. It features AI personas, AGI functions, multi-model chats, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy on-prem or in the cloud.  | 5,448  | 1,247  | 209  |  43 | 16  | MIT License  | 3 days, 11 hrs, 40 mins  |
|  35 | [inference](https://github.com/xorbitsai/inference)  | Replace OpenAI GPT with another LLM in your app by changing a single line of code. Xinference gives you the freedom to use any LLM you need. With Xinference, you're empowered to run inference with any open-source language models, speech recognition models, and multimodal models, whether in the cloud, on-premises, or even on your laptop.  | 5,261  | 424  | 206  |  77 | 87  | Apache License 2.0  | 0 days, 8 hrs, 28 mins  |
|  36 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | Run GGUF models easily with a KoboldAI UI. One File. Zero Install.  | 5,169  | 353  | 243  |  463 | 88  | GNU Affero General Public License v3.0  | 0 days, 21 hrs, 40 mins  |
|  37 | [llm](https://github.com/simonw/llm)  | Access large language models from the command-line  | 4,580  | 253  | 242  |  22 | 29  | Apache License 2.0  | 2 days, 20 hrs, 36 mins  |
|  38 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  | 4,554  | 409  | 317  |  76 | 37  | Apache License 2.0  | 0 days, 9 hrs, 8 mins  |
|  39 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Lord of Large Language Models Web User Interface  | 4,318  | 543  | 155  |  38 | 23  | Apache License 2.0  | 0 days, 13 hrs, 45 mins  |
|  40 | [exllamav2](https://github.com/turboderp/exllamav2)  | A fast inference library for running LLMs locally on modern consumer-class GPUs  | 3,619  | 279  | 90  |  46 | 34  | MIT License  | 11 days, 19 hrs, 30 mins |
|  41 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | A C#/.NET library to run LLM (🦙LLaMA/LLaVA) on your local device efficiently.  | 2,633  | 343  | 140  |  56 | 22  | MIT License  | 0 days, 8 hrs, 2 mins  |
|  42 | [cortex.cpp](https://github.com/janhq/cortex.cpp)  | Local AI API Platform  | 2,024  | 114  | 120  |  32 | 138  | Apache License 2.0  | 0 days, 8 hrs, 18 mins  |
|  43 | [nitro](https://github.com/janhq/nitro)  | Local AI API Platform  | 2,024  | 114  | 120  |  32 | 138  | Apache License 2.0  | 0 days, 8 hrs, 16 mins  |
|  44 | [page-assist](https://github.com/n4ze3m/page-assist)  | Use your locally running AI models to assist you in your web browsing  | 1,469  | 140  | 98  |  12 | 20  | MIT License  | 5 days, 19 hrs, 34 mins  |
|  45 | [maid](https://github.com/Mobile-Artificial-Intelligence/maid)  | Maid is a cross-platform Flutter app for interfacing with GGUF / llama.cpp models locally, and with Ollama and OpenAI models remotely.  | 1,434  | 159  | 17  |  21 | 31  | MIT License  | 3 days, 7 hrs, 29 mins  |
|  46 | [LLMFarm](https://github.com/guinmoon/LLMFarm)  | llama and other  large language models on iOS and MacOS offline using GGML library.  | 1,314  | 84  | 19  |  1 | 32  | MIT License  | 1 days, 19 hrs, 35 mins  |
|  47 | [oterm](https://github.com/ggozad/oterm)  | a text-based terminal client for Ollama  | 1,037  | 61  | 8  |  12 | 35  | MIT License  | 0 days, 17 hrs, 26 mins  |
|  48 | [amica](https://github.com/semperai/amica)  | Amica is an open source interface for interactive communication with 3D characters with voice synthesis and speech recognition.  | 700  | 113  | 36  |  16 | 4  | MIT License  | 3 days, 5 hrs, 46 mins  |
|  49 | [ChatterUI](https://github.com/Vali-98/ChatterUI)  | Simple frontend for LLMs built in react-native.  | 500  | 27  | 12  |  1 | 45  | GNU Affero General Public License v3.0  | 1 days, 1 hrs, 47 mins  |
|  50 | [exui](https://github.com/turboderp/exui)  | Web UI for ExLlamaV2  | 436  | 41  | 33  |  8 | 0  | MIT License  | 22 days, 16 hrs, 37 mins |
|  51 | [ava](https://github.com/cztomsik/ava)  | All-in-one desktop app for running LLMs locally.  | 417  | 15  | 3  |  3 | 0  | Other  | 6 days, 23 hrs, 57 mins  |
|  52 | [tenere](https://github.com/pythops/tenere)  | 🤖 TUI interface for LLMs written in Rust  | 351  | 8  | 2  |  7 | 13  | GNU General Public License v3.0  | 57 days, 4 hrs, 16 mins  |
|  53 | [web-llm-chat](https://github.com/mlc-ai/web-llm-chat)  | Chat with AI large language models running natively in your browser. Enjoy private, server-free, seamless AI conversations.  | 305  | 50  | 10  |  181 | 0  | Apache License 2.0  | 27 days, 18 hrs, 53 mins |
|  54 | [mikupad](https://github.com/lmg-anon/mikupad)  | LLM Frontend in a single html file  | 248  | 27  | 24  |  10 | 40  | Creative Commons Zero v1.0 Universal  | 15 days, 17 hrs, 35 mins |
|  55 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Local ML voice chat using high-end models.  | 142  | 8  | 1  |  1 | 0  | MIT License  | 5 days, 5 hrs, 5 mins  |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
