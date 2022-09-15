"""Demonstrates insertion sort."""

from typing import List

from sort_demo_helpers import print_sort_op_results, SortOperationType


def insertion_sort(lst: List[int]) -> List[str]:
    """Returns a list of operations taken during insertion sort."""
    operations = []

    for i in range(1, len(lst)):
        operations.append('\n' + SortOperationType.INIT.get_sort_operation_str(lst=lst, i=i))

        val = lst[i]
        j = i - 1

        while j >= 0 and val < lst[j]:
            operations.append('\t' + SortOperationType.COMPARE.get_sort_operation_str(lst=lst, min_idx=i, j=j))
            lst[j+1] = lst[j]
            operations.append(SortOperationType.SWITCH.get_sort_operation_str(lst=lst, i=j+1, min_idx=j))
            j -= 1
            operations.append(SortOperationType.STORE.get_sort_operation_str(lst=lst, j=j))

        operations.append('\t' + SortOperationType.COMPARE.get_sort_operation_str(lst=lst, min_idx=i, j=j))
        lst[j+1] = val

    return operations


def main():
    print_sort_op_results(insertion_sort, None)


if __name__ == '__main__':
    main()
