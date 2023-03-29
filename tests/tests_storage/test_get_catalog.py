from app.models import Bike
from app.storage.catalog import get_catalog


async def test_get_catalog_happy_path(
        fixture_prefilled_catalog,
        fixture_bike_item_1,
        fixture_bike_item_2,
):
    res = await get_catalog()

    assert res == [
        fixture_bike_item_2,
        fixture_bike_item_1,
    ]


async def test_get_catalog_empty_catalog(fixture_empty_catalog):
    res = await get_catalog()

    assert res == []
