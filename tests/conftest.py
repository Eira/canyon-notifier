from typing import List

import pytest

from app.models import Bike, SubscriptionBikeFamily
from app.storage.available_bike_list import delete_available_bike_list, save_new_available_bikes
from app.storage.catalog import clear_catalog, insert_actual_catalog
from app.storage.subscription import get_subscriptions, delete_subscription, create_subscription


@pytest.fixture(autouse=True)
async def redis_connection():
    from app.storage.conection import db_pool
    yield
    await db_pool.aclose()


@pytest.fixture(autouse=True)
async def bot_session_cleanup():
    yield
    try:
        from app.bot_runner import bot
        await bot.close()
    except Exception:
        pass


@pytest.fixture()
def fixture_bike_item_1():
    bike_item_1 = Bike(
            id='spectral_125_cf_9_m',
            title='Spectral 125 CF 9',
            link='https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
            family='Spectral',
            model='125 CF 9',
            size='M',
        )
    yield bike_item_1

@pytest.fixture()
def fixture_bike_item_1_s():
    bike_item_1 = Bike(
            id='spectral_125_cf_9_m',
            title='Spectral 125 CF 9',
            link='https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
            family='Spectral',
            model='125 CF 9',
            size='S',
        )
    yield bike_item_1

@pytest.fixture()
def fixture_bike_item_2():
    bike_item_2 = Bike(
            id='exceed_cf_7_l',
            title='Exceed CF 7',
            link='https://www.canyon.com/en-de/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-7/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
            family='Exceed',
            model='CF 7',
            size='L',
        )
    yield bike_item_2


@pytest.fixture()
def fixture_bike_item_3():
    bike_item_3 = Bike(
            id='exceed_cf_8_s',
            title='Exceed CF 8',
            link='https://www.canyon.com/en-de/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-8/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
            family='Exceed',
            model='CF 8',
            size='S',
        )
    yield bike_item_3


@pytest.fixture()
async def fixture_empty_catalog():
    await clear_catalog()
    yield


@pytest.fixture()
async def fixture_prefilled_catalog(
        fixture_empty_catalog,
        fixture_bike_item_1,
        fixture_bike_item_2,
) -> List[Bike]:
    bikes_list = [fixture_bike_item_1, fixture_bike_item_2]

    await insert_actual_catalog(bikes_list)
    yield bikes_list
    await clear_catalog()


@pytest.fixture()
async def fixture_prefilled_catalog_few_sizes(
        fixture_empty_catalog,
        fixture_bike_item_1,
        fixture_bike_item_1_s,
) -> List[Bike]:
    bikes_list = [fixture_bike_item_1, fixture_bike_item_1_s]

    await insert_actual_catalog(bikes_list)
    yield bikes_list
    await clear_catalog()


@pytest.fixture()
async def fixture_fresh_chat_id() -> int:
    chat_id = 123

    yield chat_id

    subscription_list = await get_subscriptions(chat_id)
    for subscription_item in subscription_list:
        await delete_subscription(subscription_item.subscribe_id)


@pytest.fixture()
async def fixture_prefilled_subscription(fixture_fresh_chat_id) -> SubscriptionBikeFamily:
    bike_family = 'test_bike_family'
    bike_size = 'M'

    subscription_item = await create_subscription(fixture_fresh_chat_id, bike_family, bike_size)
    yield subscription_item


@pytest.fixture()
async def fixture_empty_available_bike_list():
    await delete_available_bike_list()
    yield
    await delete_available_bike_list()


@pytest.fixture()
async def fixture_prefilled_available_bike_list(fixture_empty_available_bike_list, fixture_prefilled_catalog) -> List[Bike]:

    await save_new_available_bikes(fixture_prefilled_catalog)

    yield fixture_prefilled_catalog


@pytest.fixture()
async def fixture_prefilled_subscription_for_match_list(fixture_prefilled_available_bike_list, fixture_fresh_chat_id):
    for bike in fixture_prefilled_available_bike_list:
        await create_subscription(fixture_fresh_chat_id, bike.family, bike.size)

    yield


