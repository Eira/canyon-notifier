"""Connection to Redis."""

from redis import asyncio

from app.settings import app_settings

db_pool: asyncio.Redis = asyncio.from_url(
    app_settings.redis_dsn,
    encoding='utf-8',
    decode_responses=True,
)
