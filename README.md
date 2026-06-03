# LangGraph Search Agent

A **tool-using LangGraph agent** that decides — on its own — whether to search the web or answer directly from the LLM.

This is not a chatbot. It is a **routing agent** that simulates real agent decision-making: perceive the input, choose the right tool, act, and return a traceable result.

> Built as a foundation toward ReAct agents and Agentic RAG.

---

## What It Does

The agent receives a question and routes it through one of two paths:

```
START → Router → search_node → llm_node → END
               ↘ llm_node → END
```

- **Web questions** (news, prices, current events) → search first, then answer
- **General questions** → answer directly from the LLM

---

## Stack

| Component | Tool |
|---|---|
| Agent framework | LangGraph |
| LLM backend | LM Studio (local) |
| Web search | Serper API |
| Language | Python |

---

## Key Design Decisions

**Keyword-based router** — routes to web search if the question contains trigger words (`latest`, `news`, `price`, `who is`, `search`, `current`), otherwise goes straight to the LLM.

**Shared state** — all nodes read from and write to a single `AgentState`, keeping data flow explicit and inspectable.

**Trace system** — every run records `router_decision`, `search_results_count`, and `llm_model_name` so you can see exactly how the graph executed.

---

## What This Is Not

- ❌ No vector database
- ❌ No embeddings
- ❌ No retrieval pipeline

This is a **tool-using agent**, not a RAG system.

---

## Why I Built It

To learn agent fundamentals before moving to more complex architectures:

- Conditional routing in LangGraph
- State management across nodes
- Tool integration (web search)
- Lightweight observability with traces

This project directly prepares for **ReAct agents** (think → act → observe loops) and **Agentic RAG** (retrieval as a tool, not a pipeline).

---

## Setup

```bash
git clone https://github.com/your-username/langgraph-search-agent.git
cd langgraph-search-agent
pip install langgraph requests python-dotenv
```

Create `.env`:
```
MODEL_NAME=...
LLM_BASE_URL=...
SERPER_API_KEY=...
```

Run:
```bash
python main.py
```

---

## Feedback Welcome

Looking for feedback on:
1. Code structure and organization
2. Agent design decisions
3. LangGraph best practices
4. What to improve before moving to ReAct and Agentic RAG
