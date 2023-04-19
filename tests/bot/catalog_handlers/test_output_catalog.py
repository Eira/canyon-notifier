from unittest.mock import AsyncMock

from app.bot.catalog_handlers import _output_catalog


async def test_output_catalog_no_catalog():
    catalog = []
    message_mock = AsyncMock()
    custom_size_on = False
    user_size = 'All'
    expected_res = 'Sorry, there no any bikes available at the moment.'

    await _output_catalog(catalog, message_mock, custom_size_on, user_size)

    assert message_mock.answer.call_args[0][0] == expected_res


async def test_output_catalog_no_size_catalog():
    catalog = []
    message_mock = AsyncMock()
    custom_size_on = True
    user_size = 'XS'
    expected_res = 'Sorry, there no XS bikes available at the moment.'

    await _output_catalog(catalog, message_mock, custom_size_on, user_size)

    assert message_mock.answer.call_args[0][0] == expected_res

async def test_output_catalog_one_size(fixture_bike_item_2):
    catalog = [fixture_bike_item_2]
    message_mock = AsyncMock()
    custom_size_on = True
    user_size = 'L'
    expected_res = 'Exceed\n''<a ''href="https://www.canyon.com/en-de/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-7/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC">CF ''7</a>'

    await _output_catalog(catalog, message_mock, custom_size_on, user_size)

    assert message_mock.answer.call_args[0][0] == expected_res


async def test_output_catalog_all_sizes(
        fixture_bike_item_1, fixture_bike_item_1_s, fixture_bike_item_2
):
    catalog = [
        fixture_bike_item_1,
        fixture_bike_item_1_s,
        fixture_bike_item_2,
    ]
    message_mock = AsyncMock()
    custom_size_on = False
    user_size = 'All'
    expected_res_1 = 'Spectral\n<a href="https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR">125 CF 9</a>  M, S'
    expected_res_2 = 'Exceed\n<a href="https://www.canyon.com/en-de/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-7/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC">CF 7</a>  L'

    await _output_catalog(catalog, message_mock, custom_size_on, user_size)

    assert message_mock.answer.await_args_list[0][0][0] == expected_res_1
    assert message_mock.answer.await_args_list[1][0][0] == expected_res_2
