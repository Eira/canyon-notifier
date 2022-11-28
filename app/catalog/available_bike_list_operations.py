"""
This is the module of catalog updater.

It contains functions for create and update list of new available bikes.
"""

from typing import List

from app.models import Bike
from app.storage.available_bike_list import save_new_available_bikes


async def update_available_bikes_list(old_catalog: List[Bike], actual_catalog: List[Bike]) -> List[Bike]:
    """Create a list of bikes that wasn't available before."""
    available_bikes_list = []

    if old_catalog:
        available_bikes_list = _get_new_available_bikes(
            old_catalog,
            actual_catalog,
        )
    if available_bikes_list:
        await save_new_available_bikes(available_bikes_list)

    return available_bikes_list


def _get_new_available_bikes(old_catalog: List[Bike], actual_catalog: List[Bike]) -> List[Bike]:
    """Compare old list of available bikes with new one. Return list of bikes, that wasn't available before."""
    old_catalog_id = {bike.id for bike in old_catalog}

    return [
        new_bike
        for new_bike in actual_catalog
        if new_bike.id not in old_catalog_id
    ]
