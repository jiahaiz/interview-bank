"""
PROTECTED — Acceptance baseline for Event Ingestion API. Do not modify.

These tests define the expected behavior: POST /events (201, dedup), GET /users/{id}/stats.
"""
import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.fixture(autouse=True)
def _reset_app_state() -> None:
    from app import reset_event_service_for_test
    reset_event_service_for_test()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def test_post_events_returns_201(client: TestClient) -> None:
    """Valid event is accepted and returns 201."""
    r = client.post(
        "/events",
        json={"event_id": "e1", "user_id": "u1", "type": "click", "ts": 1000, "value": 1.5},
    )
    assert r.status_code == 201


def test_post_events_duplicate_same_event_id_no_double_count(client: TestClient) -> None:
    """Duplicate event_id (retry) must not double-count: POST twice, stats show count 1."""
    payload = {"event_id": "e-dup", "user_id": "u1", "type": "click", "ts": 1000, "value": 2.0}
    client.post("/events", json=payload)
    client.post("/events", json=payload)  # duplicate
    r = client.get("/users/u1/stats")
    assert r.status_code == 200
    data = r.json()
    assert data["totalCount"] == 1
    assert data["sumValue"] == 2.0


def test_get_user_stats_shape(client: TestClient) -> None:
    """GET /users/{user_id}/stats returns totalCount, sumValue, countByType with correct values."""
    client.post(
        "/events",
        json={"event_id": "e2", "user_id": "u2", "type": "view", "ts": 2000, "value": 0},
    )
    r = client.get("/users/u2/stats")
    assert r.status_code == 200
    data = r.json()
    assert "totalCount" in data
    assert "sumValue" in data
    assert "countByType" in data
    assert isinstance(data["countByType"], dict)
    assert data["totalCount"] == 1
    assert data["sumValue"] == 0
    assert data["countByType"] == {"view": 1}


def test_post_events_invalid_missing_field_returns_400(client: TestClient) -> None:
    """Missing required field returns 400."""
    r = client.post(
        "/events",
        json={"event_id": "e3", "user_id": "u3", "type": "click"},  # missing ts
    )
    assert r.status_code == 400


def test_health(client: TestClient) -> None:
    """Health check works."""
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}
