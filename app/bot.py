"""
This is the canyon new bikes bot.

It answers to any incoming text messages with the list of all commands.
"""

import logging
from typing import Generator

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hlink

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


async def wrong_command_helper(message: types.Message) -> None:
    """Return the list of all commands to any unknown command."""
    reply = '\n'.join((
        'Use one of the following commands:',
        '/start - welcome',
        '/help - list of all commands',
        '/catalog - list of all available bicycles',
    ))
    await message.reply(reply)


def chunks(chunkable_list: list, chunk_size: int) -> Generator:
    """Yield successive n-sized chunks from lst."""
    yield from (
        chunkable_list[index:index + chunk_size]
        for index in range(0, len(chunkable_list), chunk_size)
    )


async def show_catalog(message: types.Message) -> None:
    # todo happy path tests ?
    """Return the list of all available bicycles."""
    catalog = await get_catalog()
    bike_as_str_list = []
    for bike in catalog:
        bike_as_str_list.append(hlink(bike.title, bike.link))

    for bikes_chunks in chunks(bike_as_str_list, app_settings.telegram_max_entities):
        answer_text = '\n'.join(bikes_chunks)

        await message.answer(
            answer_text,
            parse_mode='HTML',
            disable_web_page_preview=True,
        )


def main() -> None:
    """Telegram bot app runner."""
    bot = Bot(token=app_settings.bot_token)

    router = Dispatcher(bot)
    router.register_message_handler(send_welcome, commands=['start', 'help'])
    router.register_message_handler(show_catalog, commands=['catalog'])
    router.register_message_handler(wrong_command_helper)
    executor.start_polling(router, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main()
