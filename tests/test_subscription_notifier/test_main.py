from aiogram.utils.exceptions import BadRequest

from app.subscription_notifier import main


async def test_main_smoke(fixture_empty_available_bike_list):
    res = await main(throttling_time=5.0, amount_of_iterations=2)

    assert True
    assert res == 2


async def test_main_no_matches(mocker, fixture_empty_available_bike_list):
    mock = mocker.patch('app.subscription_notifier.bot.send_message')

    await main(throttling_time=5.0, amount_of_iterations=2)

    assert mock.call_count == 0


async def test_main_happy_path(mocker, fixture_prefilled_subscription_for_match_list):
    mock = mocker.patch('app.subscription_notifier._send_subscription_message')

    await main(throttling_time=5.0, amount_of_iterations=2)

    assert mock.call_count == 2


async def test_main_invalid_id(mocker, fixture_prefilled_subscription_for_match_list):
    mocker.patch('app.subscription_notifier._send_subscription_message', side_effect=BadRequest('invalid user id'))
    mock_delete_subscription = mocker.patch('app.subscription_notifier.delete_subscription')

    await main(throttling_time=5.0, amount_of_iterations=2)

    assert mock_delete_subscription.call_count == 2
