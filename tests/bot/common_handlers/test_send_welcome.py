from unittest.mock import AsyncMock

from app.bot.common_handlers import send_welcome


async def test_bot_send_welcome_happy_path():
    expected_answer = '\n'.join((
        'I will show you which canyon bicycles are available in the store.',
    ))
    message_mock = AsyncMock()

    await send_welcome(message=message_mock)

    assert message_mock.answer.await_args[0][0] == expected_answer
    # todo проверить клавиатуру
