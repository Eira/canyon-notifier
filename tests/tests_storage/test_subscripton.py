from app.bike_model import SubscriptionBikeFamily
from app.storage import create_subscription, get_subscriptions, delete_subscription


async def test_create_subscription_happy_path():
    chat_id = '123'
    bike_family = 'NewBike'

    res = await create_subscription(chat_id, bike_family)

    res_get_subscription = await get_subscriptions(chat_id)
    assert res.chat_id == chat_id
    assert res.bike_family == bike_family
    assert res.subscribe_id > 0
    assert res in res_get_subscription == [
        SubscriptionBikeFamily(
            subscribe_id=res.subscribe_id,
            chat_id=chat_id,
            bike_family=bike_family,
        )
    ]


async def test_create_subscription_few_times():
    chat_id = '123'
    bike_family = 'NewBike'

    res_1 = await create_subscription(chat_id, bike_family)
    res_2 = await create_subscription(chat_id, bike_family)

    assert res_1.subscribe_id != res_2.subscribe_id


async def test_get_subscriptions_happy_path(fixture_prefilled_subscription: SubscriptionBikeFamily):
    res = await get_subscriptions(fixture_prefilled_subscription.chat_id)

    assert isinstance(res, list)
    assert len(res) == 1
    assert res[0].subscribe_id == fixture_prefilled_subscription.subscribe_id


async def test_get_subscriptions_empty():
    res = await get_subscriptions(0)

    assert res == []


async def test_delete_subscription_happy_path(fixture_prefilled_subscription: SubscriptionBikeFamily):
    await delete_subscription(fixture_prefilled_subscription.subscribe_id)

    subscriptions = await get_subscriptions(fixture_prefilled_subscription.chat_id)
    assert subscriptions == []



