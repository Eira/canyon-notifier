"""
This is the module of bot subscription handlers.

It contains functions for create the subscription for the concrete model of the bike.
"""
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from app import storage
from app.bike_model import SubscriptionBikeFamily


class CreateSubscription(StatesGroup):
    """Manage the state of creating subscription."""

    family_name = State()


async def start_subscription(message: types.Message) -> None:
    """Ask a bike family name."""
    reply_text = '\n'.join((
        'Please, write the bike family name.When it will be available we will let you know!',
        '/cancel - to cancel the action.',
    ))
    await CreateSubscription.family_name.set()
    await message.reply(reply_text)


async def cancel_subscription(message: types.Message, state: FSMContext) -> None:
    """Allow user to cancel action via /cancel command."""
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('Cancelled.')


async def process_subscription(message: types.Message, state: FSMContext) -> None:
    """Create the subscription."""
    created_subscription: SubscriptionBikeFamily = await storage.create_subscription(message.chat.id, message.text)

    await state.finish()
    await message.reply(f'Got it! When "{created_subscription.bike_family}" will be available we will let you know!')


async def show_subscriptions(message: types.Message) -> None:
    """Take all users subscription and show all subscriptions."""
    list_of_subscriptions = await storage.get_subscriptions(message.chat.id)

    if list_of_subscriptions:
        btn_list_subscriptions: list = []

        for subscription_item in list_of_subscriptions:
            btn_list_subscriptions.append(
                types.InlineKeyboardButton(
                    text=subscription_item.bike_family,
                    callback_data=f'delete_subscription:{subscription_item.subscribe_id}',
                ),
            )
        inline_kb1 = types.InlineKeyboardMarkup().add(*btn_list_subscriptions)
        await message.answer('Press the button to delete subscription:', reply_markup=inline_kb1)
    else:
        answer_test = '\n'.join((
            'You do not have any subscriptions yet.',
            '/subscribe - to make one.',
        ))
        await message.answer(answer_test)


async def delete_subscription(callback_query: types.CallbackQuery) -> None:
    """Delete selected subscription and show all the rest subscriptions."""
    subscription_id = int(callback_query.data.split(':')[1])
    await storage.delete_subscription(subscription_id)
    await callback_query.answer('the subscription was deleted.')
    await show_subscriptions(callback_query.message)


