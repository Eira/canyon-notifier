from typing import List

from app.bike_model import Bike
from app.catalog_updater import _update_catalog, _get_new_available_bikes


async def test_update_catalog_happy_path(fixture_prefilled_catalog: List[Bike]):
    res = await _update_catalog(fixture_prefilled_catalog)

    assert res == (2, 2)


def test__get_new_available_bikes_happy_path():
    old_bikes_list = [
        Bike(
            id='spectral_125_cf_9',
            title='Spectral 125 CF 9',
            link='https://www.canyon.com/en-cz/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
            family='Spectral',
            model='125 CF 9',
        ),
        Bike(
            id='exceed_cf_7',
            title='Exceed CF 7',
            link='https://www.canyon.com/en-cz/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-7/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
            family='Exceed',
            model='CF 7',
        )
    ]
    new_bikes_list = [
        Bike(
            id='spectral_125_cf_9',
            title='Spectral 125 CF 9',
            link='https://www.canyon.com/en-cz/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
            family='Spectral',
            model='125 CF 9',
        ),
        Bike(
            id='exceed_cf_8',
            title='Exceed CF 8',
            link='https://www.canyon.com/en-cz/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-8/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
            family='Exceed',
            model='CF 8',
        ),
    ]

    res = _get_new_available_bikes(old_bikes_list, new_bikes_list)

    assert res == [
        Bike(
            id='exceed_cf_8',
            title='Exceed CF 8',
            link='https://www.canyon.com/en-cz/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-8/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
            family='Exceed',
            model='CF 8',
        ),
    ]
