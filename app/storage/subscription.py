"""Functions for processing subscriptions about new available bikes."""

from dataclasses import asdict
from typing import List, Optional

from app.models import SubscriptionBikeFamily
from app.storage.conection import db_pool

SUBSCRIPTION_ID_INCR_KEY = 'canyon-notifier:subscription:id_incr'
SUBSCRIPTIONS_KEY = 'canyon-notifier:subscriptions'
SUBSCRIPTION_BY_ID_KEY = 'canyon-notifier:subscription:{0}'
SUBSCRIPTION_BY_CHAT_KEY = 'canyon-notifier:chat:{0}:subscriptions'


async def create_subscription(chat_id: int, bike_family: str) -> SubscriptionBikeFamily:
    """Get data from user in bot. Return the object of subscription."""
    subscription_item = SubscriptionBikeFamily(
        subscribe_id=await db_pool.incr(SUBSCRIPTION_ID_INCR_KEY),
        chat_id=chat_id,
        bike_family=bike_family,
    )

    await db_pool.hset(SUBSCRIPTION_BY_ID_KEY.format(subscription_item.subscribe_id), mapping=asdict(subscription_item))
    await db_pool.sadd(SUBSCRIPTION_BY_CHAT_KEY.format(chat_id), subscription_item.subscribe_id)
    await db_pool.sadd(SUBSCRIPTIONS_KEY, subscription_item.subscribe_id)

    return subscription_item


async def get_subscriptions(chat_id: Optional[int] = None) -> List[SubscriptionBikeFamily]:
    """Get all subscriptions or only one user subscriptions from db. Return it like the list of subscriptions items."""
    if chat_id is None:
        db_key = SUBSCRIPTIONS_KEY
    else:
        db_key = SUBSCRIPTION_BY_CHAT_KEY.format(chat_id)

    subscribe_id_list = await db_pool.smembers(db_key)
    subscriptions_list = []

    for subscribe_id in subscribe_id_list:
        subscription = await db_pool.hgetall(SUBSCRIPTION_BY_ID_KEY.format(subscribe_id))
        subscriptions_list.append(
            SubscriptionBikeFamily(
                subscribe_id=int(subscription['subscribe_id']),
                chat_id=int(subscription['chat_id']),
                bike_family=subscription['bike_family'],
            ),
        )

    return subscriptions_list


async def get_subscription_amount(chat_id: int) -> int:
    """Count how many subscription user has. Return subscription amount."""
    return len(await get_subscriptions(chat_id))


async def delete_subscription(subscribe_id: int) -> bool:
    """Delete concrete subscriptions in database. Return amount of deleted subscriptions."""
    key_name = SUBSCRIPTION_BY_ID_KEY.format(subscribe_id)
    chat_id = await db_pool.hget(key_name, 'chat_id')

    if chat_id:
        await db_pool.delete(key_name)
        await db_pool.srem(SUBSCRIPTION_BY_CHAT_KEY.format(chat_id), subscribe_id)
        await db_pool.srem(SUBSCRIPTIONS_KEY, subscribe_id)

    return True
