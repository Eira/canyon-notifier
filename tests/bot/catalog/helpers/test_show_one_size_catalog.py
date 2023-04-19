from unittest.mock import AsyncMock

from app.bot.catalog.catalog_helpers import show_one_size_catalog
from app.models import CatalogFamily, Bike


async def test_show_one_size_catalog_smoke():
    message_mock = AsyncMock()
    message_mock.text = 'M'
    catalog_family_group = [CatalogFamily(family='Spectral', bike_list=[Bike(id='spectral_125_cf_9_m', title='Spectral 125 CF 9', link='https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR', family='Spectral', model='125 CF 9', size='M')])]

    await show_one_size_catalog(catalog_family_group, message=message_mock)

    assert message_mock.answer.call_count == 1