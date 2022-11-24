import pytest
from aioredis import ResponseError

from app.storage import get_available_bike_list, save_new_available_bikes


async def test_save_new_available_bikes_happy_path(fixture_prefilled_available_bike_list):
    res = await save_new_available_bikes(fixture_prefilled_available_bike_list)

    assert res is None
    assert set([bike.id for bike in await get_available_bike_list()]) == set([bike.id for bike in fixture_prefilled_available_bike_list])


async def test_save_new_available_bikes_empty_list():
    with pytest.raises(ResponseError, match='wrong number of arguments*'):
        await save_new_available_bikes([])
