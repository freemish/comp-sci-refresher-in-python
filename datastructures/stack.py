"""Demonstration of stack data structure."""

from typing import Any, List, Optional


class Stack:
    def __init__(self, lst: Optional[List[Any]] = None):
        self._lst = lst or []

    def push(self, item: Any) -> None:
        self._lst.append(item)

    def pop(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self._lst.pop()

    def size(self) -> int:
        return len(self._lst)

    def is_empty(self) -> bool:
        return not bool(self._lst)

    def __str__(self) -> str:
        return 'Stack<{}>'.format(self._lst)


def main():
    print('Starting demonstration of stack...')
    stack = Stack()

    print('Initialized empty stack:', stack)
    print('What happens if I pop from an empty stack?', stack.pop())
    print('Is empty?', stack.is_empty(), 'Size?', stack.size())

    print('Now pushing a few items...')
    stack.push(1)
    stack.push('day')
    stack.push(Stack([1, 2, 3]))

    print('Now stack looks like:', stack)
    print('Pop:', stack.pop())
    print('Stack:', stack)


if __name__ == '__main__':
    main()

"""
$ python3 datastructures/stack.py
Starting demonstration of stack...
Initialized empty stack: Stack<[]>
What happens if I pop from an empty stack? None
Is empty? True Size? 0
Now pushing a few items...
Now stack looks like: Stack<[1, 'day', <__main__.Stack object at 0x7f5996ed2160>]>
Pop: Stack<[1, 2, 3]>
Stack: Stack<[1, 'day']>
"""
