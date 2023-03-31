from app.bot.common_handlers import get_sizes_keyboard


def test_get_main_keyboard_smoke():
    res = get_sizes_keyboard()

    assert res
