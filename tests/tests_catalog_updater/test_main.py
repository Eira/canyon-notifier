from app.catalog_updater import main
from app.storage.catalog import get_catalog


async def test_main_smoke():
    res = await main(throttling_time=5.0, amount_of_iterations=2)

    assert res == 2


async def test_main_happy_path(fixture_prefilled_catalog):
    await main(throttling_time=5.0, amount_of_iterations=1)

    assert len(await get_catalog()) != len(fixture_prefilled_catalog)


async def test_main_no_catalog_source(mocker):
    mocker.patch('app.catalog_updater.get_canyon_catalog', return_value=[])
    mock = mocker.patch('app.catalog_updater.update_catalog')

    await main(throttling_time=5.0, amount_of_iterations=2)

    assert mock.call_count == 0
