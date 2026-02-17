# 🌐 AI Web Browsing Assistant

### Playwright + LangChain + Ollama (Local LLM)

A local AI-powered web browsing assistant built using:

-   🧠 LangChain Agents
-   🔁 LangChain Tools (`@tool`)
-   🤖 Ollama (Local LLM - qwen2.5 / llama3.2)
-   🌍 Playwright (Browser Automation)
-   ⚙ Async Python

------------------------------------------------------------------------

# 🚀 Features

## 🌍 Web Browsing

-   Open any URL
-   Scroll the page
-   Extract visible content
-   Summarize web pages
-   Analyze page content step-by-step

## 🧠 Intelligent Tool Routing

-   Uses LangChain `@tool` decorators
-   Uses `create_agent()` for structured agent creation
-   Automatic tool invocation
-   Async tool support
-   Deterministic browsing behavior

## 💻 Fully Local LLM

-   Runs using Ollama
-   No OpenAI API required
-   Works offline (except website access)
-   Supports models like:
    -   `qwen2.5:7b`
    -   `llama3.2`

------------------------------------------------------------------------

# ⚠ Model Recommendation

For reliable multi-step browsing and planning:

It is recommended to use higher-parameter models (13B or above).

Smaller models like `qwen2.5:7b` work well for simple browsing and
summarization but may struggle with complex workflows.

------------------------------------------------------------------------

# 🏗 Architecture

User Input\
↓\
LLM (Ollama via LangChain)\
↓\
Tool Decision (`create_agent`)\
↓\
Playwright Tool Execution\
↓\
LLM Analysis\
↓\
Final Response

------------------------------------------------------------------------

# 📦 Installation

## Install dependencies

``` bash
pip install langchain langchain-ollama playwright langchain-core
playwright install
```

## Install Ollama

``` bash
ollama pull qwen2.5:7b
ollama serve
```

------------------------------------------------------------------------

# ▶ Run

``` bash
python your_script_name.py
```

------------------------------------------------------------------------

# 🔮 Future Improvements

-   Add search engine integration
-   Convert to LangGraph workflow
-   Add memory support
-   Add loop detection controls
