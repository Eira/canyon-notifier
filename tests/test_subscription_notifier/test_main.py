from app.subscription_notifier import main


async def test_main_smoke():
    res = await main(throttling_time=5.0, amount_of_iterations=2)

    assert True
    assert res == 2
