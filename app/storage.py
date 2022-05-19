"""Methods for access the database."""
import datetime
from typing import List

import aioredis

from app.bike_model import Bike
from app.settings import app_settings

db_pool: aioredis.Redis = aioredis.from_url(
    app_settings.redis_dsn,
    encoding="utf-8",
    decode_responses=True,
)

def clear_catalog() -> int:
    """Delete old catalog in database."""
    # todo unit test
    # todo implement

    return 0  # amount of deleted bikes


async def insert_actual_catalog(uptodate_catalog: List[Bike]) -> int:
    """Save actual catalog to the database."""
    # todo unit test
    # todo implement

    await db_pool.set('last_update_date', str(datetime.datetime.utcnow()))

    return 0  # amount added bikes
