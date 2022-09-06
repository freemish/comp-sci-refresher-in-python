"""Singleton pattern."""

import time
from typing import Optional


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


class SpecializedMultitonResource:
    def __new__(cls, special_type: Optional[str] = None):
        print("__new__ classmethod called with special_type {}...".format(special_type))
        if not hasattr(cls, 'instance') or cls.special_type != special_type:
            print("initializing class for special_type", special_type)
            cls.special_type = special_type
            cls._run_once()
            cls.instance = super(SpecializedMultitonResource, cls).__new__(cls)
    @classmethod
    def _run_once(cls):
        print("Running a method that should only run when creating a new instance of a class.")



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

    print('This is the first time we need the expensive startup resource. Once "loaded," it should not load again. (See lazy_initialization.py example.)')
    print('This uses the __new__ builtin Python class method to retain the same instance.')

    thing1 = Thing1ThatUsesExpensiveStartupResource()
    print('class instance access count:', thing1.use_startup_resource())
    print('class instance access count:', thing1.use_startup_resource())

    thing2 = Thing2ThatUsesExpensiveStartupResource()
    print('class instance access count:', thing2.use_startup_resource())

    print("Now demonstrating the singleton-like multiton.") 
    print("If the same type is provided for a class that has been previously initialized, it will not create another instance.")
    SpecializedMultitonResource()
    SpecializedMultitonResource()
    SpecializedMultitonResource("molly")


if __name__ == '__main__':
    main()

"""
$ python3 designpatterns/singleton_and_multiton.py
Demonstration of singleton pattern starting.
This is the first time we need the expensive startup resource. Once "loaded," it should not load again. (See lazy_initialization.py example.)
This uses the __new__ builtin Python class method to retain the same instance.
sleeping...
class instance access count: 1
class instance access count: 2
class instance access count: 3
Now demonstrating the singleton-like multiton.
If the same type is provided for a class that has been previously initialized, it will not create another instance.
__new__ classmethod called with special_type None...
initializing class for special_type None
Running a method that should only run when creating a new instance of a class.
__new__ classmethod called with special_type None...
__new__ classmethod called with special_type molly...
initializing class for special_type molly
Running a method that should only run when creating a new instance of a class.
"""
