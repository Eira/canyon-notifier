import pytest
from redis import asyncio as aioredis

from app.storage.available_bike_list import save_new_available_bikes, get_available_bike_list


async def test_save_new_available_bikes_happy_path(fixture_prefilled_available_bike_list):
    res = await save_new_available_bikes(fixture_prefilled_available_bike_list)

    assert res is None
    assert set([bike.id for bike in await get_available_bike_list()]) == set([bike.id for bike in fixture_prefilled_available_bike_list])


async def test_save_new_available_bikes_empty_list():
    with pytest.raises(aioredis.ResponseError, match='wrong number of arguments*'):
        await save_new_available_bikes([])
