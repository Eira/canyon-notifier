"""
This is the canyon new bikes bot.

It answers to any incoming text messages with the list of all commands.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

from app.settings import app_settings


async def send_welcome(message: types.Message) -> None:
    """Greeting user when user sends `/start` or `/help` command."""
    answer_text = '\n'.join((
        'Hi, friend!',
        'I will show you which canyon bicycles are available in the store.',
        '/all - to see all catalog.',
    ))

    await message.answer(answer_text)


async def wrong_command_helper(message: types.Message) -> None:
    """Return the list of all commands to any unknown command."""
    reply = '\n'.join((
        'Use one of the following commands:',
        '/start - welcome',
        '/help - list of all commands',
    ))
    await message.reply(reply)


def main() -> None:
    """Telegram bot app runner."""
    bot = Bot(token=app_settings.bot_token)

    router = Dispatcher(bot)
    router.register_message_handler(send_welcome, commands=['start', 'help'])
    router.register_message_handler(wrong_command_helper)
    executor.start_polling(router, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main()
