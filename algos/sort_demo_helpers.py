"""Functions to help with sort demos."""

from collections import Counter
from enum import Enum
from random import randint
from typing import Any, Callable, List, Optional, Tuple


class SortOperationType(Enum):
    INIT = 'I'
    COMPARE = 'C'
    SWITCH = 'W'
    STORE = 'V'

    def get_sort_operation_str(self, lst: List[Any], sort: Optional[str] = None, *args, **kwargs) -> str:
        return '{}: {}'.format(self.value, self.get_string_method(sort)(lst, *args, **kwargs))

    def get_string_method(self, sort: Optional[str] = None) -> Callable:
        enum_to_method = {
            self.INIT: self.operation_init_desc if not sort else self.operation_init_bubble_desc,
            self.COMPARE: self.operation_compare_desc if not sort else self.operation_compare_bubble_desc,
            self.STORE: self.operation_store_desc,
            self.SWITCH: self.operation_switch_desc,
        }
        return enum_to_method.get(self)

    @classmethod
    def operation_init_desc(cls, lst: List[Any], i: int) -> str:
        return 'List: {}; processing index {} out of {} (value {})...'.format(lst, i, len(lst) - 1, lst[i])

    @classmethod
    def operation_init_bubble_desc(cls, lst: List[Any], i: int, indexes_to_iterate: int) -> str:
        return 'List: {}; Starting iteration {}/{} (from index 0 to {})...'.format(lst, i+1, len(lst)-1, indexes_to_iterate)

    @classmethod
    def operation_compare_desc(cls, lst: List[Any], min_idx: int, j: int) -> str:
        return 'Comparing index {} (value {}) to index {} (value {})...'.format(min_idx, lst[min_idx], j, lst[j])
    
    @classmethod
    def operation_compare_bubble_desc(cls, lst: List[Any], j: int) -> str:
        return 'Comparing index {} (value {}) to neighbor index {} (value {})...'.format(j, lst[j], j+1, lst[j+1])

    @classmethod
    def operation_switch_desc(cls, lst: List[Any], i: int, min_idx: int) -> str:
        return 'Switching indexes {} and {} (values {} and {})...'.format(i, min_idx, lst[i], lst[min_idx])

    @classmethod
    def operation_store_desc(cls, lst: List[Any], j: int) -> str:
        return 'Setting index {} (value {}) as new min index...'.format(j, lst[j])


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
