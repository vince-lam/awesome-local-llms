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

*Last Updated: 10/04/2024*

|  # | Repo  | About  | Stars  | Forks  | Issues  |  Contributors | Releases  | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [transformers](https://github.com/huggingface/transformers)  | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX.  | 123,996 | 24,631  | 1,058  |  434 | 145  | Apache License 2.0  | 0 days, 8 hrs, 18 mins  |
|  2 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS). 一键拥有你自己的跨平台 ChatGPT/Gemini 应用。  | 66,992  | 54,412  | 218  |  175 | 58  | MIT License  | 0 days, 9 hrs, 12 mins  |
|  3 | [gpt4all](https://github.com/nomic-ai/gpt4all)  | gpt4all: run open-source LLMs anywhere  | 63,425  | 6,957  | 390  |  96 | 12  | MIT License  | 5 days, 16 hrs, 0 mins  |
|  4 | [gpt4free](https://github.com/xtekky/gpt4free)  | The official gpt4free repository | various collection of powerful language models  | 56,511  | 12,781  | 89  |  188 | 109  | GNU General Public License v3.0  | 0 days, 12 hrs, 31 mins  |
|  5 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | LLM inference in C/C++  | 54,841  | 7,753  | 610  |  478 | 1,651  | MIT License  | 0 days, 8 hrs, 6 mins  |
|  6 | [gpt_academic](https://github.com/binary-husky/gpt_academic)  | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。  | 54,148  | 6,839  | 235  |  77 | 28  | GNU General Public License v3.0  | 0 days, 8 hrs, 40 mins  |
|  7 | [ollama](https://github.com/ollama/ollama)  | Get up and running with Llama 2, Mistral, Gemma, and other large language models.  | 53,875  | 3,751  | 767  |  173 | 53  | MIT License  | 0 days, 13 hrs, 24 mins  |
|  8 | [privateGPT](https://github.com/imartinez/privateGPT)  | Interact with your documents using the power of GPT, 100% privately, no data leaks  | 51,263  | 6,813  | 194  |  70 | 7  | Apache License 2.0  | 1 days, 5 hrs, 29 mins  |
|  9 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | A Gradio web UI for Large Language Models. Supports transformers, GPTQ, AWQ, EXL2, llama.cpp (GGUF), Llama models.  | 35,451  | 4,721  | 227  |  299 | 38  | GNU Affero General Public License v3.0  | 0 days, 23 hrs, 42 mins  |
|  10 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | 🤯 Lobe Chat - an open-source, modern-design LLMs/AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Perplexity / Bedrock / Azure / Mistral / Ollama ), Multi-Modals (Vision/TTS) and plugin system. One-click FREE deployment of your private ChatGPT chat application.  | 26,879  | 6,066  | 300  |  89 | 510  | MIT License  | 0 days, 8 hrs, 46 mins  |
|  11 | [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui)  | AI chat for every model.  | 25,892  | 7,083  | 89  |  41 | 0  | MIT License  | 1 days, 9 hrs, 50 mins  |
|  12 | [localGPT](https://github.com/PromtEngineer/localGPT)  | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private.  | 19,015  | 2,102  | 452  |  42 | 0  | Apache License 2.0  | 10 days, 9 hrs, 5 mins  |
|  13 | [LocalAI](https://github.com/mudler/LocalAI)  | :robot: The free, Open Source OpenAI alternative. Self-hosted, community-driven and local-first. Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. It allows to generate Text, Audio, Video, Images. Also with voice cloning capabilities. | 18,803  | 1,381  | 253  |  79 | 43  | MIT License  | 0 days, 8 hrs, 11 mins  |
|  14 | [chatbox](https://github.com/Bin-Huang/chatbox)  | Chatbox is a desktop client for ChatGPT, Claude and other LLMs, available on Windows, Mac, Linux  | 18,173  | 1,870  | 237  |  28 | 55  | GNU General Public License v3.0  | 8 days, 14 hrs, 22 mins  |
|  15 | [vllm](https://github.com/vllm-project/vllm)  | A high-throughput and memory-efficient inference and serving engine for LLMs  | 17,445  | 2,252  | 787  |  267 | 23  | Apache License 2.0  | 0 days, 8 hrs, 22 mins  |
|  16 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Enable everyone to develop, optimize and deploy AI models natively on everyone's devices.  | 16,562  | 1,263  | 196  |  100 | 1  | Apache License 2.0  | 0 days, 12 hrs, 16 mins  |
|  17 | [jan](https://github.com/janhq/jan)  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer  | 16,437  | 901  | 168  |  43 | 19  | GNU Affero General Public License v3.0  | 0 days, 8 hrs, 10 mins  |
|  18 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  | 14,622  | 2,224  | 103  |  46 | 21  | GNU General Public License v3.0  | 0 days, 14 hrs, 19 mins  |
|  19 | [llamafile](https://github.com/Mozilla-Ocho/llamafile)  | Distribute and run LLMs with a single file.  | 12,800  | 611  | 55  |  29 | 11  | Other  | 1 days, 1 hrs, 48 mins  |
|  20 | [open-webui](https://github.com/open-webui/open-webui)  | User-friendly WebUI for LLMs (Formerly Ollama WebUI)  | 12,470  | 1,236  | 109  |  89 | 16  | MIT License  | 0 days, 10 hrs, 11 mins  |
|  21 | [anything-llm](https://github.com/Mintplex-Labs/anything-llm)  | A multi-user ChatGPT for any LLMs and vector database. Unlimited documents, messages, and storage in one privacy-focused app. Now available as a desktop application with a built-in LLM!  | 10,668  | 1,130  | 87  |  34 | 0  | MIT License  | 0 days, 17 hrs, 52 mins  |
|  22 | [h2ogpt](https://github.com/h2oai/h2ogpt)  | Private chat with local GPT with document, images, video, etc. 100% private, Apache 2.0. Supports oLLaMa, Mixtral, llama.cpp, and more. Demo: https://gpt.h2o.ai/ https://codellama.h2o.ai/  | 10,269  | 1,141  | 238  |  67 | 129  | Apache License 2.0  | 0 days, 9 hrs, 33 mins  |
|  23 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Enhanced ChatGPT Clone: Features OpenAI, Assistants API, Azure, Groq, GPT-4 Vision, Mistral, Bing, Anthropic, OpenRouter, Google Gemini, AI model switching, message search, langchain, DALL-E-3, ChatGPT Plugins, OpenAI Functions, Secure Multi-User System, Presets, completely open-source for self-hosting. More features in development  | 9,514  | 1,726  | 76  |  104 | 37  | MIT License  | 0 days, 8 hrs, 38 mins  |
|  24 | [chathub](https://github.com/chathub-dev/chathub)  | All-in-one chatbot client  | 9,451  | 948  | 277  |  12 | 0  | GNU General Public License v3.0  | 11 days, 9 hrs, 8 mins  |
|  25 | [FlexGen](https://github.com/FMInference/FlexGen)  | Running large language models on a single GPU for throughput-oriented scenarios.  | 8,971  | 516  | 54  |  18 | 0  | Apache License 2.0  | 12 days, 15 hrs, 30 mins |
|  26 | [web-llm](https://github.com/mlc-ai/web-llm)  | Bringing large-language models and chat to web browsers. Everything runs inside the browser with no server support.  | 8,953  | 537  | 80  |  28 | 1  | Apache License 2.0  | 0 days, 17 hrs, 37 mins  |
|  27 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Run any open-source LLMs, such as Llama 2, Mistral, as OpenAI compatible API endpoint, locally and in the cloud.  | 8,625  | 539  | 91  |  25 | 110  | Apache License 2.0  | 2 days, 1 hrs, 51 mins  |
|  28 | [text-generation-inference](https://github.com/huggingface/text-generation-inference) | Large Language Model Text Generation Inference  | 7,644  | 832  | 139  |  74 | 38  | Apache License 2.0  | 0 days, 9 hrs, 29 mins  |
|  29 | [server](https://github.com/triton-inference-server/server)  | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  | 7,244  | 1,364  | 424  |  111 | 65  | BSD 3-Clause "New" or "Revised" License | 0 days, 16 hrs, 13 mins  |
|  30 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines.  | 6,299  | 627  | 550  |  10 | 4  | Apache License 2.0  | 1 days, 3 hrs, 46 mins  |
|  31 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Python bindings for llama.cpp  | 6,210  | 730  | 327  |  123 | 120  | MIT License  | 0 days, 10 hrs, 47 mins  |
|  32 | [chat-ui](https://github.com/huggingface/chat-ui)  | Open source codebase powering the HuggingChat app  | 5,767  | 772  | 180  |  60 | 7  | Apache License 2.0  | 1 days, 0 hrs, 8 mins  |
|  33 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | LLM Frontend for Power Users.  | 5,633  | 1,758  | 298  |  99 | 75  | GNU Affero General Public License v3.0  | 0 days, 8 hrs, 32 mins  |
|  34 | [big-agi](https://github.com/enricoros/big-agi)  | Generative AI suite powered by state-of-the-art models and providing advanced AI/AGI functions. It features AI personas, AGI functions, multi-model chats, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy on-prem or in the cloud.  | 3,955  | 900  | 126  |  34 | 15  | MIT License  | 0 days, 10 hrs, 39 mins  |
|  35 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Lord of Large Language Models Web User Interface  | 3,693  | 470  | 131  |  36 | 19  | Apache License 2.0  | 0 days, 10 hrs, 55 mins  |
|  36 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | A simple one-file way to run various GGML and GGUF models with KoboldAI's UI  | 3,621  | 264  | 167  |  475 | 73  | GNU Affero General Public License v3.0  | 1 days, 7 hrs, 14 mins  |
|  37 | [llm](https://github.com/simonw/llm)  | Access large language models from the command-line  | 2,792  | 130  | 152  |  19 | 24  | Apache License 2.0  | 0 days, 14 hrs, 3 mins  |
|  38 | [exllamav2](https://github.com/turboderp/exllamav2)  | A fast inference library for running LLMs locally on modern consumer-class GPUs  | 2,785  | 207  | 90  |  31 | 17  | MIT License  | 3 days, 0 hrs, 7 mins  |
|  39 | [inference](https://github.com/xorbitsai/inference)  | Replace OpenAI GPT with another LLM in your app by changing a single line of code. Xinference gives you the freedom to use any LLM you need. With Xinference, you're empowered to run inference with any open-source language models, speech recognition models, and multimodal models, whether in the cloud, on-premises, or even on your laptop.  | 2,317  | 183  | 218  |  41 | 54  | Apache License 2.0  | 0 days, 8 hrs, 45 mins  |
|  40 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  | 2,163  | 193  | 97  |  44 | 25  | Apache License 2.0  | 0 days, 8 hrs, 38 mins  |
|  41 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | A cross-platform library to run 🦙LLaMA/LLaVA model (and others) on your local device efficiently.  | 1,803  | 242  | 89  |  39 | 15  | MIT License  | 2 days, 3 hrs, 5 mins  |
|  42 | [nitro](https://github.com/janhq/nitro)  | An inference server on top of llama.cpp. OpenAI-compatible API, queue, & scaling. Embed a prod-ready, local inference engine in your apps. Powers Jan  | 1,523  | 73  | 30  |  22 | 69  | GNU Affero General Public License v3.0  | 0 days, 8 hrs, 59 mins  |
|  43 | [chatbot-ollama](https://github.com/ivanfioravanti/chatbot-ollama)  | Chatbot Ollama is an open source chat UI for Ollama.  | 994  | 160  | 18  |  6 | 1  | Other  | 47 days, 18 hrs, 30 mins |
|  44 | [LLMFarm](https://github.com/guinmoon/LLMFarm)  | llama and other  large language models on iOS and MacOS offline using GGML library.  | 808  | 44  | 11  |  1 | 24  | MIT License  | 1 days, 1 hrs, 8 mins  |
|  45 | [maid](https://github.com/Mobile-Artificial-Intelligence/maid)  | Maid is a cross-platform Flutter app for interfacing with GGUF / llama.cpp models locally, and with Ollama and OpenAI models remotely.  | 574  | 64  | 7  |  12 | 25  | MIT License  | 0 days, 8 hrs, 4 mins  |
|  46 | [oterm](https://github.com/ggozad/oterm)  | a text-based terminal client for Ollama  | 511  | 27  | 5  |  6 | 14  | MIT License  | 8 days, 9 hrs, 25 mins  |
|  47 | [amica](https://github.com/semperai/amica)  | Amica is an open source interface for interactive communication with 3D characters with voice synthesis and speech recognition.  | 473  | 70  | 41  |  16 | 4  | MIT License  | 1 days, 1 hrs, 41 mins  |
|  48 | [FreeChat](https://github.com/psugihara/FreeChat)  | llama.cpp based AI chat app for macOS  | 347  | 25  | 18  |  4 | 0  | MIT License  | 15 days, 23 hrs, 4 mins  |
|  49 | [exui](https://github.com/turboderp/exui)  | Web UI for ExLlamaV2  | 325  | 27  | 20  |  7 | 0  | MIT License  | 4 days, 11 hrs, 2 mins  |
|  50 | [ava](https://github.com/cztomsik/ava)  | All-in-one desktop app for running LLMs locally.  | 294  | 12  | 8  |  2 | 0  | Other  | 6 days, 20 hrs, 28 mins  |
|  51 | [tenere](https://github.com/pythops/tenere)  | 🔥 TUI interface for LLMs written in Rust  | 214  | 7  | 1  |  5 | 12  | GNU General Public License v3.0  | 21 days, 22 hrs, 56 mins |
|  52 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Local ML voice chat using high-end models.  | 105  | 6  | 0  |  1 | 0  | MIT License  | 29 days, 18 hrs, 50 mins |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
