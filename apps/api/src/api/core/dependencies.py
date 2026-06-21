"""FastAPI dependencies shared across modules (settings, auth, db sessions, ...).

Module-specific dependencies live in that module's own ``dependencies.py``.
Expose shared ones as ``Annotated`` aliases so routes read cleanly, e.g.
``def handler(settings: SettingsDep) -> ...``.
"""

from typing import Annotated

from fastapi import Depends

from api.core.config import Settings, get_settings

SettingsDep = Annotated[Settings, Depends(get_settings)]

__all__ = ["SettingsDep"]
