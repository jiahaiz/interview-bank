"""Event data model for ingestion."""
from dataclasses import dataclass
from typing import Any


@dataclass
class Event:
    """A single event from an external service."""
    event_id: str
    user_id: str
    type: str
    ts: int
    value: float = 0.0

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Event":
        return cls(
            event_id=str(data["event_id"]),
            user_id=str(data["user_id"]),
            type=str(data["type"]),
            ts=int(data["ts"]),
            value=float(data.get("value", 0)),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_id": self.event_id,
            "user_id": self.user_id,
            "type": self.type,
            "ts": self.ts,
            "value": self.value,
        }
