"""Demo for recursive tower of hanoi solution."""


def tower_of_hanoi_recursive(n: int, from_rod: str, to_rod: str, aux_rod: str, print_label='from_to_aux'):
    if print_label:
        print("(Processing (label: {}): {} disks, from rod {}, to rod {}, aux rod {})".format(print_label, n, from_rod, to_rod, aux_rod))

    if n <= 0:
        if print_label:
            print("(Done - no disks to process)")
        return

    tower_of_hanoi_recursive(n-1, from_rod, aux_rod, to_rod, 'from_aux_to')
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    tower_of_hanoi_recursive(n-1, aux_rod, to_rod, from_rod, 'aux_to_from')

    if print_label:
        print("(Done processing (label: {}): {} disks, from rod {}, to rod {}, aux rod {})".format(print_label, n, from_rod, to_rod, aux_rod))


def main() -> None:
    tower_of_hanoi_recursive(4, 'a', 'b', 'c')


if __name__ == '__main__':
    main()


"""
$ python3 other/tower_of_hanoi.py 
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
"""
