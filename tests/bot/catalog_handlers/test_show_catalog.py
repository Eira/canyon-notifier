from unittest.mock import AsyncMock

from app.bot.catalog_handlers import show_catalog


async def test_show_catalog_smoke():
    message_mock = AsyncMock()
    state_mock = AsyncMock()

    await show_catalog(message=message_mock, state=state_mock)

    assert True


async def test_show_catalog_happy_path(fixture_prefilled_catalog):
    message_mock = AsyncMock()
    state_mock = AsyncMock()
    message_mock.text = 'M'
    expected_res = 'Spectral\n<a href="https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR">125 CF 9</a>'

    await show_catalog(message=message_mock, state=state_mock)

    res = message_mock.answer.call_args[0][0]
    assert message_mock.answer.call_count == 1
    assert expected_res in res
