"""Run a simulation of the Monty Hall problem: https://en.m.wikipedia.org/wiki/Monty_Hall_problem """

from random import randint, Random
from typing import List, Tuple
from contextlib import suppress

NUM_DOORS = 3
ITERATION_COUNT = 10000


def generate_prize_doors(winning_index: int, num_doors: int = NUM_DOORS) -> List[bool]:
    """
    Returns a list of "doors."
    The car (desired outcome) is represented by True
    and the goats are represented by False.
    """
    doors = [False] * num_doors
    doors[winning_index] = True
    return doors


def choose_door(num_doors: int = NUM_DOORS) -> int:
    return randint(0, (num_doors - 1))


def host_door_reveal(winning_index: int, chosen_door_index: int, door_index_choices: List[int]) -> int:
    copy_choices = list(door_index_choices)
    copy_choices.remove(winning_index)
    with suppress(ValueError):
        copy_choices.remove(chosen_door_index)
    return Random().choice(copy_choices)


def monty_hall_switch() -> bool:
    """Returns True if you win from a switch."""

    # a car is randomly put behind 3 doors
    winning_index = choose_door()
    doors = generate_prize_doors(winning_index)
    door_indexes = list(range(len(doors)))
    print('doors: {}; winning index: {}; door indexes: {}'.format(doors, winning_index, door_indexes))

    # you choose a door randomly
    chosen_door_index = choose_door()
    print('chosen door: {}'.format(chosen_door_index))

    # given your choice and the host's knowledge of the winner,
    # the host returns an index of a False value
    goat_door_index = host_door_reveal(winning_index, chosen_door_index, door_indexes)
    print('revealed door: {}'.format(goat_door_index))

    # you switch to whatever wasn't the chosen and wasn't the goat door
    door_indexes.remove(chosen_door_index)
    door_indexes.remove(goat_door_index)
    new_index = door_indexes[0]
    return new_index == winning_index


def main(iterate_times: int = ITERATION_COUNT) -> None:
    win_count = 0
    for _ in range(iterate_times):
        win = monty_hall_switch()
        if win:
            win_count += 1
    
    print('win percent: {}%'.format(win_count / iterate_times))

if __name__ == '__main__':
    main()
