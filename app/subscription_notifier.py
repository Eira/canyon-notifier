"""
This is the module of subscription notifier.

It contains functions for sending messages to the user
when the bike, to which the user is subscribed, is available in the store.
"""
import asyncio
import logging
from typing import List

from aiogram.utils.exceptions import BadRequest

from app.bot_runner import bot
from app.models import Bike, Match, SubscriptionBikeFamily
from app.settings import app_settings
from app.storage.available_bike_list import delete_available_bike_list, get_available_bike_list
from app.storage.subscription import delete_subscription, get_subscriptions


def _get_notification_bikes(
    subscription_list: List[SubscriptionBikeFamily],
    available_bike_list: List[Bike],
) -> List[Match]:
    """Compare list of notifications with list of new available bikes. Return list of results."""
    list_of_matches: List[Match] = []

    for subscription in subscription_list:
        subscriptions_search_phrase = subscription.bike_family.lower()

        for bike in available_bike_list:
            bike_title = bike.title.lower()

            if subscriptions_search_phrase in bike_title:
                list_of_matches.append(Match(bike, subscription))

    return list_of_matches


async def _send_subscription_message(subscription_to_send: Match) -> bool:
    """Get data about the available bike which user subscribed at and notify user about it."""
    message = '\n'.join((
        f'{subscription_to_send.bike.title} is available in the stock!',
        f'{subscription_to_send.bike.link}',
    ))

    await bot.send_message(subscription_to_send.subscription.chat_id, message)

    return True


async def _notify_users(list_of_matches: list[Match]) -> int:
    """Send messages about available bikes to subscribers when bikes appear in the store. Returns number of sent messages."""
    cnt_messages = 0
    for match in list_of_matches:
        try:
            await _send_subscription_message(match)
        except BadRequest:
            logging.warning('Chat is not found.')
            await delete_subscription(match.subscription.subscribe_id)
        cnt_messages += 1

    return cnt_messages


async def main(throttling_time: float, amount_of_iterations: int) -> int:
    """
    Do the main runner of subscription notifier worker.

    Get data about new available bikes, users subscribed at.
    Send messages about it.
    Return amount of iterations.
    """
    cnt = 0
    while cnt < amount_of_iterations or not amount_of_iterations:
        if cnt:
            await asyncio.sleep(throttling_time)

        subscription_list = await get_subscriptions()
        available_bike_list = await get_available_bike_list()
        list_of_matches = _get_notification_bikes(subscription_list, available_bike_list)

        if list_of_matches:
            cnt_messages = await _notify_users(list_of_matches)
            logging.info(f'{len(list_of_matches)} matches was found.')
            logging.info(f'{cnt_messages} messages was sent.')

            await delete_available_bike_list([
                bike.id for bike in available_bike_list
            ])

        logging.info(f'Current iteration is {cnt}')
        cnt += 1

    return cnt


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    asyncio.run(main(throttling_time=app_settings.throttling_time, amount_of_iterations=app_settings.amount_of_iterations))
