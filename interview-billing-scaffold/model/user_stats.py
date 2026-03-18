"""Stats response model for GET /users/{user_id}/stats."""
from dataclasses import dataclass
from typing import Any


@dataclass
class UserStats:
    """Aggregated statistics for a user's events."""
    total_count: int
    sum_value: float
    count_by_type: dict[str, int]

    def to_dict(self) -> dict[str, Any]:
        return {
            "totalCount": self.total_count,
            "sumValue": self.sum_value,
            "countByType": self.count_by_type,
        }
