"""Functions to help with sort demos."""

from collections import Counter
from random import randint
from typing import Callable, List, Optional, Tuple


def get_random_list(
        min_len_list: int = 5,
        max_len_list: int = 12,
        min_val_list: int = 1,
        max_val_list: int = 20,
    ) -> List[int]:
    return [
        randint(min_val_list, max_val_list)
        for _ in range(randint(min_len_list, max_len_list))
    ]


def get_operations(fnc: Callable, lst: List[int]) -> Tuple[List[str], Counter]:
    operations = fnc(lst)
    operation_buckets = Counter(''.join([x.strip()[0] for x in operations]))

    return (operations, operation_buckets)


def print_sort_op_results(fnc: Callable, lst: Optional[List[int]]) -> None:
    if not lst:
        lst = [8, 1, 5, 3, 9, 12, 6, 7, 3, 9]

    print('Demonstrating {}...'.format(fnc.__name__))
    operations, operation_buckets = get_operations(fnc, lst)

    print('\n'.join(operations))
    print('\nNumber of operations:', len(operations))
    print('Operation counts:', operation_buckets)
    print('{}\nImplemented correctly? {}'.format(lst, sorted(lst) == lst))
