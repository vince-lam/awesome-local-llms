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

*Last Updated: 03/05/2024*

|  # | Repo  | About  | Stars  | Forks  | Issues  |  Contributors | Releases  | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [transformers](https://github.com/huggingface/transformers)  | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX.  | 125,386 | 24,853  | 1,089  |  433 | 147  | Apache License 2.0  | 0 days, 8 hrs, 11 mins  |
|  2 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS). 一键拥有你自己的跨平台 ChatGPT/Gemini 应用。  | 68,373  | 55,353  | 242  |  177 | 59  | MIT License  | 0 days, 15 hrs, 21 mins  |
|  3 | [gpt4all](https://github.com/nomic-ai/gpt4all)  | gpt4all: run open-source LLMs anywhere  | 64,787  | 7,151  | 409  |  97 | 13  | MIT License  | 0 days, 21 hrs, 40 mins  |
|  4 | [ollama](https://github.com/ollama/ollama)  | Get up and running with Llama 3, Mistral, Gemma, and other large language models.  | 63,238  | 4,533  | 923  |  194 | 55  | MIT License  | 0 days, 8 hrs, 10 mins  |
|  5 | [gpt4free](https://github.com/xtekky/gpt4free)  | The official gpt4free repository, various collection of powerful language models  | 57,595  | 12,957  | 46  |  196 | 127  | GNU General Public License v3.0  | 0 days, 23 hrs, 46 mins  |
|  6 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | LLM inference in C/C++  | 57,395  | 8,128  | 573  |  477 | 1,737  | MIT License  | 0 days, 8 hrs, 17 mins  |
|  7 | [gpt_academic](https://github.com/binary-husky/gpt_academic)  | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。  | 57,022  | 7,210  | 256  |  80 | 28  | GNU General Public License v3.0  | 2 days, 11 hrs, 47 mins  |
|  8 | [privateGPT](https://github.com/imartinez/privateGPT)  | Interact with your documents using the power of GPT, 100% privately, no data leaks  | 51,930  | 6,935  | 230  |  72 | 7  | Apache License 2.0  | 1 days, 3 hrs, 42 mins  |
|  9 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | A Gradio web UI for Large Language Models. Supports transformers, GPTQ, AWQ, EXL2, llama.cpp (GGUF), Llama models.  | 36,524  | 4,871  | 233  |  305 | 41  | GNU Affero General Public License v3.0  | 0 days, 10 hrs, 6 mins  |
|  10 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | 🤯 Lobe Chat - an open-source, modern-design LLMs/AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Ollama / Bedrock / Azure / Mistral / Perplexity ), Multi-Modals (Vision/TTS) and plugin system. One-click FREE deployment of your private ChatGPT chat application.  | 29,913  | 6,846  | 306  |  103 | 586  | MIT License  | 0 days, 8 hrs, 15 mins  |
|  11 | [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui)  | AI chat for every model.  | 26,300  | 7,238  | 107  |  42 | 0  | MIT License  | 2 days, 1 hrs, 57 mins  |
|  12 | [LocalAI](https://github.com/mudler/LocalAI)  | :robot: The free, Open Source OpenAI alternative. Self-hosted, community-driven and local-first. Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. It allows to generate Text, Audio, Video, Images. Also with voice cloning capabilities. | 19,889  | 1,494  | 279  |  87 | 46  | MIT License  | 0 days, 14 hrs, 0 mins  |
|  13 | [localGPT](https://github.com/PromtEngineer/localGPT)  | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private.  | 19,178  | 2,127  | 456  |  42 | 0  | Apache License 2.0  | 10 days, 5 hrs, 38 mins  |
|  14 | [vllm](https://github.com/vllm-project/vllm)  | A high-throughput and memory-efficient inference and serving engine for LLMs  | 18,847  | 2,499  | 957  |  304 | 24  | Apache License 2.0  | 0 days, 10 hrs, 31 mins  |
|  15 | [chatbox](https://github.com/Bin-Huang/chatbox)  | Chatbox is a desktop client for ChatGPT, Claude and other LLMs, available on Windows, Mac, Linux  | 18,603  | 1,904  | 243  |  28 | 58  | GNU General Public License v3.0  | 15 days, 13 hrs, 30 mins |
|  16 | [open-webui](https://github.com/open-webui/open-webui)  | User-friendly WebUI for LLMs (Formerly Ollama WebUI)  | 17,936  | 1,809  | 120  |  109 | 22  | MIT License  | 0 days, 11 hrs, 46 mins  |
|  17 | [jan](https://github.com/janhq/jan)  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer. Multiple engine support (llama.cpp, TensorRT-LLM)  | 17,812  | 1,034  | 203  |  45 | 21  | GNU Affero General Public License v3.0  | 0 days, 8 hrs, 2 mins  |
|  18 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Enable everyone to develop, optimize and deploy AI models natively on everyone's devices.  | 17,032  | 1,316  | 227  |  109 | 1  | Apache License 2.0  | 0 days, 9 hrs, 2 mins  |
|  19 | [llamafile](https://github.com/Mozilla-Ocho/llamafile)  | Distribute and run LLMs with a single file.  | 14,945  | 738  | 85  |  33 | 17  | Other  | 0 days, 9 hrs, 9 mins  |
|  20 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  | 14,753  | 2,230  | 107  |  46 | 21  | GNU General Public License v3.0  | 10 days, 13 hrs, 18 mins |
|  21 | [anything-llm](https://github.com/Mintplex-Labs/anything-llm)  | The all-in-one Desktop & Docker AI application with full RAG and AI Agent capabilities.  | 12,516  | 1,336  | 107  |  36 | 0  | MIT License  | 0 days, 20 hrs, 20 mins  |
|  22 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Enhanced ChatGPT Clone: Features OpenAI, Assistants API, Azure, Groq, GPT-4 Vision, Mistral, Bing, Anthropic, OpenRouter, Vertex AI, Gemini, AI model switching, message search, langchain, DALL-E-3, ChatGPT Plugins, OpenAI Functions, Secure Multi-User System, Presets, completely open-source for self-hosting. More features in development  | 11,081  | 1,994  | 75  |  117 | 38  | MIT License  | 1 days, 1 hrs, 18 mins  |
|  23 | [h2ogpt](https://github.com/h2oai/h2ogpt)  | Private chat with local GPT with document, images, video, etc. 100% private, Apache 2.0. Supports oLLaMa, Mixtral, llama.cpp, and more. Demo: https://gpt.h2o.ai/ https://codellama.h2o.ai/  | 10,474  | 1,163  | 260  |  67 | 129  | Apache License 2.0  | 1 days, 9 hrs, 49 mins  |
|  24 | [chathub](https://github.com/chathub-dev/chathub)  | All-in-one chatbot client  | 9,515  | 954  | 290  |  12 | 0  | GNU General Public License v3.0  | 34 days, 12 hrs, 4 mins  |
|  25 | [web-llm](https://github.com/mlc-ai/web-llm)  | Bringing large-language models and chat to web browsers. Everything runs inside the browser with no server support.  | 9,139  | 557  | 93  |  28 | 1  | Apache License 2.0  | 8 days, 23 hrs, 1 mins  |
|  26 | [FlexGen](https://github.com/FMInference/FlexGen)  | Running large language models on a single GPU for throughput-oriented scenarios.  | 9,009  | 523  | 56  |  18 | 0  | Apache License 2.0  | 14 days, 2 hrs, 12 mins  |
|  27 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Run any open-source LLMs, such as Llama 2, Mistral, as OpenAI compatible API endpoint in the cloud.  | 8,828  | 556  | 92  |  25 | 110  | Apache License 2.0  | 3 days, 2 hrs, 39 mins  |
|  28 | [text-generation-inference](https://github.com/huggingface/text-generation-inference) | Large Language Model Text Generation Inference  | 7,930  | 860  | 136  |  80 | 41  | Apache License 2.0  | 0 days, 11 hrs, 30 mins  |
|  29 | [server](https://github.com/triton-inference-server/server)  | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  | 7,371  | 1,375  | 452  |  111 | 66  | BSD 3-Clause "New" or "Revised" License | 0 days, 17 hrs, 33 mins  |
|  30 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines.  | 6,639  | 684  | 599  |  10 | 5  | Apache License 2.0  | 0 days, 21 hrs, 9 mins  |
|  31 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Python bindings for llama.cpp  | 6,529  | 778  | 355  |  131 | 162  | MIT License  | 0 days, 16 hrs, 6 mins  |
|  32 | [chat-ui](https://github.com/huggingface/chat-ui)  | Open source codebase powering the HuggingChat app  | 6,255  | 845  | 193  |  68 | 9  | Apache License 2.0  | 0 days, 8 hrs, 0 mins  |
|  33 | [openplayground](https://github.com/nat/openplayground)  | An LLM playground you can run on your laptop  | 6,083  | 469  | 81  |  16 | 0  | MIT License  | 14 days, 17 hrs, 4 mins  |
|  34 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | LLM Frontend for Power Users.  | 5,979  | 1,842  | 312  |  105 | 77  | GNU Affero General Public License v3.0  | 0 days, 14 hrs, 8 mins  |
|  35 | [big-agi](https://github.com/enricoros/big-agi)  | Generative AI suite powered by state-of-the-art models and providing advanced AI/AGI functions. It features AI personas, AGI functions, multi-model chats, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy on-prem or in the cloud.  | 4,302  | 981  | 130  |  35 | 15  | MIT License  | 1 days, 14 hrs, 2 mins  |
|  36 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | A simple one-file way to run various GGML and GGUF models with KoboldAI's UI  | 3,840  | 277  | 180  |  474 | 76  | GNU Affero General Public License v3.0  | 0 days, 11 hrs, 28 mins  |
|  37 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Lord of Large Language Models Web User Interface  | 3,836  | 481  | 135  |  36 | 20  | Apache License 2.0  | 0 days, 8 hrs, 50 mins  |
|  38 | [llm](https://github.com/simonw/llm)  | Access large language models from the command-line  | 2,973  | 143  | 164  |  19 | 24  | Apache License 2.0  | 3 days, 23 hrs, 11 mins  |
|  39 | [exllamav2](https://github.com/turboderp/exllamav2)  | A fast inference library for running LLMs locally on modern consumer-class GPUs  | 2,949  | 215  | 89  |  33 | 19  | MIT License  | 1 days, 1 hrs, 48 mins  |
|  40 | [inference](https://github.com/xorbitsai/inference)  | Replace OpenAI GPT with another LLM in your app by changing a single line of code. Xinference gives you the freedom to use any LLM you need. With Xinference, you're empowered to run inference with any open-source language models, speech recognition models, and multimodal models, whether in the cloud, on-premises, or even on your laptop.  | 2,640  | 214  | 268  |  46 | 58  | Apache License 2.0  | 0 days, 10 hrs, 56 mins  |
|  41 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  | 2,389  | 213  | 110  |  49 | 26  | Apache License 2.0  | 1 days, 14 hrs, 16 mins  |
|  42 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | A C#/.NET library to run LLM models (🦙LLaMA/LLaVA) on your local device efficiently.  | 1,939  | 254  | 104  |  40 | 15  | MIT License  | 0 days, 16 hrs, 15 mins  |
|  43 | [nitro](https://github.com/janhq/nitro)  | Drop-in, local AI alternative to the OpenAI stack. Multi-engine (llama.cpp, TensorRT-LLM). Powers 👋 Jan  | 1,605  | 78  | 55  |  23 | 72  | GNU Affero General Public License v3.0  | 0 days, 14 hrs, 59 mins  |
|  44 | [chatbot-ollama](https://github.com/ivanfioravanti/chatbot-ollama)  | Chatbot Ollama is an open source chat UI for Ollama.  | 1,155  | 178  | 17  |  6 | 1  | Other  | 13 days, 11 hrs, 41 mins |
|  45 | [LLMFarm](https://github.com/guinmoon/LLMFarm)  | llama and other  large language models on iOS and MacOS offline using GGML library.  | 901  | 53  | 8  |  1 | 25  | MIT License  | 2 days, 3 hrs, 21 mins  |
|  46 | [maid](https://github.com/Mobile-Artificial-Intelligence/maid)  | Maid is a cross-platform Flutter app for interfacing with GGUF / llama.cpp models locally, and with Ollama and OpenAI models remotely.  | 744  | 76  | 8  |  13 | 27  | MIT License  | 0 days, 9 hrs, 22 mins  |
|  47 | [oterm](https://github.com/ggozad/oterm)  | a text-based terminal client for Ollama  | 584  | 33  | 5  |  8 | 17  | MIT License  | 0 days, 9 hrs, 4 mins  |
|  48 | [amica](https://github.com/semperai/amica)  | Amica is an open source interface for interactive communication with 3D characters with voice synthesis and speech recognition.  | 513  | 79  | 45  |  16 | 4  | MIT License  | 6 days, 16 hrs, 45 mins  |
|  49 | [FreeChat](https://github.com/psugihara/FreeChat)  | llama.cpp based AI chat app for macOS  | 363  | 28  | 19  |  4 | 0  | MIT License  | 7 days, 22 hrs, 46 mins  |
|  50 | [exui](https://github.com/turboderp/exui)  | Web UI for ExLlamaV2  | 345  | 31  | 24  |  7 | 0  | MIT License  | 5 days, 4 hrs, 5 mins  |
|  51 | [ava](https://github.com/cztomsik/ava)  | All-in-one desktop app for running LLMs locally.  | 311  | 14  | 11  |  2 | 0  | Other  | 2 days, 0 hrs, 12 mins  |
|  52 | [LocalAIVoiceChat](https://github.com/KoljaB/LocalAIVoiceChat)  | Local AI talk with a custom voice based on Zephyr 7B model. Uses RealtimeSTT with faster_whisper for transcription and RealtimeTTS with Coqui XTTS for synthesis.  | 303  | 25  | 6  |  1 | 1  | Other  | 12 days, 13 hrs, 17 mins |
|  53 | [tenere](https://github.com/pythops/tenere)  | 🔥 TUI interface for LLMs written in Rust  | 228  | 8  | 1  |  5 | 12  | GNU General Public License v3.0  | 45 days, 1 hrs, 52 mins  |
|  54 | [mikupad](https://github.com/lmg-anon/mikupad)  | LLM Frontend in a single html file  | 124  | 18  | 15  |  9 | 0  | Creative Commons Zero v1.0 Universal  | 1 days, 5 hrs, 6 mins  |
|  55 | [ChatterUI](https://github.com/Vali-98/ChatterUI)  | Simple frontend for LLMs built in react-native.  | 110  | 5  | 3  |  2 | 18  | GNU Affero General Public License v3.0  | 0 days, 11 hrs, 42 mins  |
|  56 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Local ML voice chat using high-end models.  | 109  | 6  | 0  |  1 | 0  | MIT License  | 12 days, 20 hrs, 11 mins |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
