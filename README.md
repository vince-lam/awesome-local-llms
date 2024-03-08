# Awesome Local LLMs

There are many ways of hosting open-source LLMs locally for inference: from the command line (CLI) tools to full GUI desktop applications. This repo aims to curate all possible options for running local LLMs. These projects can overlap in scope and may split into different components of inference backend server and UI.

GitHub repository metrics have been collected as a proxy for popularity and active maintenance. For full table with all metrics go to this [Google Sheet](https://docs.google.com/spreadsheets/d/1Xv38p90V3GiJXjq0a3qc24056Vicn1I5MG6QiFE6nVE/edit?usp=sharing). For my thoughts: <https://vinlam.com/posts/local-llm-options/>

## Open-Source Local LLM Projects

*Last Updated: 08/03/2024*

| Owner | Repository Name | About | Stars | Forks | Contributors | Issues | Releases | Watchers | Time Since Last Commit | License | Languages |
|-------|-----------------|-------|-------|-------|--------------|--------|----------|----------|------------------------|---------|-----------|
| huggingface | [transformers](https://github.com/huggingface/transformers) | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX. | 121,616 | 24,126 | 434 | 1,021 | 141 | 1084 | 0 days, 8 hrs, 38 mins | Apache License 2.0 | Python, Cuda, Shell, C++, Dockerfile, C, Makefile, Cython, Jsonnet |
| ChatGPTNextWeb | [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web) | A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS). | 63,573 | 52,611 | 166 | 217 | 57 | 377 | 0 days, 12 hrs, 30 mins | MIT License | TypeScript, SCSS, JavaScript, Shell, Dockerfile, Rust |
| nomic-ai | [gpt4all](https://github.com/nomic-ai/gpt4all) | gpt4all: run open-source LLMs anywhere | 62,163 | 6,815 | 85 | 375 | 10 | 616 | 0 days, 9 hrs, 19 mins | MIT License | C++, QML, Python, CMake, Java, C#, JavaScript, C, Go, Makefile, Shell, Qt Script, PowerShell, Batchfile, CSS |
| ggerganov | [llama.cpp](https://github.com/ggerganov/llama.cpp) | LLM inference in C/C++ | 52,456 | 7,373 | 479 | 1,218 | 1,506 | 491 | 0 days, 10 hrs, 5 mins | MIT License | C++, C, Cuda, Python, Metal, Objective-C, Shell, CMake, Makefile, Nix, Dockerfile, Zig, Swift, Batchfile |
| imartinez | [privateGPT](https://github.com/imartinez/privateGPT) | Interact with your documents using the power of GPT, 100% privately, no data leaks | 48,243 | 6,333 | 59 | 136 | 6 | 428 | 0 days, 13 hrs, 43 mins | Apache License 2.0 | Python, MDX, Makefile |
| ollama | [ollama](https://github.com/ollama/ollama) | Get up and running with Llama 2, Mistral, Gemma, and other large language models. | 45,496 | 3,019 | 146 | 788 | 50 | 292 | 0 days, 8 hrs, 21 mins | MIT License | Go, Shell, C, TypeScript, PowerShell, C++, Inno Setup, Dockerfile, Python, CMake, CSS, Objective-C, JavaScript, HTML |
| oobabooga | [text-generation-webui](https://github.com/oobabooga/text-generation-webui) | A Gradio web UI for Large Language Models. Supports transformers, GPTQ, AWQ, EXL2, llama.cpp (GGUF), Llama models. | 33,940 | 4,545 | 299 | 282 | 33 | 296 | 0 days, 15 hrs, 22 mins | GNU Affero General Public License v3.0 | Python, CSS, JavaScript, Shell, Batchfile, Jupyter Notebook, Dockerfile |
| mckaywrigley | [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui) | AI chat for every model. | 25,107 | 6,785 | 31 | 53 | 0 | 233 | 0 days, 8 hrs, 3 mins | MIT License | TypeScript, PLpgSQL, JavaScript, CSS, Shell |
| lobehub | [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤯 Lobe Chat - an open-source, modern-design LLMs/AI chat framework. | 21,597 | 4,364 | 69 | 189 | 456 | 114 | 0 days, 8 hrs, 33 mins | MIT License | TypeScript, JavaScript, Dockerfile |
| PromtEngineer | [localGPT](https://github.com/PromtEngineer/localGPT) | Chat with your documents on your local device using GPT models. | 18,696 | 2,059 | 42 | 441 | 0 | 162 | 3 days, 9 hrs, 28 mins | Apache License 2.0 | Python, HTML, Dockerfile, Roff |
| Bin-Huang | [chatbox](https://github.com/Bin-Huang/chatbox) | Chatbox is a desktop client for ChatGPT, Claude and other LLMs. | 17,428 | 1,797 | 28 | 281 | 53 | 118 | 29 days, 0 hrs, 10 mins | GNU General Public License v3.0 | TypeScript, JavaScript, SCSS, HTML, CSS, Shell, Rust, Makefile, Dockerfile |
| mudler | [LocalAI](https://github.com/mudler/LocalAI) | :robot: The free, Open Source OpenAI alternative. | 17,392 | 1,268 | 75 | 246 | 37 | 140 | 0 days, 10 hrs, 45 mins | MIT License | C++, Go, Python, Makefile, Shell, Dockerfile, CMake, Earthly |
| mlc-ai | [mlc-llm](https://github.com/mlc-ai/mlc-llm) | Enable everyone to develop. | 16,107 | 1,202 | 92 | 200 | 1 | 158 | 0 days, 8 hrs, 11 mins | Apache License 2.0 | Python, C++, Swift, Kotlin, Rust, Shell, Groovy, Objective-C++, CMake, Objective-C, Java, C |
| vllm-project | [vllm](https://github.com/vllm-project/vllm) | A high-throughput engine for LLMs | 15,731 | 1,937 | 217 | 1,275 | 21 | 164 | 0 days, 10 hrs, 13 mins | Apache License 2.0 | Python, Cuda, C++, Shell, Dockerfile, C, Jinja |
| janhq | [jan](https://github.com/janhq/jan) | Jan is an open source alternative to ChatGPT. | 11,408 | 627 | 36 | 176 | 16 | 77 | 0 days, 8 hrs, 24 mins | GNU Affero General Public License v3.0 | TypeScript, JavaScript, SCSS, Dockerfile, Makefile, Batchfile, Python, Shell |
| h2oai | [h2ogpt](https://github.com/h2oai/h2ogpt) | Private chat with local GPT. | 9,968 | 1,110 | 66 | 222 | 123 | 150 | 0 days, 23 hrs, 26 mins | Apache License 2.0 | Python, Jupyter Notebook, TeX, HTML, Shell, Groovy, Makefile, Smarty, Dockerfile |
| Mozilla-Ocho | [llamafile](https://github.com/Mozilla-Ocho/llamafile) | Distribute and run LLMs with a single file. | 9,775 | 431 | 27 | 46 | 10 | 98 | 0 days, 14 hrs, 12 mins | Other | C++, C, Metal, Objective-C, AGS Script, Roff, HTML, Python, Shell, Makefile, JavaScript, Batchfile, Cuda |
| Mintplex-Labs | [anything-llm](https://github.com/Mintplex-Labs/anything-llm) | A multi-user ChatGPT for any LLMs. | 8,802 | 932 | 31 | 67 | 0 | 77 | 0 days, 8 hrs, 2 mins | MIT License | JavaScript, CSS, Dockerfile, HTML, Shell, HCL |
| open-webui | [open-webui](https://github.com/open-webui/open-webui) | User-friendly WebUI for LLMs. | 8,489 | 758 | 64 | 73 | 9 | 65 | 0 days, 17 hrs, 41 mins | MIT License | Svelte, Python, TypeScript, Shell, CSS, Dockerfile, JavaScript, Smarty, Batchfile, HTML, Makefile |
| danny-avila | [LibreChat](https://github.com/danny-avila/LibreChat) | Enhanced ChatGPT Clone with many features. | 8,410 | 1,506 | 84 | 64 | 36 | 76 | 0 days, 9 hrs, 14 mins | MIT License | TypeScript, JavaScript, CSS, HTML, Dockerfile, Handlebars, Shell |

## Inspired By

* <https://github.com/janhq/awesome-local-ai>
* <https://github.com/mahseema/awesome-ai-tools>
* <https://github.com/steven2358/awesome-generative-ai>
* <https://github.com/e2b-dev/awesome-ai-agents>
* <https://github.com/aimerou/awesome-ai-papers>
* <https://github.com/DefTruth/Awesome-LLM-Inference>
* <https://github.com/youssefHosni/Awesome-AI-Data-GitHub-Repos>
