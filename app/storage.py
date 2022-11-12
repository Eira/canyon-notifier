"""Methods for access the database."""
import datetime
from dataclasses import asdict
from typing import List

import aioredis

from app.bike_model import Bike, SubscriptionBikeFamily
from app.settings import app_settings

BIKE_KEY = 'canyon-notifier:bike:{0}'
ACTUAL_CATALOG_KEY = 'canyon-notifier:catalog'
CATALOG_UPDATE_DATE_KEY = 'canyon-notifier:catalog:last_update_date'
SUBSCRIPTION_ID_INCR_KEY = 'canyon-notifier:subscription:id_incr'
SUBSCRIPTION_KEY = 'canyon-notifier:subscription:{0}'
SUBSCRIPTION_BY_CHAT_KEY = 'canyon-notifier:chat:{0}:subscriptions'

db_pool: aioredis.Redis = aioredis.from_url(
    app_settings.redis_dsn,
    encoding='utf-8',
    decode_responses=True,
)


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


#async def insert_new_


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


async def create_subscription(chat_id: int, bike_family: str) -> SubscriptionBikeFamily:
    """Get data from user in bot. Return the object of subscription."""
    subscription_item = SubscriptionBikeFamily(
        subscribe_id=await db_pool.incr(SUBSCRIPTION_ID_INCR_KEY),
        chat_id=chat_id,
        bike_family=bike_family,
    )

    await db_pool.hset(SUBSCRIPTION_KEY.format(subscription_item.subscribe_id), mapping=asdict(subscription_item))
    await db_pool.sadd(SUBSCRIPTION_BY_CHAT_KEY.format(chat_id), subscription_item.subscribe_id)

    return subscription_item


async def get_subscriptions(chat_id: int) -> List[SubscriptionBikeFamily]:
    """Get all users subscriptions from db. Return it like the list of subscriptions items."""
    subscribe_id_list = await db_pool.smembers(SUBSCRIPTION_BY_CHAT_KEY.format(chat_id))
    subscriptions_list = []

    for subscribe_id in subscribe_id_list:
        subscription = await db_pool.hgetall(SUBSCRIPTION_KEY.format(subscribe_id))
        bike_family_item = SubscriptionBikeFamily(
            subscribe_id=int(subscription['subscribe_id']),
            chat_id=int(subscription['chat_id']),
            bike_family=subscription['bike_family'],
        )
        subscriptions_list.append(bike_family_item)

    return subscriptions_list


async def delete_subscription(subscribe_id: int) -> bool:
    """Delete concrete subscriptions in database. Return amount of deleted subscriptions."""
    key_name = SUBSCRIPTION_KEY.format(subscribe_id)
    chat_id = await db_pool.hget(key_name, 'chat_id')

    if chat_id:
        await db_pool.delete(key_name)
        await db_pool.srem(SUBSCRIPTION_BY_CHAT_KEY.format(chat_id), subscribe_id)

    return True
