"""
This is the canyon new bike's bot.

It answers to any incoming text messages with the list of all commands.
"""
import logging
from itertools import groupby
from typing import Generator, List

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.markdown import hlink

from app import bot_subscription
from app.bike_model import Bike, CatalogFamily
from app.settings import app_settings
from app.storage import get_catalog


async def send_welcome(message: types.Message) -> None:
    """Greeting user when user sends `/start` or `/help` command."""
    answer_text = '\n'.join((
        'Hi, friend!',
        'I will show you which canyon bicycles are available in the store.',
        '/catalog - to see all catalog.',
        '/subscribe - to get the message, when the bike family you want in the stock.',
        # '/unsubscribe - not to receive messages about bike family.',
        # '/subscriptions_list - check if you waiting for any messages.',
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


def main() -> None:
    """Telegram bot app runner."""
    bot = Bot(token=app_settings.bot_token)
    storage = MemoryStorage()

    router = Dispatcher(bot, storage=storage)
    router.register_message_handler(send_welcome, commands=['start', 'help'])
    router.register_message_handler(show_catalog, commands=['catalog'])
    router.register_message_handler(bot_subscription.start_subscription, commands=['subscribe'])
    router.register_message_handler(bot_subscription.cancel_subscription, state='*', commands=['cancel'])
    router.register_message_handler(
        bot_subscription.process_subscription,
        state=bot_subscription.CreateSubscription.family_name,
    )
    router.register_message_handler(bot_subscription.remove_subscription, commands=['unsubscribe'])
    router.register_message_handler(bot_subscription.show_subscriptions, commands=['subscriptions_list'])
    executor.start_polling(router, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main()
