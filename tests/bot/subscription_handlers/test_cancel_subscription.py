from unittest.mock import AsyncMock

from app.bot.subscription_handlers import cancel_subscription


async def test_cancel_subscription_smoke():
    message_mock = AsyncMock()
    state_mock = AsyncMock()

    await cancel_subscription(message=message_mock, state=state_mock)

    message_mock.reply.await_args.assert_called_with('Cancelled.')
    assert state_mock.finish.call_count == 1
