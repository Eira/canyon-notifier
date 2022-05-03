from app.hello import main


def test_main_happy_path():
    res = main()

    assert res is True
