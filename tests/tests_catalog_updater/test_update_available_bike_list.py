from app.catalog.available_bike_list_operations import update_available_bikes_list


async def test_update_available_bike_list_happy_path(
        mocker,
        fixture_bike_item_1,
        fixture_bike_item_2,
        fixture_bike_item_3,
):
    mock = mocker.patch('app.catalog.available_bike_list_operations.save_new_available_bikes')
    old_bikes_list = [fixture_bike_item_1, fixture_bike_item_2]

    new_bikes_list = [fixture_bike_item_1, fixture_bike_item_3]

    res = await update_available_bikes_list(old_bikes_list, new_bikes_list)

    assert res == [fixture_bike_item_3]

    assert mock.call_count == 1


async def test_update_available_bike_list_empty_old_list(
        fixture_bike_item_1,
        fixture_bike_item_3,
):
    old_bikes_list = []
    new_bikes_list = [fixture_bike_item_1, fixture_bike_item_3]

    res = await update_available_bikes_list(old_bikes_list, new_bikes_list)

    assert res == []


async def test_update_available_bike_list__empty_new_list(
        mocker,
        fixture_bike_item_1,
        fixture_bike_item_2,
):
    mock = mocker.patch('app.catalog.available_bike_list_operations.save_new_available_bikes')
    old_bikes_list = [fixture_bike_item_1, fixture_bike_item_2]
    new_bikes_list = []

    res = await update_available_bikes_list(old_bikes_list, new_bikes_list)

    assert res == []
    assert mock.call_count == 0
