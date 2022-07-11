"""Demonstrates the queue data structure."""

from typing import Any, List, Optional


class Queue:
    def __init__(self, lst: Optional[List[Any]] = None):
        self._lst = lst or []
    
    def enqueue(self, item: Any) -> None:
        self._lst.append(item)
    
    def dequeue(self) -> Optional[Any]:
        if not self._lst:
            return None
        return self._lst.pop(0)
    
    def is_empty(self) -> bool:
        return not bool(self._lst)

    def size(self) -> int:
        return len(self._lst)

    def __str__(self) -> str:
        return 'Queue<{}>'.format(self._lst)


def main():
    print('Starting demo of queue...')
    
    queue = Queue()
    print('Initialized empty queue:', queue)
    print('What do we get from a dequeue operation?', queue.dequeue())
    print('Is it empty?', queue.is_empty())
    print('Size?', queue.size())

    print('Now let\'s add a few items.')
    queue.enqueue(1)
    queue.enqueue('day')
    queue.enqueue(Queue([1, 2, 3]))

    print('Now the queue looks like this:', queue)
    print('Dequeue operation output:', queue.dequeue())
    print('Now queue looks like:', queue)
    print('Size?', queue.size())
    print('Is it empty?', queue.is_empty())


if __name__ == '__main__':
    main()

"""
$ python3 datastructures/queue.py
Starting demo of queue...
Initialized empty queue: Queue<[]>
What do we get from a dequeue operation? None
Is it empty? True
Size? 0
Now let's add a few items.
Now the queue looks like this: Queue<[1, 'day', <__main__.Queue object at 0x7fdbde6e2128>]>
Dequeue operation output: 1
Now queue looks like: Queue<['day', <__main__.Queue object at 0x7fdbde6e2128>]>
Size? 2
Is it empty? False
"""
