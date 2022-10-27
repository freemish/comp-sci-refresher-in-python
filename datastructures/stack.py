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

    def peek(self) -> Optional[Any]:
        return self._lst[-1] if self._lst else None

    def size(self) -> int:
        return len(self._lst)

    def is_empty(self) -> bool:
        return not bool(self._lst)

    def __str__(self) -> str:
        return 'Stack<{}>'.format(self._lst)


# from this problem: https://www.interviewcake.com/question/python/largest-stack
class MaxStack(Stack):
    def __init__(self, lst: Optional[List[Any]]):
        self._lst = lst or []
        self._max_stack = []

        for i in self._lst:
            self._handle_push_max_stack(i)

    def _handle_push_max_stack(self, item: Any) -> None:
        if not self._max_stack or item >= self._max_stack[-1]:
            self._max_stack.append(item)

    def _handle_pop_max_stack(self, item: Any) -> None:
        if item and item == self._max_stack[-1]:
            self._max_stack.pop()
            
    def push(self, item: Any) -> None:
        super().push(item)
        self._handle_push_max_stack(item)

    def pop(self) -> Optional[Any]:
        item = super().pop()
        self._handle_pop_max_stack(item)
        return item

    def get_max(self) -> Optional[Any]:
        return self._max_stack[-1] if self._max_stack else None

    def __str__(self) -> str:
        return "{} <{} - max {}>".format(type(self).__name__, self._lst, self.get_max())


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

    print()
    print("Starting demonstration of MaxStack")
    mstack = MaxStack([1, 2, 3])
    print(mstack)
    assert mstack.get_max() == 3
    mstack.push(2)
    assert mstack.get_max() == 3
    mstack.pop()
    mstack.pop()
    assert mstack.get_max() == 2
    print(mstack)
    mstack.pop()
    assert mstack.get_max() == 1
    print(mstack)
    load_list = [4, 3, 6, 9]
    for i, item in enumerate(load_list):
        mstack.push(item)
        assert mstack.get_max() == max(load_list[0:i+1])
    print(mstack)


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

Starting demonstration of MaxStack
MaxStack <[1, 2, 3] - max 3>
MaxStack <[1, 2] - max 2>
MaxStack <[1] - max 1>
MaxStack <[1, 4, 3, 6, 9] - max 9>
"""
