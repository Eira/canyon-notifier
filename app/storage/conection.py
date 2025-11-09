"""Connection to Redis."""

from redis import asyncio as aioredis

from app.settings import app_settings

db_pool: aioredis.Redis = aioredis.from_url(
    app_settings.redis_dsn,
    encoding='utf-8',
    decode_responses=True,
)
