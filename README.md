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

*Last Updated: 22/04/2024*

|  # | Repo  | About  | Stars  | Forks  | Issues  |  Contributors | Releases  | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [transformers](https://github.com/huggingface/transformers)  | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX.  | 124,710 | 24,739  | 1,081  |  433 | 146  | Apache License 2.0  | 0 days, 16 hrs, 45 mins  |
|  2 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS). 一键拥有你自己的跨平台 ChatGPT/Gemini 应用。  | 67,768  | 54,856  | 229  |  176 | 58  | MIT License  | 0 days, 8 hrs, 10 mins  |
|  3 | [gpt4all](https://github.com/nomic-ai/gpt4all)  | gpt4all: run open-source LLMs anywhere  | 63,795  | 6,993  | 394  |  96 | 12  | MIT License  | 2 days, 16 hrs, 30 mins  |
|  4 | [ollama](https://github.com/ollama/ollama)  | Get up and running with Llama 3, Mistral, Gemma, and other large language models.  | 57,601  | 4,066  | 824  |  178 | 54  | MIT License  | 0 days, 9 hrs, 24 mins  |
|  5 | [gpt4free](https://github.com/xtekky/gpt4free)  | The official gpt4free repository - various collection of powerful language models  | 57,201  | 12,897  | 81  |  191 | 123  | GNU General Public License v3.0  | 0 days, 9 hrs, 54 mins  |
|  6 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | LLM inference in C/C++  | 56,099  | 7,932  | 551  |  477 | 1,693  | MIT License  | 0 days, 8 hrs, 8 mins  |
|  7 | [gpt_academic](https://github.com/binary-husky/gpt_academic)  | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。  | 55,602  | 7,023  | 248  |  79 | 28  | GNU General Public License v3.0  | 0 days, 16 hrs, 27 mins  |
|  8 | [privateGPT](https://github.com/imartinez/privateGPT)  | Interact with your documents using the power of GPT, 100% privately, no data leaks  | 51,641  | 6,883  | 210  |  71 | 7  | Apache License 2.0  | 1 days, 1 hrs, 50 mins  |
|  9 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | A Gradio web UI for Large Language Models. Supports transformers, GPTQ, AWQ, EXL2, llama.cpp (GGUF), Llama models.  | 36,003  | 4,821  | 224  |  303 | 40  | GNU Affero General Public License v3.0  | 0 days, 14 hrs, 50 mins  |
|  10 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | 🤯 Lobe Chat - an open-source, modern-design LLMs/AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Perplexity / Bedrock / Azure / Mistral / Ollama ), Multi-Modals (Vision/TTS) and plugin system. One-click FREE deployment of your private ChatGPT chat application.  | 28,525  | 6,519  | 312  |  95 | 538  | MIT License  | 0 days, 8 hrs, 16 mins  |
|  11 | [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui)  | AI chat for every model.  | 26,075  | 7,176  | 97  |  42 | 0  | MIT License  | 1 days, 22 hrs, 22 mins  |
|  12 | [LocalAI](https://github.com/mudler/LocalAI)  | :robot: The free, Open Source OpenAI alternative. Self-hosted, community-driven and local-first. Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. It allows to generate Text, Audio, Video, Images. Also with voice cloning capabilities. | 19,345  | 1,451  | 267  |  83 | 44  | MIT License  | 0 days, 8 hrs, 38 mins  |
|  13 | [localGPT](https://github.com/PromtEngineer/localGPT)  | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private.  | 19,110  | 2,117  | 454  |  42 | 0  | Apache License 2.0  | 22 days, 1 hrs, 29 mins  |
|  14 | [chatbox](https://github.com/Bin-Huang/chatbox)  | Chatbox is a desktop client for ChatGPT, Claude and other LLMs, available on Windows, Mac, Linux  | 18,398  | 1,890  | 229  |  28 | 58  | GNU General Public License v3.0  | 4 days, 2 hrs, 57 mins  |
|  15 | [vllm](https://github.com/vllm-project/vllm)  | A high-throughput and memory-efficient inference and serving engine for LLMs  | 18,069  | 2,376  | 868  |  282 | 24  | Apache License 2.0  | 0 days, 8 hrs, 2 mins  |
|  16 | [jan](https://github.com/janhq/jan)  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer. Multiple engine support (llama.cpp, TensorRT-LLM)  | 16,937  | 939  | 177  |  44 | 20  | GNU Affero General Public License v3.0  | 0 days, 8 hrs, 8 mins  |
|  17 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Enable everyone to develop, optimize and deploy AI models natively on everyone's devices.  | 16,800  | 1,286  | 209  |  102 | 1  | Apache License 2.0  | 0 days, 8 hrs, 19 mins  |
|  18 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  | 14,696  | 2,226  | 106  |  46 | 21  | GNU General Public License v3.0  | 3 days, 18 hrs, 9 mins  |
|  19 | [open-webui](https://github.com/open-webui/open-webui)  | User-friendly WebUI for LLMs (Formerly Ollama WebUI)  | 14,362  | 1,423  | 105  |  99 | 19  | MIT License  | 0 days, 10 hrs, 41 mins  |
|  20 | [llamafile](https://github.com/Mozilla-Ocho/llamafile)  | Distribute and run LLMs with a single file.  | 13,605  | 672  | 57  |  31 | 14  | Other  | 1 days, 0 hrs, 12 mins  |
|  21 | [anything-llm](https://github.com/Mintplex-Labs/anything-llm)  | The all-in-one AI app for any LLM with full RAG and AI Agent capabilites.  | 11,788  | 1,245  | 103  |  36 | 0  | MIT License  | 0 days, 16 hrs, 26 mins  |
|  22 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Enhanced ChatGPT Clone: Features OpenAI, Assistants API, Azure, Groq, GPT-4 Vision, Mistral, Bing, Anthropic, OpenRouter, Vertex AI, Gemini, AI model switching, message search, langchain, DALL-E-3, ChatGPT Plugins, OpenAI Functions, Secure Multi-User System, Presets, completely open-source for self-hosting. More features in development  | 10,596  | 1,913  | 76  |  108 | 37  | MIT License  | 0 days, 16 hrs, 25 mins  |
|  23 | [h2ogpt](https://github.com/h2oai/h2ogpt)  | Private chat with local GPT with document, images, video, etc. 100% private, Apache 2.0. Supports oLLaMa, Mixtral, llama.cpp, and more. Demo: https://gpt.h2o.ai/ https://codellama.h2o.ai/  | 10,376  | 1,155  | 252  |  67 | 129  | Apache License 2.0  | 0 days, 8 hrs, 24 mins  |
|  24 | [chathub](https://github.com/chathub-dev/chathub)  | All-in-one chatbot client  | 9,485  | 953  | 286  |  12 | 0  | GNU General Public License v3.0  | 23 days, 1 hrs, 31 mins  |
|  25 | [web-llm](https://github.com/mlc-ai/web-llm)  | Bringing large-language models and chat to web browsers. Everything runs inside the browser with no server support.  | 9,036  | 546  | 86  |  28 | 1  | Apache License 2.0  | 1 days, 5 hrs, 58 mins  |
|  26 | [FlexGen](https://github.com/FMInference/FlexGen)  | Running large language models on a single GPU for throughput-oriented scenarios.  | 8,995  | 520  | 55  |  18 | 0  | Apache License 2.0  | 2 days, 15 hrs, 40 mins  |
|  27 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Run any open-source LLMs, such as Llama 2, Mistral, as OpenAI compatible API endpoint, locally and in the cloud.  | 8,718  | 550  | 93  |  25 | 110  | Apache License 2.0  | 6 days, 18 hrs, 17 mins  |
|  28 | [text-generation-inference](https://github.com/huggingface/text-generation-inference) | Large Language Model Text Generation Inference  | 7,812  | 846  | 151  |  75 | 40  | Apache License 2.0  | 0 days, 19 hrs, 59 mins  |
|  29 | [server](https://github.com/triton-inference-server/server)  | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  | 7,309  | 1,367  | 439  |  111 | 65  | BSD 3-Clause "New" or "Revised" License | 2 days, 6 hrs, 11 mins  |
|  30 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines.  | 6,478  | 654  | 560  |  10 | 5  | Apache License 2.0  | 5 days, 4 hrs, 13 mins  |
|  31 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Python bindings for llama.cpp  | 6,362  | 755  | 347  |  126 | 130  | MIT License  | 0 days, 10 hrs, 26 mins  |
|  32 | [openplayground](https://github.com/nat/openplayground)  | An LLM playground you can run on your laptop  | 6,069  | 466  | 81  |  16 | 0  | MIT License  | 3 days, 6 hrs, 32 mins  |
|  33 | [chat-ui](https://github.com/huggingface/chat-ui)  | Open source codebase powering the HuggingChat app  | 5,897  | 796  | 192  |  64 | 8  | Apache License 2.0  | 0 days, 13 hrs, 41 mins  |
|  34 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | LLM Frontend for Power Users.  | 5,772  | 1,803  | 298  |  105 | 77  | GNU Affero General Public License v3.0  | 0 days, 11 hrs, 36 mins  |
|  35 | [big-agi](https://github.com/enricoros/big-agi)  | Generative AI suite powered by state-of-the-art models and providing advanced AI/AGI functions. It features AI personas, AGI functions, multi-model chats, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy on-prem or in the cloud.  | 4,152  | 936  | 129  |  35 | 15  | MIT License  | 3 days, 15 hrs, 47 mins  |
|  36 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Lord of Large Language Models Web User Interface  | 3,766  | 477  | 133  |  36 | 20  | Apache License 2.0  | 0 days, 12 hrs, 11 mins  |
|  37 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | A simple one-file way to run various GGML and GGUF models with KoboldAI's UI  | 3,729  | 271  | 167  |  474 | 75  | GNU Affero General Public License v3.0  | 0 days, 22 hrs, 37 mins  |
|  38 | [llm](https://github.com/simonw/llm)  | Access large language models from the command-line  | 2,883  | 137  | 157  |  19 | 24  | Apache License 2.0  | 0 days, 11 hrs, 52 mins  |
|  39 | [exllamav2](https://github.com/turboderp/exllamav2)  | A fast inference library for running LLMs locally on modern consumer-class GPUs  | 2,859  | 213  | 95  |  31 | 18  | MIT License  | 1 days, 4 hrs, 22 mins  |
|  40 | [inference](https://github.com/xorbitsai/inference)  | Replace OpenAI GPT with another LLM in your app by changing a single line of code. Xinference gives you the freedom to use any LLM you need. With Xinference, you're empowered to run inference with any open-source language models, speech recognition models, and multimodal models, whether in the cloud, on-premises, or even on your laptop.  | 2,473  | 191  | 243  |  41 | 57  | Apache License 2.0  | 0 days, 8 hrs, 50 mins  |
|  41 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  | 2,239  | 197  | 93  |  45 | 25  | Apache License 2.0  | 0 days, 8 hrs, 11 mins  |
|  42 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | A cross-platform library to run 🦙LLaMA/LLaVA model (and others) on your local device efficiently.  | 1,854  | 247  | 97  |  39 | 15  | MIT License  | 0 days, 10 hrs, 33 mins  |
|  43 | [nitro](https://github.com/janhq/nitro)  | An inference server on top of llama.cpp. OpenAI-compatible API, queue, & scaling. Embed a prod-ready, local inference engine in your apps. Powers Jan  | 1,563  | 74  | 50  |  23 | 72  | GNU Affero General Public License v3.0  | 0 days, 8 hrs, 36 mins  |
|  44 | [chatbot-ollama](https://github.com/ivanfioravanti/chatbot-ollama)  | Chatbot Ollama is an open source chat UI for Ollama.  | 1,063  | 168  | 16  |  6 | 1  | Other  | 2 days, 1 hrs, 9 mins  |
|  45 | [LLMFarm](https://github.com/guinmoon/LLMFarm)  | llama and other  large language models on iOS and MacOS offline using GGML library.  | 836  | 48  | 12  |  1 | 24  | MIT License  | 3 days, 16 hrs, 12 mins  |
|  46 | [maid](https://github.com/Mobile-Artificial-Intelligence/maid)  | Maid is a cross-platform Flutter app for interfacing with GGUF / llama.cpp models locally, and with Ollama and OpenAI models remotely.  | 634  | 72  | 3  |  13 | 26  | MIT License  | 0 days, 23 hrs, 12 mins  |
|  47 | [oterm](https://github.com/ggozad/oterm)  | a text-based terminal client for Ollama  | 544  | 32  | 7  |  6 | 15  | MIT License  | 0 days, 18 hrs, 55 mins  |
|  48 | [amica](https://github.com/semperai/amica)  | Amica is an open source interface for interactive communication with 3D characters with voice synthesis and speech recognition.  | 488  | 76  | 45  |  16 | 4  | MIT License  | 2 days, 22 hrs, 0 mins  |
|  49 | [FreeChat](https://github.com/psugihara/FreeChat)  | llama.cpp based AI chat app for macOS  | 351  | 26  | 20  |  4 | 0  | MIT License  | 4 days, 7 hrs, 54 mins  |
|  50 | [exui](https://github.com/turboderp/exui)  | Web UI for ExLlamaV2  | 336  | 30  | 20  |  7 | 0  | MIT License  | 1 days, 2 hrs, 0 mins  |
|  51 | [ava](https://github.com/cztomsik/ava)  | All-in-one desktop app for running LLMs locally.  | 298  | 13  | 9  |  2 | 0  | Other  | 0 days, 13 hrs, 46 mins  |
|  52 | [LocalAIVoiceChat](https://github.com/KoljaB/LocalAIVoiceChat)  | Local AI talk with a custom voice based on Zephyr 7B model. Uses RealtimeSTT with faster_whisper for transcription and RealtimeTTS with Coqui XTTS for synthesis.  | 292  | 25  | 6  |  1 | 1  | Other  | 1 days, 2 hrs, 44 mins  |
|  53 | [tenere](https://github.com/pythops/tenere)  | 🔥 TUI interface for LLMs written in Rust  | 219  | 7  | 1  |  5 | 12  | GNU General Public License v3.0  | 33 days, 15 hrs, 19 mins |
|  54 | [mikupad](https://github.com/lmg-anon/mikupad)  | LLM Frontend in a single html file  | 108  | 16  | 15  |  8 | 0  | Creative Commons Zero v1.0 Universal  | 1 days, 15 hrs, 48 mins  |
|  55 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Local ML voice chat using high-end models.  | 107  | 6  | 0  |  1 | 0  | MIT License  | 1 days, 9 hrs, 39 mins  |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
