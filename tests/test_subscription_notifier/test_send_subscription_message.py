from app.models import Bike, SubscriptionBikeFamily, Match
from app.subscription_notifier import send_subscription_message


async def test_send_subscription_message_smoke():
    # todo проверку на конкретное сообщение
    subscription_to_send = Match(
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
    )
    expected_message = '\n'.join((
        'Spectral 125 CF 9 is available in the stock!',
        'https://www.canyon.com/en-cz/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
    ))

    res = await send_subscription_message(subscription_to_send)

    assert res is True


async def test_send_subscription_message_invalid_data():
    #todo test на невалидные данные (невалидный пользователь)
    subscription_to_send = Match(
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
    )

    res = await send_subscription_message(subscription_to_send)
