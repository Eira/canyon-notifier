from app.catalog_updater import _get_canyon_catalog_html


def test_get_canyon_catalog_html():
    res = _get_canyon_catalog_html()

    assert res is not None
