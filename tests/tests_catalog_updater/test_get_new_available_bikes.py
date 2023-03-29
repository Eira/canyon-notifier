from app.catalog.available_bike_list_operations import _get_new_available_bikes


def test_get_new_available_bikes_happy_path(
        fixture_bike_item_1,
        fixture_bike_item_2,
        fixture_bike_item_3,
):
    old_bikes_list = [fixture_bike_item_1, fixture_bike_item_2]
    new_bikes_list = [fixture_bike_item_1, fixture_bike_item_3]

    res = _get_new_available_bikes(old_bikes_list, new_bikes_list)

    assert res == [fixture_bike_item_3]


def test_get_new_available_bikes_empty_old_list(
        fixture_bike_item_1,
        fixture_bike_item_3,
):
    old_bikes_list = []
    new_bikes_list = [fixture_bike_item_1, fixture_bike_item_3]

    res = _get_new_available_bikes(old_bikes_list, new_bikes_list)

    assert res == new_bikes_list


def test_get_new_available_bikes_empty_new_list(
        fixture_bike_item_1,
        fixture_bike_item_2,
):
    old_bikes_list = [fixture_bike_item_1, fixture_bike_item_2]
    new_bikes_list = []

    res = _get_new_available_bikes(old_bikes_list, new_bikes_list)

    assert res == []


def test_get_new_available_bikes_empty_all_lists():
    old_bikes_list = []
    new_bikes_list = []

    res = _get_new_available_bikes(old_bikes_list, new_bikes_list)

    assert res == []
