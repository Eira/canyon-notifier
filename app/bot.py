"""
This is the canyon new bike's bot.

It answers to any incoming text messages with the list of all commands.
"""
import logging
from itertools import groupby
from typing import Generator, List

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.markdown import hlink

from app.bike_model import Bike, CatalogFamily, SubscriptionBikeFamily
from app.settings import app_settings
from app.storage import get_catalog, create_subscription


class CreateSubscription(StatesGroup):
    family_name = State()


async def send_welcome(message: types.Message) -> None:
    """Greeting user when user sends `/start` or `/help` command."""
    answer_text = '\n'.join((
        'Hi, friend!',
        'I will show you which canyon bicycles are available in the store.',
        '/catalog - to see all catalog.',
        '/subscribe - to get the message, when the bike family you want in the stock.',
#        '/unsubscribe - not to receive messages about bike family.',
#        '/subscriptions_list - check if you waiting for any messages.',
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


async def start_subscription(message: types.Message) -> None:
    """Ask a bike family name."""
    reply_text = '\n'.join((
        'Please, write the bike family name.When it will be available we will let you know!',
        '/cancel - to cancel the action.',
    ))
    await CreateSubscription.family_name.set()
    await message.reply(reply_text)


async def cancel_subscription(message: types.Message, state: FSMContext):
    """Allow user to cancel action via /cancel command"""

    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('Cancelled.')


async def process_subscription(message: types.Message, state: FSMContext) -> None:
    """Create the subscription."""

    created_subscription: SubscriptionBikeFamily = await create_subscription(message.chat.id, message.text)

    await state.finish()
    await message.reply(f'Got it! When "{created_subscription.bike_family}" will be available we will let you know!')


# Todo может и не пригодится
async def remove_subscription(message: types.Message) -> None:
    """Ask a bike family name and delete it from subscription list."""
    answer_text = '\n'.join((
        'Please, write the bike family name you dont want to have messages about.',
    ))

    await message.answer(answer_text)


async def show_subscriptions(message: types.Message) -> None:
    """Shows all subscriptions."""
    # Todo вывереси список подписок (посмотреть на списке байков)
    ...


def main() -> None:
    """Telegram bot app runner."""
    bot = Bot(token=app_settings.bot_token)
    storage = MemoryStorage()

    router = Dispatcher(bot, storage=storage)
    router.register_message_handler(send_welcome, commands=['start', 'help'])
    router.register_message_handler(show_catalog, commands=['catalog'])
    router.register_message_handler(start_subscription, commands=['subscribe'])
    router.register_message_handler(cancel_subscription, state='*', commands=['cancel'])
    router.register_message_handler(process_subscription, state=CreateSubscription.family_name)
    router.register_message_handler(remove_subscription, commands=['unsubscribe'])
    router.register_message_handler(show_subscriptions, commands=['subscriptions_list'])
    executor.start_polling(router, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main()
