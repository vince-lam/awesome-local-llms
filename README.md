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

*Last Updated: 26/05/2024*

|  # | Repo  | About  | Stars  | Forks  | Issues  |  Contributors | Releases  | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [transformers](https://github.com/huggingface/transformers)  | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX.  | 126,593 | 25,064  | 1,075  |  433 | 150  | Apache License 2.0  | 0 days, 11 hrs, 8 mins  |
|  2 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS). 一键拥有你自己的跨平台 ChatGPT/Gemini 应用。  | 70,523  | 56,465  | 305  |  182 | 60  | MIT License  | 1 days, 3 hrs, 22 mins  |
|  3 | [ollama](https://github.com/ollama/ollama)  | Get up and running with Llama 3, Mistral, Gemma, and other large language models.  | 69,122  | 5,053  | 900  |  224 | 61  | MIT License  | 0 days, 13 hrs, 5 mins  |
|  4 | [gpt4all](https://github.com/nomic-ai/gpt4all)  | gpt4all: run open-source LLMs anywhere  | 65,335  | 7,203  | 419  |  97 | 16  | MIT License  | 0 days, 15 hrs, 48 mins  |
|  5 | [gpt_academic](https://github.com/binary-husky/gpt_academic)  | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。  | 59,182  | 7,423  | 253  |  82 | 29  | GNU General Public License v3.0  | 2 days, 18 hrs, 6 mins  |
|  6 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | LLM inference in C/C++  | 58,885  | 8,365  | 565  |  474 | 1,875  | MIT License  | 0 days, 9 hrs, 41 mins  |
|  7 | [gpt4free](https://github.com/xtekky/gpt4free)  | The official gpt4free repository, various collection of powerful language models  | 58,329  | 13,091  | 35  |  202 | 139  | GNU General Public License v3.0  | 2 days, 15 hrs, 50 mins  |
|  8 | [privateGPT](https://github.com/imartinez/privateGPT)  | Interact with your documents using the power of GPT, 100% privately, no data leaks  | 52,344  | 7,018  | 252  |  75 | 7  | Apache License 2.0  | 8 days, 22 hrs, 21 mins  |
|  9 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | A Gradio web UI for Large Language Models. Supports transformers, GPTQ, AWQ, EXL2, llama.cpp (GGUF), Llama models.  | 37,256  | 4,960  | 199  |  305 | 41  | GNU Affero General Public License v3.0  | 0 days, 19 hrs, 9 mins  |
|  10 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | 🤯 Lobe Chat - an open-source, modern-design LLMs/AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Ollama / Bedrock / Azure / Mistral / Perplexity ), Multi-Modals (Vision/TTS) and plugin system. One-click FREE deployment of your private ChatGPT chat application.  | 31,638  | 7,481  | 350  |  109 | 658  | MIT License  | 0 days, 9 hrs, 41 mins  |
|  11 | [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui)  | AI chat for every model.  | 26,757  | 7,379  | 132  |  44 | 0  | MIT License  | 2 days, 14 hrs, 26 mins  |
|  12 | [open-webui](https://github.com/open-webui/open-webui)  | User-friendly WebUI for LLMs (Formerly Ollama WebUI)  | 23,859  | 2,504  | 143  |  130 | 24  | MIT License  | 0 days, 9 hrs, 54 mins  |
|  13 | [LocalAI](https://github.com/mudler/LocalAI)  | :robot: The free, Open Source OpenAI alternative. Self-hosted, community-driven and local-first. Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. It allows to generate Text, Audio, Video, Images. Also with voice cloning capabilities. | 20,642  | 1,562  | 294  |  93 | 48  | MIT License  | 0 days, 12 hrs, 13 mins  |
|  14 | [vllm](https://github.com/vllm-project/vllm)  | A high-throughput and memory-efficient inference and serving engine for LLMs  | 20,002  | 2,701  | 1,128  |  329 | 25  | Apache License 2.0  | 0 days, 8 hrs, 9 mins  |
|  15 | [localGPT](https://github.com/PromtEngineer/localGPT)  | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private.  | 19,355  | 2,144  | 465  |  42 | 0  | Apache License 2.0  | 0 days, 13 hrs, 55 mins  |
|  16 | [chatbox](https://github.com/Bin-Huang/chatbox)  | User-friendly Desktop Client App for AI Models/LLMs (GPT, Claude, Gemini, Ollama...)  | 19,044  | 1,944  | 271  |  28 | 62  | GNU General Public License v3.0  | 4 days, 21 hrs, 54 mins  |
|  17 | [jan](https://github.com/janhq/jan)  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer. Multiple engine support (llama.cpp, TensorRT-LLM)  | 18,805  | 1,081  | 199  |  46 | 22  | GNU Affero General Public License v3.0  | 0 days, 18 hrs, 41 mins  |
|  18 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Enable everyone to develop, optimize and deploy AI models natively on everyone's devices.  | 17,302  | 1,361  | 142  |  113 | 1  | Apache License 2.0  | 0 days, 9 hrs, 47 mins  |
|  19 | [llamafile](https://github.com/Mozilla-Ocho/llamafile)  | Distribute and run LLMs with a single file.  | 15,707  | 774  | 100  |  38 | 21  | Other  | 0 days, 9 hrs, 21 mins  |
|  20 | [anything-llm](https://github.com/Mintplex-Labs/anything-llm)  | The all-in-one Desktop & Docker AI application with full RAG and AI Agent capabilities.  | 14,900  | 1,542  | 144  |  44 | 0  | MIT License  | 1 days, 7 hrs, 9 mins  |
|  21 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  | 14,867  | 2,247  | 120  |  48 | 21  | GNU General Public License v3.0  | 5 days, 19 hrs, 34 mins  |
|  22 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Enhanced ChatGPT Clone: Features OpenAI, Assistants API, Azure, Groq, GPT-4 Vision, Mistral, Bing, Anthropic, OpenRouter, Vertex AI, Gemini, AI model switching, message search, langchain, DALL-E-3, ChatGPT Plugins, OpenAI Functions, Secure Multi-User System, Presets, completely open-source for self-hosting. More features in development  | 11,961  | 2,132  | 89  |  122 | 40  | MIT License  | 0 days, 13 hrs, 9 mins  |
|  23 | [h2ogpt](https://github.com/h2oai/h2ogpt)  | Private chat with local GPT with document, images, video, etc. 100% private, Apache 2.0. Supports oLLaMa, Mixtral, llama.cpp, and more. Demo: https://gpt.h2o.ai/ https://codellama.h2o.ai/  | 10,781  | 1,190  | 286  |  67 | 129  | Apache License 2.0  | 0 days, 8 hrs, 37 mins  |
|  24 | [web-llm](https://github.com/mlc-ai/web-llm)  | High-performance In-browser LLM Inference Engine  | 10,717  | 666  | 94  |  32 | 1  | Apache License 2.0  | 0 days, 10 hrs, 56 mins  |
|  25 | [chathub](https://github.com/chathub-dev/chathub)  | All-in-one chatbot client  | 9,611  | 962  | 308  |  12 | 0  | GNU General Public License v3.0  | 57 days, 0 hrs, 59 mins  |
|  26 | [FlexGen](https://github.com/FMInference/FlexGen)  | Running large language models on a single GPU for throughput-oriented scenarios.  | 9,038  | 527  | 56  |  18 | 0  | Apache License 2.0  | 36 days, 15 hrs, 8 mins  |
|  27 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Run any open-source LLMs, such as Llama 2, Mistral, as OpenAI compatible API endpoint in the cloud.  | 8,995  | 571  | 86  |  26 | 110  | Apache License 2.0  | 2 days, 17 hrs, 42 mins  |
|  28 | [text-generation-inference](https://github.com/huggingface/text-generation-inference) | Large Language Model Text Generation Inference  | 8,097  | 890  | 147  |  87 | 43  | Apache License 2.0  | 1 days, 1 hrs, 40 mins  |
|  29 | [server](https://github.com/triton-inference-server/server)  | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  | 7,498  | 1,396  | 482  |  112 | 67  | BSD 3-Clause "New" or "Revised" License | 1 days, 5 hrs, 8 mins  |
|  30 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines.  | 6,907  | 722  | 656  |  13 | 5  | Apache License 2.0  | 1 days, 0 hrs, 53 mins  |
|  31 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Python bindings for llama.cpp  | 6,779  | 806  | 379  |  138 | 204  | MIT License  | 0 days, 14 hrs, 49 mins  |
|  32 | [chat-ui](https://github.com/huggingface/chat-ui)  | Open source codebase powering the HuggingChat app  | 6,437  | 890  | 209  |  75 | 10  | Apache License 2.0  | 0 days, 17 hrs, 27 mins  |
|  33 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | LLM Frontend for Power Users.  | 6,301  | 1,911  | 307  |  117 | 79  | GNU Affero General Public License v3.0  | 0 days, 8 hrs, 48 mins  |
|  34 | [openplayground](https://github.com/nat/openplayground)  | An LLM playground you can run on your laptop  | 6,115  | 471  | 84  |  16 | 0  | MIT License  | 3 days, 10 hrs, 8 mins  |
|  35 | [big-agi](https://github.com/enricoros/big-agi)  | Generative AI suite powered by state-of-the-art models and providing advanced AI/AGI functions. It features AI personas, AGI functions, multi-model chats, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy on-prem or in the cloud.  | 4,492  | 1,024  | 148  |  37 | 16  | MIT License  | 0 days, 11 hrs, 47 mins  |
|  36 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | A simple one-file way to run various GGML and GGUF models with KoboldAI's UI  | 4,055  | 296  | 193  |  471 | 78  | GNU Affero General Public License v3.0  | 1 days, 7 hrs, 52 mins  |
|  37 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Lord of Large Language Models Web User Interface  | 3,924  | 496  | 139  |  38 | 21  | Apache License 2.0  | 0 days, 10 hrs, 43 mins  |
|  38 | [llm](https://github.com/simonw/llm)  | Access large language models from the command-line  | 3,178  | 155  | 180  |  19 | 25  | Apache License 2.0  | 2 days, 18 hrs, 31 mins  |
|  39 | [exllamav2](https://github.com/turboderp/exllamav2)  | A fast inference library for running LLMs locally on modern consumer-class GPUs  | 3,051  | 225  | 101  |  34 | 21  | MIT License  | 0 days, 10 hrs, 50 mins  |
|  40 | [inference](https://github.com/xorbitsai/inference)  | Replace OpenAI GPT with another LLM in your app by changing a single line of code. Xinference gives you the freedom to use any LLM you need. With Xinference, you're empowered to run inference with any open-source language models, speech recognition models, and multimodal models, whether in the cloud, on-premises, or even on your laptop.  | 2,902  | 237  | 301  |  49 | 62  | Apache License 2.0  | 1 days, 22 hrs, 49 mins  |
|  41 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  | 2,650  | 240  | 125  |  54 | 27  | Apache License 2.0  | 1 days, 20 hrs, 16 mins  |
|  42 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | A C#/.NET library to run LLM (🦙LLaMA/LLaVA) on your local device efficiently.  | 2,076  | 280  | 110  |  44 | 16  | MIT License  | 0 days, 16 hrs, 37 mins  |
|  43 | [nitro](https://github.com/janhq/nitro)  | Drop-in, local AI alternative to the OpenAI stack. Multi-engine (llama.cpp, TensorRT-LLM). Powers 👋 Jan  | 1,653  | 83  | 71  |  24 | 80  | No license  | 0 days, 18 hrs, 52 mins  |
|  44 | [chatbot-ollama](https://github.com/ivanfioravanti/chatbot-ollama)  | Chatbot Ollama is an open source chat UI for Ollama.  | 1,205  | 187  | 18  |  6 | 1  | Other  | 36 days, 0 hrs, 37 mins  |
|  45 | [LLMFarm](https://github.com/guinmoon/LLMFarm)  | llama and other  large language models on iOS and MacOS offline using GGML library.  | 977  | 56  | 10  |  1 | 27  | MIT License  | 2 days, 15 hrs, 37 mins  |
|  46 | [maid](https://github.com/Mobile-Artificial-Intelligence/maid)  | Maid is a cross-platform Flutter app for interfacing with GGUF / llama.cpp models locally, and with Ollama and OpenAI models remotely.  | 881  | 87  | 3  |  15 | 28  | MIT License  | 0 days, 19 hrs, 24 mins  |
|  47 | [oterm](https://github.com/ggozad/oterm)  | a text-based terminal client for Ollama  | 638  | 36  | 7  |  9 | 18  | MIT License  | 3 days, 16 hrs, 51 mins  |
|  48 | [page-assist](https://github.com/n4ze3m/page-assist)  | Use your locally running AI models to assist you in your web browsing  | 618  | 73  | 44  |  5 | 7  | MIT License  | 0 days, 11 hrs, 42 mins  |
|  49 | [amica](https://github.com/semperai/amica)  | Amica is an open source interface for interactive communication with 3D characters with voice synthesis and speech recognition.  | 550  | 82  | 45  |  16 | 4  | MIT License  | 0 days, 16 hrs, 9 mins  |
|  50 | [catai](https://github.com/withcatai/catai)  | Run AI ✨ assistant locally! with simple API for Node.js 🚀  | 414  | 27  | 1  |  4 | 24  | MIT License  | 12 days, 22 hrs, 37 mins |
|  51 | [FreeChat](https://github.com/psugihara/FreeChat)  | llama.cpp based AI chat app for macOS  | 378  | 30  | 20  |  4 | 0  | MIT License  | 30 days, 11 hrs, 41 mins |
|  52 | [exui](https://github.com/turboderp/exui)  | Web UI for ExLlamaV2  | 363  | 31  | 24  |  7 | 0  | MIT License  | 9 days, 3 hrs, 33 mins  |
|  53 | [LocalAIVoiceChat](https://github.com/KoljaB/LocalAIVoiceChat)  | Local AI talk with a custom voice based on Zephyr 7B model. Uses RealtimeSTT with faster_whisper for transcription and RealtimeTTS with Coqui XTTS for synthesis.  | 339  | 34  | 8  |  2 | 1  | Other  | 10 days, 22 hrs, 17 mins |
|  54 | [ava](https://github.com/cztomsik/ava)  | All-in-one desktop app for running LLMs locally.  | 338  | 14  | 8  |  3 | 0  | Other  | 17 days, 13 hrs, 42 mins |
|  55 | [tenere](https://github.com/pythops/tenere)  | 🔥 TUI interface for LLMs written in Rust  | 245  | 9  | 1  |  6 | 12  | GNU General Public License v3.0  | 0 days, 14 hrs, 22 mins  |
|  56 | [ChatterUI](https://github.com/Vali-98/ChatterUI)  | Simple frontend for LLMs built in react-native.  | 149  | 7  | 4  |  2 | 21  | GNU Affero General Public License v3.0  | 3 days, 20 hrs, 6 mins  |
|  57 | [mikupad](https://github.com/lmg-anon/mikupad)  | LLM Frontend in a single html file  | 145  | 22  | 18  |  9 | 0  | Creative Commons Zero v1.0 Universal  | 1 days, 0 hrs, 20 mins  |
|  58 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Local ML voice chat using high-end models.  | 120  | 6  | 0  |  1 | 0  | MIT License  | 9 days, 14 hrs, 52 mins  |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
