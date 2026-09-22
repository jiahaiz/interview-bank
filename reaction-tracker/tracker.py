"""Reaction tracker — candidate starter file.

Standard library only. No web framework, no database.
Implement the two methods below. See SPEC.md for the requirements.
"""


class ReactionTracker:
    """Tracks which users are currently in the "liked" state for each target.

    ``record`` is called from several threads at once.
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def record(
        self,
        event_id: str,
        user_id: str,
        target_id: str,
        kind: str,
        ts: int,
    ) -> None:
        """Ingest one reaction event.

        ``kind`` is either ``"like"`` or ``"unlike"``.
        ``ts`` is an integer timestamp assigned by the producer.

        Events may arrive in any order, may be delivered more than once, and
        may be duplicated under different ``event_id`` values.
        """
        raise NotImplementedError

    def like_count(self, target_id: str) -> int:
        """Number of distinct users currently in the liked state for ``target_id``."""
        raise NotImplementedError
