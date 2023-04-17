from unittest.mock import AsyncMock

from app.bot.catalog_handlers import send_all_sizes_catalog
from app.models import CatalogFamily, Bike


async def test_get_all_sizes_catalog(fixture_prefilled_catalog_few_sizes):
    message_mock = AsyncMock()
    message_mock.text = 'all'
    catalog_family_group = [
        CatalogFamily(
            family='Spectral',
            bike_list=[
                Bike(
                    id='spectral_125_cf_9_m',
                    title='Spectral 125 CF 9',
                    link='https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
                    family='Spectral',
                    model='125 CF 9',
                    size='S'
                ),
                Bike(
                    id='spectral_125_cf_9_m',
                    title='Spectral 125 CF 9',
                    link='https://www.canyon.com/en-de/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR',
                    family='Spectral',
                    model='125 CF 9',
                    size='M',
                ),
            ]
        )
    ]
    await send_all_sizes_catalog(catalog_family_group, message=message_mock)
    # todo write assert
