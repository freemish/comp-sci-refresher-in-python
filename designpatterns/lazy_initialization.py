# Demonstrates lazy initialization of properties in Python.

from functools import cached_property
from time import sleep


class ExpensiveObject:
    @property
    def connection(self) -> bool:
        if not hasattr(self, '_CONNECTION'):
            print('sleeping to create first connection...')
            sleep(1)
            self._CONNECTION = True
        return self._CONNECTION

    @cached_property
    def connection_two(self) -> bool:
        print('sleeping to create second connection...')
        sleep(1)
        return True


def main() -> None:
    print("Starting demonstration of lazy initialization...")
    
    eo = ExpensiveObject()

    print("connection just uses property decorator and caches manually.")
    print(eo.connection)
    print(eo.connection)
    print(eo.connection)

    print("connection_two uses the cached_property decorator.")
    print(eo.connection_two)
    print(eo.connection_two)
    print(eo.connection_two)


if __name__ == '__main__':
    main()

"""
$ python3 designpatterns/lazy_initialization.py
Starting demonstration of lazy initialization...
connection just uses property decorator and caches manually.
sleeping to create first connection...
True
True
True
connection_two uses the cached_property decorator.
sleeping to create second connection...
True
True
True
"""