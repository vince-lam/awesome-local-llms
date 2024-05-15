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

*Last Updated: 15/05/2024*

|  # | Repo  | About  | Stars  | Forks  | Issues  |  Contributors | Releases  | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [transformers](https://github.com/huggingface/transformers)  | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX.  | 126,055 | 24,968  | 1,096  |  433 | 148  | Apache License 2.0  | 0 days, 8 hrs, 6 mins  |
|  2 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS). 一键拥有你自己的跨平台 ChatGPT/Gemini 应用。  | 69,372  | 55,841  | 276  |  179 | 60  | MIT License  | 0 days, 10 hrs, 13 mins  |
|  3 | [ollama](https://github.com/ollama/ollama)  | Get up and running with Llama 3, Mistral, Gemma, and other large language models.  | 66,609  | 4,845  | 861  |  220 | 60  | MIT License  | 0 days, 13 hrs, 24 mins  |
|  4 | [gpt4all](https://github.com/nomic-ai/gpt4all)  | gpt4all: run open-source LLMs anywhere  | 65,076  | 7,195  | 415  |  97 | 14  | MIT License  | 0 days, 16 hrs, 22 mins  |
|  5 | [gpt_academic](https://github.com/binary-husky/gpt_academic)  | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。  | 58,221  | 7,326  | 233  |  81 | 29  | GNU General Public License v3.0  | 1 days, 4 hrs, 58 mins  |
|  6 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | LLM inference in C/C++  | 58,200  | 8,252  | 566  |  476 | 1,798  | MIT License  | 0 days, 8 hrs, 27 mins  |
|  7 | [gpt4free](https://github.com/xtekky/gpt4free)  | The official gpt4free repository, various collection of powerful language models  | 57,953  | 13,075  | 40  |  199 | 131  | GNU General Public License v3.0  | 0 days, 13 hrs, 14 mins  |
|  8 | [privateGPT](https://github.com/imartinez/privateGPT)  | Interact with your documents using the power of GPT, 100% privately, no data leaks  | 52,154  | 6,971  | 242  |  74 | 7  | Apache License 2.0  | 4 days, 5 hrs, 20 mins  |
|  9 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | A Gradio web UI for Large Language Models. Supports transformers, GPTQ, AWQ, EXL2, llama.cpp (GGUF), Llama models.  | 36,938  | 4,926  | 218  |  305 | 41  | GNU Affero General Public License v3.0  | 1 days, 1 hrs, 6 mins  |
|  10 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | 🤯 Lobe Chat - an open-source, modern-design LLMs/AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Ollama / Bedrock / Azure / Mistral / Perplexity ), Multi-Modals (Vision/TTS) and plugin system. One-click FREE deployment of your private ChatGPT chat application.  | 30,696  | 7,169  | 323  |  108 | 627  | MIT License  | 0 days, 8 hrs, 13 mins  |
|  11 | [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui)  | AI chat for every model.  | 26,518  | 7,297  | 116  |  43 | 0  | MIT License  | 0 days, 21 hrs, 29 mins  |
|  12 | [open-webui](https://github.com/open-webui/open-webui)  | User-friendly WebUI for LLMs (Formerly Ollama WebUI)  | 21,507  | 2,221  | 153  |  114 | 23  | MIT License  | 0 days, 13 hrs, 5 mins  |
|  13 | [LocalAI](https://github.com/mudler/LocalAI)  | :robot: The free, Open Source OpenAI alternative. Self-hosted, community-driven and local-first. Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. It allows to generate Text, Audio, Video, Images. Also with voice cloning capabilities. | 20,320  | 1,526  | 280  |  90 | 47  | MIT License  | 0 days, 10 hrs, 50 mins  |
|  14 | [vllm](https://github.com/vllm-project/vllm)  | A high-throughput and memory-efficient inference and serving engine for LLMs  | 19,483  | 2,611  | 1,047  |  312 | 25  | Apache License 2.0  | 0 days, 8 hrs, 0 mins  |
|  15 | [localGPT](https://github.com/PromtEngineer/localGPT)  | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private.  | 19,301  | 2,143  | 459  |  42 | 0  | Apache License 2.0  | 11 days, 15 hrs, 1 mins  |
|  16 | [chatbox](https://github.com/Bin-Huang/chatbox)  | User-friendly Desktop App for LLMs (GPT, Claude, Ollama...)  | 18,830  | 1,924  | 251  |  28 | 61  | GNU General Public License v3.0  | 1 days, 1 hrs, 14 mins  |
|  17 | [jan](https://github.com/janhq/jan)  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer. Multiple engine support (llama.cpp, TensorRT-LLM)  | 18,348  | 1,055  | 204  |  45 | 21  | GNU Affero General Public License v3.0  | 0 days, 9 hrs, 29 mins  |
|  18 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Enable everyone to develop, optimize and deploy AI models natively on everyone's devices.  | 17,177  | 1,334  | 133  |  109 | 1  | Apache License 2.0  | 0 days, 8 hrs, 8 mins  |
|  19 | [llamafile](https://github.com/Mozilla-Ocho/llamafile)  | Distribute and run LLMs with a single file.  | 15,369  | 767  | 90  |  36 | 19  | Other  | 1 days, 8 hrs, 28 mins  |
|  20 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  | 14,820  | 2,242  | 115  |  48 | 21  | GNU General Public License v3.0  | 0 days, 9 hrs, 56 mins  |
|  21 | [anything-llm](https://github.com/Mintplex-Labs/anything-llm)  | The all-in-one Desktop & Docker AI application with full RAG and AI Agent capabilities.  | 14,081  | 1,471  | 127  |  41 | 0  | MIT License  | 0 days, 13 hrs, 27 mins  |
|  22 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Enhanced ChatGPT Clone: Features OpenAI, Assistants API, Azure, Groq, GPT-4 Vision, Mistral, Bing, Anthropic, OpenRouter, Vertex AI, Gemini, AI model switching, message search, langchain, DALL-E-3, ChatGPT Plugins, OpenAI Functions, Secure Multi-User System, Presets, completely open-source for self-hosting. More features in development  | 11,601  | 2,079  | 83  |  119 | 40  | MIT License  | 0 days, 8 hrs, 18 mins  |
|  23 | [h2ogpt](https://github.com/h2oai/h2ogpt)  | Private chat with local GPT with document, images, video, etc. 100% private, Apache 2.0. Supports oLLaMa, Mixtral, llama.cpp, and more. Demo: https://gpt.h2o.ai/ https://codellama.h2o.ai/  | 10,675  | 1,181  | 273  |  67 | 129  | Apache License 2.0  | 0 days, 15 hrs, 31 mins  |
|  24 | [web-llm](https://github.com/mlc-ai/web-llm)  | Bringing large-language models and chat to web browsers. Everything runs inside the browser with no server support.  | 9,783  | 592  | 99  |  30 | 1  | Apache License 2.0  | 0 days, 11 hrs, 1 mins  |
|  25 | [chathub](https://github.com/chathub-dev/chathub)  | All-in-one chatbot client  | 9,535  | 958  | 297  |  12 | 0  | GNU General Public License v3.0  | 46 days, 4 hrs, 17 mins  |
|  26 | [FlexGen](https://github.com/FMInference/FlexGen)  | Running large language models on a single GPU for throughput-oriented scenarios.  | 9,025  | 526  | 56  |  18 | 0  | Apache License 2.0  | 25 days, 18 hrs, 26 mins |
|  27 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Run any open-source LLMs, such as Llama 2, Mistral, as OpenAI compatible API endpoint in the cloud.  | 8,924  | 566  | 93  |  25 | 110  | Apache License 2.0  | 1 days, 7 hrs, 15 mins  |
|  28 | [text-generation-inference](https://github.com/huggingface/text-generation-inference) | Large Language Model Text Generation Inference  | 8,016  | 877  | 142  |  82 | 41  | Apache License 2.0  | 0 days, 9 hrs, 17 mins  |
|  29 | [server](https://github.com/triton-inference-server/server)  | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  | 7,427  | 1,383  | 462  |  112 | 66  | BSD 3-Clause "New" or "Revised" License | 0 days, 12 hrs, 45 mins  |
|  30 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines.  | 6,754  | 704  | 642  |  10 | 5  | Apache License 2.0  | 1 days, 5 hrs, 8 mins  |
|  31 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Python bindings for llama.cpp  | 6,677  | 789  | 358  |  137 | 192  | MIT License  | 0 days, 20 hrs, 50 mins  |
|  32 | [chat-ui](https://github.com/huggingface/chat-ui)  | Open source codebase powering the HuggingChat app  | 6,354  | 870  | 202  |  73 | 10  | Apache License 2.0  | 0 days, 18 hrs, 15 mins  |
|  33 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | LLM Frontend for Power Users.  | 6,127  | 1,872  | 334  |  105 | 77  | GNU Affero General Public License v3.0  | 0 days, 15 hrs, 18 mins  |
|  34 | [openplayground](https://github.com/nat/openplayground)  | An LLM playground you can run on your laptop  | 6,101  | 470  | 83  |  16 | 0  | MIT License  | 8 days, 13 hrs, 42 mins  |
|  35 | [big-agi](https://github.com/enricoros/big-agi)  | Generative AI suite powered by state-of-the-art models and providing advanced AI/AGI functions. It features AI personas, AGI functions, multi-model chats, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy on-prem or in the cloud.  | 4,400  | 1,001  | 138  |  37 | 16  | MIT License  | 0 days, 15 hrs, 39 mins  |
|  36 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | A simple one-file way to run various GGML and GGUF models with KoboldAI's UI  | 3,951  | 285  | 188  |  473 | 77  | GNU Affero General Public License v3.0  | 0 days, 22 hrs, 51 mins  |
|  37 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Lord of Large Language Models Web User Interface  | 3,879  | 490  | 136  |  38 | 20  | Apache License 2.0  | 0 days, 15 hrs, 10 mins  |
|  38 | [llm](https://github.com/simonw/llm)  | Access large language models from the command-line  | 3,054  | 147  | 174  |  19 | 25  | Apache License 2.0  | 0 days, 16 hrs, 10 mins  |
|  39 | [exllamav2](https://github.com/turboderp/exllamav2)  | A fast inference library for running LLMs locally on modern consumer-class GPUs  | 3,010  | 221  | 99  |  34 | 20  | MIT License  | 0 days, 17 hrs, 20 mins  |
|  40 | [inference](https://github.com/xorbitsai/inference)  | Replace OpenAI GPT with another LLM in your app by changing a single line of code. Xinference gives you the freedom to use any LLM you need. With Xinference, you're empowered to run inference with any open-source language models, speech recognition models, and multimodal models, whether in the cloud, on-premises, or even on your laptop.  | 2,789  | 229  | 291  |  49 | 59  | Apache License 2.0  | 0 days, 10 hrs, 48 mins  |
|  41 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  | 2,518  | 231  | 117  |  53 | 27  | Apache License 2.0  | 0 days, 12 hrs, 34 mins  |
|  42 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | A C#/.NET library to run LLM models (🦙LLaMA/LLaVA) on your local device efficiently.  | 2,015  | 271  | 109  |  43 | 16  | MIT License  | 0 days, 15 hrs, 34 mins  |
|  43 | [nitro](https://github.com/janhq/nitro)  | Drop-in, local AI alternative to the OpenAI stack. Multi-engine (llama.cpp, TensorRT-LLM). Powers 👋 Jan  | 1,635  | 80  | 63  |  23 | 75  | GNU Affero General Public License v3.0  | 0 days, 8 hrs, 53 mins  |
|  44 | [chatbot-ollama](https://github.com/ivanfioravanti/chatbot-ollama)  | Chatbot Ollama is an open source chat UI for Ollama.  | 1,181  | 185  | 18  |  6 | 1  | Other  | 25 days, 3 hrs, 55 mins  |
|  45 | [LLMFarm](https://github.com/guinmoon/LLMFarm)  | llama and other  large language models on iOS and MacOS offline using GGML library.  | 943  | 55  | 6  |  1 | 27  | MIT License  | 0 days, 10 hrs, 22 mins  |
|  46 | [maid](https://github.com/Mobile-Artificial-Intelligence/maid)  | Maid is a cross-platform Flutter app for interfacing with GGUF / llama.cpp models locally, and with Ollama and OpenAI models remotely.  | 817  | 85  | 4  |  15 | 28  | MIT License  | 0 days, 9 hrs, 34 mins  |
|  47 | [oterm](https://github.com/ggozad/oterm)  | a text-based terminal client for Ollama  | 622  | 35  | 6  |  9 | 17  | MIT License  | 4 days, 5 hrs, 5 mins  |
|  48 | [amica](https://github.com/semperai/amica)  | Amica is an open source interface for interactive communication with 3D characters with voice synthesis and speech recognition.  | 533  | 80  | 45  |  16 | 4  | MIT License  | 3 days, 3 hrs, 59 mins  |
|  49 | [catai](https://github.com/withcatai/catai)  | Run AI ✨ assistant locally! with simple API for Node.js 🚀  | 412  | 27  | 1  |  4 | 24  | MIT License  | 2 days, 1 hrs, 55 mins  |
|  50 | [FreeChat](https://github.com/psugihara/FreeChat)  | llama.cpp based AI chat app for macOS  | 369  | 29  | 19  |  4 | 0  | MIT License  | 19 days, 14 hrs, 59 mins |
|  51 | [exui](https://github.com/turboderp/exui)  | Web UI for ExLlamaV2  | 356  | 31  | 24  |  7 | 0  | MIT License  | 3 days, 15 hrs, 26 mins  |
|  52 | [ava](https://github.com/cztomsik/ava)  | All-in-one desktop app for running LLMs locally.  | 329  | 14  | 8  |  3 | 0  | Other  | 6 days, 17 hrs, 0 mins  |
|  53 | [LocalAIVoiceChat](https://github.com/KoljaB/LocalAIVoiceChat)  | Local AI talk with a custom voice based on Zephyr 7B model. Uses RealtimeSTT with faster_whisper for transcription and RealtimeTTS with Coqui XTTS for synthesis.  | 318  | 30  | 6  |  1 | 1  | Other  | 24 days, 5 hrs, 30 mins  |
|  54 | [tenere](https://github.com/pythops/tenere)  | 🔥 TUI interface for LLMs written in Rust  | 236  | 8  | 1  |  5 | 12  | GNU General Public License v3.0  | 56 days, 18 hrs, 5 mins  |
|  55 | [ChatterUI](https://github.com/Vali-98/ChatterUI)  | Simple frontend for LLMs built in react-native.  | 135  | 7  | 3  |  2 | 19  | GNU Affero General Public License v3.0  | 0 days, 10 hrs, 49 mins  |
|  56 | [mikupad](https://github.com/lmg-anon/mikupad)  | LLM Frontend in a single html file  | 128  | 18  | 17  |  9 | 0  | Creative Commons Zero v1.0 Universal  | 8 days, 3 hrs, 11 mins  |
|  57 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Local ML voice chat using high-end models.  | 111  | 6  | 0  |  1 | 0  | MIT License  | 10 days, 1 hrs, 46 mins  |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
