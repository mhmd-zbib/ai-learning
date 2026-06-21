"""Versioned API assembly.

Aggregates every feature module's router into a single ``api_router`` that
``api.app.create_app`` mounts under ``settings.api_v1_prefix``. Register a new
module here as it is built::

    from api.modules.courses import router as courses_router

    api_router.include_router(courses_router, prefix="/courses", tags=["courses"])

The health module is intentionally absent: its probes are mounted at the app
root, not under the version prefix.
"""

from fastapi import APIRouter

api_router = APIRouter()
