"""Bot runner."""
import logging

from aiogram import Bot, Dispatcher, executor, filters
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.bot import buttons, catalog_handlers, common_handlers, subscription_handlers
from app.settings import app_settings

bot = Bot(token=app_settings.bot_token)


def main() -> None:
    """Telegram bot app runner."""
    storage = MemoryStorage()
    router = Dispatcher(bot, storage=storage)

    _setup_main_routers(router)
    _setup_catalog_routers(router)
    _setup_subscription_routers(router)

    executor.start_polling(router, skip_updates=True)


def _setup_main_routers(router: Dispatcher) -> None:
    """Contain main routers."""
    router.register_message_handler(common_handlers.send_welcome, commands=['start', 'help'])
    router.register_message_handler(
        common_handlers.cancel,
        filters.Text(equals=buttons.BACK_FROM_SUBSCR_BUTTON, ignore_case=True),
        state='*',
    )


def _setup_catalog_routers(router: Dispatcher) -> None:
    """Contain catalog routers."""
    router.register_message_handler(
        catalog_handlers.start_show_catalog,
        filters.Text(equals=buttons.CATALOG_BUTTON, ignore_case=True),
    )
    router.register_message_handler(
        catalog_handlers.show_catalog,
        state=catalog_handlers.SortCatalogBySize.size_for_sort,
    )


def _setup_subscription_routers(router: Dispatcher) -> None:
    """Contain subscription routers."""
    router.register_message_handler(
        subscription_handlers.cancel_subscription,
        filters.Text(equals=buttons.CANCEL_SUBSCR_BUTTON, ignore_case=True),
        state='*',
    )
    router.register_message_handler(
        subscription_handlers.process_family_name,
        state=subscription_handlers.CreateSubscription.family_name,
    )
    router.register_message_handler(
        subscription_handlers.process_size_subscription,
        state=subscription_handlers.CreateSubscription.model_size,
    )
    router.register_message_handler(
        subscription_handlers.show_subscriptions,
        filters.Text(equals=buttons.SUBSCRIBTIONS_BUTTON, ignore_case=True),
    )
    router.register_message_handler(
        subscription_handlers.start_subscription,
        filters.Text(equals=buttons.SUBSCRIBE_BUTTON, ignore_case=True),
    )
    router.register_callback_query_handler(
        subscription_handlers.delete_subscription,
        lambda callback: callback.data and callback.data.startswith('delete_subscription:'),
    )


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main()
