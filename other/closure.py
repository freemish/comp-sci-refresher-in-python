"""Demonstrates retention of a locally-scoped variable."""

from typing import Callable


def outer_fnc() -> Callable:
    inner_var = 'a'

    def inner_fnc() -> None:
        print(inner_var)

    return inner_fnc


if __name__ == '__main__':
    inner_fnc = outer_fnc()
    inner_fnc()
