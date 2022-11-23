from app.storage import get_available_bike_list


async def test_get_available_bike_list_happy_path(fixture_prefilled_available_bike_list):
    res = await get_available_bike_list()

    assert res == fixture_prefilled_available_bike_list

# todo test на пустой каталог
