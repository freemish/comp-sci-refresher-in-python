"""
Demonstrate quicksort algorithm.
"""

from typing import List, Tuple

from sort_demo_helpers import print_sort_op_results, SortOperationType



def partition(lst: List[int], low: int = 0, high: int = -1) -> Tuple[int, List[str]]:
    """
    Returns a pivot index and a list of operations performed on list.
    """
    ops: List[str] = []
    pivot = lst[high]
    i = low

    ops.append("{}: Running partition on array: {}; low: {}; high: {}; pivot: {}; i: {}".format(
        SortOperationType.INIT.value, lst, low, high, pivot, i))
  
    for j in range(low, high):
        ops.append("{}: Comparing index {} (value {}) with pivot {}...".format(SortOperationType.COMPARE.value, j, lst[j], pivot))
        if lst[j] <= pivot:
  
            (lst[i], lst[j]) = (lst[j], lst[i])
            ops.append("{}: Swapping {} and {} to get {}".format(SortOperationType.SWITCH.value, lst[j], lst[i], lst))

            i += 1
            ops.append("{}: Incrementing i to {}".format(SortOperationType.STORE.value, i))

    (lst[i], lst[high]) = (lst[high], lst[i])
    ops.append("{}: Swapping {} and {} to get {}".format(SortOperationType.SWITCH.value, lst[high], lst[i], lst))

    return i, ops


def quick_sort(lst: List[int], low: int = 0, high: int = -1) -> List[str]:
    """
    Sorts list of ints in place with quicksort method.
    """
    if high == -1:
        high = len(lst) - 1
    
    if low >= high:
        return []

    pi, ops = partition(lst, low, high)

    low_ops = quick_sort(lst, low, pi-1)
    high_ops = quick_sort(lst, pi+1, high)
    return ops + low_ops + high_ops


def main() -> None:
    print_sort_op_results(quick_sort, None)


if __name__ == '__main__':
    main()
