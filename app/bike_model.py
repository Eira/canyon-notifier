"""Description of available canyon bike item."""

from dataclasses import dataclass
from typing import List


@dataclass
class Bike:
    """type of available bike."""

    id: str
    title: str
    link: str
    family: str
    model: str


@dataclass
class CatalogFamily:
    """type of element in bikes catalog grouped by family."""

    family: str
    bike_list: List[Bike]


@dataclass
class SubscriptionBikeFamily:
    """type of subscription with information about it."""
    subscribe_id: int
    chat_id: int
    bike_family: str
