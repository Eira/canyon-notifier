from app.storage.subscription import get_subscription_amount, create_subscription


async def test_get_subscription_amount_happy_path(fixture_fresh_chat_id):
    bike_family = 'NewBike'
    subscription_num = 5
    bike_size = 'M'

    for counter in range( 0, subscription_num):
        await create_subscription(fixture_fresh_chat_id, bike_family, bike_size)
        counter += 1

    assert await get_subscription_amount(fixture_fresh_chat_id) == subscription_num