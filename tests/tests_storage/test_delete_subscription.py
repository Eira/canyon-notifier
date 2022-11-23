from app.models import SubscriptionBikeFamily
from app.storage import get_subscriptions, delete_subscription


async def test_delete_subscription_happy_path(fixture_prefilled_subscription: SubscriptionBikeFamily):
    await delete_subscription(fixture_prefilled_subscription.subscribe_id)

    subscriptions = await get_subscriptions(fixture_prefilled_subscription.chat_id)
    assert subscriptions == []


async def test_delete_subscription_invalid():
    res = await delete_subscription(0)

    assert res is True
