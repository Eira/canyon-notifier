"""Modules required to display bikes in selected size."""

from aiogram import types
from aiogram.utils.markdown import hlink

from app.bot.common_handlers import get_main_keyboard
from app.models import CatalogFamily


async def send_one_size_catalog(catalog_family_group: list[CatalogFamily], message: types.Message) -> None:
    """Send messages with bikes of selected size."""
    for catalog_family in catalog_family_group:
        bike_answer = [catalog_family.family] + [
            hlink(f'{bike.model}', bike.link)
            for bike in catalog_family.bike_list
        ]

        await message.answer(
            '\n'.join(bike_answer),
            parse_mode='HTML',
            disable_web_page_preview=True,
            reply_markup=get_main_keyboard(),
        )
