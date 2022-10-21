"""Messing around with linked lists."""

from typing import Any, Optional, List, Union


class LinkedListNode:
    def __init__(self, val: Any = None, next: Optional['LinkedListNode'] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        """Warning: recursive, assumes no circularity!"""
        return 'LinkedListNode({}) -> {}'.format(self.val, str(self.next))

    def is_circular(self) -> bool:
        """If is circular, returns True."""
        visited = []
        node = self
        while node is not None:
            if node in visited:
                return True

            visited.append(node)
            node = node.next
            
        return False


class DoublyLinkedListNode(LinkedListNode):
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


def create_linked_list(
    lst: List[Any],
    doubly_linked: bool = False,
) -> Optional[Union[LinkedListNode, DoublyLinkedListNode]]:
    """Accepts an array of values and outputs head of singly linked list."""
    head = None
    last_node = None
    node_class = DoublyLinkedListNode if doubly_linked else LinkedListNode
    for i in range(len(lst)):
        node = node_class(val=lst[i])
        if i == 0:
            head = node
            last_node = node
        else:
            last_node.next = node
            if doubly_linked:
                node.last = last_node
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
    print('list from linked list:', new_list)
    print('is equal?', orig_list == new_list)

    print('Make original list into doubly-linked list...')
    dlinked_list_head = create_linked_list(orig_list, doubly_linked=True)
    print('doubly-linked list:', dlinked_list_head)
    new_list = get_array_from_linked_list(dlinked_list_head)
    print('list from linked list:', new_list)
    print('is equal?', orig_list == new_list)

    backwards_dlinked_list = get_array_from_linked_list(
        get_last_node_in_linked_list(dlinked_list_head),
        attr_name_next_node='last',
    )
    print('backwards list from doubly-linked list:', backwards_dlinked_list)
    print('is equal to reversed orig list?', orig_list[::-1] == backwards_dlinked_list)

    print()
    print("Is the original linked list circular?", linked_list_head.is_circular())
    print("Is the doubly-linked list circular?", dlinked_list_head.is_circular())
    print("Now creating circular singly and doubly linked lists (linked head to tail)...")
    single_head = create_linked_list(orig_list)
    single_tail = get_last_node_in_linked_list(single_head)
    single_tail.next = single_head

    double_head = create_linked_list(orig_list, doubly_linked=True)
    double_tail = get_last_node_in_linked_list(double_head)
    double_head.last = double_tail
    double_tail.next = double_head

    print("singly-linked:", single_head.is_circular())
    print("(from tail)", single_tail.is_circular())
    print("doubly-linked:", double_head.is_circular())
    print("(from tail):", single_tail.is_circular())


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
backwards list from doubly-linked list: [None, 'girl', 1, 'only', 'am', 'I']
is equal to reversed orig list? True

Is the original linked list circular? False
Is the doubly-linked list circular? False
Now creating circular singly and doubly linked lists (linked head to tail)...
singly-linked: True
(from tail) True
doubly-linked: True
(from tail): True
"""
