"""Health module business logic."""

from api.core.config import settings
from api.modules.health.schemas import HealthResponse


def get_health() -> HealthResponse:
    """Liveness: the process is up and serving."""
    return HealthResponse(
        status="ok",
        version=settings.version,
        environment=settings.environment,
    )


def get_readiness() -> HealthResponse:
    """Readiness: the service is able to handle traffic."""
    # TODO: probe dependencies (DB, cache, vector store) before reporting ready.
    return get_health()
