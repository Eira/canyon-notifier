"""Application settings."""

import os

from pydantic import BaseSettings, RedisDsn


class AppSettings(BaseSettings):
    """Application settings class."""

    redis_dsn: RedisDsn


app_settings = AppSettings(
    _env_file=os.path.join(os.path.dirname(__file__), '..', '.env'),
)
