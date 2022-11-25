"""Demonstrates mergesort."""

from typing import List

from sort_demo_helpers import SortOperationType, print_sort_op_results


def merge_sort(lst: List[int], operations: List[str] = []) -> List[str]:
    operations.append(SortOperationType.INIT.get_sort_operation_str(lst=lst, sort='merge'))
    if len(lst) <= 1:
        return
    
    mid_index = len(lst) // 2
    left_lst = lst[:mid_index]
    right_lst = lst[mid_index:]

    operations.append(SortOperationType.COPY_LIST.get_sort_operation_str(left_lst))
    operations.append(SortOperationType.COPY_LIST.get_sort_operation_str(right_lst))
    
    merge_sort(left_lst)
    merge_sort(right_lst)

    lst_index = 0
    while left_lst or right_lst:
        left_value = None if not left_lst else left_lst[0]
        right_value = None if not right_lst else right_lst[0]
        operations.append(SortOperationType.COMPARE.get_sort_operation_str(lst, 'merge', lst_index, left_value, right_value))

        if not right_lst or (left_lst and left_value <= right_value):
            lst[lst_index] = left_lst.pop(0)
        else:
            lst[lst_index] = right_lst.pop(0)
        lst_index += 1

    return operations


def main() -> None: 
    print_sort_op_results(merge_sort, [5, 7, 3, 9, 5, 6, 1, 1, 2])


if __name__ == '__main__':
    main()
