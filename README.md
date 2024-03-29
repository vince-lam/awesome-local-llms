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

*Last Updated: 29/03/2024*

|  # | Repo  | About  | Stars  | Forks  | Issues  |  Contributors | Releases  | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [transformers](https://github.com/huggingface/transformers)  | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX.  | 123,278 | 24,444  | 1,047  |  433 | 144  | Apache License 2.0  | 0 days, 8 hrs, 37 mins  |
|  2 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS). 一键拥有你自己的跨平台 ChatGPT/Gemini 应用。  | 65,910  | 53,879  | 223  |  174 | 58  | MIT License  | 0 days, 13 hrs, 29 mins  |
|  3 | [gpt4all](https://github.com/nomic-ai/gpt4all)  | gpt4all: run open-source LLMs anywhere  | 63,030  | 6,919  | 374  |  94 | 12  | MIT License  | 0 days, 19 hrs, 48 mins  |
|  4 | [gpt4free](https://github.com/xtekky/gpt4free)  | The official gpt4free repository. Various collection of powerful language models  | 55,252  | 12,613  | 96  |  185 | 101  | GNU General Public License v3.0  | 1 days, 0 hrs, 24 mins  |
|  5 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | LLM inference in C/C++  | 53,882  | 7,598  | 1,309  |  477 | 1,636  | MIT License  | 0 days, 8 hrs, 6 mins  |
|  6 | [gpt_academic](https://github.com/binary-husky/gpt_academic)  | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。  | 53,585  | 6,775  | 225  |  75 | 27  | GNU General Public License v3.0  | 4 days, 14 hrs, 49 mins  |
|  7 | [ollama](https://github.com/ollama/ollama)  | Get up and running with Llama 2, Mistral, Gemma, and other large language models.  | 51,314  | 3,513  | 678  |  164 | 52  | MIT License  | 0 days, 14 hrs, 42 mins  |
|  8 | [privateGPT](https://github.com/imartinez/privateGPT)  | Interact with your documents using the power of GPT, 100% privately, no data leaks  | 50,636  | 6,717  | 188  |  65 | 6  | Apache License 2.0  | 0 days, 17 hrs, 18 mins  |
|  9 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | A Gradio web UI for Large Language Models. Supports transformers, GPTQ, AWQ, EXL2, llama.cpp (GGUF), Llama models.  | 34,956  | 4,657  | 241  |  299 | 36  | GNU Affero General Public License v3.0  | 0 days, 12 hrs, 59 mins  |
|  10 | [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui)  | AI chat for every model.  | 25,628  | 6,993  | 71  |  38 | 0  | MIT License  | 0 days, 20 hrs, 45 mins  |
|  11 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | 🤯 Lobe Chat - an open-source, modern-design LLMs/AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Perplexity / Bedrock / Azure / Mistral / Ollama ), Multi-Modals (Vision/TTS) and plugin system. One-click FREE deployment of your private ChatGPT chat application.  | 25,556  | 5,578  | 270  |  83 | 493  | MIT License  | 0 days, 8 hrs, 10 mins  |
|  12 | [localGPT](https://github.com/PromtEngineer/localGPT)  | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private.  | 18,917  | 2,088  | 448  |  42 | 0  | Apache License 2.0  | 3 days, 4 hrs, 56 mins  |
|  13 | [LocalAI](https://github.com/mudler/LocalAI)  | :robot: The free, Open Source OpenAI alternative. Self-hosted, community-driven and local-first. Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. It allows to generate Text, Audio, Video, Images. Also with voice cloning capabilities. | 18,271  | 1,332  | 244  |  79 | 40  | MIT License  | 0 days, 16 hrs, 43 mins  |
|  14 | [chatbox](https://github.com/Bin-Huang/chatbox)  | Chatbox is a desktop client for ChatGPT, Claude and other LLMs, available on Windows, Mac, Linux  | 17,969  | 1,845  | 221  |  28 | 55  | MIT License  | 3 days, 2 hrs, 23 mins  |
|  15 | [vllm](https://github.com/vllm-project/vllm)  | A high-throughput and memory-efficient inference and serving engine for LLMs  | 16,802  | 2,143  | 868  |  250 | 21  | Apache License 2.0  | 0 days, 8 hrs, 21 mins  |
|  16 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Enable everyone to develop, optimize and deploy AI models natively on everyone's devices.  | 16,404  | 1,242  | 225  |  96 | 1  | Apache License 2.0  | 0 days, 8 hrs, 53 mins  |
|  17 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  | 14,563  | 2,212  | 107  |  45 | 20  | GNU General Public License v3.0  | 1 days, 23 hrs, 7 mins  |
|  18 | [jan](https://github.com/janhq/jan)  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer  | 14,054  | 736  | 154  |  39 | 18  | GNU Affero General Public License v3.0  | 0 days, 8 hrs, 3 mins  |
|  19 | [open-webui](https://github.com/open-webui/open-webui)  | User-friendly WebUI for LLMs (Formerly Ollama WebUI)  | 11,102  | 1,067  | 108  |  77 | 14  | MIT License  | 0 days, 12 hrs, 21 mins  |
|  20 | [llamafile](https://github.com/Mozilla-Ocho/llamafile)  | Distribute and run LLMs with a single file.  | 10,806  | 517  | 53  |  27 | 10  | Other  | 0 days, 17 hrs, 47 mins  |
|  21 | [h2ogpt](https://github.com/h2oai/h2ogpt)  | Private chat with local GPT with document, images, video, etc. 100% private, Apache 2.0. Supports oLLaMa, Mixtral, llama.cpp, and more. Demo: <https://gpt.h2o.ai/> <https://codellama.h2o.ai/>  | 10,164  | 1,131  | 228  |  67 | 129  | Apache License 2.0  | 0 days, 8 hrs, 25 mins  |
|  22 | [anything-llm](https://github.com/Mintplex-Labs/anything-llm)  | A multi-user ChatGPT for any LLMs and vector database. Unlimited documents, messages, and storage in one privacy-focused app. Now available as a desktop application with a built-in LLM!  | 9,815  | 1,055  | 83  |  32 | 0  | MIT License  | 0 days, 16 hrs, 46 mins  |
|  23 | [chathub](https://github.com/chathub-dev/chathub)  | All-in-one chatbot client  | 9,416  | 934  | 269  |  12 | 0  | GNU General Public License v3.0  | 25 days, 10 hrs, 20 mins |
|  24 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Enhanced ChatGPT Clone: Features OpenAI, Assistants API, Azure, Groq, GPT-4 Vision, Mistral, Bing, Anthropic, OpenRouter, Google Gemini, AI model switching, message search, langchain, DALL-E-3, ChatGPT Plugins, OpenAI Functions, Secure Multi-User System, Presets, completely open-source for self-hosting. More features in development  | 9,126  | 1,640  | 68  |  90 | 36  | MIT License  | 0 days, 14 hrs, 29 mins  |
|  25 | [FlexGen](https://github.com/FMInference/FlexGen)  | Running large language models on a single GPU for throughput-oriented scenarios.  | 8,948  | 513  | 54  |  18 | 0  | Apache License 2.0  | 0 days, 13 hrs, 23 mins  |
|  26 | [web-llm](https://github.com/mlc-ai/web-llm)  | Bringing large-language models and chat to web browsers. Everything runs inside the browser with no server support.  | 8,869  | 531  | 79  |  28 | 1  | Apache License 2.0  | 2 days, 9 hrs, 43 mins  |
|  27 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Operating LLMs in production  | 8,517  | 529  | 91  |  24 | 110  | Apache License 2.0  | 3 days, 12 hrs, 38 mins  |
|  28 | [text-generation-inference](https://github.com/huggingface/text-generation-inference) | Large Language Model Text Generation Inference  | 7,375  | 794  | 150  |  74 | 37  | Other  | 1 days, 0 hrs, 41 mins  |
|  29 | [server](https://github.com/triton-inference-server/server)  | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  | 7,178  | 1,356  | 413  |  111 | 65  | BSD 3-Clause "New" or "Revised" License | 1 days, 15 hrs, 20 mins  |
|  30 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines.  | 6,140  | 614  | 543  |  10 | 4  | Apache License 2.0  | 0 days, 9 hrs, 9 mins  |
|  31 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Python bindings for llama.cpp  | 6,065  | 715  | 334  |  119 | 106  | MIT License  | 0 days, 10 hrs, 23 mins  |
|  32 | [openplayground](https://github.com/nat/openplayground)  | An LLM playground you can run on your laptop  | 6,047  | 461  | 78  |  16 | 0  | MIT License  | 56 days, 11 hrs, 4 mins  |
|  33 | [chat-ui](https://github.com/huggingface/chat-ui)  | Open source codebase powering the HuggingChat app  | 5,683  | 752  | 183  |  59 | 5  | Apache License 2.0  | 0 days, 8 hrs, 15 mins  |
|  34 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | LLM Frontend for Power Users.  | 5,485  | 1,712  | 286  |  94 | 74  | GNU Affero General Public License v3.0  | 0 days, 11 hrs, 45 mins  |
|  35 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Lord of Large Language Models Web User Interface  | 3,644  | 464  | 129  |  36 | 18  | Apache License 2.0  | 0 days, 16 hrs, 0 mins  |
|  36 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | A simple one-file way to run various GGML and GGUF models with KoboldAI's UI  | 3,501  | 259  | 159  |  475 | 72  | GNU Affero General Public License v3.0  | 9 days, 7 hrs, 40 mins  |
|  37 | [big-agi](https://github.com/enricoros/big-agi)  | Generative AI suite powered by state-of-the-art LLMs. Bundling AI personas, AGI functions, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy on-prem or in the cloud.  | 3,339  | 809  | 121  |  32 | 13  | MIT License  | 0 days, 10 hrs, 21 mins  |
|  38 | [exllamav2](https://github.com/turboderp/exllamav2)  | A fast inference library for running LLMs locally on modern consumer-class GPUs  | 2,736  | 199  | 84  |  31 | 15  | MIT License  | 2 days, 13 hrs, 17 mins  |
|  39 | [llm](https://github.com/simonw/llm)  | Access large language models from the command-line  | 2,713  | 122  | 146  |  19 | 24  | Apache License 2.0  | 2 days, 19 hrs, 44 mins  |
|  40 | [inference](https://github.com/xorbitsai/inference)  | Replace OpenAI GPT with another LLM in your app by changing a single line of code. Xinference gives you the freedom to use any LLM you need. With Xinference, you're empowered to run inference with any open-source language models, speech recognition models, and multimodal models, whether in the cloud, on-premises, or even on your laptop.  | 2,136  | 170  | 195  |  38 | 54  | Apache License 2.0  | 0 days, 8 hrs, 2 mins  |
|  41 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  | 2,090  | 184  | 100  |  43 | 24  | Apache License 2.0  | 0 days, 8 hrs, 12 mins  |
|  42 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | Run local LLaMA/GPT model easily and fast in C#!🤗 It's also easy to integrate LLamaSharp with semantic-kernel, unity, WPF and WebApp.  | 1,749  | 230  | 79  |  37 | 14  | MIT License  | 0 days, 20 hrs, 12 mins  |
|  43 | [nitro](https://github.com/janhq/nitro)  | An inference server on top of llama.cpp. OpenAI-compatible API, queue, & scaling. Embed a prod-ready, local inference engine in your apps. Powers Jan  | 1,452  | 69  | 31  |  19 | 65  | GNU Affero General Public License v3.0  | 3 days, 6 hrs, 12 mins  |
|  44 | [chatbot-ollama](https://github.com/ivanfioravanti/chatbot-ollama)  | Chatbot Ollama is an open source chat UI for Ollama.  | 939  | 142  | 17  |  6 | 1  | Other  | 35 days, 16 hrs, 21 mins |
|  45 | [LLMFarm](https://github.com/guinmoon/LLMFarm)  | llama and other  large language models on iOS and MacOS offline using GGML library.  | 789  | 42  | 11  |  1 | 24  | MIT License  | 8 days, 21 hrs, 57 mins  |
|  46 | [maid](https://github.com/Mobile-Artificial-Intelligence/maid)  | Maid is a cross-platform Flutter app for interfacing with GGUF / llama.cpp models locally, and with Ollama and OpenAI models remotely.  | 529  | 61  | 3  |  12 | 24  | MIT License  | 1 days, 17 hrs, 10 mins  |
|  47 | [oterm](https://github.com/ggozad/oterm)  | a text-based terminal client for Ollama  | 484  | 25  | 5  |  6 | 13  | MIT License  | 1 days, 18 hrs, 2 mins  |
|  48 | [amica](https://github.com/semperai/amica)  | Amica is an open source interface for interactive communication with 3D characters with voice synthesis and speech recognition.  | 453  | 68  | 47  |  13 | 4  | MIT License  | 2 days, 17 hrs, 37 mins  |
|  49 | [FreeChat](https://github.com/psugihara/FreeChat)  | llama.cpp based AI chat app for macOS  | 340  | 24  | 18  |  4 | 0  | MIT License  | 3 days, 20 hrs, 55 mins  |
|  50 | [exui](https://github.com/turboderp/exui)  | Web UI for ExLlamaV2  | 308  | 25  | 19  |  7 | 0  | MIT License  | 2 days, 9 hrs, 59 mins  |
|  51 | [ava](https://github.com/cztomsik/ava)  | All-in-one desktop app for running LLMs locally.  | 283  | 11  | 9  |  2 | 0  | Other  | 0 days, 22 hrs, 26 mins  |
|  52 | [tenere](https://github.com/pythops/tenere)  | 🔥 TUI interface for LLMs written in Rust  | 212  | 7  | 1  |  5 | 12  | GNU General Public License v3.0  | 9 days, 20 hrs, 46 mins  |
|  53 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Local ML voice chat using high-end models.  | 102  | 6  | 0  |  1 | 0  | MIT License  | 17 days, 16 hrs, 41 mins |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
