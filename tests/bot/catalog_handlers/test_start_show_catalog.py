from unittest.mock import AsyncMock

from app.bot.catalog_handlers import start_show_catalog


async def test_start_show_catalog_smoke(mocker):

    mock = mocker.patch('app.bot.catalog_handlers.SortCatalogBySize.size_for_sort.set')
    expected_reply = 'Choose the bike size:'
    message_mock = AsyncMock()

    await start_show_catalog(message=message_mock)

    assert mock.call_count == 1
    # todo проверить текст
