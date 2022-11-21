"""Demo for recursive tower of hanoi solution."""

from collections import namedtuple
from typing import Dict, List


Instruction = namedtuple("Instruction", ["disk_num", "from_rod", "to_rod"])


def tower_of_hanoi(number_of_disks: int, from_rod: str, to_rod: str, aux_rod: str, print_debug=True) -> List[Instruction]:
    args = [number_of_disks, from_rod, to_rod, aux_rod]
    if not print_debug:
        args.append(None)
    return tower_of_hanoi_recursive(*args)


def tower_of_hanoi_recursive(n: int, from_rod: str, to_rod: str, aux_rod: str, print_label='from_to_aux') -> List[Instruction]:
    if print_label:
        print("(Processing (label: {}): {} disks, from rod {}, to rod {}, aux rod {})".format(print_label, n, from_rod, to_rod, aux_rod))

    if n <= 0:
        if print_label:
            print("(Done - no disks to process)")
        return []

    instr_list_1 = tower_of_hanoi_recursive(n-1, from_rod, aux_rod, to_rod, 'from_aux_to' if print_label else None)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    instr_list_2 = [Instruction(n, from_rod, to_rod)]
    instr_list_3 = tower_of_hanoi_recursive(n-1, aux_rod, to_rod, from_rod, 'aux_to_from' if print_label else None)

    if print_label:
        print("(Done processing (label: {}): {} disks, from rod {}, to rod {}, aux rod {})".format(print_label, n, from_rod, to_rod, aux_rod))

    return instr_list_1 + instr_list_2 + instr_list_3


def main() -> None:
    num_disks = 4
    stacks = {'a': [x for x in range(num_disks, 0, -1)], 'c': [], 'b': [],}
    print("Stacks: initial setup:", stacks)
    
    print()
    instructions = tower_of_hanoi(num_disks, *stacks.keys())
    
    print()
    for i in instructions:
        print(i)

    print()

    def follow_instruction(stacks: Dict[str, List[int]], instruction: Instruction) -> None:
        disk = stacks[instruction.from_rod].pop()
        assert disk == instruction.disk_num
        stacks[instruction.to_rod].append(disk)
    
    for i in instructions:
        follow_instruction(stacks, i)

    print("Stacks: final setup after instructions followed:", stacks)


if __name__ == '__main__':
    main()


"""
$ python3 other/tower_of_hanoi_recursion.py
Stacks: initial setup: {'a': [4, 3, 2, 1], 'b': [], 'c': []}

(Processing (label: from_to_aux): 4 disks, from rod a, to rod b, aux rod c)
(Processing (label: from_aux_to): 3 disks, from rod a, to rod c, aux rod b)
(Processing (label: from_aux_to): 2 disks, from rod a, to rod b, aux rod c)
(Processing (label: from_aux_to): 1 disks, from rod a, to rod c, aux rod b)
(Processing (label: from_aux_to): 0 disks, from rod a, to rod b, aux rod c)
(Done - no disks to process)
Move disk 1 from rod a to rod c
(Processing (label: aux_to_from): 0 disks, from rod b, to rod c, aux rod a)
(Done - no disks to process)
(Done processing (label: from_aux_to): 1 disks, from rod a, to rod c, aux rod b)
Move disk 2 from rod a to rod b
(Processing (label: aux_to_from): 1 disks, from rod c, to rod b, aux rod a)
(Processing (label: from_aux_to): 0 disks, from rod c, to rod a, aux rod b)
(Done - no disks to process)
Move disk 1 from rod c to rod b
(Processing (label: aux_to_from): 0 disks, from rod a, to rod b, aux rod c)
(Done - no disks to process)
(Done processing (label: aux_to_from): 1 disks, from rod c, to rod b, aux rod a)
(Done processing (label: from_aux_to): 2 disks, from rod a, to rod b, aux rod c)
Move disk 3 from rod a to rod c
(Processing (label: aux_to_from): 2 disks, from rod b, to rod c, aux rod a)
(Processing (label: from_aux_to): 1 disks, from rod b, to rod a, aux rod c)
(Processing (label: from_aux_to): 0 disks, from rod b, to rod c, aux rod a)
(Done - no disks to process)
Move disk 1 from rod b to rod a
(Processing (label: aux_to_from): 0 disks, from rod c, to rod a, aux rod b)
(Done - no disks to process)
(Done processing (label: from_aux_to): 1 disks, from rod b, to rod a, aux rod c)
Move disk 2 from rod b to rod c
(Processing (label: aux_to_from): 1 disks, from rod a, to rod c, aux rod b)
(Processing (label: from_aux_to): 0 disks, from rod a, to rod b, aux rod c)
(Done - no disks to process)
Move disk 1 from rod a to rod c
(Processing (label: aux_to_from): 0 disks, from rod b, to rod c, aux rod a)
(Done - no disks to process)
(Done processing (label: aux_to_from): 1 disks, from rod a, to rod c, aux rod b)
(Done processing (label: aux_to_from): 2 disks, from rod b, to rod c, aux rod a)
(Done processing (label: from_aux_to): 3 disks, from rod a, to rod c, aux rod b)
Move disk 4 from rod a to rod b
(Processing (label: aux_to_from): 3 disks, from rod c, to rod b, aux rod a)
(Processing (label: from_aux_to): 2 disks, from rod c, to rod a, aux rod b)
(Processing (label: from_aux_to): 1 disks, from rod c, to rod b, aux rod a)
(Processing (label: from_aux_to): 0 disks, from rod c, to rod a, aux rod b)
(Done - no disks to process)
Move disk 1 from rod c to rod b
(Processing (label: aux_to_from): 0 disks, from rod a, to rod b, aux rod c)
(Done - no disks to process)
(Done processing (label: from_aux_to): 1 disks, from rod c, to rod b, aux rod a)
Move disk 2 from rod c to rod a
(Processing (label: aux_to_from): 1 disks, from rod b, to rod a, aux rod c)
(Processing (label: from_aux_to): 0 disks, from rod b, to rod c, aux rod a)
(Done - no disks to process)
Move disk 1 from rod b to rod a
(Processing (label: aux_to_from): 0 disks, from rod c, to rod a, aux rod b)
(Done - no disks to process)
(Done processing (label: aux_to_from): 1 disks, from rod b, to rod a, aux rod c)
(Done processing (label: from_aux_to): 2 disks, from rod c, to rod a, aux rod b)
Move disk 3 from rod c to rod b
(Processing (label: aux_to_from): 2 disks, from rod a, to rod b, aux rod c)
(Processing (label: from_aux_to): 1 disks, from rod a, to rod c, aux rod b)
(Processing (label: from_aux_to): 0 disks, from rod a, to rod b, aux rod c)
(Done - no disks to process)
Move disk 1 from rod a to rod c
(Processing (label: aux_to_from): 0 disks, from rod b, to rod c, aux rod a)
(Done - no disks to process)
(Done processing (label: from_aux_to): 1 disks, from rod a, to rod c, aux rod b)
Move disk 2 from rod a to rod b
(Processing (label: aux_to_from): 1 disks, from rod c, to rod b, aux rod a)
(Processing (label: from_aux_to): 0 disks, from rod c, to rod a, aux rod b)
(Done - no disks to process)
Move disk 1 from rod c to rod b
(Processing (label: aux_to_from): 0 disks, from rod a, to rod b, aux rod c)
(Done - no disks to process)
(Done processing (label: aux_to_from): 1 disks, from rod c, to rod b, aux rod a)
(Done processing (label: aux_to_from): 2 disks, from rod a, to rod b, aux rod c)
(Done processing (label: aux_to_from): 3 disks, from rod c, to rod b, aux rod a)
(Done processing (label: from_to_aux): 4 disks, from rod a, to rod b, aux rod c)

Instruction(disk_num=1, from_rod='a', to_rod='c')
Instruction(disk_num=2, from_rod='a', to_rod='b')
Instruction(disk_num=1, from_rod='c', to_rod='b')
Instruction(disk_num=3, from_rod='a', to_rod='c')
Instruction(disk_num=1, from_rod='b', to_rod='a')
Instruction(disk_num=2, from_rod='b', to_rod='c')
Instruction(disk_num=1, from_rod='a', to_rod='c')
Instruction(disk_num=4, from_rod='a', to_rod='b')
Instruction(disk_num=1, from_rod='c', to_rod='b')
Instruction(disk_num=2, from_rod='c', to_rod='a')
Instruction(disk_num=1, from_rod='b', to_rod='a')
Instruction(disk_num=3, from_rod='c', to_rod='b')
Instruction(disk_num=1, from_rod='a', to_rod='c')
Instruction(disk_num=2, from_rod='a', to_rod='b')
Instruction(disk_num=1, from_rod='c', to_rod='b')

Stacks: final setup after instructions followed: {'a': [], 'b': [4, 3, 2, 1], 'c': []}
"""
