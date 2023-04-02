from unittest.mock import AsyncMock

from app.bot.subscription_handlers import start_subscription


async def test_start_subscription_smoke(mocker):
    mock = mocker.patch('app.bot.subscription_handlers.CreateSubscription.family_name.set')
    expected_reply = '\n'.join((
        'Please, write the bike family name.When it will be available we will let you know!',
    ))
    message_mock = AsyncMock()

    await start_subscription(message=message_mock)

    message_mock.reply.await_args.assert_called_with(expected_reply)
    assert mock.call_count == 1


async def test_start_subscription_to_much_subscriptions(mocker):
    mocker.patch('app.bot.subscription_handlers.CreateSubscription.family_name.set')
    mocker.patch('app.bot.subscription_handlers.get_subscription_amount', return_value = 10)
    expected_reply = '\n'.join((
        'You have already 10 subscriptions.',
        'Delete some to create a new one, please.',
    ))
    message_mock = AsyncMock()

    await start_subscription(message=message_mock)

    message_mock.reply.await_args.assert_called_with(expected_reply)