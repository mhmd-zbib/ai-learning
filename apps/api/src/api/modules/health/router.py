"""Health module HTTP routes.

Mounted at the app root (not under the version prefix) because liveness and
readiness probes are operational endpoints, not part of the versioned API.
"""

from fastapi import APIRouter

from api.core.config import settings
from api.modules.health import service
from api.modules.health.schemas import HealthResponse

router = APIRouter(tags=["meta"])


@router.get("/", include_in_schema=False)
async def root() -> dict[str, str]:
    return {"service": settings.project_name, "docs": "/docs"}


@router.get("/health", response_model=HealthResponse, summary="Liveness probe")
async def health() -> HealthResponse:
    return service.get_health()


@router.get("/health/ready", response_model=HealthResponse, summary="Readiness probe")
async def readiness() -> HealthResponse:
    return service.get_readiness()
