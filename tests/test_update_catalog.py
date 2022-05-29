from typing import List

from app.bike_model import Bike
from app.update import _update_catalog


async def test_update_catalog_happy_path(fixture_prefilled_catalog: List[Bike]):
    res = await _update_catalog(fixture_prefilled_catalog)

    assert res == (2, 2)
