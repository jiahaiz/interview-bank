"""Business logic: ingest events (with dedup) and compute user stats.

TODO: Candidate implements ingest() and get_user_stats() to meet requirements.
"""
from model.event import Event
from model.user_stats import UserStats
from store.event_store import EventStore


class EventService:
    """Handles event ingestion (idempotent by event_id) and stats queries."""

    def __init__(self, store: EventStore) -> None:
        self._store = store

    def ingest(self, event: Event) -> bool:
        """
        Ingest one event. Deduplication by event_id: if already seen, skip and return False.
        Returns True if the event was newly stored, False if it was a duplicate.
        """
        # TODO: implement — store event, deduplicate by event_id
        pass

    def get_user_stats(self, user_id: str) -> UserStats:
        """Return aggregated stats for the given user (totalCount, sumValue, countByType)."""
        # TODO: implement — aggregate events for user_id from store
        return UserStats(total_count=0, sum_value=0.0, count_by_type={})
