import pytest
from aioredis import ResponseError

from app.storage.available_bike_list import delete_available_bike_list, get_available_bike_list


async def test_delete_available_bike_list_happy_path(fixture_empty_available_bike_list):
    bike_id_set = {'spectral_125_cf_9', 'exceed_cf_7'}

    await delete_available_bike_list(bike_id_set)

    rest_bike_id_list = {
        bike.id
        for bike in await get_available_bike_list()
    }

    assert bike_id_set not in rest_bike_id_list


async def test_delete_available_bike_list_delete_all(fixture_empty_available_bike_list):
    await delete_available_bike_list()

    assert await get_available_bike_list() == []


async def test_delete_available_bike_list_empty_catalog(fixture_empty_available_bike_list):
    bike_id_set = set()

    with pytest.raises(ResponseError, match='wrong number of arguments*'):
        await delete_available_bike_list(bike_id_set)


async def test_delete_available_bike_list_wrong_id(fixture_empty_available_bike_list):
    bike_id_set = {'test123', 'test2123'}

    res = await delete_available_bike_list(bike_id_set)

    rest_bike_id_list = {
            bike.id
            for bike in await get_available_bike_list()
        }

    assert res is None
    assert bike_id_set not in rest_bike_id_list
