# Evaluator Rubric: AI Agent Design & POC

Use this when reviewing the candidate’s zip (README + code). **Primary focus: design and POC**, not production quality.

---

## 1. Design (Highest Weight)

| Criterion | 1 – Weak | 2 – Adequate | 3 – Good | 4 – Strong |
|----------|----------|--------------|----------|------------|
| **Architecture clarity** | Unclear or missing components | Components listed but flow unclear | Clear components and data flow; diagram or structured text | Clear architecture with explicit boundaries and one sensible alternative considered |
| **RAG design** | No or vague RAG description | Chunking/retrieval mentioned | Chunking + retrieval + prompt role described | Chunking strategy justified; retrieval choice (e.g. vector vs keyword) and tradeoff stated |
| **Tool integration** | Tool not integrated or not described | One tool present; no design explanation | Tool(s) and invocation pattern (e.g. function calling) described | Tool design and routing (when to call) explained with a tradeoff |
| **Tradeoffs** | None discussed | One tradeoff mentioned | 1–2 tradeoffs with reasoning | Multiple tradeoffs (e.g. latency vs accuracy, simplicity vs flexibility) with clear reasoning |

**Design notes (free text):**  
…………………………………………………………………………………………………………………  
…………………………………………………………………………………………………………………

---

## 2. POC (Runnable Demo)

| Criterion | 1 – Weak | 2 – Adequate | 3 – Good | 4 – Strong |
|----------|----------|--------------|----------|------------|
| **Runs** | Does not run or major steps missing | Runs with non-obvious fixes | Runs with README instructions | Runs first time with README; env/config clear |
| **RAG works** | No retrieval or no answer from docs | Retrieval or answer broken/incomplete | Correct answer over provided docs for at least one query | Multiple RAG queries work; retrieval clearly used |
| **Tool works** | Tool not implemented or not callable | Tool exists but not invoked correctly | One tool call works (e.g. calculator/time) | Tool routing works (e.g. “what is 2+2” → tool; doc question → RAG) |
| **Code quality** | Unreadable or no structure | Readable but messy | Clear structure; main flow easy to follow | Clear structure; minimal but coherent; easy to extend |

**POC notes (free text):**  
…………………………………………………………………………………………………………………  
…………………………………………………………………………………………………………………

---

## 3. Documentation & AI Usage

| Criterion | 1 – Weak | 2 – Adequate | 3 – Good | 4 – Strong |
|----------|----------|--------------|----------|------------|
| **README** | Missing or cannot run from it | Run steps exist but incomplete | Complete run steps; design summarized | Run steps + design + tradeoffs; optional diagram |
| **AI usage section** | Missing or generic | Briefly mentions using AI | Describes how AI was used for design | Explains AI role and what candidate kept/changed (shows judgment) |

**Doc notes (free text):**  
…………………………………………………………………………………………………………………  
…………………………………………………………………………………………………………………

---

## 4. Overall

| Dimension | Score (1–4) | Comment |
|-----------|--------------|--------|
| Design | __ / 4 | |
| POC | __ / 4 | |
| Documentation & AI usage | __ / 4 | |

**Summary (design + POC by AI):**  
…………………………………………………………………………………………………………………  
…………………………………………………………………………………………………………………  
**Recommendation:** Proceed to interview / Reject / Borderline (discuss in debrief)
