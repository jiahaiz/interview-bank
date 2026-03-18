"""Raised when the same event_id is submitted again (retry/duplicate)."""


class DuplicateEventException(Exception):
    """Event with this event_id was already ingested. Used internally; API may return 201 idempotently."""
    pass
