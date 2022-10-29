# https://medium.com/codex/3-most-effective-yet-underutilized-functions-in-python-d865ffaca0bb

from functools import reduce
from typing import Any, Callable, List, Optional

tests = {
    'map': {
        'double': {
            'input': [1, 2, 3, 4],
            'output': [2, 4, 6, 8],
        },
    },
    'filter': {
        'no_gt_3': {
            'input': [1, 2, 3, 4],
            'output': [1, 2],
        },
    },
    'reduce': {
        'subtract': {
            'input': [21, 11, 3, 4],
            'output': 3,
        },
    },
}


def map_with_loop(lst: List[Any], fnc: Callable) -> List[Any]:
    new_list = []
    for item in lst:
        new_list.append(fnc(item))
    return new_list


def map_without_loop(lst: List[Any], fnc: Callable) -> List[Any]:
    return list(map(fnc, lst))


def filter_with_loop(lst: List[Any], fnc: Callable) -> List[Any]:
    new_list = []
    for item in lst:
        if fnc(item):
            new_list.append(item)
    return new_list


def filter_without_loop(lst: List[Any], fnc: Callable) -> List[Any]:
    return list(filter(fnc, lst))


def reduce_with_loop(lst: List[Any], fnc: Callable) -> Optional[Any]:
    if not lst:
        return None
    val = lst[0]
    for item in lst[1:]:
        val = fnc(val, item)
    return val


def reduce_without_loop(lst: List[Any], fnc: Callable) -> Optional[Any]:
    return reduce(fnc, lst)


def main() -> None:
    double_func = lambda x: x*2
    assert (
        map_with_loop(tests['map']['double']['input'], double_func)
        == map_without_loop(tests['map']['double']['input'], double_func)
        == tests['map']['double']['output']
    )
    print("Map works")

    not_gt_3_func = lambda x: x if x < 3 else None
    assert (
        filter_with_loop(tests['filter']['no_gt_3']['input'], not_gt_3_func)
        == filter_without_loop(tests['filter']['no_gt_3']['input'], not_gt_3_func)
        == tests['filter']['no_gt_3']['output']
    )
    print("Filter works")

    subtract_func = lambda x, y: x-y
    assert (
        reduce_with_loop(tests['reduce']['subtract']['input'], subtract_func)
        == reduce_without_loop(tests['reduce']['subtract']['input'], subtract_func)
        == tests['reduce']['subtract']['output']
    )
    print("Reduce works")


if __name__ == '__main__':
    main()


"""
$ python3 other/fancy_ways_to_loop.py 
Map works
Filter works
Reduce works
"""
