# See this video for an approachable explanation of monads:
# https://youtu.be/C2w45qRc3aU

from typing import Callable, List, Optional


# Functions that don't use monoids:

def square(num: int) -> int:
    return num * num


def add_one(num: int) -> int:
    return num + 1


result = add_one(square(2))
assert result == 5
print("Result of simple number operation functions without logging:", result)


# Now we want to add logging. When we call these two functions,
# they should both return logs such that we end up with a list of operations:

desired_logs = [
    "Squared 2 to get 4.",
    "Added 1 to 4 to get 5.",
]


# To this end, the functions above will be rewritten so that they return
# an object that has both the result and relevant logs.

class NumberWithLogs:
    def __init__(self, result: int, logs: List[str]):
        self.result = result
        self.logs = logs

    def __str__(self) -> str:
        return '\n\tresult: {}\n\tlogs: {}'.format(self.result, self.logs)


def square(num: int) -> NumberWithLogs:
    return NumberWithLogs(result=num*num, logs=[f'Squared {num} to get {num * num}.'])


def add_one(num_with_logs: NumberWithLogs) -> NumberWithLogs:
    return NumberWithLogs(
        result=num_with_logs.result+1,
        logs=num_with_logs.logs +
        [f'Added 1 to {num_with_logs.result} to get {num_with_logs.result+1}.']
    )


result = add_one(square(2))
assert result.result == 5
assert result.logs == desired_logs
print("Result with NumberWithLogs initial implementation:", str(result))

# The problem with this is that any other order of operations isn't accounted for.

try:
    result = square(square(2))
except Exception as exc:
    print("Expected error from trying to square 2 twice with new logging type implementation:", exc)


try:
    result = add_one(4)
except Exception as exc:
    print("Expected error from trying to add one to a number directly with new logging type implementation:", exc)


# This can be fixed with a new "wrapper" function + by tweaking the square function
# *(could also "overload" constructor of new type to accept no list param, but whatever, pretend with me that this is The Way)

def wrap_with_logs(num: int) -> NumberWithLogs:
    return NumberWithLogs(result=num, logs=[])


def square(num_with_logs: NumberWithLogs) -> NumberWithLogs:
    return NumberWithLogs(
        result=num_with_logs.result * num_with_logs.result,
        logs=(
            num_with_logs.logs
            + [f'Squared {num_with_logs.result} to get {num_with_logs.result * num_with_logs.result}.']
        )
    )


result1 = add_one(square(wrap_with_logs(2)))
result2 = square(square(wrap_with_logs(2)))
result3 = add_one(wrap_with_logs(4))

print("1. squared 2 and added one:", result1)
print("2. squared 2 and squared the result", result2)
print("3. added 1 to 4", result3)


# Next issue to address: the code is not dry. Both functions do the same logic with log concatenation.

def run_with_logs(input_nwl: NumberWithLogs, fnc: Callable[[NumberWithLogs], NumberWithLogs]) -> NumberWithLogs:
    num_with_logs = fnc(input_nwl)
    return NumberWithLogs(
        result=num_with_logs.result,
        logs=input_nwl.logs + num_with_logs.logs,
    )


def square(num_with_logs: NumberWithLogs) -> NumberWithLogs:
    return NumberWithLogs(
        result=num_with_logs.result * num_with_logs.result,
        logs=[
            f'Squared {num_with_logs.result} to get {num_with_logs.result * num_with_logs.result}.'],
    )


def add_one(num_with_logs: NumberWithLogs) -> NumberWithLogs:
    return NumberWithLogs(
        result=num_with_logs.result+1,
        logs=[
            f'Added 1 to {num_with_logs.result} to get {num_with_logs.result+1}.'],
    )


result1_1 = run_with_logs(run_with_logs(wrap_with_logs(2), square), add_one)
result2_1 = run_with_logs(run_with_logs(wrap_with_logs(2), square), square)
result3_1 = run_with_logs(wrap_with_logs(4), add_one)

print("1.1 squared 2 and added one:", result1_1)
print("2.1 squared 2 and squared the result", result2_1)
print("3.1 added 1 to 4", result3_1)

assert result1.result == result1_1.result
assert result1.logs == result1_1.logs
assert result2.result == result2_1.result
assert result2.logs == result2_1.logs
assert result3.result == result3_1.result
assert result3.logs == result3_1.logs


# Should make it easy to add other transformation functions, e.g.:

def multiply_by_three(num_with_logs: NumberWithLogs) -> NumberWithLogs:
    return NumberWithLogs(
        result=num_with_logs.result*3,
        logs=[
            f'Multiplied {num_with_logs.result} by 3 to get {num_with_logs.result*3}.']
    )


desired_logs_2 = [
    'Multiplied 1 by 3 to get 3.',
    'Added 1 to 3 to get 4.',
]

result = run_with_logs(run_with_logs(
    wrap_with_logs(1), multiply_by_three), add_one)
print('New multiply by 3 func:', result)
assert result.result == 4
assert result.logs == desired_logs_2


# A way that I might simplify this for readability slightly using methods on the NumberWithLogs class:

class NumberWithLogs:
    def __init__(self, result: int, logs: Optional[List[str]] = None):
        # Optional logs param removes need for wrap_with_logs func
        self.result = result
        self.logs = logs or []

    def __str__(self) -> str:
        return '\n\tresult: {}\n\tlogs: {}'.format(self.result, self.logs)

    def run_transformation(self, transform_func: Callable[[NumberWithLogs], NumberWithLogs]) -> NumberWithLogs:
        # Use instead of run_with_logs func
        num_with_logs = transform_func(self)
        return NumberWithLogs(
            result=num_with_logs.result,
            logs=self.logs + num_with_logs.logs,
        )


result1_2 = NumberWithLogs(2).run_transformation(square).run_transformation(add_one)
print('1.2 with readability modification:', result1_2)
assert result1.result == result1_2.result
assert result1.logs == result1_2.logs

# Monads are a pattern that have these three components:
# - wrapper type (NumberWithLogs)
# - wrap function (allows entry to monad by converting type to wrapper type: wrap_with_logs)
# - run function (runs transformations on monadic values: run_with_logs)
