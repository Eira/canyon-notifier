from app.catalog.catalog_operations import get_canyon_catalog_html


def test_get_canyon_catalog_html():
    res = get_canyon_catalog_html()

    assert res is not None
