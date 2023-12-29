"""Functions for processing catalog of canyon bikes."""

import datetime
from dataclasses import asdict
from typing import List

from app.models import Bike
from app.storage.conection import db_pool

BIKE_KEY = 'canyon-notifier:bike:{0}'
ACTUAL_CATALOG_KEY = 'canyon-notifier:catalog'
CATALOG_UPDATE_DATE_KEY = 'canyon-notifier:catalog:last_update_date'


async def clear_catalog() -> int:
    """Delete old catalog in database. Return amount of deleted bikes."""
    deleted_bikes_amount = await db_pool.scard(ACTUAL_CATALOG_KEY)
    await db_pool.delete(ACTUAL_CATALOG_KEY)

    return deleted_bikes_amount


async def insert_actual_catalog(actual_catalog: List[Bike]) -> int:
    """Save actual catalog to the database. Return amount of inserted items."""
    for bike_item in actual_catalog:

        await db_pool.sadd(ACTUAL_CATALOG_KEY, bike_item.id)
        await db_pool.hset(BIKE_KEY.format(bike_item.id), mapping=asdict(bike_item))

    await db_pool.set(CATALOG_UPDATE_DATE_KEY, str(datetime.datetime.utcnow()))

    return await db_pool.scard(ACTUAL_CATALOG_KEY)


async def get_catalog() -> List[Bike]:
    """Get actual catalog from the database. Return list of bikes in elements."""
    list_bike_id = await db_pool.smembers(ACTUAL_CATALOG_KEY)

    output: List[Bike] = []
    for bike_id in list_bike_id:
        bike_item: Bike = Bike(
            **await db_pool.hgetall(BIKE_KEY.format(bike_id)),
        )
        output.append(bike_item)

    return sorted(output, key=lambda bike: bike.id)


async def get_update_date() -> str:
    """Get last catalog updated date."""
    return str(await db_pool.get(CATALOG_UPDATE_DATE_KEY)) or ''
