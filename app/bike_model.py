"""Description of available canyon bike item."""

from dataclasses import dataclass


@dataclass
class Bike:
    """type of available bike."""

    title: str
    link: str
