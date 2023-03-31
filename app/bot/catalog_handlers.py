"""This is the module of bot catalog handlers."""

from itertools import groupby
from typing import Generator

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.markdown import hlink

from app.bot import buttons
from app.bot.common_handlers import get_main_keyboard, get_sizes_keyboard
from app.models import Bike, CatalogFamily
from app.storage.catalog import get_catalog


class SortCatalogBySize(StatesGroup):
    """Manage the state of creating subscription."""

    size_for_sort = State()


async def start_show_catalog(message: types.Message) -> None:
    """Ask user about the bike size. Show keyboard with sizes."""
    answer_text = 'Choose the bike size:'

    await SortCatalogBySize.size_for_sort.set()
    await message.answer(answer_text, reply_markup=get_sizes_keyboard())


def chunks(chunkable_list: list, chunk_size: int) -> Generator:
    """Yield successive n-sized chunks from lst."""
    # todo test
    yield from (
        chunkable_list[index:index + chunk_size]
        for index in range(0, len(chunkable_list), chunk_size)
    )


async def show_catalog(message: types.Message, state: FSMContext) -> None:  # noqa: WPS210
    """Return the list of all available bicycles."""
    sizes_list = {
        buttons.SIZE_ALL_BUTTON,
        buttons.SIZE_3XS_BUTTON,
        buttons.SIZE_2XS_BUTTON,
        buttons.SIZE_XS_BUTTON,
        buttons.SIZE_S_BUTTON,
        buttons.SIZE_M_BUTTON,
        buttons.SIZE_L_BUTTON,
        buttons.SIZE_XL_BUTTON,
        buttons.SIZE_2XL_BUTTON,
    }
    user_size = message.text

    if user_size in sizes_list:
        catalog: list[Bike] = await get_catalog()

        if user_size != buttons.SIZE_ALL_BUTTON:
            catalog: list[Bike] = [bike for bike in catalog if bike.size == user_size]

        if not catalog:
            await message.answer(
                f'Sorry, there no {user_size} bikes available at the moment.',
                reply_markup=get_main_keyboard(),
            )

        catalog_family_group: list[CatalogFamily] = [
            CatalogFamily(
                family=key,
                bike_list=list(group),
            )
            for key, group in groupby(catalog, lambda bike: bike.family)
        ]

        for catalog_family in catalog_family_group:
            bike_answer = [catalog_family.family] + [
                hlink(f'{bike.model} {bike.size}', bike.link)
                for bike in catalog_family.bike_list
            ]

            await message.answer(
                '\n'.join(bike_answer),
                parse_mode='HTML',
                disable_web_page_preview=True,
                reply_markup=get_main_keyboard(),
            )
    else:
        await message.answer('There no such size in Canyon size grid.', reply_markup=get_main_keyboard())

    await state.finish()
