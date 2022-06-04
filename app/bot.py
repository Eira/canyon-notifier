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
async def send_welcome(message: types.Message):
    """ This handler will be called when user sends `/start` or `/help` command."""

    await message.answer(
        "Hi, friend!\n"
        "I will show you which canyon bicycles are available in the store.\n"
        "/all - to see all catalog."
    )


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(
        "Use one of the following commands:\n"
        "/start - welcome\n"
        "/help - list of all commands\n"
    )


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    executor.start_polling(dp, skip_updates=True)
