from app.bot.catalog_all_sizes import _get_all_sizes_bike_list
from app.models import CatalogFamily, Bike


async def test_get_all_sizes_bike_list():
    catalog_family = CatalogFamily(family='Spectral', bike_list=[Bike(id='spectral_125_cf_9_m', title='Spectral 125 CF 9', link='https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR', family='Spectral', model='125 CF 9', size='M')])

    res = _get_all_sizes_bike_list(catalog_family)

    assert res == [
        '<a '
        'href="https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR">125 '
        'CF 9</a>  M'
    ]