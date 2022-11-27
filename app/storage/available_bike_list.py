"""Functions for processing list of available bikes, that is needed for subscriptions."""

from typing import List, Optional

from app.models import Bike
from app.storage.catalog import BIKE_KEY
from app.storage.conection import db_pool

SUBSCRIPTION_AVAILABLE_KEY = 'canyon-notifier:subscription:available'


async def save_new_available_bikes(available_bikes_list: List[Bike]) -> None:
    """Save list available bikes, mentioned in subscriptions, to the database."""
    await db_pool.sadd(
        SUBSCRIPTION_AVAILABLE_KEY,
        *[bike.id for bike in available_bikes_list],
    )


async def get_available_bike_list() -> List[Bike]:
    """Get bikes, now available in the store, from database. Return list of it."""
    output: List[Bike] = []
    bike_id_list = await db_pool.smembers(SUBSCRIPTION_AVAILABLE_KEY)

    for bike_id in bike_id_list:
        bike_item: Bike = Bike(
            **await db_pool.hgetall(BIKE_KEY.format(bike_id)),
        )

        output.append(bike_item)

    return output


async def delete_available_bike_list(bike_id_list: Optional[List[str]] = None) -> None:
    """Delete items from the list of available bikes."""
    if bike_id_list is None:
        await db_pool.delete(SUBSCRIPTION_AVAILABLE_KEY)
    else:
        await db_pool.srem(SUBSCRIPTION_AVAILABLE_KEY, *bike_id_list)
