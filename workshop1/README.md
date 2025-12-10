# Building LLM Apps with LangGraph and LangChain

### PyDay Barcelona 2025 Workshop

### by Enric Domingo 
*Data & AI Services Lead at ERNI*  
*Instructor at EAE Business School*    


📹 YouTube: https://youtube.com/@enricd  
📝 Medium: https://medium.com/@enricdomingo   
👨‍💻 GitHub: https://github.com/enricd  
👔 LinkedIn: https://linkedin.com/in/e-domingo/  
📧 Email: contact.enricd@gmail.com   


## 0. Index:

1. [Setup](#1-setup)
2. [Intro to the LangChain stack and Agents](#2-intro-to-the-langchain-stack-and-agents)
3. [LangChain Basics](#3-langchain-basics)
4. [LangGraph Basics](#4-langgraph-basics)
5. [Agentic LangGraph App example](#5-agentic-langgraph-app-example)
6. [Monitoring and Observability](#6-monitoring-and-observability)
7. [Deployment](#7-deployment)

## 1. Setup:

There are some alternatives for the tooling of this workshop, but I will be using: `uv`, `Python 3.13`, `VSCode`, the `OpenAI API`, the `LangSmith API` (optional), and the `tavily API`. Let's see how to set them up:

### 1.1. Install `uv`:

Astral UV is a CLI tool to manage Python versions, dependencies, and virtual environments for Python projects. It can also scaffold new projects quickly and manage package building and publishing. 

If you install UV, you don't even need to have Python pre-installed on your machine, as UV will handle that for you.

Docs: https://docs.astral.sh/uv/getting-started

MacOS / Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows (Powershell):
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```


### 1.2. Download a code editor:

I recommend using [VSCode](https://code.visualstudio.com/), but you can use any code editor of your choice that works fine with Python and Jupyter Notebooks.


### 1.3. Clone this repository and install dependencies:

```bash
git clone https://github.com/enricd/langgraph_agents_pyday_bcn.git
cd langgraph_agents_pyday_bcn
uv sync
```


### 1.4. Create an OpenAI API account and get your API key:

Sign up at https://platform.openai.com/signup and get your API key from https://platform.openai.com/account/api-keys. You will probably need to add a payment method and few credits (5-10 eur is more than enough, we won't probably spend even a euro in this workshop).

Add your API key to a `.env` file in the root of the project:

```bash
OPENAI_API_KEY="sk-..."
```

LangChain and LangGraph can be used with almost any LLM provider, but for this workshop we will use OpenAI. You can adapt the code to use local LLMs with Ollama, or use Anthopic's Claude, Google's Gemini or any other easily.


### 1.5. (Optional) Create a LangSmith account and get your API key:

Sign up at https://langsmith.langchain.com/signup and get your API key from https://langsmith.langchain.com/settings/api-keys. You can use LangSmith for tracing and evaluating your agentic applications.

Add your API key to a `.env` file in the root of the project:

```bash
LANGSMITH_API_KEY="lsv2_..."
```


### 1.6. Create a Tavily account and get your API key:

Tavily allows us to do 1000 free web searches per month, which is great for our web-searching agent.

Sign up and get you API key at:
https://app.tavily.com/



## 2. Intro to the LangChain stack, Agents, and resources

The LangChain stack is a powerful framework for building applications powered by language models. It provides a modular and flexible architecture that allows developers to easily integrate various components such as LLMs, tools, memory, and agents.

ppt: [langchain_langgraph_intro.pptx](langchain_langgraph_intro.pptx)


### Resources:

- Docs:
    - LangChain: https://docs.langchain.com/oss/python/langchain/overview
    - LangGraph: https://docs.langchain.com/oss/python/langgraph/overview
    - Code References: https://reference.langchain.com/python/
    - Integrations: https://docs.langchain.com/oss/python/integrations/providers/overview

- LangChain Academy Free Courses: https://academy.langchain.com/ 

- LangChain YouTube Channel: https://www.youtube.com/@LangChain



## 3. LangChain Basics

[./00_langchain_basics.ipynb](./00_langchain_basics.ipynb)


## 4. LangGraph Basics

[./01_langgraph_basics.ipynb](./01_langgraph_basics.ipynb)
    

## 5. Agentic LangGraph App example

[./02_email_agent.ipynb](./02_email_agent.ipynb)

Then you can check 2 more examples under agents/ running the LangSmith Studio by running:

```bash
uv run langgraph dev
````

This will run a local server available at localhost:2024 where you will be able to query in a nicer UI the 2 example agents.

Additionally, you can try to create a new folder (like I did on langgraph_new/), do cd into it, and run:

```bash
cd <your_new_folder>
uv run langgraph new
```

It will ask you some questions and scaffold a new LangGraph project for you to start building your own agents!

You can learn better project structures from these more complete examples.


## 6. Monitoring and Observability

If you have already registered for a LangSmith account and added your API key to the `.env` file, you can enable tracing in your LangGraph apps by setting the `LANGSMITH_TRACING` environment variable to `true` in the `.env` file:

```bash
LANGSMITH_TRACING=true
LANGSMITH_PROJECT="langgraph-agents-pyday-bcn"
```

Then you will be able to see all the traces of your agent executions, costs, error traces and more in the LangSmith dashboard: https://smith.langchain.com/


## 7. Deployment

We can deploy our LangGraph agents in multiple ways, including:
- As a REST API using FastAPI or Flask
- As a serverless function using AWS Lambda, Google Cloud Functions, or Azure Functions
- As a containerized application using Docker and Kubernetes
- Using LangSmith Deploy


