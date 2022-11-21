"""This module is parsing canyon catalog page to the database, and updating that catalog at given time intervals."""
import asyncio
import logging
from typing import List, Tuple

import httpx
from lxml import etree

from app import storage
from app.bike_model import Bike
from app.settings import app_settings


def _get_canyon_catalog_html() -> etree._Element:  # noqa: WPS437
    """Get HTML from the canyon catalog web page. Return HTML."""
    query_params = {
        'cgid': 'orderable-bikes',
        'prefn1': 'isInStock',
        'prefv1': 'In-stock',
        'start': '0',
        'sz': '300',
        'searchredirect': 'false',
        'pn': '1',
        'format': 'ajax',
    }

    catalog_response = httpx.get(
        'https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Search-IncludeProductGrid',
        timeout=app_settings.timeout,
        params=query_params,
    )
    html_source: str = catalog_response.text

    return etree.HTML(html_source)


def normalize_bike_id(bike_title: str) -> str:
    """Bring the id to the same view: lowercase, underscore instead of whitespace. Return bike id normalized."""
    return bike_title.replace(' ', '_').lower()


def _parse_canyon_catalog(html_tree: etree._Element) -> List[Bike]:  # noqa: WPS437, WPS210
    """Make the list of bike elements from HTML. Return list of bikes in elements."""
    output: List[Bike] = []

    html_bike_list = html_tree.cssselect('.productGrid__listItem')

    for list_item in html_bike_list:
        bike_name_element: etree.Element = list_item.cssselect('.productTile__link')[0]

        bike_title_list = bike_name_element.get('title').split(' ')
        if bike_name_element.get('title').startswith('Grand Canyon'):
            bike_family = f'{bike_title_list[0]} {bike_title_list[1]}'
            bike_model = ' '.join(bike_title_list[2:])
        else:
            bike_family = bike_title_list[0]
            bike_model = ' '.join(bike_title_list[1:])

        bike_item: Bike = Bike(
            id=normalize_bike_id(bike_name_element.get('title')),
            title=bike_name_element.get('title'),
            link=bike_name_element.get('href'),
            family=bike_family,
            model=bike_model,
        )
        output.append(bike_item)

    return output


async def _update_catalog(actual_catalog: List[Bike]) -> Tuple[int, int]:
    """Clear the old catalog in database and insert actual. Return amount of deleted and added items."""
    items_deleted: int = await storage.clear_catalog()
    items_added: int = await storage.insert_actual_catalog(actual_catalog)

    return items_deleted, items_added


def _get_canyon_catalog() -> List[Bike]:
    html_tree = _get_canyon_catalog_html()
    return _parse_canyon_catalog(html_tree)


def _get_new_available_bikes(old_catalog: List[Bike], actual_catalog: List[Bike]) -> List[Bike]:
    """Compare old list of available bikes with new one. Return list of bikes, that wasn't available before."""
    old_catalog_id = {bike.id for bike in old_catalog}

    return [
        new_bike
        for new_bike in actual_catalog
        if new_bike.id not in old_catalog_id
    ]


async def main(throttling_time: float, amount_of_iterations: int) -> int:
    """
    Do the main runner of our worker.

    Keep catalog of available bikes uptodate.
    # todo дописать
    Return amount of iterations.
    """
    cnt = 0
    while cnt < amount_of_iterations or not amount_of_iterations:
        if cnt:
            await asyncio.sleep(throttling_time)

        logging.info(f'Current iteration is {cnt}')
        cnt += 1

        actual_catalog: List[Bike] = _get_canyon_catalog()
        logging.info(f'{len(actual_catalog)} bikes was got')
        logging.debug(f'{actual_catalog=}')

        if not actual_catalog:
            logging.warning('empty catalog found!')
            continue

        available_bikes_list = _get_new_available_bikes(
            await storage.get_catalog(),
            actual_catalog,
        )

        await storage.save_new_available_bikes(available_bikes_list)
        items_deleted, items_added = await _update_catalog(actual_catalog)
        logging.info(f'{items_deleted} old bikes was deleted. {items_added} new bikes was added.')

    return cnt


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    asyncio.run(main(throttling_time=app_settings.throttling_time, amount_of_iterations=app_settings.amount_of_iterations))
