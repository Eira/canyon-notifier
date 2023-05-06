from unittest.mock import AsyncMock

from app import storage
from app.bot.subscription_handlers import process_size_subscription
from app.storage.subscription import get_subscriptions


async def test_process_size_subscription_invalid_size(mocker):
    message_mock = AsyncMock()
    state_mock = AsyncMock()
    mock = mocker.patch('app.storage.subscription.create_subscription')
    message_mock.text = 'qwdfg'

    await process_size_subscription(message=message_mock, state=state_mock)

    assert message_mock.reply.call_count == 1
    assert mock.call_count == 0


async def test_process_size_subscription_happy_path(mocker, fixture_fresh_chat_id):
    message_mock = AsyncMock()
    state_mock = AsyncMock()
    mock = mocker.patch('app.storage.subscription.create_subscription')
    mock_usage_counter = mocker.spy(storage.subscription, 'create_subscription')
    message_mock.text = 'XS'

    await process_size_subscription(message=message_mock, state=state_mock)

    assert message_mock.reply.call_count == 0
    assert message_mock.answer.call_count == 1
    assert mock.call_count == 1
    assert mock_usage_counter.call_count == 1
    assert state_mock.finish.call_count == 1
