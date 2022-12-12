"""Does some worst/best/avg case comparisons of sorting algos."""

from pprint import pprint
from statistics import mean

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from heap_sort import heapsort
from merge_sort import merge_sort
from quicksort import quick_sort
from sort_demo_helpers import get_operations, get_random_list


def main() -> None:
    print('About to run some operational count comparisons for sorting algos...')

    algos_to_outcomes = {}
    algos = [selection_sort, bubble_sort, insertion_sort, heapsort, merge_sort, quick_sort]

    labels_to_examples = {
        'best': [x+1 for x in range(10)],
        'worst': [x for x in range(10, 0, -1)],
        'random': get_random_list(min_len_list=10, max_len_list=10),
    }
    random_ex_to_average = [
        get_random_list(min_len_list=10, max_len_list=10)
        for _ in range(100)
    ]

    print('Examples:')
    pprint(labels_to_examples)

    for algo in algos:
        outcomes = {}
        for label, ex in labels_to_examples.items():
            ops, op_counter = get_operations(algo, list(ex))
            outcomes[label] = {
                'total_op_count': len(ops),
                'total_minus_index_store': len(ops) - op_counter.get('V', 0),
                'index_store_operations': op_counter.get('V', 0),
                'switch_operations': op_counter.get('W', 0),
            }
        random_outcomes_to_avg = []
        for avg_ex in random_ex_to_average:
            random_outcomes_to_avg.append(get_operations(algo, list(avg_ex)))

        outcomes['avg'] = {
            'total_op_count': mean(
                [len(x[0]) for x in random_outcomes_to_avg]
            ),
            'index_store_operations': mean(
                [x[1].get('V', 0) for x in random_outcomes_to_avg]
            ),
            'switch_operations': mean(
                [x[1].get('W', 0) for x in random_outcomes_to_avg]
            ),
        }
        outcomes['avg']['total_minus_index_store'] = (
            outcomes['avg']['total_op_count']
            - outcomes['avg']['index_store_operations']
        )
        algos_to_outcomes[algo.__name__] = outcomes

    print('Outcomes:')
    pprint(algos_to_outcomes)


if __name__ == '__main__':
    main()
