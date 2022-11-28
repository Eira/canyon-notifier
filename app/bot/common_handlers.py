"""List of common bot handlers."""

from itertools import groupby
from typing import Generator, List

from aiogram import types
from aiogram.utils.markdown import hlink

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

    await message.answer(answer_text)


def chunks(chunkable_list: list, chunk_size: int) -> Generator:
    """Yield successive n-sized chunks from lst."""
    yield from (
        chunkable_list[index:index + chunk_size]
        for index in range(0, len(chunkable_list), chunk_size)
    )


async def show_catalog(message: types.Message) -> None:  # noqa: WPS210
    """Return the list of all available bicycles."""
    catalog: List[Bike] = await get_catalog()

    catalog_family_group: List[CatalogFamily] = [
        CatalogFamily(
            family=key,
            bike_list=list(group),
        )
        for key, group in groupby(catalog, lambda bike: bike.family)
    ]

    for catalog_family in catalog_family_group:
        bike_answer = [catalog_family.family] + [
            hlink(bike.model, bike.link)
            for bike in catalog_family.bike_list
        ]

        await message.answer(
            '\n'.join(bike_answer),
            parse_mode='HTML',
            disable_web_page_preview=True,
        )
