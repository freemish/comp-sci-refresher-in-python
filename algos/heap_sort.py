"""Demonstrates heapsort."""

from heapq import heapify, heappop, heappush, heappushpop
from typing import List

from sort_demo_helpers import SortOperationType, print_sort_op_results

def heapsort(lst: List[int]) -> List[str]:
    """Returns a list of operations done during heapsort."""
    operations = []

    heap = list(lst)
    operations.append(SortOperationType.COPY_HEAP.get_sort_operation_str(lst))
    heapify(heap)
    for _ in lst:
        operations.append(SortOperationType.LOAD_HEAP.get_sort_operation_str(heap))

    for i in range(len(lst)):
        lst[i] = heappop(heap)
        operations.append(SortOperationType.POP_HEAP.get_sort_operation_str(
            lst=lst, index=i, value=lst[i], heap=heap))

    return operations

def main() -> None:
    print_sort_op_results(heapsort, [5, 8, 9, 2, 6, 1, 7, 2, 4])


if __name__ == '__main__':
    main()
