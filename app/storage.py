"""Methods for access the database."""

from typing import List

from app.bike_model import Bike


def clear_catalog() -> int:
    """Delete old catalog in database."""
    # todo unit test

    ...


def insert_uptodate_catalog(uptodate_catalog: List[Bike]) -> int:
    """Save actual catalog to the database."""
    # todo unit test

    ...
