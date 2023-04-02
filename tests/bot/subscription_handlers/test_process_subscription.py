from unittest.mock import AsyncMock

from app import storage
from app.bot.subscription_handlers import process_subscription
from app.storage.subscription import get_subscriptions


async def test_process_subscription_smoke(mocker, fixture_fresh_chat_id):
    message_mock = AsyncMock()
    message_mock.chat.id = fixture_fresh_chat_id
    message_mock.text = 'Bike_test'
    state_mock = AsyncMock()
    mock_usage_counter = mocker.spy(storage.subscription, 'create_subscription')

    expected_reply = f'Got it! When "{message_mock.text}" will be available we will let you know!'

    await process_subscription(message=message_mock, state=state_mock)

    message_mock.reply.await_args.assert_called_with(expected_reply)
    assert mock_usage_counter.call_count == 1
    assert state_mock.finish.call_count == 1
