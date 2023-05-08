from unittest.mock import AsyncMock

from app.bot.subscription_handlers import show_subscriptions


async def test_show_subscriptions_happy_path(fixture_prefilled_subscription):
    message_mock = AsyncMock()
    message_mock.chat.id = fixture_prefilled_subscription.chat_id
    expected_bike_family =f'{fixture_prefilled_subscription.bike_family} {fixture_prefilled_subscription.bike_size}'

    await show_subscriptions(message=message_mock)

    real_bike_family = message_mock.answer.await_args_list[0].args[0]
    reply_markup = message_mock.answer.await_args.kwargs['reply_markup']

    assert message_mock.answer.call_count == 2
    assert reply_markup.keyboard[0][0].text == 'subscribe'
    assert reply_markup.keyboard[1][0].text == 'back'
    assert real_bike_family == expected_bike_family


async def test_show_subscriptions_empty():
    message_mock = AsyncMock()
    message_mock.chat.id = 0
    expected_answer = '\n'.join((
        'You do not have any subscriptions yet.',
    ))

    await show_subscriptions(message=message_mock)

    message_mock.answer.await_args.assert_called_with(expected_answer)

