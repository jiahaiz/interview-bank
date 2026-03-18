# Take-Home Project: AI Agent Design & POC

**Role:** 人工智能工程师 / 数据与智能化工程师  
**Goal:** Evaluate **design thinking** and **proof-of-concept (POC)** quality. You are encouraged to use an **AI assistant** (e.g. Cursor, ChatGPT, Claude) to discuss and refine your design before coding.

---

## 1. What We Care About

- **Design first:** Clear architecture, component boundaries, and tradeoffs.
- **POC that runs:** Minimal but runnable code demonstrating the core flow.
- **How you used AI:** Brief note on how the AI assistant influenced your design (no penalty for using it; we want to see thoughtful collaboration).

We do **not** expect production-ready code, full test coverage, or deployment configs. We **do** expect a readable design and a working POC.

---

## 2. Task

Design and implement a **minimal AI Agent** that:

1. **Answers questions over a small document corpus** using a RAG-style flow (retrieve relevant chunks, then generate an answer with an LLM).
2. **Can call at least one tool** (e.g. calculator, current time, or a simple API of your choice) when the user request clearly needs it.
3. **Decides per request** whether to use only RAG, only the tool, or both (e.g. “What does the doc say about X?” → RAG; “What is 12 * 34?” → tool; you can keep the routing logic simple).

**Scope:**  
- Use a **small static corpus** (e.g. 3–5 markdown or text files you provide in the repo; no need for a large dataset).  
- One LLM provider is enough (e.g. OpenAI API, or a local/open model if you prefer).  
- One tool is enough; two is fine if you want to show tool routing.

**Out of scope for this POC:**  
- Multi-agent systems, complex memory, or production deployment.  
- Perfect accuracy or comprehensive evaluation.

---

## 3. Process (AI-Assisted Design)

1. **Discuss with an AI assistant** (recommended):  
   - Describe the task and ask for an architecture sketch (components, data flow, tech choices).  
   - Iterate on: RAG pipeline (chunking, retrieval, prompt), tool-calling pattern (e.g. function calling vs ReAct), and how the agent decides “RAG vs tool vs both.”  
   - You can paste this assignment into the assistant and refine the design together.

2. **Lock your design** and document it in the README (see Deliverables).

3. **Implement a minimal POC** that matches your design and runs end-to-end.

---

## 4. Deliverables (Single Zip)

Submit **one zip file** containing:

| Item | Required | Description |
|------|----------|-------------|
| **README** | Yes | Design doc + how to run the POC + **short “AI usage” section** (see below). |
| **Code** | Yes | Source code that runs with clear setup/run instructions (e.g. `README` or `scripts/README`). |
| **Sample docs** | Yes | The small document corpus (3–5 files) used for RAG. |
| **Env / config** | As needed | e.g. `.env.example` with placeholder API keys; no real secrets. |

### README must include

1. **Design**
   - High-level architecture (text + optional diagram).
   - Main components (e.g. retriever, LLM, tool executor, router/orchestrator).
   - Key choices (e.g. chunking strategy, retrieval method, how tool is invoked) and **one or two tradeoffs** you considered.

2. **How to run the POC**
   - Prerequisites (Python version, optional venv).
   - Install steps (e.g. `pip install -r requirements.txt`).
   - How to set API keys (e.g. copy `.env.example` to `.env`).
   - One or two example commands or a short CLI/script to run a RAG query and a tool query.

3. **AI usage (short)**
   - How you used an AI assistant during design (e.g. “Used Claude to sketch the RAG + tool flow and chose function calling over ReAct because …”).
   - What you changed or kept after the discussion (helps us see your judgment).

---

## 5. Tech Suggestions (Non-Binding)

- **Language:** Python preferred (fits our stack).
- **Libraries:** Any you like (e.g. LangChain, LangGraph, LlamaIndex, or minimal custom code with `openai` SDK).
- **Retrieval:** Simple vector search (e.g. in-memory with sentence-transformers, or FAISS/Chroma) is enough; no need for Elasticsearch unless you want to show it.
- **LLM:** Any one API (OpenAI, Azure OpenAI, DashScope, etc.) or a local model; document what you use.

---

## 6. Time and Submission

- **Suggested time:** 2–4 hours (design + POC).
- **Submission:** Reply to the email with **one zip file** named e.g. `yourname-ai-agent-poc.zip`.  
- **Deadline:** [To be filled by recruiter/hiring manager.]

---

## 7. Evaluation Focus

We will primarily evaluate:

1. **Design:** Clarity, coherence, and sensible tradeoffs (RAG vs tool routing, chunking, retrieval).
2. **POC:** Does it run? Does it demonstrate RAG and at least one tool call?
3. **Documentation:** Can we run it and understand your design and AI-assisted process?

If you have any clarification questions before submitting, you can ask the contact person for this role. Good luck.
