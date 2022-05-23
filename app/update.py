"""todo docstring."""
import asyncio
import logging
import time
from typing import List, Tuple

import httpx
from lxml import etree

from app import storage
from app.bike_model import Bike
from app.settings import app_settings


def _get_canyon_catalog_html() -> etree._Element:  # noqa: WPS437
    query_params = {
        'prefn1': 'isInStock',
        'prefv1': 'In-stock',
        'prefn2': 'masterAvailabilityFlag',
        'prefv2': '1',
        'start': '0',
        'sz': '125',
        'searchredirect': 'false',
        'pn': '1',
        'format': 'ajax',
    }
    catalog_response = httpx.get(
        'https://www.canyon.com/en-cz/orderable-bikes/',
        timeout=app_settings.timeout,
        params=query_params,
    )
    html_source: str = catalog_response.text

    return etree.HTML(html_source)


def _parse_canyon_catalog(html_tree: etree._Element) -> List[Bike]:  # noqa: WPS437
    output: List[Bike] = []

    html_bike_list = html_tree.cssselect('.productGrid__listItem')

    for list_item in html_bike_list:
        bike_name_element: etree.Element = list_item.cssselect('.productTile__link')[0]
        bike_item: Bike = Bike(
            title=bike_name_element.get('title'),
            link=bike_name_element.get('href'),
        )
        output.append(bike_item)
    return output


def _get_canyon_catalog() -> List[Bike]:
    html_tree = _get_canyon_catalog_html()
    return _parse_canyon_catalog(html_tree)


async def _update_catalog(uptodate_catalog: List[Bike]) -> Tuple[int, int]:
    # TODO unit test
    items_deleted: int = storage.clear_catalog()
    items_added: int = await storage.insert_actual_catalog(uptodate_catalog)

    return items_deleted, items_added


async def main(throttling_time: float) -> None:
    """Держит актуальным каталог велосипедов в наличии."""
    # todo unittest
    cnt = 0
    while cnt < 2:  # todo написать true
        if cnt:
            time.sleep(throttling_time)

        logging.info(f'Current iteration is {cnt}')
        cnt += 1
        # todo try except for request errors

        actual_catalog: List[Bike] = _get_canyon_catalog()
        logging.info(f'{len(actual_catalog)} bikes was got')
        logging.debug(f'{actual_catalog=}')

        if not actual_catalog:
            logging.warning('empty catalog found!')
            continue

        items_deleted, items_added = await _update_catalog(actual_catalog)
        logging.info(f'{items_deleted} old bikes was deleted. {items_added} new bikes was added.')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG if app_settings.debug else logging.INFO)

    asyncio.run(main(throttling_time=app_settings.throttling_time))
