"""
This is the canyon new bike's bot.

It answers to any incoming text messages with the list of all commands.
"""
import itertools
import logging
from itertools import groupby
from typing import Generator, List, Tuple

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hlink

from app.bike_model import Bike
from app.settings import app_settings
from app.storage import get_catalog


async def send_welcome(message: types.Message) -> None:
    """Greeting user when user sends `/start` or `/help` command."""
    answer_text = '\n'.join((
        'Hi, friend!',
        'I will show you which canyon bicycles are available in the store.',
        '/catalog - to see all catalog.',
    ))

    await message.answer(answer_text)


def chunks(chunkable_list: list, chunk_size: int) -> Generator:
    """Yield successive n-sized chunks from lst."""
    yield from (
        chunkable_list[index:index + chunk_size]
        for index in range(0, len(chunkable_list), chunk_size)
    )


async def show_catalog(message: types.Message) -> None:
    """Return the list of all available bicycles."""
    catalog: List[Bike] = await get_catalog()

    catalog_family_group: List[Tuple[str, List[Bike]]] = []
    for key, group in groupby(catalog, lambda x: x.family):
        catalog_family_group.append((key, list(group)))

    for bike_family_name, bikes in catalog_family_group:
        bike_model_link_list = [hlink(bike.model, bike.link) for bike in bikes]
        bike_answer = [bike_family_name] + bike_model_link_list

        await message.answer(
            '\n'.join(bike_answer),
            parse_mode='HTML',
            disable_web_page_preview=True,
        )


def main() -> None:
    """Telegram bot app runner."""
    bot = Bot(token=app_settings.bot_token)

    router = Dispatcher(bot)
    router.register_message_handler(send_welcome, commands=['start', 'help'])
    router.register_message_handler(show_catalog, commands=['catalog'])
    executor.start_polling(router, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main()