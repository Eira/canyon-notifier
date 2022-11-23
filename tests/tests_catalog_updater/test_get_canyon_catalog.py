from app.catalog_updater import _get_canyon_catalog
from app.models import Bike


def test_get_canyon_catalog():
    res = _get_canyon_catalog()

    assert isinstance(res, list)
    assert len(res) > 0
    for item in res:
        assert isinstance(item, Bike)
