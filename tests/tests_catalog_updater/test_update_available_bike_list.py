from app.catalog.available_bike_list_operations import update_available_bikes_list
from app.models import Bike


async def test_update_available_bike_list_happy_path(mocker):
    # todo f а хороший ли это тест?
    mock = mocker.patch('app.catalog.available_bike_list_operations.save_new_available_bikes')
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

    res = await update_available_bikes_list(old_bikes_list, new_bikes_list)

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
    assert mock.call_count == 1


async def test_update_available_bike_list_empty_old_list():
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

    res = await update_available_bikes_list(old_bikes_list, new_bikes_list)

    assert res == []


async def test_update_available_bike_list__empty_new_list(mocker):
    mock = mocker.patch('app.catalog.available_bike_list_operations.save_new_available_bikes')
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

    res = await update_available_bikes_list(old_bikes_list, new_bikes_list)

    assert res == []
    assert mock.call_count == 0
