from app.bot_runner import main


def test_bot_main_smoke(mocker):
    mock = mocker.patch('app.bot_runner.executor.start_polling')

    res = main()

    assert res is None
    assert mock.call_count == 1
