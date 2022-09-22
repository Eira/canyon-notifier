"""
This is the module of canyon new bike's bot.

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


# Todo может и не пригодится
async def remove_subscription(message: types.Message) -> None:
    """Ask a bike family name and delete it from subscription list."""
    answer_text = '\n'.join((
        'Please, write the bike family name you dont want to have messages about.',
    ))

    await message.answer(answer_text)


async def show_subscriptions(message: types.Message) -> None:
    """Take all users subscription and show all subscriptions."""
    # Todo вывереси список подписок (посмотреть на списке байков)
    ...
