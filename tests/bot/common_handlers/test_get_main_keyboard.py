from app.bot.common_handlers import get_main_keyboard


def test_get_main_keyboard_smoke():
    res = get_main_keyboard()

    assert res
