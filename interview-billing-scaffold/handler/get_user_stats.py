"""GET /users/{user_id}/stats: return aggregated stats for the user.

TODO: Candidate implements by calling service.get_user_stats() and returning JSON.
Response shape: { "totalCount": int, "sumValue": float, "countByType": { str: int } }.
"""
from fastapi.responses import JSONResponse, Response

from service.event_service import EventService


async def get_user_stats(user_id: str, event_service: EventService) -> Response:
    """Return JSON stats. Not implemented — returns 501 until candidate implements."""
    # TODO: implement — call event_service.get_user_stats(user_id), return 200 + JSON
    return Response(status_code=501, content="Not implemented")
