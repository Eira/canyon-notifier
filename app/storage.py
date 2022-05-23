"""Methods for access the database."""
import datetime
from dataclasses import asdict
from typing import List

import aioredis

from app.bike_model import Bike
from app.settings import app_settings

BIKE_KEY = 'canyon-notifier:bike:{0}'
ACTUAL_CATALOG_KEY = 'canyon-notifier:catalog'
CATALOG_UPDATE_DATE_KEY = 'canyon-notifier:catalog:last_update_date'

db_pool: aioredis.Redis = aioredis.from_url(
    app_settings.redis_dsn,
    encoding='utf-8',
    decode_responses=True,
)


def clear_catalog() -> int:
    """Delete old catalog in database."""
    # todo unit test
    # todo implement

    return 0  # amount of deleted bikes


async def insert_actual_catalog(actual_catalog: List[Bike]) -> int:
    """Save actual catalog to the database."""
    # todo unit test

    # todo implement
    for bike_item in actual_catalog:
        await db_pool.sadd(ACTUAL_CATALOG_KEY, bike_item.title)
        await db_pool.hset(BIKE_KEY.format(bike_item.title), mapping=asdict(bike_item))

    await db_pool.set(CATALOG_UPDATE_DATE_KEY, str(datetime.datetime.utcnow()))

    return await db_pool.scard(ACTUAL_CATALOG_KEY)
