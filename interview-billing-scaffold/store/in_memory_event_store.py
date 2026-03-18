"""In-memory implementation of EventStore."""
from collections import defaultdict
from threading import Lock

from model.event import Event
from model.user_stats import UserStats
from store.event_store import EventStore


class InMemoryEventStore(EventStore):
    """Thread-safe in-memory event store. Deduplication by event_id is enforced by EventService."""

    def __init__(self) -> None:
        self._events: list[Event] = []
        self._event_ids: set[str] = set()
        self._lock = Lock()

    def add(self, event: Event) -> None:
        with self._lock:
            if event.event_id in self._event_ids:
                return
            self._event_ids.add(event.event_id)
            self._events.append(event)

    def get_stats(self, user_id: str) -> UserStats:
        with self._lock:
            total_count = 0
            sum_value = 0.0
            count_by_type: dict[str, int] = defaultdict(int)
            for e in self._events:
                if e.user_id != user_id:
                    continue
                total_count += 1
                sum_value += e.value
                count_by_type[e.type] += 1
            return UserStats(
                total_count=total_count,
                sum_value=sum_value,
                count_by_type=dict(count_by_type),
            )

    def has_event(self, event_id: str) -> bool:
        with self._lock:
            return event_id in self._event_ids
