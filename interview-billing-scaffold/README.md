# Q2: Reliable Event Ingestion for Analytics Pipeline

> **If your interviewer used a design-only phase:** You should have discussed the problem **before** receiving this folder. Do not skip that discussion retroactively — implement to match what you agreed, then align with the tests below.

> **Interviewers:** For the **design phase without code**, use **`DESIGN_PHASE_SPEC.md`** only. See **`INTERVIEWER.md`**.

---

## How This Exercise Works (implementation phase)

1. **You already did design** (with your interviewer) — deduplication, validation, stats semantics. Now map that to this codebase.
2. **Tests do not pass initially** — The protected test suite and unit tests define the system requirements but **fail** because POST, GET, and the service layer are **not implemented** (stubbed).
3. **Your job** — Implement POST /events, GET /users/{user_id}/stats, and `EventService` so that **all tests pass** and the service meets the requirements. You may add more tests for edge cases.
4. **AI is allowed** — Use AI as you would in your normal workflow; you will be evaluated on both tech skill and how you use AI.

---

## Scenario

Your team runs an internal analytics pipeline. External services push event data to your HTTP API. The service feeds **two downstream consumers** with different reliability needs:

1. **Billing pipeline** — charges customers based on event counts. A double-counted event means an overcharge, which triggers a billing dispute and compliance review. Billing runs hourly batch jobs against your stats endpoint.

2. **Real-time analytics dashboard** — shows per-user activity to internal analysts. Staleness beyond 5 seconds is a P1 operations concern. The dashboard polls your stats endpoint every few seconds.

Operations has flagged several production issues:

- **Upstream clients retry after timeouts**, sometimes sending the same event two or more times. The billing team reports customers are being overcharged.
- **Events arrive out of order** — timestamps don't match arrival order.
- **The analytics dashboard shows incorrect counts** under burst traffic.

The previous developer left a **stub**: the HTTP server and routing exist, but **POST, GET, and the event service are not implemented**. A test suite defines the required behavior; the tests **fail** until you implement the logic.

**Your job:** Design your approach, then implement the service so that all system requirements are met and all tests pass.

## Choose Your Language

| Language | Build | Test |
|----------|-------|------|
| **Python** | — | `pytest -v` |

## API Surface

### POST /events

Accepts a JSON event and stores it. **Not implemented** — you must implement it.

**Request body:**
```json
{ "event_id": "e1", "user_id": "u1", "type": "click", "ts": 1000, "value": 1.5 }
```

**Response codes:**
| Status | Meaning |
|--------|---------|
| 201 | Event created |
| 400 | Invalid request |
| 500 | Server error |

### GET /users/{user_id}/stats

Returns aggregated statistics for a user's events. **Not implemented** — you must implement it.

**Expected response shape:**
```json
{
  "totalCount": 3,
  "sumValue": 7.0,
  "countByType": { "click": 2, "view": 1 }
}
```

## What You Receive

- A working HTTP server with routing (do not modify)
- **Stubbed** POST and GET handlers (return 501) — you implement them
- **Stubbed** `EventService` (ingest and get_user_stats not implemented) — you implement them
- In-memory event store (implemented; you use it from the service)
- A **protected test suite** that defines acceptance behavior — do not modify; make it pass
- **Unit tests** for `EventService` that fail until you implement the service

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run tests (they fail until you implement POST, GET, and EventService)
pytest -v

# Run API
uvicorn app:app --reload
```

## Project Structure

```
interview-billing-scaffold/
├── app.py                          # HTTP server (complete — do not modify)
├── handler/
│   ├── post_events.py              # POST /events — implement
│   └── get_user_stats.py           # GET /users/{id}/stats — implement
├── model/
│   ├── event.py                    # Event data model
│   └── user_stats.py               # Stats response model
├── service/
│   ├── event_service.py            # Business logic — implement ingest() and get_user_stats()
│   ├── duplicate_event_error.py    # Optional
│   └── test_event_service.py       # Unit tests (fail until service implemented); add more tests here
├── store/
│   ├── event_store.py              # Store interface
│   └── in_memory_event_store.py    # In-memory implementation (use as-is)
├── test_event_ingestion_server.py  # PROTECTED — do not modify; make tests pass
├── requirements.txt
└── README.md
```

## Rules

- **Design first**, then implement. The spec is intentionally incomplete — make and justify design decisions (e.g. dedup by event_id, validation rules).
- **All tests must pass** when you are done. The protected tests and the unit tests in `service/test_event_service.py` define the requirements.
- **AI tools are allowed and expected.** You are evaluated on both technical implementation and how you use AI.
- You must be able to explain any code you submit, including AI-generated code.
- You **may not modify** `test_event_ingestion_server.py`.
- You **may add** more tests in `service/test_event_service.py` for edge cases.
