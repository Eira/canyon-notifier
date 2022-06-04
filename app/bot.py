"""
This is the canyon new bikes bot.

It answers to any incoming text messages with the list of all commands.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

from app.settings import app_settings

API_TOKEN = app_settings.bot_token


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message) -> None:
    """Greeting user when user sends `/start` or `/help` command."""
    answer_text: str = """
        Hi, friend!
I will show you which canyon bicycles are available in the store.
/all - to see all catalog.
    """
    await message.answer(answer_text)


@dp.message_handler()
async def echo(message: types.Message) -> None:
    """Return the list of all commands to any unknown command."""
    reply_test: str = """
        Use one of the following commands:
/start - welcome
/help - list of all commands
    """
    await message.reply(reply_test)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    executor.start_polling(dp, skip_updates=True)
