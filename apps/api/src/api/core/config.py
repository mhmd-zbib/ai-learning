"""Application settings.

Loaded once from environment variables (prefix ``API_``) and an optional
``.env`` file. Import the module-level ``settings`` singleton, or depend on
``get_settings`` where you want it overridable in tests.
"""

from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

Environment = Literal["local", "staging", "production"]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="API_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Application
    project_name: str = "Lumen API"
    version: str = "0.1.0"
    environment: Environment = "local"
    debug: bool = False

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    # API
    api_v1_prefix: str = "/api/v1"

    # CORS — list of allowed origins (use ["*"] only for local development)
    cors_origins: list[str] = ["*"]


@lru_cache
def get_settings() -> Settings:
    """Return the cached settings instance."""
    return Settings()


settings = get_settings()
