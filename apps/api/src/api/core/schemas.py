"""Pydantic schemas shared across modules.

Module-specific request/response models live in that module's own
``schemas.py``.
"""

from pydantic import BaseModel


class Message(BaseModel):
    """Generic single-message response."""

    detail: str
