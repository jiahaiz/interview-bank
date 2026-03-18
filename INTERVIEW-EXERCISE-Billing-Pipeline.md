# In-Interview Exercise: Billing Pipeline (Design + AI-Assisted Build)

**Use:** During the technical interview.  
**Goal:** See how the candidate uses **AI** to go from **system design** to a **released service** (APIs + duplicate handling + consistency + unit tests). Keep it simple.

---

## 1. What We Evaluate

- **System design:** Clear APIs, duplicate handling, consistency choices.
- **AI skill:** How they prompt, iterate, and correct with an AI assistant to produce runnable code and tests.
- **Outcome:** A minimal but working billing pipeline (GET/POST, no duplicates, consistent behavior, a few unit tests).

---

## 2. Exercise Flow (in interview)

| Phase | Duration (suggested) | What happens |
|-------|----------------------|----------------|
| **1. Design** | ~15–20 min | Candidate designs a simple billing pipeline: GET/POST APIs, how to handle duplicates, consistency (e.g. double charge, read-after-write). Whiteboard or doc. |
| **2. Build with AI** | ~25–35 min | Candidate uses an AI assistant (Cursor/ChatGPT/Claude, etc.) to implement the service: API layer, storage, idempotency/duplicate handling, and a few unit tests. |
| **3. Wrap-up** | ~5 min | Run the service and tests; briefly discuss tradeoffs and what they’d improve. |

Total ~45–60 min. Candidate can share screen so you see how they work with AI.

---

## 3. Problem Statement (give to candidate)

**Build a minimal billing pipeline service.**

- **POST** – Create a billing record (e.g. `user_id`, `amount`, `currency`, idempotency key).
- **GET** – Get a billing record by id (or by idempotency key).
- **Duplicate handling:** Same request (e.g. same idempotency key) must not create two charges; explain your approach (e.g. idempotency key in DB, return existing).
- **Consistency:** Describe how you avoid double charge and keep reads consistent (e.g. single DB, transaction, or simple rules).

No auth, no real payment gateway. In-memory or SQLite is enough. Focus on API shape, duplicate handling, and consistency design.

---

## 4. Design Points to Probe (interviewer)

- **APIs:** RESTful GET/POST; request/response shape (e.g. idempotency key in header or body).
- **Duplicate handling:** Idempotency key stored and checked before insert; return 200 + same resource if key seen before (no 201 duplicate).
- **Consistency:** One source of truth (e.g. one DB/table); POST in a transaction if needed; GET reads after write (or eventual consistency if they mention it—discuss tradeoff).
- **Storage:** Table/key design (e.g. `id`, `idempotency_key` unique, `user_id`, `amount`, `currency`, `created_at`).

---

## 5. Implementation Expectations (with AI)

Candidate uses AI to generate/refine:

- **Service/API:** e.g. FastAPI or Flask with POST (create billing) and GET (by id or idempotency_key).
- **Storage:** In-memory dict or SQLite; idempotency key unique constraint or check.
- **Duplicate logic:** On POST, if idempotency key exists → return existing record (same response body), same status (e.g. 200); no second insert.
- **Unit tests:** At least 2–3 tests, e.g.: (1) POST then GET returns same data, (2) duplicate POST (same key) returns same record and no double charge, (3) GET missing id → 404.

No need for Docker, CI, or production deployment. “Release” = service runs and tests pass.

---

## 6. Deliverable (by end of interview)

- **Design:** On whiteboard or in a doc (APIs, duplicate handling, consistency).
- **Code:** Small project (e.g. one app file + one test file) that runs.
- **Tests:** `pytest` or similar; run and show green.
- **How they used AI:** Observable from screen share; optionally 1–2 sentences at the end (“I used AI to … then I changed …”).

---

## 7. Evaluation (short)

| Dimension | What to look for |
|-----------|-------------------|
| **Design** | Clear GET/POST, idempotency key, one sensible consistency approach. |
| **Duplicate handling** | Same key → no second record; returns existing. |
| **Consistency** | No double charge; reads make sense (e.g. after POST, GET sees it). |
| **AI skill** | Good prompts, iterates on errors, doesn’t blindly accept wrong code. |
| **Tests** | A few unit tests that cover happy path and duplicate case. |

Keep it simple; we care more about design clarity and effective use of AI than production-grade code.
