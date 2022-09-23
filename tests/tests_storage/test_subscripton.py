from app.bike_model import SubscriptionBikeFamily
from app.storage import create_subscription, subscriptions_from_db


async def test_create_subscription_happy_path():
    chat_id = '123'
    bike_family = 'NewBike'

    res = await create_subscription(chat_id, bike_family)

    assert res.chat_id == chat_id
    assert res.bike_family == bike_family
    assert res.subscribe_id > 0


async def test_create_subscription_few_times():
    chat_id = '123'
    bike_family = 'NewBike'

    res_1 = await create_subscription(chat_id, bike_family)
    res_2 = await create_subscription(chat_id, bike_family)

    assert res_1.subscribe_id != res_2.subscribe_id


async def test_subscriptions_from_db_happy_path(fixture_prefilled_subscription: SubscriptionBikeFamily):
    res = await subscriptions_from_db(fixture_prefilled_subscription.chat_id)

    assert isinstance(res, list)
    assert len(res) == 1
    assert res == [
        SubscriptionBikeFamily(
            subscribe_id=fixture_prefilled_subscription.subscribe_id,
            chat_id=fixture_prefilled_subscription.chat_id,
            bike_family=fixture_prefilled_subscription.bike_family,
        )
    ]
