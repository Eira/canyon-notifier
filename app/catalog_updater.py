"""This module is parsing canyon catalog page to the database, and updating that catalog at given time intervals."""
import asyncio
import logging
from typing import List

from app import storage
from app.catalog.available_bike_list_operations import update_available_bikes_list
from app.catalog.catalog_operations import get_canyon_catalog, update_catalog
from app.models import Bike
from app.settings import app_settings


async def main(throttling_time: float, amount_of_iterations: int) -> int:
    """
    Do the main runner of catalog updater worker.

    Keep catalog of available bikes uptodate.
    Create also a list of bikes that wasn't available before (needed for subscriptions).
    Return amount of iterations.
    """
    cnt = 0
    while cnt < amount_of_iterations or not amount_of_iterations:
        if cnt:
            await asyncio.sleep(throttling_time)

        logging.info(f'Current iteration is {cnt}')
        cnt += 1

        actual_catalog: List[Bike] = get_canyon_catalog()
        logging.info(f'{len(actual_catalog)} bikes was got')
        logging.debug(f'{actual_catalog=}')

        if not actual_catalog:
            logging.warning('empty catalog found!')
            continue

        old_catalog = await storage.get_catalog()

        items_deleted, items_added = await update_catalog(actual_catalog)
        await update_available_bikes_list(old_catalog, actual_catalog)
        logging.info(f'{items_deleted} old bikes was deleted. {items_added} new bikes was added.')

    return cnt


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    asyncio.run(main(throttling_time=app_settings.throttling_time, amount_of_iterations=app_settings.amount_of_iterations))
