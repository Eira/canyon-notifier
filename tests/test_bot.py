from unittest.mock import AsyncMock

from app.bot import send_welcome, main, show_catalog


async def test_bot_send_welcome_happy_path():
    text_mock = '\n'.join((
        'Hi, friend!',
        'I will show you which canyon bicycles are available in the store.',
        '/catalog - to see all catalog.',
    ))
    message_mock = AsyncMock()

    await send_welcome(message=message_mock)

    message_mock.answer.assert_called_with(text_mock)


async def test_show_catalog_smoke():
    message_mock = AsyncMock()

    await show_catalog(message_mock)

    assert True


async def test_show_catalog_happy_path(fixture_prefilled_catalog):
    message_mock = AsyncMock()
    expected_res = 'Spectral\n<a href="https://www.canyon.com/en-cz/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR">125 CF 9</a>'

    await show_catalog(message_mock)

    res = message_mock.answer.call_args[0][0]
    assert message_mock.answer.call_count == 2
    assert expected_res in res


def test_bot_main_smoke(mocker):
    mock = mocker.patch('app.bot.executor.start_polling')

    res = main()

    assert res is None
    assert mock.call_count == 1
