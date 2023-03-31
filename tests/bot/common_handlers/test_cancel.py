from unittest.mock import AsyncMock

from app.bot.common_handlers import cancel


async def test_cancel_subscription_smoke():
    message_mock = AsyncMock()
    state_mock = AsyncMock()

    await cancel(message=message_mock, state=state_mock)

    assert state_mock.finish.call_count == 1
