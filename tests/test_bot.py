from unittest.mock import AsyncMock

from app import storage
from app.bot.common_handlers import send_welcome, show_catalog
from app.bot.subscription_handlers import start_subscription, process_subscription, cancel_subscription, show_subscriptions, delete_subscription
from app.bot_runner import main
from app.storage.subscription import get_subscriptions


async def test_bot_send_welcome_happy_path():
    expected_answer = '\n'.join((
        'Hi, friend!',
        'I will show you which canyon bicycles are available in the store.',
        '/catalog - to see all catalog.',
        '/subscribe - to get the message, when the bike family you want in the stock.',
    ))
    message_mock = AsyncMock()

    await send_welcome(message=message_mock)

    message_mock.answer.assert_called_with(expected_answer)


async def test_show_catalog_smoke():
    message_mock = AsyncMock()

    await show_catalog(message_mock)

    assert True


async def test_show_catalog_happy_path(fixture_prefilled_catalog):
    message_mock = AsyncMock()
    expected_res = 'Spectral\n<a href="https://www.canyon.com/en-cz/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR">125 CF 9</a>'

    await show_catalog(message_mock)

    res = message_mock.answer.call_args[0][0]
    assert message_mock.answer.call_count == 2
    assert expected_res in res


def test_bot_main_smoke(mocker):
    mock = mocker.patch('app.bot_runner.executor.start_polling')

    res = main()

    assert res is None
    assert mock.call_count == 1


async def test_start_subscription_smoke(mocker):
    mock = mocker.patch('app.bot.subscription_handlers.CreateSubscription.family_name.set')
    expected_reply = '\n'.join((
        'Please, write the bike family name.When it will be available we will let you know!',
        '/cancel - to cancel the action.',
    ))
    message_mock = AsyncMock()

    await start_subscription(message=message_mock)

    message_mock.reply.assert_called_with(expected_reply)
    assert mock.call_count == 1


async def test_process_subscription_smoke(mocker, fixture_fresh_chat_id):
    message_mock = AsyncMock()
    message_mock.chat.id = fixture_fresh_chat_id
    message_mock.text = 'Bike_test'
    state_mock = AsyncMock()
    mock_usage_counter = mocker.spy(storage.subscription, 'create_subscription')

    expected_reply = f'Got it! When "{message_mock.text}" will be available we will let you know!'

    await process_subscription(message=message_mock, state=state_mock)

    message_mock.reply.assert_called_with(expected_reply)
    assert mock_usage_counter.call_count == 1
    assert state_mock.finish.call_count == 1


async def test_cancel_subscription_smoke():
    message_mock = AsyncMock()
    state_mock = AsyncMock()

    await cancel_subscription(message=message_mock, state=state_mock)

    message_mock.reply.assert_called_with('Cancelled.')
    assert state_mock.finish.call_count == 1


async def test_show_subscriptions_happy_path(fixture_prefilled_subscription):
    message_mock = AsyncMock()
    message_mock.chat.id = fixture_prefilled_subscription.chat_id
    expected_bike_family = fixture_prefilled_subscription.bike_family

    await show_subscriptions(message=message_mock)

    real_bike_family = message_mock.answer.await_args.kwargs['reply_markup'].inline_keyboard[0][0].text

    assert message_mock.answer.call_count == 1
    assert expected_bike_family == real_bike_family


async def test_show_subscriptions_empty():
    message_mock = AsyncMock()
    message_mock.chat.id = 0
    expected_answer = '\n'.join((
        'You do not have any subscriptions yet.',
        '/subscribe - to make one.',
    ))

    await show_subscriptions(message=message_mock)

    message_mock.answer.assert_called_with(expected_answer)


async def test_delete_subscription_happy_path(fixture_prefilled_subscription):
    callback_query_mock = AsyncMock()
    callback_query_mock.data = f'delete_subscription:{fixture_prefilled_subscription.subscribe_id}'

    res = await delete_subscription(callback_query=callback_query_mock)
    subscriptions_list = await get_subscriptions(fixture_prefilled_subscription.chat_id)

    assert res is None
    assert subscriptions_list == []
