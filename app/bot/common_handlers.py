"""List of common bot handlers."""

from aiogram import types
from aiogram.dispatcher import FSMContext

from app.bot import buttons


async def send_welcome(message: types.Message) -> None:
    """Greeting user when user sends `/start` or `/help` command."""
    answer_text = '\n'.join((
        'Hi, friend!',
        'I will show you which canyon bicycles are available in the store.',
        '/catalog - to see all catalog.',
        '/subscribe - to get the message, when the bike family you want in the stock.',
        '/subscriptions_list - check if you are waiting for any messages.',
    ))

    await message.answer(answer_text, reply_markup=get_main_keyboard())


async def cancel(message: types.Message, state: FSMContext) -> None:
    """Cancel of current operation in bot. Return welcome message and keyboard."""
    await state.finish()
    await send_welcome(message)


def get_main_keyboard() -> types.ReplyKeyboardMarkup:
    """Return the main keyboard markup."""
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
    ).row(
        types.KeyboardButton(buttons.CATALOG_BUTTON),
    ).row(
        types.KeyboardButton(buttons.SUBSCRIBTIONS_BUTTON),
    )


def get_sizes_keyboard() -> types.ReplyKeyboardMarkup:
    """Return the keyboard markup with bike sizes."""
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
    ).row(
        types.KeyboardButton(buttons.SIZE_ALL_BUTTON),
    ).row(
        types.KeyboardButton(buttons.SIZE_3XS_BUTTON),
        types.KeyboardButton(buttons.SIZE_2XS_BUTTON),
        types.KeyboardButton(buttons.SIZE_XS_BUTTON),
        types.KeyboardButton(buttons.SIZE_S_BUTTON),
    ).row(
        types.KeyboardButton(buttons.SIZE_M_BUTTON),
        types.KeyboardButton(buttons.SIZE_L_BUTTON),
        types.KeyboardButton(buttons.SIZE_XL_BUTTON),
        types.KeyboardButton(buttons.SIZE_2XL_BUTTON),
    ).row(
        types.KeyboardButton(buttons.BACK_FROM_SUBSCR_BUTTON),
    )
