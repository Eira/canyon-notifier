import pytest

from app.storage import insert_actual_catalog


@pytest.mark.asyncio
async def test_insert_actual_catalog():
    res = await insert_actual_catalog([])

    assert res == 0
