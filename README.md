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

*Last Updated: 11/07/2024*

|  # | Repo  | About  | Stars  | Forks  | Issues  |  Contributors | Releases  | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [transformers](https://github.com/huggingface/transformers)  | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX.  | 129,092 | 25,602  | 1,170  |  433 | 155  | Apache License 2.0  | 0 days, 8 hrs, 0 mins  |
|  2 | [ollama](https://github.com/ollama/ollama)  | Get up and running with Llama 3, Mistral, Gemma 2, and other large language models.  | 77,910  | 5,896  | 1,141  |  242 | 72  | MIT License  | 0 days, 10 hrs, 3 mins  |
|  3 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS). 一键拥有你自己的跨平台 ChatGPT/Gemini 应用。  | 72,827  | 57,828  | 345  |  189 | 61  | MIT License  | 0 days, 11 hrs, 7 mins  |
|  4 | [gpt4all](https://github.com/nomic-ai/gpt4all)  | GPT4All: Chat with Local LLMs on Any Device  | 67,220  | 7,399  | 494  |  107 | 17  | MIT License  | 0 days, 18 hrs, 49 mins  |
|  5 | [gpt_academic](https://github.com/binary-husky/gpt_academic)  | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。  | 61,559  | 7,665  | 290  |  85 | 29  | GNU General Public License v3.0  | 1 days, 16 hrs, 5 mins  |
|  6 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | LLM inference in C/C++  | 61,494  | 8,793  | 546  |  472 | 2,083  | MIT License  | 0 days, 8 hrs, 2 mins  |
|  7 | [gpt4free](https://github.com/xtekky/gpt4free)  | The official gpt4free repository, various collection of powerful language models  | 59,204  | 13,174  | 30  |  208 | 141  | GNU General Public License v3.0  | 0 days, 21 hrs, 36 mins  |
|  8 | [privateGPT](https://github.com/imartinez/privateGPT)  | Interact with your documents using the power of GPT, 100% privately, no data leaks  | 52,935  | 7,115  | 230  |  82 | 7  | Apache License 2.0  | 2 days, 9 hrs, 56 mins  |
|  9 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | A Gradio web UI for Large Language Models.  | 38,292  | 5,076  | 183  |  317 | 44  | GNU Affero General Public License v3.0  | 1 days, 4 hrs, 52 mins  |
|  10 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | 🤯 Lobe Chat - an open-source, modern-design LLMs/AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Ollama / Bedrock / Azure / Mistral / Perplexity ), Multi-Modals (Vision/TTS) and plugin system. One-click FREE deployment of your private ChatGPT chat application.  | 35,111  | 8,253  | 358  |  123 | 742  | Other  | 0 days, 8 hrs, 37 mins  |
|  11 | [open-webui](https://github.com/open-webui/open-webui)  | User-friendly WebUI for LLMs (Formerly Ollama WebUI)  | 30,889  | 3,375  | 127  |  171 | 39  | MIT License  | 0 days, 12 hrs, 54 mins  |
|  12 | [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui)  | AI chat for every model.  | 27,390  | 7,604  | 155  |  47 | 0  | MIT License  | 3 days, 6 hrs, 23 mins  |
|  13 | [vllm](https://github.com/vllm-project/vllm)  | A high-throughput and memory-efficient inference and serving engine for LLMs  | 22,735  | 3,202  | 1,393  |  397 | 30  | Apache License 2.0  | 0 days, 8 hrs, 22 mins  |
|  14 | [LocalAI](https://github.com/mudler/LocalAI)  | :robot: The free, Open Source OpenAI alternative. Self-hosted, community-driven and local-first. Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. It allows to generate Text, Audio, Video, Images. Also with voice cloning capabilities. | 21,786  | 1,666  | 329  |  99 | 52  | MIT License  | 0 days, 9 hrs, 2 mins  |
|  15 | [jan](https://github.com/janhq/jan)  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer. Multiple engine support (llama.cpp, TensorRT-LLM)  | 20,868  | 1,197  | 173  |  51 | 25  | GNU Affero General Public License v3.0  | 0 days, 9 hrs, 25 mins  |
|  16 | [chatbox](https://github.com/Bin-Huang/chatbox)  | User-friendly Desktop Client App for AI Models/LLMs (GPT, Claude, Gemini, Ollama...)  | 19,800  | 2,016  | 306  |  28 | 62  | GNU General Public License v3.0  | 2 days, 5 hrs, 4 mins  |
|  17 | [localGPT](https://github.com/PromtEngineer/localGPT)  | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private.  | 19,613  | 2,193  | 472  |  42 | 0  | Apache License 2.0  | 13 days, 12 hrs, 18 mins |
|  18 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Universal LLM Deployment Engine with ML Compilation  | 17,756  | 1,411  | 152  |  117 | 1  | Apache License 2.0  | 0 days, 13 hrs, 9 mins  |
|  19 | [anything-llm](https://github.com/Mintplex-Labs/anything-llm)  | The all-in-one Desktop & Docker AI application with full RAG and AI Agent capabilities.  | 17,216  | 1,848  | 132  |  53 | 0  | MIT License  | 0 days, 16 hrs, 52 mins  |
|  20 | [llamafile](https://github.com/Mozilla-Ocho/llamafile)  | Distribute and run LLMs with a single file.  | 16,959  | 842  | 102  |  43 | 24  | Other  | 5 days, 6 hrs, 34 mins  |
|  21 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Enhanced ChatGPT Clone: Features OpenAI, Assistants API, Azure, Groq, GPT-4 Vision, Mistral, Bing, Anthropic, OpenRouter, Vertex AI, Gemini, AI model switching, message search, langchain, DALL-E-3, ChatGPT Plugins, OpenAI Functions, Secure Multi-User System, Presets, completely open-source for self-hosting. More features in development  | 15,367  | 2,555  | 106  |  133 | 43  | MIT License  | 0 days, 9 hrs, 40 mins  |
|  22 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  | 15,011  | 2,277  | 117  |  50 | 22  | GNU General Public License v3.0  | 13 days, 3 hrs, 40 mins  |
|  23 | [web-llm](https://github.com/mlc-ai/web-llm)  | High-performance In-browser LLM Inference Engine  | 11,767  | 734  | 53  |  35 | 1  | Apache License 2.0  | 0 days, 15 hrs, 26 mins  |
|  24 | [h2ogpt](https://github.com/h2oai/h2ogpt)  | Private chat with local GPT with document, images, video, etc. 100% private, Apache 2.0. Supports oLLaMa, Mixtral, llama.cpp, and more. Demo: https://gpt.h2o.ai/ https://codellama.h2o.ai/  | 10,968  | 1,199  | 259  |  66 | 2  | Apache License 2.0  | 0 days, 9 hrs, 57 mins  |
|  25 | [chathub](https://github.com/chathub-dev/chathub)  | All-in-one chatbot client  | 9,772  | 979  | 306  |  12 | 0  | GNU General Public License v3.0  | 8 days, 6 hrs, 11 mins  |
|  26 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Run any open-source LLMs, such as Llama 2, Mistral, as OpenAI compatible API endpoint in the cloud.  | 9,288  | 592  | 60  |  30 | 121  | Apache License 2.0  | 0 days, 10 hrs, 23 mins  |
|  27 | [text-generation-inference](https://github.com/huggingface/text-generation-inference) | Large Language Model Text Generation Inference  | 8,367  | 948  | 129  |  102 | 45  | Apache License 2.0  | 0 days, 8 hrs, 8 mins  |
|  28 | [server](https://github.com/triton-inference-server/server)  | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  | 7,751  | 1,423  | 543  |  113 | 68  | BSD 3-Clause "New" or "Revised" License | 0 days, 10 hrs, 9 mins  |
|  29 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines.  | 7,441  | 803  | 659  |  13 | 6  | Apache License 2.0  | 1 days, 8 hrs, 26 mins  |
|  30 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Python bindings for llama.cpp  | 7,175  | 850  | 419  |  145 | 227  | MIT License  | 1 days, 21 hrs, 15 mins  |
|  31 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | LLM Frontend for Power Users.  | 6,806  | 2,013  | 319  |  127 | 82  | GNU Affero General Public License v3.0  | 0 days, 10 hrs, 32 mins  |
|  32 | [chat-ui](https://github.com/huggingface/chat-ui)  | Open source codebase powering the HuggingChat app  | 6,787  | 959  | 243  |  88 | 12  | Apache License 2.0  | 0 days, 8 hrs, 31 mins  |
|  33 | [openplayground](https://github.com/nat/openplayground)  | An LLM playground you can run on your laptop  | 6,156  | 478  | 86  |  16 | 0  | MIT License  | 1 days, 8 hrs, 53 mins  |
|  34 | [big-agi](https://github.com/enricoros/big-agi)  | Generative AI suite powered by state-of-the-art models and providing advanced AI/AGI functions. It features AI personas, AGI functions, multi-model chats, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy on-prem or in the cloud.  | 4,834  | 1,094  | 161  |  41 | 16  | MIT License  | 0 days, 8 hrs, 5 mins  |
|  35 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | A simple one-file way to run various GGML and GGUF models with KoboldAI's UI  | 4,386  | 318  | 227  |  469 | 81  | GNU Affero General Public License v3.0  | 0 days, 9 hrs, 21 mins  |
|  36 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Lord of Large Language Models Web User Interface  | 4,072  | 515  | 142  |  38 | 21  | Apache License 2.0  | 0 days, 18 hrs, 32 mins  |
|  37 | [inference](https://github.com/xorbitsai/inference)  | Replace OpenAI GPT with another LLM in your app by changing a single line of code. Xinference gives you the freedom to use any LLM you need. With Xinference, you're empowered to run inference with any open-source language models, speech recognition models, and multimodal models, whether in the cloud, on-premises, or even on your laptop.  | 3,645  | 304  | 399  |  57 | 69  | Apache License 2.0  | 0 days, 9 hrs, 5 mins  |
|  38 | [llm](https://github.com/simonw/llm)  | Access large language models from the command-line  | 3,489  | 181  | 207  |  19 | 25  | Apache License 2.0  | 1 days, 20 hrs, 23 mins  |
|  39 | [simpleaichat](https://github.com/minimaxir/simpleaichat)  | Python package for easily interfacing with chat apps, with robust features and minimal code complexity.  | 3,430  | 225  | 55  |  11 | 6  | MIT License  | 8 days, 1 hrs, 31 mins  |
|  40 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  | 3,287  | 293  | 222  |  59 | 29  | Apache License 2.0  | 0 days, 8 hrs, 11 mins  |
|  41 | [exllamav2](https://github.com/turboderp/exllamav2)  | A fast inference library for running LLMs locally on modern consumer-class GPUs  | 3,240  | 239  | 73  |  40 | 27  | MIT License  | 0 days, 18 hrs, 53 mins  |
|  42 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | A C#/.NET library to run LLM (🦙LLaMA/LLaVA) on your local device efficiently.  | 2,279  | 303  | 114  |  50 | 18  | MIT License  | 0 days, 18 hrs, 13 mins  |
|  43 | [nitro](https://github.com/janhq/nitro)  | Drop-in, local AI alternative to the OpenAI stack. Multi-engine (llama.cpp, TensorRT-LLM, ONNX). Powers 👋 Jan  | 1,777  | 97  | 56  |  30 | 95  | Apache License 2.0  | 0 days, 8 hrs, 37 mins  |
|  44 | [LLMFarm](https://github.com/guinmoon/LLMFarm)  | llama and other  large language models on iOS and MacOS offline using GGML library.  | 1,063  | 64  | 12  |  1 | 29  | MIT License  | 1 days, 2 hrs, 2 mins  |
|  45 | [maid](https://github.com/Mobile-Artificial-Intelligence/maid)  | Maid is a cross-platform Flutter app for interfacing with GGUF / llama.cpp models locally, and with Ollama and OpenAI models remotely.  | 1,033  | 98  | 3  |  15 | 30  | MIT License  | 1 days, 11 hrs, 41 mins  |
|  46 | [page-assist](https://github.com/n4ze3m/page-assist)  | Use your locally running AI models to assist you in your web browsing  | 877  | 98  | 57  |  9 | 11  | MIT License  | 2 days, 23 hrs, 36 mins  |
|  47 | [oterm](https://github.com/ggozad/oterm)  | a text-based terminal client for Ollama  | 856  | 44  | 10  |  9 | 18  | MIT License  | 50 days, 0 hrs, 14 mins  |
|  48 | [amica](https://github.com/semperai/amica)  | Amica is an open source interface for interactive communication with 3D characters with voice synthesis and speech recognition.  | 588  | 92  | 44  |  16 | 4  | MIT License  | 0 days, 11 hrs, 16 mins  |
|  49 | [catai](https://github.com/withcatai/catai)  | Run AI ✨ assistant locally! with simple API for Node.js 🚀  | 428  | 27  | 1  |  4 | 25  | MIT License  | 20 days, 0 hrs, 37 mins  |
|  50 | [FreeChat](https://github.com/psugihara/FreeChat)  | llama.cpp based AI chat app for macOS  | 402  | 34  | 21  |  4 | 0  | MIT License  | 14 days, 0 hrs, 49 mins  |
|  51 | [LocalAIVoiceChat](https://github.com/KoljaB/LocalAIVoiceChat)  | Local AI talk with a custom voice based on Zephyr 7B model. Uses RealtimeSTT with faster_whisper for transcription and RealtimeTTS with Coqui XTTS for synthesis.  | 397  | 39  | 9  |  2 | 1  | Other  | 36 days, 4 hrs, 10 mins  |
|  52 | [exui](https://github.com/turboderp/exui)  | Web UI for ExLlamaV2  | 397  | 32  | 27  |  7 | 0  | MIT License  | 31 days, 22 hrs, 5 mins  |
|  53 | [tenere](https://github.com/pythops/tenere)  | 🔥 TUI interface for LLMs written in Rust  | 268  | 9  | 1  |  7 | 12  | GNU General Public License v3.0  | 30 days, 8 hrs, 9 mins  |
|  54 | [ChatterUI](https://github.com/Vali-98/ChatterUI)  | Simple frontend for LLMs built in react-native.  | 188  | 13  | 5  |  3 | 24  | GNU Affero General Public License v3.0  | 7 days, 15 hrs, 3 mins  |
|  55 | [mikupad](https://github.com/lmg-anon/mikupad)  | LLM Frontend in a single html file  | 173  | 24  | 20  |  10 | 22  | Creative Commons Zero v1.0 Universal  | 1 days, 15 hrs, 59 mins  |
|  56 | [web-llm-chat](https://github.com/mlc-ai/web-llm-chat)  | Chat with AI large language models running natively in your browser. Enjoy private, server-free, seamless AI conversations.  | 130  | 23  | 7  |  180 | 0  | Apache License 2.0  | 3 days, 12 hrs, 10 mins  |
|  57 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Local ML voice chat using high-end models.  | 125  | 6  | 0  |  1 | 0  | MIT License  | 15 days, 22 hrs, 57 mins |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
