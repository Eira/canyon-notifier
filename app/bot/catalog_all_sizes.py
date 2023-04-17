"""Modules required to display bikes of all sizes."""

from itertools import groupby

from aiogram import types
from aiogram.utils.markdown import hlink

from app.bot.common_handlers import get_main_keyboard
from app.models import CatalogFamily


async def send_all_sizes_catalog(catalog_family_group: list[CatalogFamily], message: types.Message) -> None:
    """Send messages with all bikes in the catalog."""
    for catalog_family in catalog_family_group:
        catalog_answer = [catalog_family.family] + _get_all_sizes_bike_list(catalog_family)

        await message.answer(
            '\n'.join(catalog_answer),
            parse_mode='HTML',
            disable_web_page_preview=True,
            reply_markup=get_main_keyboard(),
        )


def _get_all_sizes_bike_list(catalog_family: CatalogFamily) -> list[str]:
    """Return list of unique models of bikes with links and sizes."""
    # todo test
    catalog_positions = []
    for model, bikes in groupby(catalog_family.bike_list, lambda bike: bike.model):
        bikes_list = list(bikes)
        sizes_list = [bike.size for bike in list(bikes_list)]

        catalog_positions.append(
            '{link}  {sizes_list}'.format(
                link=hlink(f'{model}', bikes_list[0].link),
                sizes_list=', '.join(sizes_list),
            ),
        )

    return catalog_positions
