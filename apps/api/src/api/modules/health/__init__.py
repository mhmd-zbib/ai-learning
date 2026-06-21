"""Health module: liveness/readiness probes and service metadata."""

from api.modules.health.router import router

__all__ = ["router"]
