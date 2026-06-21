"""Database engine, session, and declarative base.

Module entity models (e.g. ``modules/users/entity.py``) subclass ``Base``.
Depend on ``DbDep`` in routes/services to get a session per request.
"""

from collections.abc import Iterator
from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from api.core.config import settings

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db() -> Iterator[Session]:
    with SessionLocal() as session:
        yield session


DbDep = Annotated[Session, Depends(get_db)]
