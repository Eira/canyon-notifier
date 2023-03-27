from app.catalog.available_bike_list_operations import _get_new_available_bikes
from app.models import Bike


def test_get_new_available_bikes_happy_path():
    # todo тут тоже тест не очень
    old_bikes_list = [
        Bike(
            id='spectral_125_cf_9 M',
            title='Spectral 125 CF 9',
            link='https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
            family='Spectral',
            model='125 CF 9',
            size='M',

        ),
        Bike(
            id='exceed_cf_7 L',
            title='Exceed CF 7',
            link='https://www.canyon.com/en-de/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-7/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
            family='Exceed',
            model='CF 7',
            size='L',
        )
    ]
    new_bikes_list = [
        Bike(
            id='spectral_125_cf_9 M',
            title='Spectral 125 CF 9',
            link='https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
            family='Spectral',
            model='125 CF 9',
            size='M',
        ),
        Bike(
            id='exceed_cf_8 S',
            title='Exceed CF 8',
            link='https://www.canyon.com/en-de/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-8/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
            family='Exceed',
            model='CF 8',
            size='S',
        ),
    ]

    res = _get_new_available_bikes(old_bikes_list, new_bikes_list)

    assert res == [
        Bike(
            id='exceed_cf_8 S',
            title='Exceed CF 8',
            link='https://www.canyon.com/en-de/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-8/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
            family='Exceed',
            model='CF 8',
            size='S',
        ),
    ]


def test_get_new_available_bikes_empty_old_list():
    old_bikes_list = []
    new_bikes_list = [
        Bike(
            id='spectral_125_cf_9 M',
            title='Spectral 125 CF 9',
            link='https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
            family='Spectral',
            model='125 CF 9',
            size='M',
        ),
        Bike(
            id='exceed_cf_8 S',
            title='Exceed CF 8',
            link='https://www.canyon.com/en-de/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-8/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
            family='Exceed',
            model='CF 8',
            size='S',
        ),
    ]

    res = _get_new_available_bikes(old_bikes_list, new_bikes_list)

    assert res == new_bikes_list


def test_get_new_available_bikes_empty_new_list():
    old_bikes_list = [
        Bike(
            id='spectral_125_cf_9 M',
            title='Spectral 125 CF 9',
            link='https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
            family='Spectral',
            model='125 CF 9',
            size='M',
        ),
        Bike(
            id='exceed_cf_7 L',
            title='Exceed CF 7',
            link='https://www.canyon.com/en-de/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-7/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
            family='Exceed',
            model='CF 7',
            size='L',
        )
    ]
    new_bikes_list = []

    res = _get_new_available_bikes(old_bikes_list, new_bikes_list)

    assert res == []


def test_get_new_available_bikes_empty_all_lists():
    old_bikes_list = []
    new_bikes_list = []

    res = _get_new_available_bikes(old_bikes_list, new_bikes_list)

    assert res == []
