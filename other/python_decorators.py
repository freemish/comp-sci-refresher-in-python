"""
Demo of how to create and use different kinds of custom Python decorators.
See: 
    https://www.freecodecamp.org/news/python-decorators-explained-with-examples/
    https://realpython.com/primer-on-python-decorators/
"""

from typing import Any, Callable, List, Optional, Tuple, Type


def basic_print_before_function_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        print("Hi, I'm about to run this function: {}".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper


def basic_print_after_function_decorator_no_return(func: Callable) -> Callable:
    def wrapper() -> Any:
        func()
        print("Hi, I just ran this function: {}".format(func.__name__))
    return wrapper


class Limiter:
    def __init__(self, func: Callable):
        self.func = func
        self.count = 0
    
    def __call__(self, limit: Optional[int] = None, *args, **kwargs) -> Tuple[bool, Any]:
        print("Using the Limiter decorator... limit is being enforced as {} and count is currently {}".format(limit, self.count))
        if limit is not None:
            if self.count >= limit:
                return (False, "Reached limit on calls")
        
        self.count += 1
        return (True, self.func(*args, **kwargs))


def repeat(num_times: int = 1) -> Callable:
    def decorator_repeater(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> List[Any]:
            results = []
            for _ in range(num_times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator_repeater


def class_decorator(klass: Type) -> Type:
    def funk_me_up(obj: Any) -> str:
        return "FUNKY DECORATOR: {}".format(obj._old_funk_me_up())
    
    setattr(klass, '_old_funk_me_up', klass.funk_me_up)
    setattr(klass, 'funk_me_up', funk_me_up)
    return klass


@basic_print_before_function_decorator
def funky() -> int:
    print("The funky function is running")
    return 0


@basic_print_after_function_decorator_no_return
def funky2() -> int:
    print("The funky2 function is running")
    return 1


@basic_print_before_function_decorator
def funky3(my_arg: str) -> int:
    print(my_arg)
    return 2


@Limiter
def funky4() -> int:
    print("funky4 is on the move")
    return 3

@repeat(5)
def funky5() -> int:
    print("funky5 is getting run")
    return 4


@class_decorator
class FunkyClass:
    def __init__(self, funktastic: bool = True):
        self.funktastic = funktastic
    
    def funk_me_up(self) -> str:
        return 'freaky funkyyy!' if self.funktastic else 'mock funk!'


def main() -> None:
    print(":Demo of a basic function decorator that accepts no arguments:")
    ret_val = funky()
    print(":Returned from funky:", ret_val)

    print(":Beware that your custom decorator can obscure the return value of the wrapped function.")
    ret_val = funky2()
    print(":Returned from funky2:", ret_val)

    print(":Also beware that your custom decorator will need special handling to support a wrapped function that accepts arguments.")
    print(":Make sure the inner wrapper function ")
    funky3("Hello")
    
    print(":You can use a class to create decorators as well so the decorator class can maintain independent state.")
    print(":Result for limit 0:", funky4(limit=0))
    print(":Result for limit 2:", funky4(2))

    print(":You can also wrap decorators in functions that return the decorator.")
    print(funky5())

    print(":You can even modify classes with decorators:", FunkyClass().funk_me_up())


if __name__ == '__main__':
    main()


"""
$ python3 other/python_decorators.py
:Demo of a basic function decorator that accepts no arguments:
Hi, I'm about to run this function: funky
The funky function is running
:Returned from funky: 0
:Beware that your custom decorator can obscure the return value of the wrapped function.
The funky2 function is running
Hi, I just ran this function: funky2
:Returned from funky2: None
:Also beware that your custom decorator will need special handling to support a wrapped function that accepts arguments.
:Make sure the inner wrapper function 
Hi, I'm about to run this function: funky3
Hello
:You can use a class to create decorators as well so the decorator class can maintain independent state.
Using the Limiter decorator... limit is being enforced as 0 and count is currently 0
(False, 'Reached limit on calls')
Using the Limiter decorator... limit is being enforced as 2 and count is currently 0
funky4 is on the move
(True, 3)
:You can also wrap decorators in functions that return the decorator.
funky5 is getting run
funky5 is getting run
funky5 is getting run
funky5 is getting run
funky5 is getting run
[4, 4, 4, 4, 4]
:You can even modify classes with decorators: FUNKY DECORATOR: freaky funkyyy!
"""
