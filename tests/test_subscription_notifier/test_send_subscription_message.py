import pytest
from aiogram.utils.exceptions import ChatNotFound

from app.models import SubscriptionBikeFamily, Match
from app.subscription_notifier import _send_subscription_message


async def test_send_subscription_message_smoke(
        mocker,
        fixture_bike_item_1,
):
    mock = mocker.patch('app.subscription_notifier.bot.send_message')
    subscription_to_send = Match(
        fixture_bike_item_1,
        SubscriptionBikeFamily(
            subscribe_id=12345678,
            chat_id=915745042,
            bike_family='Spectral',
            bike_size='M',
        ),
    )
    expected_message = '\n'.join((
        'Spectral 125 CF 9 is available in the stock!',
        'https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
    ))

    res = await _send_subscription_message(subscription_to_send)

    assert res is True
    assert mock.call_count == 1
    assert mock.call_args.args[1] == expected_message


async def test_send_subscription_message_invalid_data(fixture_bike_item_1):
    subscription_to_send = Match(
        fixture_bike_item_1,
        SubscriptionBikeFamily(
            subscribe_id=12345678,
            chat_id=-1,
            bike_family='Spectral',
            bike_size='M',
        ),
    )

    with pytest.raises(ChatNotFound, match='Chat not found'):
        await _send_subscription_message(subscription_to_send)
