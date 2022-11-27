from app.storage.catalog import clear_catalog, get_catalog


async def test_clear_catalog_empty(fixture_empty_catalog):
    res = await clear_catalog()

    assert await get_catalog() == []
    assert res == 0


async def test_clear_catalog_happy_pass(fixture_prefilled_catalog):
    res = await clear_catalog()

    assert await get_catalog() == []
    assert res == 2
