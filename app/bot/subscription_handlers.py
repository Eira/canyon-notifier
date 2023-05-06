"""
This is the module of bot subscription handlers.

It contains functions for create the subscription for the concrete model of the bike.
"""
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from app.bot import buttons
from app.bot.common_handlers import get_main_keyboard, get_sizes_keyboard
from app.settings import app_settings
from app.storage import subscription as subscription_storage
from app.storage.subscription import get_subscription_amount


class CreateSubscription(StatesGroup):
    """Manage the state of creating subscription."""

    family_name = State()
    model_size = State()


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
            'Please, write the bike family name.',
        ))
        await CreateSubscription.family_name.set()

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
    ).row(
        types.KeyboardButton(buttons.CANCEL_SUBSCR_BUTTON),
    )

    await message.reply(
        reply_text,
        reply_markup=markup,  # todo перенести в ифы
    )


async def cancel_subscription(message: types.Message, state: FSMContext) -> None:
    """Allow user to cancel action via /cancel command."""
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('Cancelled.', reply_markup=get_main_keyboard())


async def process_family_name(message: types.Message, state: FSMContext) -> None:
    """Save family name to db and ask about the size."""
    await state.update_data(family_name=message.text)
    answer_text = 'Please, choose the size of the bike.'

    await CreateSubscription.next()

    await message.answer(answer_text, reply_markup=get_sizes_keyboard())


async def process_size_subscription(message: types.Message, state: FSMContext) -> None:
    """Create the subscription."""
    # todo test "all" size
    bike_size = message.text
    if bike_size not in buttons.available_sizes_list:
        await message.reply(
            f'There no such bike size.\n Try one of this: {buttons.available_sizes_list}',
            reply_markup=get_sizes_keyboard(),
        )

        return

    if bike_size == buttons.SIZE_ALL_BUTTON:
        # todo
        ...

    created_subscription = await subscription_storage.create_subscription(
        message.chat.id,
        (await state.get_data())['family_name'],
        bike_size,
    )

    await state.finish()
    await message.answer(
        f'Got it! When "{created_subscription.bike_family} {bike_size}" will be available we will let you know!',
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
