import asyncio
from typing import List

import pytest

from app.bike_model import Bike, SubscriptionBikeFamily
from app.storage import clear_catalog, insert_actual_catalog, create_subscription


@pytest.fixture()
async def fixture_empty_catalog():
    await clear_catalog()
    yield


@pytest.fixture()
async def fixture_prefilled_catalog(fixture_empty_catalog) -> List[Bike]:
    bikes_list = [
        Bike(
            id='spectral_125_cf_9',
            title='Spectral 125 CF 9',
            link='https://www.canyon.com/en-cz/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
            family='Spectral',
            model='125 CF 9',
        ),
        Bike(
            id='exceed_cf_7',
            title='Exceed CF 7',
            link='https://www.canyon.com/en-cz/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-7/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
            family='Exceed',
            model='CF 7',
        )
    ]

    await insert_actual_catalog(bikes_list)
    yield bikes_list
    await clear_catalog()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture()
async def fixture_prefilled_subscription() -> SubscriptionBikeFamily:
    chat_id = 12345
    bike_family = 'test_bike_family'

    subscription_item = await create_subscription(chat_id, bike_family)
    yield subscription_item


