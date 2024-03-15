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

## Open-Source Local LLM Projects

*Last Updated: 15/03/2024*

|  # | Repo  | About  | Stars  | Forks  | Issues  |  Contributors | Releases  | License  | Time Since Last Commit  |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|  1 | [transformers](https://github.com/huggingface/transformers)  | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX.  | 122,098 | 24,220  | 1,021  |  434 | 141  | Apache License 2.0  | 0 days, 8 hrs, 49 mins  |
|  2 | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)  | A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS). 一键拥有你自己的跨平台 ChatGPT/Gemini 应用。  | 64,319  | 53,066  | 232  |  168 | 58  | MIT License  | 1 days, 5 hrs, 44 mins  |
|  3 | [gpt4all](https://github.com/nomic-ai/gpt4all)  | gpt4all: run open-source LLMs anywhere  | 62,426  | 6,843  | 367  |  90 | 12  | MIT License  | 0 days, 8 hrs, 25 mins  |
|  4 | [gpt4free](https://github.com/xtekky/gpt4free)  | The official gpt4free repository. Various collection of powerful language models  | 54,477  | 12,496  | 94  |  180 | 86  | GNU General Public License v3.0  | 0 days, 14 hrs, 8 mins  |
|  5 | [llama.cpp](https://github.com/ggerganov/llama.cpp)  | LLM inference in C/C++  | 52,846  | 7,446  | 1,243  |  479 | 1,562  | MIT License  | 0 days, 8 hrs, 2 mins  |
|  6 | [gpt_academic](https://github.com/binary-husky/gpt_academic)  | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。  | 52,832  | 6,696  | 211  |  74 | 27  | GNU General Public License v3.0  | 1 days, 5 hrs, 12 mins  |
|  7 | [privateGPT](https://github.com/imartinez/privateGPT)  | Interact with your documents using the power of GPT, 100% privately, no data leaks  | 48,680  | 6,412  | 147  |  63 | 6  | Apache License 2.0  | 0 days, 15 hrs, 42 mins  |
|  8 | [ollama](https://github.com/ollama/ollama)  | Get up and running with Llama 2, Mistral, Gemma, and other large language models.  | 47,501  | 3,188  | 626  |  148 | 51  | MIT License  | 0 days, 8 hrs, 33 mins  |
|  9 | [text-generation-webui](https://github.com/oobabooga/text-generation-webui)  | A Gradio web UI for Large Language Models. Supports transformers, GPTQ, AWQ, EXL2, llama.cpp (GGUF), Llama models.  | 34,246  | 4,578  | 273  |  299 | 34  | GNU Affero General Public License v3.0  | 0 days, 15 hrs, 35 mins  |
|  10 | [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui)  | AI chat for every model.  | 25,274  | 6,861  | 69  |  31 | 0  | MIT License  | 1 days, 2 hrs, 4 mins  |
|  11 | [lobe-chat](https://github.com/lobehub/lobe-chat)  | 🤯 Lobe Chat - an open-source, modern-design LLMs/AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Perplexity / Bedrock / Azure / Mistral / Ollama ), Multi-Modals (Vision/TTS) and plugin system. One-click FREE deployment of your private ChatGPT chat application.  | 22,112  | 4,570  | 219  |  70 | 465  | MIT License  | 0 days, 15 hrs, 28 mins  |
|  12 | [localGPT](https://github.com/PromtEngineer/localGPT)  | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private.  | 18,771  | 2,066  | 444  |  42 | 0  | Apache License 2.0  | 0 days, 16 hrs, 8 mins  |
|  13 | [chatbox](https://github.com/Bin-Huang/chatbox)  | Chatbox is a desktop client for ChatGPT, Claude and other LLMs, available on Windows, Mac, Linux  | 17,617  | 1,811  | 281  |  28 | 54  | GNU General Public License v3.0  | 1 days, 20 hrs, 40 mins  |
|  14 | [LocalAI](https://github.com/mudler/LocalAI)  | :robot: The free, Open Source OpenAI alternative. Self-hosted, community-driven and local-first. Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. It allows to generate Text, Audio, Video, Images. Also with voice cloning capabilities. | 17,609  | 1,292  | 245  |  77 | 37  | MIT License  | 0 days, 8 hrs, 19 mins  |
|  15 | [mlc-llm](https://github.com/mlc-ai/mlc-llm)  | Enable everyone to develop, optimize and deploy AI models natively on everyone's devices.  | 16,203  | 1,218  | 208  |  93 | 1  | Apache License 2.0  | 0 days, 11 hrs, 26 mins  |
|  16 | [vllm](https://github.com/vllm-project/vllm)  | A high-throughput and memory-efficient inference and serving engine for LLMs  | 16,029  | 2,013  | 1,029  |  227 | 21  | Apache License 2.0  | 0 days, 8 hrs, 4 mins  |
|  17 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)  | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.  | 14,452  | 2,214  | 101  |  45 | 20  | GNU General Public License v3.0  | 3 days, 2 hrs, 0 mins  |
|  18 | [jan](https://github.com/janhq/jan)  | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer  | 11,626  | 640  | 193  |  37 | 17  | GNU Affero General Public License v3.0  | 0 days, 8 hrs, 7 mins  |
|  19 | [llamafile](https://github.com/Mozilla-Ocho/llamafile)  | Distribute and run LLMs with a single file.  | 10,055  | 453  | 52  |  27 | 10  | Other  | 1 days, 19 hrs, 9 mins  |
|  20 | [h2ogpt](https://github.com/h2oai/h2ogpt)  | Private chat with local GPT with document, images, video, etc. 100% private, Apache 2.0. Supports oLLaMa, Mixtral, llama.cpp, and more. Demo: <https://gpt.h2o.ai/> <https://codellama.h2o.ai/>  | 10,052  | 1,117  | 217  |  65 | 129  | Apache License 2.0  | 0 days, 8 hrs, 4 mins  |
|  21 | [open-webui](https://github.com/open-webui/open-webui)  | User-friendly WebUI for LLMs (Formerly Ollama WebUI)  | 9,412  | 866  | 79  |  67 | 10  | MIT License  | 0 days, 11 hrs, 6 mins  |
|  22 | [chathub](https://github.com/chathub-dev/chathub)  | All-in-one chatbot client  | 9,347  | 913  | 261  |  12 | 0  | GNU General Public License v3.0  | 11 days, 1 hrs, 35 mins  |
|  23 | [anything-llm](https://github.com/Mintplex-Labs/anything-llm)  | A multi-user ChatGPT for any LLMs and vector database. Unlimited documents, messages, and storage in one privacy-focused app. Now available as a desktop application!  | 9,042  | 966  | 72  |  32 | 0  | MIT License  | 0 days, 8 hrs, 0 mins  |
|  24 | [FlexGen](https://github.com/FMInference/FlexGen)  | Running large language models on a single GPU for throughput-oriented scenarios.  | 8,874  | 510  | 50  |  18 | 0  | Apache License 2.0  | 169 days, 20 hrs, 30 mins |
|  25 | [web-llm](https://github.com/mlc-ai/web-llm)  | Bringing large-language models and chat to web browsers. Everything runs inside the browser with no server support.  | 8,790  | 527  | 77  |  28 | 1  | Apache License 2.0  | 0 days, 10 hrs, 0 mins  |
|  26 | [LibreChat](https://github.com/danny-avila/LibreChat)  | Enhanced ChatGPT Clone: Features OpenAI, Assistants API, Azure, Groq, GPT-4 Vision, Mistral, Bing, Anthropic, OpenRouter, Google Gemini, AI model switching, message search, langchain, DALL-E-3, ChatGPT Plugins, OpenAI Functions, Secure Multi-User System, Presets, completely open-source for self-hosting. More features in development  | 8,631  | 1,544  | 68  |  85 | 36  | MIT License  | 0 days, 10 hrs, 35 mins  |
|  27 | [OpenLLM](https://github.com/bentoml/OpenLLM)  | Operating LLMs in production  | 8,380  | 519  | 90  |  24 | 108  | Apache License 2.0  | 2 days, 0 hrs, 10 mins  |
|  28 | [text-generation-inference](https://github.com/huggingface/text-generation-inference) | Large Language Model Text Generation Inference  | 7,216  | 773  | 180  |  70 | 36  | Other  | 2 days, 19 hrs, 21 mins  |
|  29 | [server](https://github.com/triton-inference-server/server)  | The Triton Inference Server provides an optimized cloud and edge inferencing solution.  | 7,019  | 1,343  | 381  |  109 | 64  | BSD 3-Clause "New" or "Revised" License | 0 days, 12 hrs, 5 mins  |
|  30 | [openplayground](https://github.com/nat/openplayground)  | An LLM playground you can run on your laptop  | 6,024  | 456  | 77  |  16 | 0  | MIT License  | 42 days, 2 hrs, 22 mins  |
|  31 | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  | Python bindings for llama.cpp  | 5,909  | 701  | 308  |  119 | 106  | MIT License  | 0 days, 15 hrs, 29 mins  |
|  32 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines.  | 5,873  | 562  | 534  |  10 | 4  | Apache License 2.0  | 1 days, 12 hrs, 10 mins  |
|  33 | [chat-ui](https://github.com/huggingface/chat-ui)  | Open source codebase powering the HuggingChat app  | 5,567  | 730  | 173  |  55 | 5  | Apache License 2.0  | 0 days, 8 hrs, 28 mins  |
|  34 | [SillyTavern](https://github.com/SillyTavern/SillyTavern)  | LLM Frontend for Power Users.  | 5,271  | 1,668  | 265  |  89 | 73  | GNU Affero General Public License v3.0  | 0 days, 8 hrs, 20 mins  |
|  35 | [lollms-webui](https://github.com/ParisNeo/lollms-webui)  | Lord of Large Language Models Web User Interface  | 3,602  | 454  | 123  |  36 | 17  | Apache License 2.0  | 1 days, 9 hrs, 35 mins  |
|  36 | [koboldcpp](https://github.com/LostRuins/koboldcpp)  | A simple one-file way to run various GGML and GGUF models with KoboldAI's UI  | 3,347  | 250  | 157  |  476 | 72  | GNU Affero General Public License v3.0  | 0 days, 16 hrs, 20 mins  |
|  37 | [simpleaichat](https://github.com/minimaxir/simpleaichat)  | Python package for easily interfacing with chat apps, with robust features and minimal code complexity.  | 3,328  | 211  | 53  |  11 | 6  | MIT License  | 67 days, 2 hrs, 49 mins  |
|  38 | [LLM-As-Chatbot](https://github.com/deep-diver/LLM-As-Chatbot)  | LLM as a Chatbot Service  | 3,209  | 380  | 19  |  7 | 0  | Apache License 2.0  | 115 days, 17 hrs, 24 mins |
|  39 | [big-agi](https://github.com/enricoros/big-agi)  | 💬 Personal AI application powered by GPT-4 and beyond, with AI personas, AGI functions, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy and gift #big-AGI-energy! Using Next.js, React, Joy.  | 3,081  | 772  | 116  |  32 | 13  | MIT License  | 0 days, 8 hrs, 6 mins  |
|  40 | [exllamav2](https://github.com/turboderp/exllamav2)  | A fast inference library for running LLMs locally on modern consumer-class GPUs  | 2,640  | 190  | 102  |  28 | 14  | MIT License  | 0 days, 19 hrs, 31 mins  |
|  41 | [llm](https://github.com/simonw/llm)  | Access large language models from the command-line  | 2,596  | 116  | 141  |  19 | 24  | Apache License 2.0  | 1 days, 4 hrs, 30 mins  |
|  42 | [exllama](https://github.com/turboderp/exllama)  | A more memory-efficient rewrite of the HF transformers implementation of Llama for use with quantized weights.  | 2,522  | 204  | 65  |  16 | 0  | MIT License  | 166 days, 12 hrs, 50 mins |
|  43 | [lmdeploy](https://github.com/InternLM/lmdeploy)  | LMDeploy is a toolkit for compressing, deploying, and serving LLMs.  | 1,977  | 176  | 90  |  43 | 23  | Apache License 2.0  | 0 days, 18 hrs, 44 mins  |
|  44 | [inference](https://github.com/xorbitsai/inference)  | Replace OpenAI GPT with another LLM in your app by changing a single line of code. Xinference gives you the freedom to use any LLM you need. With Xinference, you're empowered to run inference with any open-source language models, speech recognition models, and multimodal models, whether in the cloud, on-premises, or even on your laptop.  | 1,976  | 156  | 198  |  34 | 51  | Apache License 2.0  | 0 days, 20 hrs, 29 mins  |
|  45 | [LLamaSharp](https://github.com/SciSharp/LLamaSharp)  | Run local LLaMA/GPT model easily and fast in C#!🤗 It's also easy to integrate LLamaSharp with semantic-kernel, unity, WPF and WebApp.  | 1,672  | 224  | 75  |  35 | 14  | MIT License  | 0 days, 15 hrs, 24 mins  |
|  46 | [ctransformers](https://github.com/marella/ctransformers)  | Python bindings for the Transformer models implemented in C/C++ using GGML library.  | 1,639  | 126  | 106  |  6 | 30  | MIT License  | 47 days, 0 hrs, 19 mins  |
|  47 | [nitro](https://github.com/janhq/nitro)  | An inference server on top of llama.cpp. OpenAI-compatible API, queue, & scaling. Embed a prod-ready, local inference engine in your apps. Powers Jan  | 1,332  | 60  | 30  |  18 | 63  | GNU Affero General Public License v3.0  | 0 days, 14 hrs, 55 mins  |
|  48 | [llama2.rs](https://github.com/srush/llama2.rs)  | A fast llama2 decoder in pure Rust.  | 940  | 46  | 13  |  4 | 0  | MIT License  | 106 days, 7 hrs, 56 mins  |
|  49 | [chatbot-ollama](https://github.com/ivanfioravanti/chatbot-ollama)  | Chatbot Ollama is an open source chat UI for Ollama.  | 862  | 125  | 18  |  6 | 1  | Other  | 21 days, 7 hrs, 38 mins  |
|  50 | [LLMFarm](https://github.com/guinmoon/LLMFarm)  | llama and other  large language models on iOS and MacOS offline using GGML library.  | 765  | 43  | 11  |  1 | 22  | MIT License  | 1 days, 14 hrs, 3 mins  |
|  51 | [maid](https://github.com/Mobile-Artificial-Intelligence/maid)  | Maid is a cross-platform Flutter app for interfacing with GGUF / llama.cpp models locally, and with Ollama and OpenAI models remotely.  | 482  | 53  | 6  |  10 | 23  | MIT License  | 0 days, 8 hrs, 18 mins  |
|  52 | [oterm](https://github.com/ggozad/oterm)  | a text-based terminal client for Ollama  | 446  | 23  | 3  |  6 | 12  | MIT License  | 14 days, 10 hrs, 39 mins  |
|  53 | [amica](https://github.com/semperai/amica)  | Amica is an open source interface for interactive communication with 3D characters with voice synthesis and speech recognition.  | 430  | 66  | 46  |  13 | 4  | MIT License  | 0 days, 14 hrs, 9 mins  |
|  54 | [catai](https://github.com/withcatai/catai)  | UI for 🦙model . Run AI assistant locally ✨  | 393  | 26  | 1  |  4 | 22  | MIT License  | 48 days, 12 hrs, 30 mins  |
|  55 | [FreeChat](https://github.com/psugihara/FreeChat)  | llama.cpp based AI chat app for macOS  | 328  | 24  | 18  |  4 | 0  | MIT License  | 2 days, 11 hrs, 10 mins  |
|  56 | [exui](https://github.com/turboderp/exui)  | Web UI for ExLlamaV2  | 299  | 23  | 14  |  7 | 0  | MIT License  | 0 days, 19 hrs, 30 mins  |
|  57 | [ava](https://github.com/cztomsik/ava)  | All-in-one desktop app for running LLMs locally.  | 268  | 11  | 9  |  2 | 0  | Other  | 16 days, 13 hrs, 17 mins  |
|  58 | [LocalAIVoiceChat](https://github.com/KoljaB/LocalAIVoiceChat)  | Local AI talk with a custom voice based on Zephyr 7B model. Uses RealtimeSTT with faster_whisper for transcription and RealtimeTTS with Coqui XTTS for synthesis.  | 248  | 21  | 5  |  1 | 1  | Other  | 101 days, 9 hrs, 54 mins  |
|  59 | [tenere](https://github.com/pythops/tenere)  | 🔥 TUI interface for LLMs written in Rust  | 174  | 6  | 1  |  4 | 11  | GNU General Public License v3.0  | 36 days, 16 hrs, 41 mins  |
|  60 | [emeltal](https://github.com/ptsochantaris/emeltal)  | Local ML voice chat using high-end models.  | 101  | 6  | 0  |  1 | 0  | MIT License  | 3 days, 7 hrs, 59 mins  |
|  61 | [mikupad](https://github.com/lmg-anon/mikupad)  | LLM Frontend in a single html file  | 84  | 15  | 16  |  6 | 0  | Creative Commons Zero v1.0 Universal  | 24 days, 8 hrs, 45 mins  |
|  62 | [neurochat](https://github.com/ortegaalfredo/neurochat)  | Native gui to serveral AI services plus llama.cpp local AIs.  | 72  | 6  | 1  |  1 | 6  | BSD 2-Clause "Simplified" License  | 60 days, 14 hrs, 36 mins  |
|  63 | [ChatterUI](https://github.com/Vali-98/ChatterUI)  | Simple frontend for LLMs built in react-native.  | 67  | 2  | 2  |  2 | 14  | GNU Affero General Public License v3.0  | 6 days, 2 hrs, 4 mins  |
|  64 | [lite.koboldai.net](https://github.com/LostRuins/lite.koboldai.net)  | A zero dependency web UI for KoboldAI Horde  | 45  | 24  | 7  |  14 | 0  | GNU Affero General Public License v3.0  | 0 days, 17 hrs, 27 mins  |
|  65 | [local-chat](https://github.com/nathanlesage/local-chat)  | LocalChat is a ChatGPT-like chat that runs on your computer  | 42  | 1  | 3  |  1 | 12  | GNU General Public License v3.0  | 1 days, 22 hrs, 14 mins  |
|  66 | [gatogpt](https://github.com/elgatopanzon/gatogpt)  | Local LLM inference & management server with built-in OpenAI API  | 28  | 2  | 0  |  1 | 0  | GNU Affero General Public License v3.0  | 40 days, 3 hrs, 48 mins  |
|  67 | [GPT-Sequencer](https://github.com/dbddv01/GPT-Sequencer)  | A chatbot for local gguf llm models with easy sequencing via csv file.  A toy tool for everyone to build advanced prompt engineering sequences.  | 6  | 0  | 0  |  1 | 0  | MIT License  | 10 days, 19 hrs, 19 mins  |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://huyenchip.com/2024/03/14/ai-oss.html>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
