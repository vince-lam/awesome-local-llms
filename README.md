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

*Last Updated: 15/10/2024*

|  # | Repo  | About  | Stars  | Forks  | Issues  |  Contributors | Releases  | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [transformers](https://github.com/huggingface/transformers)  | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX.  | 133,422 | 26,644  | 1,419  |  432 | 167  | Apache License 2.0  | 0 days, 1 hrs, 5 mins  |
|  2 | [ollama](https://github.com/ollama/ollama)  | Get up and running with Llama 3.2, Mistral, Gemma 2, and other large language models.  | 93,343  | 7,368  | 1,399  |  304 | 93  | MIT License  | 0 days, 14 hrs, 40 mins  |
|  3 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS). 一键拥有你自己的跨平台 ChatGPT/Gemini 应用。  | 75,708  | 58,871  | 441  |  225 | 72  | MIT License  | 0 days, 5 hrs, 18 mins  |
|  4 | [gpt4all](https://github.com/nomic-ai/gpt4all)  | GPT4All: Run Local LLMs on Any Device. Open-source and available for commercial use.  | 70,014  | 7,654  | 603  |  113 | 27  | MIT License  | 1 days, 1 hrs, 25 mins  |
|  5 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | LLM inference in C/C++  | 66,283  | 9,531  | 556  |  464 | 2,436  | MIT License  | 0 days, 1 hrs, 10 mins  |
|  6 | [gpt_academic](https://github.com/binary-husky/gpt_academic)  | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。  | 64,813  | 8,009  | 360  |  90 | 31  | GNU General Public License v3.0  | 0 days, 5 hrs, 37 mins  |
|  7 | [gpt4free](https://github.com/xtekky/gpt4free)  | The official gpt4free repository, various collection of powerful language models  | 60,332  | 13,253  | 18  |  215 | 150  | GNU General Public License v3.0  | 0 days, 4 hrs, 54 mins  |
|  8 | [privateGPT](https://github.com/imartinez/privateGPT)  | Interact with your documents using the power of GPT, 100% privately, no data leaks  | 53,901  | 7,245  | 235  |  89 | 10  | Apache License 2.0  | 19 days, 0 hrs, 16 mins  |
|  9 | [open-webui](https://github.com/open-webui/open-webui)  | User-friendly AI Interface (Supports Ollama, OpenAI API, ...)  | 42,874  | 5,161  | 136  |  221 | 63  | MIT License  | 0 days, 2 hrs, 33 mins  |
|  10 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | 🤯 Lobe Chat - an open-source, modern-design AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Ollama / Azure /  DeepSeek), Knowledge Base (file upload / knowledge management / RAG ), Multi-Modals (Vision/TTS) and plugin system. One-click FREE deployment of your private ChatGPT/ Claude application.  | 42,683  | 9,631  | 398  |  153 | 972  | Other  | 0 days, 10 hrs, 38 mins  |
|  11 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | A Gradio web UI for Large Language Models.  | 40,094  | 5,259  | 278  |  327 | 51  | GNU Affero General Public License v3.0  | 0 days, 1 hrs, 7 mins  |
|  12 | [vllm](https://github.com/vllm-project/vllm)  | A high-throughput and memory-efficient inference and serving engine for LLMs  | 28,414  | 4,214  | 2,165  |  453 | 40  | Apache License 2.0  | 0 days, 8 hrs, 27 mins  |
|  13 | [anything-llm](https://github.com/Mintplex-Labs/anything-llm)  | The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, and more.  | 24,558  | 2,468  | 194  |  77 | 7  | MIT License  | 0 days, 13 hrs, 34 mins  |
|  14 | [LocalAI](https://github.com/mudler/LocalAI)  | :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement for OpenAI,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. Features: Generate Text, Audio, Video, Images, Voice Cloning, Distributed inference  | 23,933  | 1,837  | 370  |  109 | 62  | MIT License  | 0 days, 7 hrs, 5 mins  |
|  15 | [jan](https://github.com/janhq/jan)  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer. Multiple engine support (llama.cpp, TensorRT-LLM)  | 22,687  | 1,309  | 154  |  54 | 30  | GNU Affero General Public License v3.0  | 0 days, 3 hrs, 2 mins  |
|  16 | [chatbox](https://github.com/Bin-Huang/chatbox)  | User-friendly Desktop Client App for AI Models/LLMs (GPT, Claude, Gemini, Ollama...)  | 21,235  | 2,143  | 394  |  29 | 43  | GNU General Public License v3.0  | 8 days, 1 hrs, 11 mins  |
|  17 | [localGPT](https://github.com/PromtEngineer/localGPT)  | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private.  | 19,998  | 2,230  | 473  |  43 | 0  | Apache License 2.0  | 17 days, 8 hrs, 4 mins  |
|  18 | [llamafile](https://github.com/Mozilla-Ocho/llamafile)  | Distribute and run LLMs with a single file.  | 19,783  | 996  | 132  |  45 | 29  | Other  | 1 days, 6 hrs, 31 mins  |
|  19 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Universal LLM Deployment Engine with ML Compilation  | 18,914  | 1,545  | 186  |  126 | 1  | Apache License 2.0  | 0 days, 1 hrs, 1 mins  |
|  20 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Enhanced ChatGPT Clone: Features Anthropic, AWS, OpenAI, Assistants API, Azure, Groq, o1, GPT-4o, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, langchain, DALL-E-3, ChatGPT Plugins, OpenAI Functions, Secure Multi-User System, Presets, completely open-source for self-hosting. Actively in public development. | 18,165  | 3,035  | 189  |  158 | 46  | MIT License  | 0 days, 17 hrs, 26 mins  |
|  21 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  | 15,191  | 2,293  | 121  |  51 | 25  | GNU General Public License v3.0  | 20 days, 0 hrs, 38 mins  |
|  22 | [web-llm](https://github.com/mlc-ai/web-llm)  | High-performance In-browser LLM Inference Engine  | 13,294  | 850  | 71  |  40 | 1  | Apache License 2.0  | 8 days, 1 hrs, 48 mins  |
|  23 | [h2ogpt](https://github.com/h2oai/h2ogpt)  | Private chat with local GPT with document, images, video, etc. 100% private, Apache 2.0. Supports oLLaMa, Mixtral, llama.cpp, and more. Demo: https://gpt.h2o.ai/ https://gpt-docs.h2o.ai/  | 11,321  | 1,240  | 283  |  68 | 2  | Apache License 2.0  | 0 days, 5 hrs, 3 mins  |
|  24 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Run any open-source LLMs, such as Llama 3.1, Gemma, as OpenAI compatible API endpoint in the cloud.  | 9,879  | 628  | 22  |  31 | 128  | Apache License 2.0  | 0 days, 22 hrs, 19 mins  |
|  25 | [FlexGen](https://github.com/FMInference/FlexGen)  | Running large language models on a single GPU for throughput-oriented scenarios.  | 9,168  | 547  | 57  |  19 | 0  | Apache License 2.0  | 7 days, 8 hrs, 17 mins  |
|  26 | [text-generation-inference](https://github.com/huggingface/text-generation-inference) | Large Language Model Text Generation Inference  | 8,910  | 1,053  | 128  |  117 | 48  | Apache License 2.0  | 0 days, 2 hrs, 32 mins  |
|  27 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines.  | 8,415  | 949  | 769  |  15 | 9  | Apache License 2.0  | 0 days, 7 hrs, 19 mins  |
|  28 | [server](https://github.com/triton-inference-server/server)  | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  | 8,183  | 1,462  | 613  |  119 | 71  | BSD 3-Clause "New" or "Revised" License | 0 days, 8 hrs, 46 mins  |
|  29 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Python bindings for llama.cpp  | 7,921  | 944  | 511  |  156 | 276  | MIT License  | 5 days, 18 hrs, 36 mins  |
|  30 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | LLM Frontend for Power Users.  | 7,849  | 2,344  | 261  |  156 | 83  | GNU Affero General Public License v3.0  | 0 days, 6 hrs, 54 mins  |
|  31 | [chat-ui](https://github.com/huggingface/chat-ui)  | Open source codebase powering the HuggingChat app  | 7,394  | 1,076  | 270  |  106 | 14  | Apache License 2.0  | 0 days, 4 hrs, 55 mins  |
|  32 | [big-agi](https://github.com/enricoros/big-agi)  | Generative AI suite powered by state-of-the-art models and providing advanced AI/AGI functions. It features AI personas, AGI functions, multi-model chats, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy on-prem or in the cloud.  | 5,373  | 1,222  | 203  |  43 | 16  | MIT License  | 0 days, 4 hrs, 23 mins  |
|  33 | [inference](https://github.com/xorbitsai/inference)  | Replace OpenAI GPT with another LLM in your app by changing a single line of code. Xinference gives you the freedom to use any LLM you need. With Xinference, you're empowered to run inference with any open-source language models, speech recognition models, and multimodal models, whether in the cloud, on-premises, or even on your laptop.  | 5,071  | 407  | 205  |  75 | 85  | Apache License 2.0  | 3 days, 4 hrs, 10 mins  |
|  34 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | Run GGUF models easily with a KoboldAI UI. One File. Zero Install.  | 5,065  | 354  | 235  |  463 | 88  | GNU Affero General Public License v3.0  | 1 days, 0 hrs, 36 mins  |
|  35 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  | 4,428  | 398  | 307  |  74 | 36  | Apache License 2.0  | 0 days, 1 hrs, 20 mins  |
|  36 | [llm](https://github.com/simonw/llm)  | Access large language models from the command-line  | 4,416  | 241  | 231  |  21 | 27  | Apache License 2.0  | 32 days, 15 hrs, 25 mins |
|  37 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Lord of Large Language Models Web User Interface  | 4,286  | 540  | 155  |  38 | 23  | Apache License 2.0  | 2 days, 0 hrs, 8 mins  |
|  38 | [exllamav2](https://github.com/turboderp/exllamav2)  | A fast inference library for running LLMs locally on modern consumer-class GPUs  | 3,570  | 277  | 87  |  46 | 34  | MIT License  | 13 days, 16 hrs, 45 mins |
|  39 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | A C#/.NET library to run LLM (🦙LLaMA/LLaVA) on your local device efficiently.  | 2,583  | 337  | 131  |  54 | 21  | MIT License  | 1 days, 19 hrs, 39 mins  |
|  40 | [nitro](https://github.com/janhq/nitro)  | Run and customize Local LLMs.  | 1,958  | 109  | 126  |  32 | 135  | Apache License 2.0  | 0 days, 1 hrs, 2 mins  |
|  41 | [page-assist](https://github.com/n4ze3m/page-assist)  | Use your locally running AI models to assist you in your web browsing  | 1,395  | 135  | 91  |  12 | 19  | MIT License  | 1 days, 22 hrs, 19 mins  |
|  42 | [maid](https://github.com/Mobile-Artificial-Intelligence/maid)  | Maid is a cross-platform Flutter app for interfacing with GGUF / llama.cpp models locally, and with Ollama and OpenAI models remotely.  | 1,380  | 146  | 15  |  20 | 31  | MIT License  | 3 days, 9 hrs, 5 mins  |
|  43 | [LLMFarm](https://github.com/guinmoon/LLMFarm)  | llama and other  large language models on iOS and MacOS offline using GGML library.  | 1,269  | 79  | 18  |  1 | 31  | MIT License  | 4 days, 0 hrs, 3 mins  |
|  44 | [oterm](https://github.com/ggozad/oterm)  | a text-based terminal client for Ollama  | 1,023  | 60  | 7  |  12 | 35  | MIT License  | 3 days, 5 hrs, 23 mins  |
|  45 | [amica](https://github.com/semperai/amica)  | Amica is an open source interface for interactive communication with 3D characters with voice synthesis and speech recognition.  | 690  | 112  | 40  |  16 | 4  | MIT License  | 0 days, 2 hrs, 16 mins  |
|  46 | [exui](https://github.com/turboderp/exui)  | Web UI for ExLlamaV2  | 430  | 41  | 33  |  8 | 0  | MIT License  | 5 days, 16 hrs, 29 mins  |
|  47 | [ChatterUI](https://github.com/Vali-98/ChatterUI)  | Simple frontend for LLMs built in react-native.  | 422  | 25  | 10  |  1 | 44  | GNU Affero General Public License v3.0  | 0 days, 3 hrs, 13 mins  |
|  48 | [ava](https://github.com/cztomsik/ava)  | All-in-one desktop app for running LLMs locally.  | 410  | 15  | 3  |  3 | 0  | Other  | 2 days, 16 hrs, 32 mins  |
|  49 | [tenere](https://github.com/pythops/tenere)  | 🤖 TUI interface for LLMs written in Rust  | 314  | 9  | 1  |  7 | 13  | GNU General Public License v3.0  | 40 days, 4 hrs, 8 mins  |
|  50 | [web-llm-chat](https://github.com/mlc-ai/web-llm-chat)  | Chat with AI large language models running natively in your browser. Enjoy private, server-free, seamless AI conversations.  | 286  | 47  | 10  |  181 | 0  | Apache License 2.0  | 10 days, 18 hrs, 44 mins |
|  51 | [mikupad](https://github.com/lmg-anon/mikupad)  | LLM Frontend in a single html file  | 238  | 27  | 23  |  10 | 35  | Creative Commons Zero v1.0 Universal  | 8 days, 18 hrs, 44 mins  |
|  52 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Local ML voice chat using high-end models.  | 142  | 8  | 1  |  1 | 0  | MIT License  | 2 days, 2 hrs, 44 mins  |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
