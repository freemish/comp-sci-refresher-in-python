"""Singleton pattern."""

import time


class ExpensiveStartupResource:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.access_count = 1
            cls._long_running_imaginary_connection_op()
            cls.instance = super(ExpensiveStartupResource, cls).__new__(cls)
        else:
            cls.access_count += 1
        return cls.instance

    @classmethod
    def _long_running_imaginary_connection_op(cls):
        print('sleeping...')
        time.sleep(2)


class Thing1ThatUsesExpensiveStartupResource:
    @staticmethod
    def use_startup_resource() -> int:
        return ExpensiveStartupResource().access_count


class Thing2ThatUsesExpensiveStartupResource:
    @staticmethod
    def use_startup_resource() -> bool:
        return ExpensiveStartupResource().access_count


def main():
    print('Demonstration of singleton pattern starting.')

    print('This is the first time we need the expensive startup resource. Once "loaded," it should not load again.')
    print('This uses the __new__ builtin Python class method to retain the same instance.')

    thing1 = Thing1ThatUsesExpensiveStartupResource()
    print('class instance access count:', thing1.use_startup_resource())
    print('class instance access count:', thing1.use_startup_resource())

    thing2 = Thing2ThatUsesExpensiveStartupResource()
    print('class instance access count:', thing2.use_startup_resource())


if __name__ == '__main__':
    main()

"""
$ python3 designpatterns/singleton.py
Demonstration of singleton pattern starting.
This is the first time we need the expensive startup resource. Once loaded, it should not load again.
This uses the __new__ builtin Python class method to retain the same instance.
sleeping...
class instance access count: 1
class instance access count: 2
class instance access count: 3
"""
