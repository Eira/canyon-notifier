from app.catalog_updater import main


async def test_main_happy_path():
    res = await main(throttling_time=5.0, amount_of_iterations=2)

    assert res == 2

# todo сделать проверки на пустой каталог снаружи и на пустой каталог в бд
