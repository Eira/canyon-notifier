"""
This is the module of subscription notifier.

It contains functions for sending messages to the user when a bike to which the user is subscribed is available in the store.
"""
import asyncio
import logging

from app.bike_model import Bike
from app.settings import app_settings


def send_subscription_message(available_bike: Bike, subscriber: int) -> bool:
    """get data about the available bike which user subscribed at and notify user about it."""
    # todo impl
    # todo test

    return True


async def main(throttling_time: float, amount_of_iterations: int) -> int:
    """
    Do the main runner of subscription notifier worker.

    Get data about new available bikes, users subscribed.
    Send messages about it.
    Return amount of iterations.
    """
    # todo impl
    # todo test

    cnt = 0
    while cnt < amount_of_iterations or not amount_of_iterations:
        if cnt:
            await asyncio.sleep(throttling_time)

        logging.info(f'Current iteration is {cnt}')
        cnt += 1

#        if  #доступны новые велики из подписок в каталоге
#            send_subscription_message()

    return cnt


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    asyncio.run(main(throttling_time=app_settings.throttling_time, amount_of_iterations=app_settings.amount_of_iterations))
