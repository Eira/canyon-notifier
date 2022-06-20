from unittest.mock import AsyncMock

from app.bot import send_welcome, wrong_command_helper, main, show_catalog


async def test_bot_send_welcome_smoke():
    message_mock = AsyncMock()

    await send_welcome(message_mock)

    assert True


async def test_bot_send_welcome_happy_path():
    text_mock = '\n'.join((
        'Hi, friend!',
        'I will show you which canyon bicycles are available in the store.',
        '/catalog - to see all catalog.',
    ))
    message_mock = AsyncMock()

    await send_welcome(message=message_mock)

    message_mock.answer.assert_called_with(text_mock)


async def test_wrong_command_helper_smoke():
    message_mock = AsyncMock()

    await wrong_command_helper(message_mock)

    assert True


async def test_show_catalog_smoke():
    message_mock = AsyncMock()

    await show_catalog(message_mock)

    assert True


def test_bot_main_smoke(mocker):
    mock = mocker.patch('app.bot.executor.start_polling')

    res = main()

    assert res is None
    assert mock.call_count == 1
