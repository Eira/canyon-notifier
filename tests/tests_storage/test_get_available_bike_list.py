from app.models import Bike
from app.storage import get_available_bike_list


async def test_get_available_bike_list_happy_path(fixture_prefilled_available_bike_list):
    res = await get_available_bike_list()

    assert isinstance(res, list)
    for item in res:
        assert isinstance(item, Bike)
    assert set([bike.id for bike in res]) == set([bike.id for bike in fixture_prefilled_available_bike_list])


async def test_get_available_bike_list_empty_catalog(fixture_empty_available_bike_list):
    res = await get_available_bike_list()

    assert set([bike.id for bike in res]) == set()
