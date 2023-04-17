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


async def show_catalog(message: types.Message, state: FSMContext) -> None:
    """Return the list of all available bicycles."""
    await state.finish()

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

    if user_size not in sizes_list:
        await message.answer('There no such size in Canyon size grid.', reply_markup=get_main_keyboard())
        return

    custom_size_on: bool = user_size != buttons.SIZE_ALL_BUTTON

    catalog: list[Bike] = await get_catalog()
    if custom_size_on:
        catalog = [bike for bike in catalog if bike.size == user_size]

    if not catalog:
        no_bike_text = 'Sorry, there no any bikes available at the moment.'
        no_bike_size_text = f'Sorry, there no {user_size} bikes available at the moment.'
        await message.answer(
            no_bike_size_text if custom_size_on else no_bike_text,
            reply_markup=get_main_keyboard(),
        )
        return

    catalog_family_group: list[CatalogFamily] = [
        CatalogFamily(
            family=family,
            bike_list=list(bikes),
        )
        for family, bikes in groupby(catalog, lambda bike: bike.family)
    ]

    if custom_size_on:
        await _get_one_size_catalog(catalog_family_group, message)
    else:
        await _get_all_sizes_catalog(catalog_family_group, message)


async def _get_all_sizes_catalog(catalog_family_group: list[CatalogFamily], message: types.Message) -> None:
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


async def _get_one_size_catalog(catalog_family_group: list[CatalogFamily], message: types.Message) -> None:
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


def _chunks(chunkable_list: list, chunk_size: int) -> Generator:
    """Yield successive n-sized chunks from lst."""
    # todo test
    yield from (
        chunkable_list[index:index + chunk_size]
        for index in range(0, len(chunkable_list), chunk_size)
    )
