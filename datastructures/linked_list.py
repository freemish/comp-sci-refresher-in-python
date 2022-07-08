"""Messing around with linked lists."""

from typing import Any, Optional, List


class LinkedListNode:
    def __init__(self, val: Any = None, next: Optional['LinkedListNode'] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return 'LinkedListNode({}) -> {}'.format(self.val, str(self.next))


class DoublyLinkedListNode:
    def __init__(
        self,
        val: Any = None,
        last: Optional['DoublyLinkedListNode'] = None,
        next: Optional['DoublyLinkedListNode'] = None,
    ):
        self.val = val
        self.last = last
        self.next = next


class GraphNode:
    def __init__(self, val: Any = None, connection_nodes: Optional[List['GraphNode']] = None):
        self.val = val
        self.next_nodes = connection_nodes or []


def create_linked_list(lst: List[Any]) -> Optional[LinkedListNode]:
    """Accepts an array of values and outputs head of singly linked list."""
    head = None
    last_node = None
    for i in range(len(lst)):
        node = LinkedListNode(val=lst[i])
        if i == 0:
            head = node
            last_node = node
        else:
            last_node.next = node
            last_node = node
    return head


def get_array_from_linked_list(linked_list_head: Optional[LinkedListNode]) -> List[Any]:
    """Accepts head of singly linked list and outputs values in a list. TODO: detect if circular."""
    lst = []
    if not linked_list_head:
        return lst
    lst.append(linked_list_head.val)
    while linked_list_head.next:
        linked_list_head = linked_list_head.next
        lst.append(linked_list_head.val)
    return lst


def main() -> None:
    print('Starting demo of linked lists...')
    orig_list = ['I', 'am', 'only', 1, 'girl', None]
    print('original list:', orig_list)
    linked_list_head = create_linked_list(orig_list)
    print('linked list:', linked_list_head)
    new_list = get_array_from_linked_list(linked_list_head)
    print('list from linked list:', new_list, '\nis equal?', orig_list == new_list)


if __name__ == '__main__':
    main()

"""
$ python3 datastructures/linked_list.py
Starting demo of linked lists...
original list: ['I', 'am', 'only', 1, 'girl', None]
linked list: LinkedListNode(I) -> LinkedListNode(am) -> LinkedListNode(only) -> LinkedListNode(1) -> LinkedListNode(girl) -> LinkedListNode(None) -> None
list from linked list: ['I', 'am', 'only', 1, 'girl', None] 
is equal? True
"""
