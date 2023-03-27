from app.models import Bike
from app.storage.catalog import get_catalog


async def test_get_catalog_happy_path(fixture_prefilled_catalog):
    res = await get_catalog()

    assert res == [
        Bike(
            id='exceed_cf_7 L',
            title='Exceed CF 7',
            link='https://www.canyon.com/en-de/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-7/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
            family='Exceed',
            model='CF 7',
            size='L',
        ),
        Bike(
            id='spectral_125_cf_9 M',
            title='Spectral 125 CF 9',
            link='https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
            family='Spectral',
            model='125 CF 9',
            size='M',
        ),
    ]


async def test_get_catalog_empty_catalog(fixture_empty_catalog):
    res = await get_catalog()

    assert res == []
