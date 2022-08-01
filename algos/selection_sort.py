"""Demonstrates selection sort."""

from typing import List, Optional

from sort_demo_helpers import print_sort_op_results


def selection_sort(lst: List[int]) -> List[str]:
    """Returns a list of operations."""
    operations = []
    for i in range(len(lst)-1):
        init_op ='\n\tI: List: {}; processing index {} out of {} (value {})...'.format(lst, i, len(lst) - 1, lst[i])
        operations.append(init_op)
      
        # find minimum element in lst[i+1:]
        min_idx = i
        for j in range(i+1, len(lst)):
            comp_op = '\t\tC: Comparing index {} (value {}) to index {} (value {})...'.format(min_idx, lst[min_idx], j, lst[j])
            operations.append(comp_op)
            if lst[min_idx] > lst[j]:
                min_idx = j
                store_op = '\tV: Setting index {} (value {}) as new min index...'.format(j, lst[j])
                operations.append(store_op)
              
        # swap minimum element with i (could be i itself)
        switch_op = '\tW: Switching indexes {} and {} (values {} and {})...'.format(i, min_idx, lst[i], lst[min_idx])
        operations.append(switch_op)  
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    return operations


def main(some_random_list: Optional[List[int]] = None):
    print_sort_op_results(selection_sort, some_random_list)


if __name__ == '__main__':
    main()

"""
$ python3 algos/selection_sort.py
Demonstrating selection_sort...

        I: List: [8, 1, 5, 3, 9, 12, 6, 7, 3, 9]; processing index 0 out of 9 (value 8)...
                C: Comparing index 0 (value 8) to index 1 (value 1)...
        V: Setting index 1 (value 1) as new min index...
                C: Comparing index 1 (value 1) to index 2 (value 5)...
                C: Comparing index 1 (value 1) to index 3 (value 3)...
                C: Comparing index 1 (value 1) to index 4 (value 9)...
                C: Comparing index 1 (value 1) to index 5 (value 12)...
                C: Comparing index 1 (value 1) to index 6 (value 6)...
                C: Comparing index 1 (value 1) to index 7 (value 7)...
                C: Comparing index 1 (value 1) to index 8 (value 3)...
                C: Comparing index 1 (value 1) to index 9 (value 9)...
        W: Switching indexes 0 and 1 (values 8 and 1)...

        I: List: [1, 8, 5, 3, 9, 12, 6, 7, 3, 9]; processing index 1 out of 9 (value 8)...
                C: Comparing index 1 (value 8) to index 2 (value 5)...
        V: Setting index 2 (value 5) as new min index...
                C: Comparing index 2 (value 5) to index 3 (value 3)...
        V: Setting index 3 (value 3) as new min index...
                C: Comparing index 3 (value 3) to index 4 (value 9)...
                C: Comparing index 3 (value 3) to index 5 (value 12)...
                C: Comparing index 3 (value 3) to index 6 (value 6)...
                C: Comparing index 3 (value 3) to index 7 (value 7)...
                C: Comparing index 3 (value 3) to index 8 (value 3)...
                C: Comparing index 3 (value 3) to index 9 (value 9)...
        W: Switching indexes 1 and 3 (values 8 and 3)...

        I: List: [1, 3, 5, 8, 9, 12, 6, 7, 3, 9]; processing index 2 out of 9 (value 5)...
                C: Comparing index 2 (value 5) to index 3 (value 8)...
                C: Comparing index 2 (value 5) to index 4 (value 9)...
                C: Comparing index 2 (value 5) to index 5 (value 12)...
                C: Comparing index 2 (value 5) to index 6 (value 6)...
                C: Comparing index 2 (value 5) to index 7 (value 7)...
                C: Comparing index 2 (value 5) to index 8 (value 3)...
        V: Setting index 8 (value 3) as new min index...
                C: Comparing index 8 (value 3) to index 9 (value 9)...
        W: Switching indexes 2 and 8 (values 5 and 3)...

        I: List: [1, 3, 3, 8, 9, 12, 6, 7, 5, 9]; processing index 3 out of 9 (value 8)...
                C: Comparing index 3 (value 8) to index 4 (value 9)...
                C: Comparing index 3 (value 8) to index 5 (value 12)...
                C: Comparing index 3 (value 8) to index 6 (value 6)...
        V: Setting index 6 (value 6) as new min index...
                C: Comparing index 6 (value 6) to index 7 (value 7)...
                C: Comparing index 6 (value 6) to index 8 (value 5)...
        V: Setting index 8 (value 5) as new min index...
                C: Comparing index 8 (value 5) to index 9 (value 9)...
        W: Switching indexes 3 and 8 (values 8 and 5)...

        I: List: [1, 3, 3, 5, 9, 12, 6, 7, 8, 9]; processing index 4 out of 9 (value 9)...
                C: Comparing index 4 (value 9) to index 5 (value 12)...
                C: Comparing index 4 (value 9) to index 6 (value 6)...
        V: Setting index 6 (value 6) as new min index...
                C: Comparing index 6 (value 6) to index 7 (value 7)...
                C: Comparing index 6 (value 6) to index 8 (value 8)...
                C: Comparing index 6 (value 6) to index 9 (value 9)...
        W: Switching indexes 4 and 6 (values 9 and 6)...

        I: List: [1, 3, 3, 5, 6, 12, 9, 7, 8, 9]; processing index 5 out of 9 (value 12)...
                C: Comparing index 5 (value 12) to index 6 (value 9)...
        V: Setting index 6 (value 9) as new min index...
                C: Comparing index 6 (value 9) to index 7 (value 7)...
        V: Setting index 7 (value 7) as new min index...
                C: Comparing index 7 (value 7) to index 8 (value 8)...
                C: Comparing index 7 (value 7) to index 9 (value 9)...
        W: Switching indexes 5 and 7 (values 12 and 7)...

        I: List: [1, 3, 3, 5, 6, 7, 9, 12, 8, 9]; processing index 6 out of 9 (value 9)...
                C: Comparing index 6 (value 9) to index 7 (value 12)...
                C: Comparing index 6 (value 9) to index 8 (value 8)...
        V: Setting index 8 (value 8) as new min index...
                C: Comparing index 8 (value 8) to index 9 (value 9)...
        W: Switching indexes 6 and 8 (values 9 and 8)...

        I: List: [1, 3, 3, 5, 6, 7, 8, 12, 9, 9]; processing index 7 out of 9 (value 12)...
                C: Comparing index 7 (value 12) to index 8 (value 9)...
        V: Setting index 8 (value 9) as new min index...
                C: Comparing index 8 (value 9) to index 9 (value 9)...
        W: Switching indexes 7 and 8 (values 12 and 9)...

        I: List: [1, 3, 3, 5, 6, 7, 8, 9, 12, 9]; processing index 8 out of 9 (value 12)...
                C: Comparing index 8 (value 12) to index 9 (value 9)...
        V: Setting index 9 (value 9) as new min index...
        W: Switching indexes 8 and 9 (values 12 and 9)...

Number of operations: 75
Operation counts: Counter({'C': 45, 'V': 12, 'I': 9, 'W': 9})
[1, 3, 3, 5, 6, 7, 8, 9, 9, 12]
Implemented correctly? True
"""