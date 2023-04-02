"""
This is the module of bot subscription handlers.

It contains functions for create the subscription for the concrete model of the bike.
"""
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from app.bot import buttons
from app.bot.common_handlers import get_main_keyboard
from app.settings import app_settings
from app.storage import subscription as subscription_storage
from app.storage.subscription import get_subscription_amount


class CreateSubscription(StatesGroup):
    """Manage the state of creating subscription."""

    family_name = State()


async def start_subscription(message: types.Message) -> None:
    """Check amount of subscriptions.If it's ok, ask a bike family name."""
    subscription_amount = await get_subscription_amount(message.chat.id)

    if subscription_amount >= app_settings.max_amount_subscriptions:
        reply_text = '\n'.join((
            'You have already 10 subscriptions.',
            'Delete some to create a new one, please.',
        ))
    else:
        reply_text = '\n'.join((
            'Please, write the bike family name.When it will be available we will let you know!',
        ))
        await CreateSubscription.family_name.set()
    await message.reply(reply_text, reply_markup=_get_subscription_keyboard())


async def cancel_subscription(message: types.Message, state: FSMContext) -> None:
    """Allow user to cancel action via /cancel command."""
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('Cancelled.', reply_markup=get_main_keyboard())


async def process_subscription(message: types.Message, state: FSMContext) -> None:
    """Create the subscription."""
    created_subscription = await subscription_storage.create_subscription(
        message.chat.id,
        message.text,
    )

    await state.finish()
    await message.reply(
        f'Got it! When "{created_subscription.bike_family}" will be available we will let you know!',
        reply_markup=get_main_keyboard(),
    )


async def show_subscriptions(message: types.Message) -> None:
    """Take all users subscription and show all subscriptions."""
    list_of_subscriptions = await subscription_storage.get_subscriptions(message.chat.id)

    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
    ).row(
        types.KeyboardButton(buttons.SUBSCRIBE_BUTTON),
    ).row(
        types.KeyboardButton(buttons.BACK_FROM_SUBSCR_BUTTON),
    )

    if list_of_subscriptions:
        for subscription_item in list_of_subscriptions:
            inline_kb1 = types.InlineKeyboardMarkup().add(
                types.InlineKeyboardButton(
                    text=buttons.DELETE_BUTTON,
                    callback_data=f'delete_subscription:{subscription_item.subscribe_id}',
                ),
            )

            await message.answer(
                subscription_item.bike_family,
                reply_markup=inline_kb1,
            )

        await message.answer('That is all subscriptions you have.', reply_markup=keyboard)
    else:
        answer_text = '\n'.join((
            'You do not have any subscriptions yet.',
        ))
        await message.answer(answer_text, reply_markup=keyboard)


async def delete_subscription(callback_query: types.CallbackQuery) -> None:
    """Delete selected subscription and show all the rest subscriptions."""
    subscription_id = int(callback_query.data.split(':')[1])
    await subscription_storage.delete_subscription(subscription_id)
    await callback_query.answer('the subscription was deleted.')
    await show_subscriptions(callback_query.message)


def _get_subscription_keyboard() -> types.ReplyKeyboardMarkup:
    """Return the subscription keyboard markup."""
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
    ).row(
        types.KeyboardButton(buttons.CANCEL_SUBSCR_BUTTON),
    )
