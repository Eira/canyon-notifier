from app.models import Bike, SubscriptionBikeFamily, Match
from app.subscription_notifier import _get_notification_bikes


def test_get_notification_bikes_happy_path(
        fixture_bike_item_1,
        fixture_bike_item_1_s,
        fixture_bike_item_2,
):
    subscription_list = [
        SubscriptionBikeFamily(
            subscribe_id=12345678,
            chat_id=915745042,
            bike_family='Spectral',
            bike_size='M',
        ),
        SubscriptionBikeFamily(
            subscribe_id=12345678,
            chat_id=915745042,
            bike_family='Spectral',
            bike_size='all',
        ),
        SubscriptionBikeFamily(
            subscribe_id=12345679,
            chat_id=915745042,
            bike_family='Something',
            bike_size='XL'
        ),
        SubscriptionBikeFamily(
            subscribe_id=12345680,
            chat_id=915745042,
            bike_family='Exceed CF',
            bike_size='L'
        ),
    ]
    available_bike_list = [
        fixture_bike_item_1,
        fixture_bike_item_1_s,
        fixture_bike_item_2,
        Bike(
            id='Test_1_1 L',
            title='Test 1 1',
            link='https://test',
            family='Test',
            model='1 1',
            size='L',
        ),
    ]

    res = _get_notification_bikes(subscription_list, available_bike_list)

    assert len(res) == 4
    assert isinstance(res, list)
    for match in res:
        assert isinstance(match, Match)
    match_id_list: list[tuple] = [
        (f'{match.bike.id} {match.bike.size}', match.subscription.subscribe_id)
        for match in res
    ]
    assert match_id_list == [
        ('spectral_125_cf_9_m M', 12345678),
        ('spectral_125_cf_9_m M', 12345678),
        ('spectral_125_cf_9_m S', 12345678),
        ('exceed_cf_7_l L', 12345680),
    ]


def test_get_notification_bikes_empty_subscription_list(
        fixture_bike_item_1,
        fixture_bike_item_2,
):
    subscription_list = []
    available_bike_list = [
        fixture_bike_item_1,
        fixture_bike_item_2,
        Bike(
            id='Test_1_1_s',
            title='Test 1 1',
            link='https://test',
            family='Test',
            model='1 1',
            size='S',
        ),
    ]

    res = _get_notification_bikes(subscription_list, available_bike_list)

    assert res == []


def test_get_notification_bikes_empty_available_list():
    subscription_list = [
        SubscriptionBikeFamily(
            subscribe_id=12345678,
            chat_id=915745042,
            bike_family='Spectral',
            bike_size='M'
        ),
        SubscriptionBikeFamily(
            subscribe_id=12345679,
            chat_id=915745042,
            bike_family='Something',
            bike_size='XL'
        ),
        SubscriptionBikeFamily(
            subscribe_id=12345680,
            chat_id=915745042,
            bike_family='Exceed CF',
            bike_size='L'
        ),
    ]
    available_bike_list = []

    res = _get_notification_bikes(subscription_list, available_bike_list)

    assert res == []
