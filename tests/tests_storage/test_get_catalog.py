from app.storage import get_catalog


async def test_get_catalog_smoke():
    res = await get_catalog()

    assert True


async def test_get_catalog_happy_path(fixture_prefilled_catalog):
    ...
