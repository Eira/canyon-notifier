from typing import List

from app.catalog.catalog_operations import update_catalog
from app.models import Bike


async def test_update_catalog_happy_path(fixture_prefilled_catalog: List[Bike]):
    res = await update_catalog(fixture_prefilled_catalog)

    assert res == (2, 2)
