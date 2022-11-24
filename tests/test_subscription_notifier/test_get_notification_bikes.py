from app.models import Bike, SubscriptionBikeFamily, Match
from app.subscription_notifier import get_notification_bikes


def test_get_notification_bikes_happy_path():
    subscription_list = [
        SubscriptionBikeFamily(
            subscribe_id=12345678,
            chat_id=915745042,
            bike_family='Spectral',
        ),
        SubscriptionBikeFamily(
            subscribe_id=12345679,
            chat_id=915745042,
            bike_family='Something',
        ),
        SubscriptionBikeFamily(
            subscribe_id=12345680,
            chat_id=915745042,
            bike_family='Exceed CF',
        ),
    ]
    available_bike_list = [
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
        ),
        Bike(
            id='Test_1_1',
            title='Test 1 1',
            link='https://test',
            family='Test',
            model='1 1',
        ),
    ]

    res = get_notification_bikes(subscription_list, available_bike_list)

    assert len(res) == 2
    assert isinstance(res, list)
    for match in res:
        assert isinstance(match, Match)
    match_id_list: list[tuple] = [
        (match.bike.id, match.subscription.subscribe_id)
        for match in res
    ]
    assert match_id_list == [
        ('spectral_125_cf_9', 12345678),
        ('exceed_cf_7', 12345680),
    ]


def test_get_notification_bikes_empty_subscription_list():
    subscription_list = []
    available_bike_list = [
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
        ),
        Bike(
            id='Test_1_1',
            title='Test 1 1',
            link='https://test',
            family='Test',
            model='1 1',
        ),
    ]

    res = get_notification_bikes(subscription_list, available_bike_list)

    assert res == []


def test_get_notification_bikes_empty_available_list():
    subscription_list = [
        SubscriptionBikeFamily(
            subscribe_id=12345678,
            chat_id=915745042,
            bike_family='Spectral',
        ),
        SubscriptionBikeFamily(
            subscribe_id=12345679,
            chat_id=915745042,
            bike_family='Something',
        ),
        SubscriptionBikeFamily(
            subscribe_id=12345680,
            chat_id=915745042,
            bike_family='Exceed CF',
        ),
    ]
    available_bike_list = []

    res = get_notification_bikes(subscription_list, available_bike_list)

    assert res == []
