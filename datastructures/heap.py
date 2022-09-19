"""Messing around with heaps."""

import sys
#from heapq import heappush, heappop, heapify


class MinHeap:
    def __init__(self, max_size: int = 100):
        self.max_size = max_size
        self.size = 0
        self._heap = [0]*(self.max_size + 1)
        self._heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def get_parent_index(self, child_index: int) -> int:
        return (child_index) // 2

    def get_left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index

    def get_right_child_index(self, parent_index: int) -> int:
        return (2 * parent_index) + 1

    def is_leaf(self, index: int) -> bool:
        return index * 2 > self.size

    def swap(self, index1: int, index2: int) -> None:
        self._heap[index1], self._heap[index2] = self._heap[index2], self._heap[index1]

    def _min_heapify(self, index: int) -> None:
        if self.is_leaf(index):
            return
        
        left_child_index = self.get_left_child_index(index)
        right_child_index = self.get_right_child_index(index)

        if self._heap[index] > self._heap[left_child_index]:
            self.swap(index, left_child_index)
            self._min_heapify(left_child_index)

        elif self._heap[index] > self._heap[right_child_index]:
            self.swap(index, right_child_index)
            self._min_heapify(right_child_index)

    def insert(self, value: int):
        if self.size >= self.max_size :
            return

        self.size += 1
        self._heap[self.size] = value

        current = self.size
        while self._heap[current] < self._heap[self.get_parent_index(current)]:
            self.swap(current, self.get_parent_index(current))
            current = self.get_parent_index(current)

    def pop_min(self) -> int:
        popped = self._heap[self.FRONT]
        self._heap[self.FRONT] = self._heap[self.size]
        self._min_heapify(self.FRONT)
        self._heap[self.size] = 0
        self.size-= 1
        return popped

    def print_contents(self):
        for i in range(self.FRONT, (self.size//2)+1):
            right_child_index = self.get_right_child_index(i)
            print(
                'Parent: {}; Left child: {}; Right child: {}'.format(
                    self._heap[i],
                    self._heap[self.get_left_child_index(i)],
                    self._heap[right_child_index] if right_child_index <= self.size else "<No child>",
                )
            )


def main():
    print('Demonstrating properties of heaps...')

    min_heap = MinHeap(15)
    values_to_load = [5, 3, 17, 10, 84, 19, 6, 22, 9]

    print("Loading the following values into a min heap: {} ({} total values)".format(values_to_load, len(values_to_load)))
    for v in values_to_load:
        min_heap.insert(v)

    min_heap.print_contents()
    print("Underlying array (shh, don't tell anyone I accessed this for demo purposes):", min_heap._heap)
    print("Heap size:", min_heap.size)

    print("The min val (which was popped) is {}.".format(min_heap.pop_min()))
    print('New heap:')
    min_heap.print_contents()
    print("Underlying array (again, don't tell anyone I accessed this for demo purposes):", min_heap._heap)
    print("New heap size:", min_heap.size)

    min_heap.insert(1)
    min_heap.print_contents()
    min_heap.insert(199)
    min_heap.print_contents()


if __name__ == '__main__':
    main()


"""
$ python3 datastructures/heap.py
Demonstrating properties of heaps...
Loading the following values into a min heap: [5, 3, 17, 10, 84, 19, 6, 22, 9] (9 total values)
Parent: 3; Left child: 5; Right child: 6
Parent: 5; Left child: 9; Right child: 84
Parent: 6; Left child: 19; Right child: 17
Parent: 9; Left child: 22; Right child: 10
Underlying array (shh, don't tell anyone I accessed this for demo purposes): [-9223372036854775807, 3, 5, 6, 9, 84, 19, 17, 22, 10, 0, 0, 0, 0, 0, 0]
Heap size: 9
The min val (which was popped) is 3.
New heap:
Parent: 5; Left child: 9; Right child: 6
Parent: 9; Left child: 10; Right child: 84
Parent: 6; Left child: 19; Right child: 17
Parent: 10; Left child: 22; Right child: <No child>
Underlying array (again, don't tell anyone I accessed this for demo purposes): [-9223372036854775807, 5, 9, 6, 10, 84, 19, 17, 22, 0, 0, 0, 0, 0, 0, 0]
New heap size: 8
"""
