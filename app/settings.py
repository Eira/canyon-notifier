"""Application settings."""
import os
from typing import Optional

from pydantic import BaseSettings, RedisDsn


class AppSettings(BaseSettings):
    """Application settings class."""

    redis_dsn: Optional[RedisDsn] = None
    timeout: int = 10
    throttling_time: float = 600.0
    debug: bool = False


app_settings = AppSettings(
    _env_file=os.path.join(os.path.dirname(__file__), '..', '.env'),
)
