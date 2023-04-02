from unittest.mock import AsyncMock

from app.bot.subscription_handlers import delete_subscription
from app.storage.subscription import get_subscriptions


async def test_delete_subscription_happy_path(fixture_prefilled_subscription):
    callback_query_mock = AsyncMock()
    callback_query_mock.data = f'delete_subscription:{fixture_prefilled_subscription.subscribe_id}'

    res = await delete_subscription(callback_query=callback_query_mock)
    subscriptions_list = await get_subscriptions(fixture_prefilled_subscription.chat_id)

    assert res is None
    assert subscriptions_list == []
