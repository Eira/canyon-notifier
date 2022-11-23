from app.storage import get_available_bike_list, delete_available_bike_list


async def test_delete_available_bike_list_happy_path(fixture_empty_available_bike_list):
    bike_id_set = {'spectral_125_cf_9', 'exceed_cf_7'}

    await delete_available_bike_list(bike_id_set)

    rest_bike_id_list = {
        bike.id
        for bike in await get_available_bike_list()
    }

    assert bike_id_set not in rest_bike_id_list

# todo test на пустой каталог
# todo test на уже удаленный байк из списка доступных
