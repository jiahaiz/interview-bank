"""
Event Ingestion API – server and routing (complete; do not modify).

- POST /events — ingest event (idempotent by event_id)
- GET /users/{user_id}/stats — aggregated stats for user
"""
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends, Request

from handler.get_user_stats import get_user_stats as get_user_stats_handler
from handler.post_events import post_events as post_events_handler
from service.event_service import EventService
from store.in_memory_event_store import InMemoryEventStore


def get_event_service() -> EventService:
    store = InMemoryEventStore()
    return EventService(store)


# Single app-scoped service instance (in-memory state)
_event_service: EventService | None = None


def get_event_service_app() -> EventService:
    global _event_service
    if _event_service is None:
        _event_service = get_event_service()
    return _event_service


def reset_event_service_for_test() -> None:
    """Reset in-memory store between tests. Used only by the protected test suite."""
    global _event_service
    _event_service = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    get_event_service_app()
    yield
    # teardown if needed


app = FastAPI(
    title="Event Ingestion API",
    description="Reliable event ingestion for billing and analytics.",
    lifespan=lifespan,
)


@app.post("/events")
async def post_events(
    request: Request,
    event_service: Annotated[EventService, Depends(get_event_service_app)],
):
    return await post_events_handler(request, event_service)


@app.get("/users/{user_id}/stats")
async def get_user_stats(
    user_id: str,
    event_service: Annotated[EventService, Depends(get_event_service_app)],
):
    return await get_user_stats_handler(user_id, event_service)


@app.get("/health")
def health():
    return {"status": "ok"}
