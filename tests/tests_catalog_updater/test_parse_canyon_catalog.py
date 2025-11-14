from lxml import etree

from app.catalog.catalog_operations import _parse_canyon_catalog


def test_parse_canyon_catalog_not_found():
    no_bike_tree = etree.HTML('<ul></ul>')

    res = _parse_canyon_catalog(no_bike_tree)

    assert len(res) == 0





