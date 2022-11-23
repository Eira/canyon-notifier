"""Bot runner."""
import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.bot import common_handlers, subscription_handlers
from app.settings import app_settings

bot = Bot(token=app_settings.bot_token)


def main() -> None:
    """Telegram bot app runner."""
    storage = MemoryStorage()

    router = Dispatcher(bot, storage=storage)
    router.register_message_handler(common_handlers.send_welcome, commands=['start', 'help'])
    router.register_message_handler(common_handlers.show_catalog, commands=['catalog'])
    router.register_message_handler(subscription_handlers.start_subscription, commands=['subscribe'])
    router.register_message_handler(subscription_handlers.cancel_subscription, state='*', commands=['cancel'])
    router.register_message_handler(
        subscription_handlers.process_subscription,
        state=subscription_handlers.CreateSubscription.family_name,
    )
    router.register_message_handler(subscription_handlers.show_subscriptions, commands=['subscriptions_list'])
    router.register_callback_query_handler(
        subscription_handlers.delete_subscription,
        lambda callback: callback.data and callback.data.startswith('delete_subscription:'),
    )
    executor.start_polling(router, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main()
