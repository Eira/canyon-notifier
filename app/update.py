"""todo docstring."""

from dataclasses import dataclass
from typing import List

import httpx

from app.settings import app_settings


@dataclass
class Bike:
    """type of available bike."""

    title: str
    link: str


def _get_canyon_catalog() -> List[Bike]:
    output: List[Bike] = []

    query_params = {
        'prefn1': 'isInStock',
        'prefv1': 'In - stock',
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
    html_source = catalog_response.text

    # todo find bike-blocks (ul.li) (https://lxml.de/parsing.html) (XPATH)

    # todo for i in bike-blocks:
        # todo search title+link
        # todo save new bike
    return output


def _update_catalog() -> None:
    ...


def main() -> None:
    """Держит актуальным каталог велосипедов в наличии."""
    # todo while True:
        # todo не чаще чем раз в 10 минут (time.sleep)
        # todo get actual data from canyon (_get_canyon_catalog)
        # todo update data in storage (added new & deleted missed) (_update_catalog)
    ...


if __name__ == '__main__':
    main()

# todo unittest _get_canyon_catalog
