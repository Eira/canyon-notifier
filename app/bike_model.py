"""Description of available canyon bike item."""

from dataclasses import dataclass


@dataclass
class Bike:
    """type of available bike."""

    id: str
    title: str
    link: str
    family: str
    model: str
