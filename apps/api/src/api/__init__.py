"""Lumen API package.

The ASGI application lives in :mod:`api.app` (`api.app:app`). This module only
exposes the `main` console-script entry point so importing the package stays
cheap and free of side effects.
"""


def main() -> None:
    """Run the API with uvicorn. Entry point for the `api` console script."""
    import uvicorn

    from api.core.config import settings

    uvicorn.run(
        "api.app:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )
