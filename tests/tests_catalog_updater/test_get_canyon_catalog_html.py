from lxml import etree

from app.catalog.catalog_operations import _get_canyon_catalog_html


def test_get_canyon_catalog_html():
    res = _get_canyon_catalog_html()

    assert res is not None
    assert isinstance(res, etree._Element)
