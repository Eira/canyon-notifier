import pytest

from app.storage import clear_catalog, get_catalog


@pytest.mark.asyncio
async def test_clear_catalog_empty(fixture_empty_catalog):
    res = await clear_catalog()

    assert await get_catalog() == []
    assert res == 0


@pytest.mark.asyncio
async def test_clear_catalog(fixture_prefilled_catalog):
    res = await clear_catalog()

    assert await get_catalog() == []
    assert res == 2
