"""todo docstring."""

from typing import List

import httpx
from lxml import etree

from app import storage
from app.bike_model import Bike
from app.settings import app_settings


def _get_canyon_catalog_html() -> etree.HTML:
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


def _parse_canyon_catalog(html_tree: etree.HTML) -> List[Bike]:
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


def _update_catalog(uptodate_catalog: List[Bike]) -> None:
    # TODO unit test
    storage.clear_catalog()
    storage.insert_uptodate_catalog(uptodate_catalog)


def main() -> None:
    """Держит актуальным каталог велосипедов в наличии."""
    # todo while True:
        # todo не чаще чем раз в 10 минут (time.sleep)
        #_get_canyon_catalog()
        #_update_catalog()


if __name__ == '__main__':
    main()

# todo unittest _get_canyon_catalog
