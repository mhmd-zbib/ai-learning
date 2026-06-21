"""Application lifespan: startup and shutdown.

Initialize shared resources (DB pools, cache/vector-store clients, model
clients) on startup and release them on shutdown. Stash long-lived handles on
``app.state`` so dependencies can reach them.
"""

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    logger.info("Lumen API starting up")
    # TODO: acquire resources here (e.g. app.state.db = await create_pool())
    yield
    # TODO: release resources here
    logger.info("Lumen API shutting down")
