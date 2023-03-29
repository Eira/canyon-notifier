from app.storage.catalog import insert_actual_catalog


async def test_insert_actual_catalog_empty_catalog(fixture_empty_catalog):
    res = await insert_actual_catalog([])

    assert res == 0


async def test_insert_actual_catalog_happy_path(fixture_bike_item_1, fixture_bike_item_2):
    bikes_list = [fixture_bike_item_1, fixture_bike_item_2]
    res = await insert_actual_catalog(bikes_list)

    assert res == 2
