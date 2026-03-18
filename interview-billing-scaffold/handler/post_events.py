"""POST /events: accept JSON event and store (idempotent by event_id).

TODO: Candidate implements validation (required fields, types) and calls service.ingest().
Returns 201 (created), 400 (invalid request), 500 (server error).
"""
from fastapi import Request, Response

from model.event import Event
from service.event_service import EventService


async def post_events(request: Request, event_service: EventService) -> Response:
    """Parse JSON, validate, ingest. Not implemented — returns 501 until candidate implements."""
    # TODO: implement — parse body, validate event_id/user_id/type/ts (return 400 if invalid), call event_service.ingest(), return 201
    return Response(status_code=501, content="Not implemented")
