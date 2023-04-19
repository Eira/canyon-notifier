"""This is the module of bot catalog handlers."""

from itertools import groupby

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from app.bot import buttons
from app.bot.catalog.catalog_helpers import show_all_sizes_catalog, show_one_size_catalog
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
    """Prepare bikes catalog. Send it to the user."""
    await state.finish()

    user_size = message.text

    if user_size not in buttons.available_sizes_list:
        await message.answer('There no such size in Canyon size grid.', reply_markup=get_main_keyboard())
        return

    custom_size_on: bool = user_size != buttons.SIZE_ALL_BUTTON

    catalog: list[Bike] = await get_catalog()
    if custom_size_on:
        catalog = [bike for bike in catalog if bike.size == user_size]

    await _output_catalog(
        catalog,
        message,
        custom_size_on,
        user_size,
    )


async def _output_catalog(
    catalog: list[Bike],
    message: types.Message,
    custom_size_on: bool,
    user_size: str,
) -> None:
    """Send messages with customised catalog."""
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
        await show_one_size_catalog(catalog_family_group, message)
    else:
        await show_all_sizes_catalog(catalog_family_group, message)
