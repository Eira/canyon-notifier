"""
This is the module of bot subscription handlers.

It contains functions for create the subscription for the concrete model of the bike.
"""
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from app.bike_model import SubscriptionBikeFamily
from app.storage import create_subscription


class CreateSubscription(StatesGroup):
    """#TODO write what or is it."""

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
    created_subscription: SubscriptionBikeFamily = await create_subscription(message.chat.id, message.text)

    await state.finish()
    await message.reply(f'Got it! When "{created_subscription.bike_family}" will be available we will let you know!')
