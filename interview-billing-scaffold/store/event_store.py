"""Event store interface."""
from abc import ABC, abstractmethod
from typing import Optional

from model.event import Event
from model.user_stats import UserStats


class EventStore(ABC):
    """Abstract store for events and derived stats."""

    @abstractmethod
    def add(self, event: Event) -> None:
        """Store an event. Idempotency (same event_id) is handled by the service layer."""
        ...

    @abstractmethod
    def get_stats(self, user_id: str) -> UserStats:
        """Return aggregated stats for the given user."""
        ...

    @abstractmethod
    def has_event(self, event_id: str) -> bool:
        """Return True if an event with this event_id is already stored."""
        ...
