"""
Unit tests for EventService. These tests FAIL until the candidate implements
EventService.ingest() and EventService.get_user_stats() (and handlers as needed).

Candidate must design first, then implement to make these tests pass.
"""
import pytest

from model.event import Event
from service.event_service import EventService
from store.in_memory_event_store import InMemoryEventStore


@pytest.fixture
def event_service() -> EventService:
    """Fresh store per test."""
    return EventService(InMemoryEventStore())


def test_ingest_stores_event(event_service: EventService) -> None:
    """After ingest(event), get_user_stats for that user shows totalCount 1."""
    event = Event(event_id="e1", user_id="u1", type="click", ts=1000, value=1.5)
    event_service.ingest(event)
    stats = event_service.get_user_stats("u1")
    assert stats.total_count == 1
    assert stats.sum_value == 1.5
    assert stats.count_by_type == {"click": 1}


def test_ingest_dedup_no_double_count(event_service: EventService) -> None:
    """Same event_id ingested twice must count once (idempotent for billing)."""
    event = Event(event_id="e-dup", user_id="u1", type="click", ts=1000, value=2.0)
    event_service.ingest(event)
    event_service.ingest(event)  # duplicate
    stats = event_service.get_user_stats("u1")
    assert stats.total_count == 1
    assert stats.sum_value == 2.0


def test_get_user_stats_aggregates_by_type(event_service: EventService) -> None:
    """Multiple events for same user: totalCount, sumValue, countByType correct."""
    event_service.ingest(Event("e1", "u1", "click", 1000, 1.0))
    event_service.ingest(Event("e2", "u1", "click", 2000, 2.0))
    event_service.ingest(Event("e3", "u1", "view", 3000, 0))
    stats = event_service.get_user_stats("u1")
    assert stats.total_count == 3
    assert stats.sum_value == 3.0
    assert stats.count_by_type == {"click": 2, "view": 1}


def test_get_user_stats_unknown_user_returns_zero(event_service: EventService) -> None:
    """User with no events gets totalCount 0, sumValue 0, empty countByType."""
    stats = event_service.get_user_stats("nonexistent")
    assert stats.total_count == 0
    assert stats.sum_value == 0.0
    assert stats.count_by_type == {}
