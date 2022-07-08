"""Messing around with linked lists."""

from typing import Any, Optional, List, Union


class LinkedListNode:
    def __init__(self, val: Any = None, next: Optional['LinkedListNode'] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        """Warning: recursive, assumes no circularity!"""
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
    
    def __str__(self) -> str:
        return 'DoublyLinkedListNode({}) <-> {}'.format(self.val, str(self.next))


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


def get_array_from_linked_list(
        linked_list_head: Optional[Union[LinkedListNode, DoublyLinkedListNode]],
        attr_name_next_node: str = 'next',
    ) -> List[Any]:
    """
    Accepts head of linked list and outputs values in a list.
    WARNING! Assumes linked list not circular.
    """
    lst = []
    if not linked_list_head:
        return lst
    lst.append(linked_list_head.val)
    while getattr(linked_list_head, attr_name_next_node):
        linked_list_head = getattr(linked_list_head, attr_name_next_node)
        lst.append(linked_list_head.val)
    return lst


def create_doubly_linked_list(lst: List[Any]) -> DoublyLinkedListNode:
    """Accepts a list and returns head of a doubly-linked list."""
    head = None
    last_node = None
    for i in range(len(lst)):
        node = DoublyLinkedListNode(val=lst[i])
        if i == 0:
            head = node
            last_node = node
        else:
            last_node.next = node
            node.last = last_node
            last_node = node
    return head


def get_last_node_in_linked_list(
        head: Union[LinkedListNode, DoublyLinkedListNode]
    ) -> Union[LinkedListNode, DoublyLinkedListNode]:
    """Assumes no circularity."""
    current_node = head
    while current_node.next:
        current_node = current_node.next
    return current_node


def main() -> None:
    print('Starting demo of linked lists...')
    orig_list = ['I', 'am', 'only', 1, 'girl', None]
    print('original list:', orig_list)
    linked_list_head = create_linked_list(orig_list)
    print('linked list:', linked_list_head)
    new_list = get_array_from_linked_list(linked_list_head)
    print('list from linked list:', new_list, '\nis equal?', orig_list == new_list)

    print('Make original list into doubly-linked list...')
    dlinked_list_head = create_doubly_linked_list(orig_list)
    print('doubly-linked list:', dlinked_list_head)
    new_list = get_array_from_linked_list(dlinked_list_head)
    print('list from linked list:', new_list, '\nis equal?', orig_list == new_list)
    last_node = get_last_node_in_linked_list(dlinked_list_head)
    backwards_dlinked_list = get_array_from_linked_list(last_node, attr_name_next_node='last')
    print('backwards list from linked list:', backwards_dlinked_list, '\nis equal to reversed orig list?', orig_list[::-1] == backwards_dlinked_list)



if __name__ == '__main__':
    main()

"""
$ python3 datastructures/linked_list.py
Starting demo of linked lists...
original list: ['I', 'am', 'only', 1, 'girl', None]
linked list: LinkedListNode(I) -> LinkedListNode(am) -> LinkedListNode(only) -> LinkedListNode(1) -> LinkedListNode(girl) -> LinkedListNode(None) -> None
list from linked list: ['I', 'am', 'only', 1, 'girl', None] 
is equal? True
Make original list into doubly-linked list...
doubly-linked list: DoublyLinkedListNode(I) <-> DoublyLinkedListNode(am) <-> DoublyLinkedListNode(only) <-> DoublyLinkedListNode(1) <-> DoublyLinkedListNode(girl) <-> DoublyLinkedListNode(None) <-> None
list from linked list: ['I', 'am', 'only', 1, 'girl', None] 
is equal? True
backwards list from linked list: [None, 'girl', 1, 'only', 'am', 'I'] 
is equal? True
"""
