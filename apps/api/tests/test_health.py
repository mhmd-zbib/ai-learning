"""Smoke tests for the health/metadata endpoints."""

from httpx import AsyncClient


async def test_health_ok(client: AsyncClient) -> None:
    response = await client.get("/health")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert "version" in body
    assert "environment" in body


async def test_readiness_ok(client: AsyncClient) -> None:
    response = await client.get("/health/ready")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


async def test_request_id_header_is_returned(client: AsyncClient) -> None:
    response = await client.get("/health")

    assert response.headers.get("X-Request-ID")
