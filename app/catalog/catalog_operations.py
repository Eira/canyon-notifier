"""
This is the module of catalog updater.

It contains functions for create and update catalog of bicycles from canyon web page.
"""

from typing import List, Tuple

import httpx
from lxml import etree

from app.models import Bike
from app.settings import app_settings
from app.storage.catalog import clear_catalog, insert_actual_catalog


def get_canyon_catalog() -> List[Bike]:
    """Get html from the web page. Return list of bikes in elements."""
    html_tree = _get_canyon_catalog_html()
    return _parse_canyon_catalog(html_tree)


async def update_catalog(actual_catalog: List[Bike]) -> Tuple[int, int]:
    """Clear the old catalog in database and insert actual. Return amount of deleted and added items."""
    items_deleted: int = await clear_catalog()
    items_added: int = await insert_actual_catalog(actual_catalog)

    return items_deleted, items_added


def _create_bike_id(bike_title: str, bike_size: str) -> str:
    """Bring the id to the same view: lowercase, underscore instead of whitespace + bike size. Return bike id."""
    if not bike_title or not bike_size:
        raise RuntimeError('No bike title or bike size.')

    return '{title}_{size}'.format(
        title=bike_title.replace(' ', '_').lower(),
        size=bike_size.lower(),
    )


def _get_canyon_catalog_html() -> etree._Element:  # noqa: WPS437
    """Get HTML from the canyon catalog web page. Return HTML."""
    query_params = {
        'srule': 'sort_master_availability',
        'searchredirect': 'false',
        'start': '0',
        'sz': '300',
        'pn': '1',
        'format': 'ajax',
        'prefn1': 'pc_rahmengroesse',
        'prefv1': '3XS|2XS|XS|S|M|L|XL|2XL',
    }
    catalog_response = httpx.get(
        'https://www.canyon.com/en-de/buying-tools/in-stock-bikes/',
        timeout=app_settings.timeout,
        params=query_params,
    )
    html_source: str = catalog_response.text

    return etree.HTML(html_source)


def _parse_canyon_catalog(html_tree: etree._Element) -> List[Bike]:  # noqa: WPS437
    """Make the list of bike elements from HTML. Return list of bikes in elements."""
    output: List[Bike] = []

    html_bike_list = html_tree.cssselect('.productGrid__listItem')
    for list_item in html_bike_list:
        bike_item_list = _parse_bike_list_item(list_item)
        if bike_item_list:
            output += bike_item_list

    return output


def _parse_bike_list_item(list_item: etree._Element) -> list[Bike]:  # noqa: WPS437, WPS210
    """Make the list of bike elements for one bike model from HTML. Return list of bikes in elements."""
    try:
        bike_name_element: etree.Element = list_item.cssselect('.productTileDefault__productName')[0]
    except IndexError:
        return []

    bike_title_list = bike_name_element.get('title').split(' ')
    if bike_name_element.get('title').startswith('Grand Canyon'):
        bike_family = f'{bike_title_list[0]} {bike_title_list[1]}'
        bike_model = ' '.join(bike_title_list[2:])
    else:
        bike_family = bike_title_list[0]
        bike_model = ' '.join(bike_title_list[1:])

    link: str = bike_name_element.get('href')
    if not link.startswith('http'):
        link = f'https://www.canyon.com{link}'

    try:
        sizes_element = list_item.xpath('.//li[contains(@class, productBadges__listItem)]//span')[0]
    except IndexError:
        return []
    sizes = sizes_element.text.replace('Available to buy in ', '').strip().split('|')

    return [
        Bike(
            id=_create_bike_id(bike_name_element.get('title'), size.strip()),
            title=bike_name_element.get('title'),
            link=link,
            family=bike_family,
            model=bike_model,
            size=size.strip(),
        )
        for size in sizes
    ]
