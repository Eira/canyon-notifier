from app.catalog_updater import main


def test_happy_path():
    res = main(5, 0)

    assert res == 5
