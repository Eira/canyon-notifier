"""List of common bot handlers."""

from itertools import groupby
from typing import Generator, List

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.markdown import hlink

from app.bot import buttons
from app.models import Bike, CatalogFamily
from app.storage.catalog import get_catalog


async def send_welcome(message: types.Message) -> None:
    """Greeting user when user sends `/start` or `/help` command."""
    answer_text = '\n'.join((
        'Hi, friend!',
        'I will show you which canyon bicycles are available in the store.',
        '/catalog - to see all catalog.',
        '/subscribe - to get the message, when the bike family you want in the stock.',
        '/subscriptions_list - check if you are waiting for any messages.',
    ))

    await message.answer(answer_text, reply_markup=_get_main_keyboard())


class SortCatalogBySize(StatesGroup):
    """Manage the state of creating subscription."""

    size_for_sort = State()


async def start_show_catalog(message: types.Message) -> None:
    """Ask user about the bike size. Show keyboard with sizes."""
    answer_text = 'Choose the bike size:'

    await SortCatalogBySize.size_for_sort.set()
    await message.answer(answer_text, reply_markup=_get_sizes_keyboard())


def chunks(chunkable_list: list, chunk_size: int) -> Generator:
    """Yield successive n-sized chunks from lst."""
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
        catalog: List[Bike] = await get_catalog()

        if user_size != buttons.SIZE_ALL_BUTTON:
            catalog: List[Bike] = [bike for bike in catalog if bike.size == user_size]

        if not catalog:
            await message.answer(
                f'Sorry, there no {user_size} bikes available at the moment.',
                reply_markup=_get_main_keyboard(),
            )

        catalog_family_group: List[CatalogFamily] = [
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
                reply_markup=_get_main_keyboard(),
            )
    else:
        await message.answer('There no such size in Canyon size grid.', reply_markup=_get_main_keyboard())

    await state.finish()


def _get_main_keyboard() -> types.ReplyKeyboardMarkup:
    """Return the keyboard markup."""
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
    ).row(
        types.KeyboardButton(buttons.KATALOG_BUTTON),
    ).row(
        types.KeyboardButton(buttons.SUBSCRIBTIONS_BUTTON),
    )


def _get_sizes_keyboard() -> types.ReplyKeyboardMarkup:
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
    ).row(
        types.KeyboardButton(buttons.SIZE_ALL_BUTTON),
    ).row(
        types.KeyboardButton(buttons.SIZE_3XS_BUTTON),
        types.KeyboardButton(buttons.SIZE_2XS_BUTTON),
        types.KeyboardButton(buttons.SIZE_XS_BUTTON),
        types.KeyboardButton(buttons.SIZE_S_BUTTON),
    ).row(
        types.KeyboardButton(buttons.SIZE_M_BUTTON),
        types.KeyboardButton(buttons.SIZE_L_BUTTON),
        types.KeyboardButton(buttons.SIZE_XL_BUTTON),
        types.KeyboardButton(buttons.SIZE_2XL_BUTTON),
    ).row(
        types.KeyboardButton(buttons.BACK_FROM_SUBSCR_BUTTON),
    )
