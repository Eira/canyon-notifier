"""todo docstring."""

from dataclasses import dataclass
from typing import List

import httpx
from lxml import etree

from app.settings import app_settings


@dataclass
class Bike:
    """type of available bike."""

    title: str
    link: str


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


def _update_catalog() -> None:
    ...


def main() -> None:
    """Держит актуальным каталог велосипедов в наличии."""
    # todo while True:
        # todo не чаще чем раз в 10 минут (time.sleep)
        # todo get actual data from canyon (_get_canyon_catalog)
        # todo update data in storage (added new & deleted missed) (_update_catalog)
    _get_canyon_catalog()


if __name__ == '__main__':
    main()

# todo unittest _get_canyon_catalog
