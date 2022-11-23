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

# todo разбить на ассерты маленьке
    assert len(res) == 2
    assert res == [
        Match(
            Bike(
                id='spectral_125_cf_9',
                title='Spectral 125 CF 9',
                link='https://www.canyon.com/en-cz/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
                family='Spectral',
                model='125 CF 9',
            ),
            SubscriptionBikeFamily(
                subscribe_id=12345678,
                chat_id=915745042,
                bike_family='Spectral',
            ),
        ),
        Match(
            Bike(
                id='exceed_cf_7',
                title='Exceed CF 7',
                link='https://www.canyon.com/en-cz/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-7/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
                family='Exceed',
                model='CF 7',
            ),
            SubscriptionBikeFamily(
                subscribe_id=12345680,
                chat_id=915745042,
                bike_family='Exceed CF',
            ),
        )
    ]

