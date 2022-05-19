"""Methods for access the database."""

from typing import List

import aioredis

from app.bike_model import Bike

db_pool: aioredis.Redis = await aioredis.from_url("redis://localhost",  db=1)

def clear_catalog() -> int:
    """Delete old catalog in database."""
    # todo unit test
    # todo implement

    return 0  # amount of deleted bikes


def insert_uptodate_catalog(uptodate_catalog: List[Bike]) -> int:
    """Save actual catalog to the database."""
    # todo unit test
    # todo implement

    return 0  # amount added bikes
