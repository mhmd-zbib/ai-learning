"""Application factory and the ASGI `app` instance.

`create_app()` wires together configuration, logging, middleware, exception
handlers, and routers. Keeping construction in a factory makes the app easy to
configure differently in tests without import-time side effects leaking out.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.core.config import settings
from api.core.exceptions import register_exception_handlers
from api.core.lifespan import lifespan
from api.core.logging import configure_logging
from api.core.middleware.request_id import RequestIDMiddleware
from api.modules.health import router as health_router
from api.router import api_router


def create_app() -> FastAPI:
    configure_logging()

    app = FastAPI(
        title=settings.project_name,
        version=settings.version,
        debug=settings.debug,
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    app.add_middleware(RequestIDMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_exception_handlers(app)

    app.include_router(health_router)
    app.include_router(api_router, prefix=settings.api_v1_prefix)

    return app


app = create_app()
