from unittest.mock import AsyncMock

from app.bot.common_handlers import send_welcome


async def test_bot_send_welcome_happy_path():
    expected_answer = '\n'.join((
        'Hi, friend!',
        'I will show you which canyon bicycles are available in the store.',
        '/catalog - to see all catalog.',
        '/subscribe - to get the message, when the bike family you want in the stock.',
        '/subscriptions_list - check if you are waiting for any messages.',
    ))
    message_mock = AsyncMock()

    await send_welcome(message=message_mock)

    assert message_mock.answer.await_args[0][0] == expected_answer
    # todo проверить клавиатуру
