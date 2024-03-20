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

*Last Updated: 20/03/2024*

|  # | Repo  | About  | Stars  | Forks  | Issues  |  Contributors | Releases  | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [transformers](https://github.com/huggingface/transformers)  | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX.  | 122,449 | 24,278  | 1,037  |  434 | 141  | Apache License 2.0  | 0 days, 8 hrs, 6 mins  |
|  2 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS). 一键拥有你自己的跨平台 ChatGPT/Gemini 应用。  | 65,141  | 53,443  | 248  |  169 | 58  | MIT License  | 0 days, 11 hrs, 13 mins  |
|  3 | [gpt4all](https://github.com/nomic-ai/gpt4all)  | gpt4all: run open-source LLMs anywhere  | 62,673  | 6,869  | 373  |  92 | 12  | MIT License  | 0 days, 11 hrs, 55 mins  |
|  4 | [gpt4free](https://github.com/xtekky/gpt4free)  | The official gpt4free repository | various collection of powerful language models  | 54,706  | 12,519  | 94  |  183 | 98  | GNU General Public License v3.0  | 0 days, 23 hrs, 9 mins  |
|  5 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | LLM inference in C/C++  | 53,263  | 7,498  | 1,263  |  478 | 1,589  | MIT License  | 0 days, 8 hrs, 42 mins  |
|  6 | [gpt_academic](https://github.com/binary-husky/gpt_academic)  | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。  | 53,067  | 6,731  | 212  |  74 | 27  | GNU General Public License v3.0  | 0 days, 8 hrs, 8 mins  |
|  7 | [privateGPT](https://github.com/imartinez/privateGPT)  | Interact with your documents using the power of GPT, 100% privately, no data leaks  | 49,730  | 6,598  | 163  |  64 | 6  | Apache License 2.0  | 0 days, 15 hrs, 39 mins  |
|  8 | [ollama](https://github.com/ollama/ollama)  | Get up and running with Llama 2, Mistral, Gemma, and other large language models.  | 49,075  | 3,311  | 672  |  149 | 51  | MIT License  | 0 days, 9 hrs, 12 mins  |
|  9 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | A Gradio web UI for Large Language Models. Supports transformers, GPTQ, AWQ, EXL2, llama.cpp (GGUF), Llama models.  | 34,547  | 4,612  | 269  |  299 | 35  | GNU Affero General Public License v3.0  | 0 days, 8 hrs, 55 mins  |
|  10 | [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui)  | AI chat for every model.  | 25,424  | 6,927  | 76  |  31 | 0  | MIT License  | 0 days, 8 hrs, 9 mins  |
|  11 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | 🤯 Lobe Chat - an open-source, modern-design LLMs/AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Perplexity / Bedrock / Azure / Mistral / Ollama ), Multi-Modals (Vision/TTS) and plugin system. One-click FREE deployment of your private ChatGPT chat application.  | 23,342  | 4,873  | 249  |  75 | 474  | MIT License  | 0 days, 8 hrs, 51 mins  |
|  12 | [localGPT](https://github.com/PromtEngineer/localGPT)  | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private.  | 18,841  | 2,078  | 446  |  42 | 0  | Apache License 2.0  | 1 days, 22 hrs, 42 mins  |
|  13 | [LocalAI](https://github.com/mudler/LocalAI)  | :robot: The free, Open Source OpenAI alternative. Self-hosted, community-driven and local-first. Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. It allows to generate Text, Audio, Video, Images. Also with voice cloning capabilities. | 17,819  | 1,305  | 243  |  77 | 39  | MIT License  | 0 days, 8 hrs, 5 mins  |
|  14 | [chatbox](https://github.com/Bin-Huang/chatbox)  | Chatbox is a desktop client for ChatGPT, Claude and other LLMs, available on Windows, Mac, Linux  | 17,740  | 1,827  | 226  |  28 | 55  | GNU General Public License v3.0  | 1 days, 13 hrs, 51 mins  |
|  15 | [vllm](https://github.com/vllm-project/vllm)  | A high-throughput and memory-efficient inference and serving engine for LLMs  | 16,304  | 2,065  | 1,046  |  235 | 21  | Apache License 2.0  | 0 days, 8 hrs, 33 mins  |
|  16 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Enable everyone to develop, optimize and deploy AI models natively on everyone's devices.  | 16,282  | 1,225  | 208  |  94 | 1  | Apache License 2.0  | 0 days, 10 hrs, 39 mins  |
|  17 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  | 14,500  | 2,211  | 105  |  45 | 20  | GNU General Public License v3.0  | 4 days, 9 hrs, 42 mins  |
|  18 | [jan](https://github.com/janhq/jan)  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer  | 11,825  | 644  | 194  |  38 | 18  | GNU Affero General Public License v3.0  | 0 days, 10 hrs, 51 mins  |
|  19 | [llamafile](https://github.com/Mozilla-Ocho/llamafile)  | Distribute and run LLMs with a single file.  | 10,370  | 470  | 54  |  27 | 10  | Other  | 3 days, 19 hrs, 52 mins  |
|  20 | [open-webui](https://github.com/open-webui/open-webui)  | User-friendly WebUI for LLMs (Formerly Ollama WebUI)  | 10,128  | 942  | 86  |  69 | 12  | MIT License  | 0 days, 10 hrs, 45 mins  |
|  21 | [h2ogpt](https://github.com/h2oai/h2ogpt)  | Private chat with local GPT with document, images, video, etc. 100% private, Apache 2.0. Supports oLLaMa, Mixtral, llama.cpp, and more. Demo: <https://gpt.h2o.ai/> <https://codellama.h2o.ai/>  | 10,085  | 1,126  | 219  |  65 | 129  | Apache License 2.0  | 0 days, 8 hrs, 10 mins  |
|  22 | [chathub](https://github.com/chathub-dev/chathub)  | All-in-one chatbot client  | 9,365  | 922  | 266  |  12 | 0  | GNU General Public License v3.0  | 16 days, 12 hrs, 32 mins |
|  23 | [anything-llm](https://github.com/Mintplex-Labs/anything-llm)  | A multi-user ChatGPT for any LLMs and vector database. Unlimited documents, messages, and storage in one privacy-focused app. Now available as a desktop application!  | 9,337  | 992  | 77  |  32 | 0  | MIT License  | 0 days, 8 hrs, 52 mins  |
|  24 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Enhanced ChatGPT Clone: Features OpenAI, Assistants API, Azure, Groq, GPT-4 Vision, Mistral, Bing, Anthropic, OpenRouter, Google Gemini, AI model switching, message search, langchain, DALL-E-3, ChatGPT Plugins, OpenAI Functions, Secure Multi-User System, Presets, completely open-source for self-hosting. More features in development  | 8,831  | 1,587  | 66  |  86 | 36  | MIT License  | 0 days, 17 hrs, 59 mins  |
|  25 | [web-llm](https://github.com/mlc-ai/web-llm)  | Bringing large-language models and chat to web browsers. Everything runs inside the browser with no server support.  | 8,816  | 530  | 76  |  28 | 1  | Apache License 2.0  | 0 days, 12 hrs, 10 mins  |
|  26 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Operating LLMs in production  | 8,439  | 520  | 90  |  24 | 109  | Apache License 2.0  | 2 days, 1 hrs, 59 mins  |
|  27 | [text-generation-inference](https://github.com/huggingface/text-generation-inference) | Large Language Model Text Generation Inference  | 7,277  | 780  | 165  |  73 | 36  | Other  | 1 days, 1 hrs, 28 mins  |
|  28 | [server](https://github.com/triton-inference-server/server)  | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  | 7,107  | 1,352  | 388  |  110 | 64  | BSD 3-Clause "New" or "Revised" License | 0 days, 17 hrs, 57 mins  |
|  29 | [openplayground](https://github.com/nat/openplayground)  | An LLM playground you can run on your laptop  | 6,034  | 457  | 78  |  16 | 0  | MIT License  | 47 days, 13 hrs, 19 mins |
|  30 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines.  | 5,978  | 578  | 536  |  10 | 4  | Apache License 2.0  | 1 days, 9 hrs, 14 mins  |
|  31 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Python bindings for llama.cpp  | 5,966  | 705  | 322  |  119 | 106  | MIT License  | 0 days, 20 hrs, 43 mins  |
|  32 | [chat-ui](https://github.com/huggingface/chat-ui)  | Open source codebase powering the HuggingChat app  | 5,613  | 736  | 179  |  58 | 5  | Apache License 2.0  | 0 days, 8 hrs, 55 mins  |
|  33 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | LLM Frontend for Power Users.  | 5,360  | 1,684  | 267  |  93 | 74  | GNU Affero General Public License v3.0  | 0 days, 19 hrs, 24 mins  |
|  34 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Lord of Large Language Models Web User Interface  | 3,620  | 459  | 128  |  36 | 18  | Apache License 2.0  | 0 days, 9 hrs, 50 mins  |
|  35 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | A simple one-file way to run various GGML and GGUF models with KoboldAI's UI  | 3,412  | 256  | 156  |  475 | 72  | GNU Affero General Public License v3.0  | 0 days, 9 hrs, 55 mins  |
|  36 | [big-agi](https://github.com/enricoros/big-agi)  | Generative AI suite powered by the newest LLMs. Bundling AI personas, AGI functions, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy on-prem or in the cloud.  | 3,230  | 790  | 117  |  32 | 13  | MIT License  | 0 days, 9 hrs, 44 mins  |
|  37 | [exllamav2](https://github.com/turboderp/exllamav2)  | A fast inference library for running LLMs locally on modern consumer-class GPUs  | 2,680  | 192  | 104  |  30 | 15  | MIT License  | 0 days, 11 hrs, 30 mins  |
|  38 | [llm](https://github.com/simonw/llm)  | Access large language models from the command-line  | 2,631  | 118  | 142  |  19 | 24  | Apache License 2.0  | 2 days, 8 hrs, 24 mins  |
|  39 | [inference](https://github.com/xorbitsai/inference)  | Replace OpenAI GPT with another LLM in your app by changing a single line of code. Xinference gives you the freedom to use any LLM you need. With Xinference, you're empowered to run inference with any open-source language models, speech recognition models, and multimodal models, whether in the cloud, on-premises, or even on your laptop.  | 2,035  | 163  | 194  |  36 | 52  | Apache License 2.0  | 0 days, 8 hrs, 2 mins  |
|  40 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  | 2,010  | 178  | 81  |  43 | 24  | Apache License 2.0  | 0 days, 9 hrs, 0 mins  |
|  41 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | Run local LLaMA/GPT model easily and fast in C#!🤗 It's also easy to integrate LLamaSharp with semantic-kernel, unity, WPF and WebApp.  | 1,689  | 226  | 79  |  35 | 14  | MIT License  | 0 days, 11 hrs, 51 mins  |
|  42 | [ctransformers](https://github.com/marella/ctransformers)  | Python bindings for the Transformer models implemented in C/C++ using GGML library.  | 1,642  | 126  | 106  |  6 | 30  | MIT License  | 52 days, 11 hrs, 16 mins |
|  43 | [nitro](https://github.com/janhq/nitro)  | An inference server on top of llama.cpp. OpenAI-compatible API, queue, & scaling. Embed a prod-ready, local inference engine in your apps. Powers Jan  | 1,349  | 61  | 30  |  18 | 63  | GNU Affero General Public License v3.0  | 6 days, 1 hrs, 52 mins  |
|  44 | [chatbot-ollama](https://github.com/ivanfioravanti/chatbot-ollama)  | Chatbot Ollama is an open source chat UI for Ollama.  | 899  | 132  | 18  |  6 | 1  | Other  | 26 days, 18 hrs, 35 mins |
|  45 | [LLMFarm](https://github.com/guinmoon/LLMFarm)  | llama and other  large language models on iOS and MacOS offline using GGML library.  | 780  | 43  | 8  |  1 | 23  | MIT License  | 1 days, 3 hrs, 57 mins  |
|  46 | [maid](https://github.com/Mobile-Artificial-Intelligence/maid)  | Maid is a cross-platform Flutter app for interfacing with GGUF / llama.cpp models locally, and with Ollama and OpenAI models remotely.  | 506  | 56  | 6  |  10 | 23  | MIT License  | 0 days, 8 hrs, 2 mins  |
|  47 | [oterm](https://github.com/ggozad/oterm)  | a text-based terminal client for Ollama  | 460  | 23  | 3  |  6 | 13  | MIT License  | 1 days, 8 hrs, 34 mins  |
|  48 | [amica](https://github.com/semperai/amica)  | Amica is an open source interface for interactive communication with 3D characters with voice synthesis and speech recognition.  | 442  | 67  | 46  |  13 | 4  | MIT License  | 6 days, 1 hrs, 6 mins  |
|  49 | [catai](https://github.com/withcatai/catai)  | UI for 🦙model . Run AI assistant locally ✨  | 395  | 26  | 1  |  4 | 22  | MIT License  | 53 days, 23 hrs, 27 mins |
|  50 | [FreeChat](https://github.com/psugihara/FreeChat)  | llama.cpp based AI chat app for macOS  | 328  | 24  | 18  |  4 | 0  | MIT License  | 4 days, 2 hrs, 39 mins  |
|  51 | [exui](https://github.com/turboderp/exui)  | Web UI for ExLlamaV2  | 302  | 23  | 16  |  7 | 0  | MIT License  | 0 days, 10 hrs, 37 mins  |
|  52 | [ava](https://github.com/cztomsik/ava)  | All-in-one desktop app for running LLMs locally.  | 272  | 11  | 9  |  2 | 0  | Other  | 0 days, 8 hrs, 5 mins  |
|  53 | [tenere](https://github.com/pythops/tenere)  | 🔥 TUI interface for LLMs written in Rust  | 200  | 7  | 1  |  5 | 12  | GNU General Public License v3.0  | 0 days, 23 hrs, 1 mins  |
|  54 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Local ML voice chat using high-end models.  | 102  | 6  | 0  |  1 | 0  | MIT License  | 8 days, 18 hrs, 56 mins  |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
