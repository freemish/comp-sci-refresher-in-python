"""Messing around with heaps."""

def calculate_parent_index(i: int) -> int:
    """Returns index of parent."""
    if i <= 0:
        return 0

    if i % 2:
        i += 1
    return i // 2 - 1


def calculate_parent_index_long_way(i: int) -> int:
    if i <= 0:
        return 0

    parent_index = 0
    nodes_on_parent_index = 0

    for ci in range(1, i+1):
        if nodes_on_parent_index >= 2:
            parent_index += 1
            nodes_on_parent_index = 1
        else:
            nodes_on_parent_index += 1
        
    return parent_index


def main():
    print('Demonstrating properties of heaps...')

    print('A common implementation of heaps is with an array. Index 0 is parent to 1, 2; Index 1 is parent to 3, 4; Index 2 is parent to 5, 6; etc.')
    print('Let\'s calculate what the parent index is given a child index.')

    i = 500
    shortcut_calc = calculate_parent_index(i)
    long_calc = calculate_parent_index_long_way(i)
    print(f'Index: {i}; Short calc: {shortcut_calc}; long calc: {long_calc}; equal? {shortcut_calc == long_calc}')


if __name__ == '__main__':
    main()
