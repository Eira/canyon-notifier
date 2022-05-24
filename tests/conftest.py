import asyncio

import pytest

from app.bike_model import Bike
from app.storage import clear_catalog, insert_actual_catalog


@pytest.fixture()
async def fixture_empty_catalog():
    await clear_catalog()
    yield


@pytest.fixture()
async def fixture_prefilled_catalog(fixture_empty_catalog):
    bikes_list = [
        Bike(
            title='Spectral 125 CF 9',
            link='https://www.canyon.com/en-cz/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
        ),
        Bike(
            title='Exceed CF 7',
            link='https://www.canyon.com/en-cz/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-7/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
        )
    ]

    await insert_actual_catalog(bikes_list)
    yield
    await clear_catalog()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
