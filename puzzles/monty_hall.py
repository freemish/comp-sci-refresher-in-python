"""Run a simulation of the Monty Hall problem: https://en.m.wikipedia.org/wiki/Monty_Hall_problem """

import time
from random import randint
from typing import List

NUM_DOORS = 3
HOST_REVEAL_COUNT = 1
ITERATION_COUNT = 10000


def generate_prize_doors(winning_index: int, num_doors: int = NUM_DOORS) -> List[str]:
    """
    Returns a list of "doors" where there are all goats and one car placed randomly in the list.
    """
    doors = ['goat'] * num_doors
    doors[winning_index] = 'car'
    return doors


def choose_door(num_doors: int = NUM_DOORS) -> int:
    return randint(0, (num_doors - 1))


def host_door_reveal(winning_index: int, chosen_door_index: int, door_index_choices: List[int]) -> int:
    choices = list(set(door_index_choices).difference(set([winning_index, chosen_door_index])))
    return choices[randint(0, len(choices) - 1)]


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
    goat_door_indexes = []
    for _ in range(HOST_REVEAL_COUNT):
        goat_door_indexes.append(host_door_reveal(winning_index, chosen_door_index, door_indexes))
    print('revealed doors: {}'.format(goat_door_indexes))

    # you switch to whatever wasn't the chosen and wasn't the goat door
    new_index = list(set(door_indexes).difference(goat_door_indexes + [chosen_door_index]))[0]
    print('final door: {}'.format(new_index))
    return new_index == winning_index


def main(iterate_times: int = ITERATION_COUNT) -> None:
    start_time = time.time()
    win_count = 0
    for _ in range(iterate_times):
        win = monty_hall_switch()
        if win:
            win_count += 1
    end_time = time.time()
    
    print('win count: {}/{}'.format(win_count, iterate_times))
    print('win ratio: {}'.format(win_count / iterate_times))
    print('time elapsed (s): {}'.format(end_time - start_time))


if __name__ == '__main__':
    main()
