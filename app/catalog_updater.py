"""Docstring."""
import time
from typing import Optional


def main(limit: Optional[int] = None, throttling_sec: int = 10) -> int:
    """Hello world function."""
    current_iteration = 0

    while limit is None or current_iteration < limit:
        current_iteration += 1
        print('it works!')  # noqa: WPS421
        time.sleep(throttling_sec)

    return current_iteration


if __name__ == '__main__':
    main()
