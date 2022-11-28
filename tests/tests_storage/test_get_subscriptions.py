from app.models import SubscriptionBikeFamily
from app.storage.subscription import get_subscriptions


async def test_get_subscriptions_happy_path(fixture_prefilled_subscription: SubscriptionBikeFamily):
    res = await get_subscriptions(fixture_prefilled_subscription.chat_id)

    assert isinstance(res, list)
    assert len(res) == 1
    assert res[0].subscribe_id == fixture_prefilled_subscription.subscribe_id


async def test_get_subscriptions_empty():
    res = await get_subscriptions(0)

    assert res == []
