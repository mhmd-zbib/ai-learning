"""Logging configuration.

A single ``configure_logging`` call set up at app construction. Kept minimal for
now; swap the formatter for structured/JSON logging when wiring up tracing.
"""

import logging

from api.core.config import settings

_LOG_FORMAT = "%(asctime)s %(levelname)-8s %(name)s: %(message)s"


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.DEBUG if settings.debug else logging.INFO,
        format=_LOG_FORMAT,
    )
