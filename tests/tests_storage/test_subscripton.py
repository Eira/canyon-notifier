from app.bike_model import SubscriptionBikeFamily, Bike
from app.storage import create_subscription, get_subscriptions, delete_subscription, get_available_bike_list, save_new_available_bikes, delete_available_bike_list
from app.subscription_notifier import main


async def test_create_subscription_happy_path(fixture_fresh_chat_id):
    bike_family = 'NewBike'

    res = await create_subscription(fixture_fresh_chat_id, bike_family)

    res_get_subscription = await get_subscriptions(fixture_fresh_chat_id)
    assert res.chat_id == fixture_fresh_chat_id
    assert res.bike_family == bike_family
    assert res.subscribe_id > 0
    assert res_get_subscription == [
        SubscriptionBikeFamily(
            subscribe_id=res.subscribe_id,
            chat_id=fixture_fresh_chat_id,
            bike_family=bike_family,
        )
    ]


async def test_create_subscription_few_times(fixture_fresh_chat_id):
    bike_family = 'NewBike'

    res_1 = await create_subscription(fixture_fresh_chat_id, bike_family)
    res_2 = await create_subscription(fixture_fresh_chat_id, bike_family)

    assert res_1.subscribe_id != res_2.subscribe_id


async def test_get_subscriptions_happy_path(fixture_prefilled_subscription: SubscriptionBikeFamily):
    res = await get_subscriptions(fixture_prefilled_subscription.chat_id)

    assert isinstance(res, list)
    assert len(res) == 1
    assert res[0].subscribe_id == fixture_prefilled_subscription.subscribe_id


async def test_get_subscriptions_empty():
    res = await get_subscriptions(0)

    assert res == []


async def test_delete_subscription_happy_path(fixture_prefilled_subscription: SubscriptionBikeFamily):
    await delete_subscription(fixture_prefilled_subscription.subscribe_id)

    subscriptions = await get_subscriptions(fixture_prefilled_subscription.chat_id)
    assert subscriptions == []


async def test_delete_subscription_invalid():
    res = await delete_subscription(0)

    assert res is True


async def test_save_new_available_bikes():
    available_bikes_list = [
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

    res = await save_new_available_bikes(available_bikes_list)

    assert res is None


async def test_get_available_bike_list_happy_path():
    # todo вероятно надо чистить базу
    res = await get_available_bike_list()

    assert res == [
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


async def test_delete_available_bike_list_happy_path():
    # todo тут явно нужна фикстура
    bike_id_set = {'spectral_125_cf_9', 'exceed_cf_7'}

    await delete_available_bike_list(bike_id_set)

    rest_bike_id_list = {
        bike.id
        for bike in await get_available_bike_list()
    }

    assert bike_id_set not in rest_bike_id_list


async def test_main_smoke():
    res = await main(throttling_time=5.0, amount_of_iterations=2)

    assert True
    assert res == 2
