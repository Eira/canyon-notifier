from app.models import SubscriptionBikeFamily
from app.storage.subscription import create_subscription, get_subscriptions


async def test_create_subscription_happy_path(fixture_fresh_chat_id):
    bike_family = 'test_bike_family'
    bike_size = 'M'

    res = await create_subscription(fixture_fresh_chat_id, bike_family, bike_size)

    res_get_subscription = await get_subscriptions(fixture_fresh_chat_id)
    assert res.chat_id == fixture_fresh_chat_id
    assert res.bike_family == bike_family
    assert res.subscribe_id > 0
    assert res_get_subscription == [
        SubscriptionBikeFamily(
            subscribe_id=res.subscribe_id,
            chat_id=fixture_fresh_chat_id,
            bike_family=bike_family,
            bike_size=bike_size,
        )
    ]


async def test_create_subscription_few_times(fixture_fresh_chat_id):
    bike_family = 'test_bike_family'
    bike_size = 'M'

    res_1 = await create_subscription(fixture_fresh_chat_id, bike_family, bike_size)
    res_2 = await create_subscription(fixture_fresh_chat_id, bike_family, bike_size)

    assert res_1.subscribe_id != res_2.subscribe_id
