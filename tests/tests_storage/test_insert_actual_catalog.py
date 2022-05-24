import pytest

from app.bike_model import Bike
from app.storage import insert_actual_catalog


@pytest.mark.asyncio
async def test_insert_actual_catalog_empty_catalog(fixture_empty_catalog):
    res = await insert_actual_catalog([])

    assert res == 0


@pytest.mark.asyncio
async def test_insert_actual_catalog():
    bikes_list = [
        Bike(
            title='Spectral 125 CF 9',
            link='https://www.canyon.com/en-cz/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
        ),
        Bike(
            title='Exceed CF 7',
            link='https://www.canyon.com/en-cz/mountain-bikes/cross-country-bikes/exceed/cf/exceed-cf-7/3128.html?dwvar_3128_pv_rahmenfarbe=WH%2FMC',
        )
    ]
    res = await insert_actual_catalog(bikes_list)

    assert res == 2
