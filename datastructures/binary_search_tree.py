# Demonstrates constructing a binary search tree with an unsorted list, inserting nodes, deleting nodes.
# Also demonstrates an AVL tree that inherits that functionality and adds automatic balancing.

from typing import List, Optional


class Node:
    """Represents a binary tree node."""
    def __init__(self, val: int = 0, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '{}<{}>'.format(type(self).__name__, self.val)
    
    def get_leftmost_node(self) -> 'Node':
        current = self
        while current.left is not None:
            current = current.left
        return current

    @property
    def height(self) -> int:
        return 1 + max(getattr(self.left, 'height', 0), getattr(self.right, 'height', 0))


class BinarySearchTree:
    def __init__(self, root: Optional[Node] = None):
        self.root = root

    def search(self, val: int) -> Optional[Node]:
        """
        Looks through tree to find a node with matching value.
        If no nodes match, returns None; else, returns Node.
        """
        return self._search(self.root, val)
    
    def get_inorder_nodes(self) -> List[Node]:
        """
        Returns a flat list of Nodes traversed inorder from root of tree.
        """
        return self._get_inorder_nodes(self.root)
    
    def insert(self, val: int) -> None:
        """Inserts a new Node with given val into tree."""
        self.root = self._insert(self.root, val)
    
    def delete(self, val: int) -> None:
        """Deletes a node with given val from tree."""
        self._delete(self.root, val)

    def print_tree(self, current_node: Optional[Node], indent: str = '', last: bool = True):
        if current_node is not None:
            print(indent, end='')
            if last:
                print("R----", end='')
                indent += "     "
            else:
                print("L----", end='')
                indent += "|    "
            print(current_node.val)
            self.print_tree(current_node.left, indent, False)
            self.print_tree(current_node.right, indent, True)

    def _search(self, root: Optional[Node], val: int) -> Optional[Node]:
        if root is None or root.val == val:
            return root
        if val < root.val:
            return self._search(root.left, val)
        return self._search(root.right, val)

    def _get_inorder_nodes(self, root: Optional[Node]) -> List[Node]:
        if not root:
            return []
        left = self._get_inorder_nodes(root.left)
        mid = [root]
        right = self._get_inorder_nodes(root.right)
        return left + mid + right
 
    def _insert(self, root: Optional[Node], val: int):
        if root is None:
            root = Node(val)
            return root

        if val < root.val:
            root.left = self._insert(root.left, val)
        elif val > root.val:
            root.right = self._insert(root.right, val)

        return root

    def _delete(self, root: Optional[Node], val: int) -> Optional[Node]:
        if root is None:
            return root

        if val < root.val:
            root.left = self._delete(root.left, val)
        elif val > root.val:
            root.right = self._delete(root.right, val)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            if root.right is None:
                temp = root.left
                root = None
                return temp

            temp = root.right.get_leftmost_node()
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)

        return root


class AVLTree(BinarySearchTree):
    """Same as BinarySearchTree except that the tree is automatically balanced after insertions and deletions."""

    def _insert(self, root: Optional[Node], val: int):
        result = super()._insert(root, val)
        if root:
            balance_node = self._balance_tree(root, val)
            if balance_node:
                return balance_node
        return result

    def _delete(self, root: Optional[Node], val: int) -> Optional[Node]:
        result = super()._delete(root, val)
        if result is not None and result == root:
            balance_node = self._balance_tree(root, val)
            if balance_node:
                return balance_node
        return result

    def _balance_tree(self, root: Optional[Node], val: int) -> Optional[Node]:
        balance_factor = self.get_balance(root)
        if balance_factor > 1:
            if val < root.left.val:
                return self._right_rotate(root)

            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        if balance_factor < -1:
            if val > root.right.val:
                return self._left_rotate(root)

            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

    def _left_rotate(self, current_root: Node):
        print('---Left rotating', current_root)
        new_root = current_root.right
        temp = new_root.left
        new_root.left = current_root
        current_root.right = temp
        return new_root

    def _right_rotate(self, current_root: Node):
        print('---Right rotating', current_root)
        new_root = current_root.left
        temp = new_root.right
        new_root.right = current_root
        current_root.left = temp
        return new_root

    def get_balance(self, root: Optional[Node]):
        if not root:
            return 0
        return getattr(root.left, 'height', 0) - getattr(root.right, 'height', 0)


def main() -> None:
    lst = [5, 4, 7, 2, 11]
    print('Building a binary search tree with this list:', lst)
    bst = BinarySearchTree()
    for i in lst:
        bst.insert(i)
    bst.print_tree(bst.root)

    print('Inorder nodes:', [str(x) for x in bst.get_inorder_nodes()])

    print('Looking for 4:', bst.search(4))
    print('Looking for 14:', bst.search(14))

    print('Deleting 2 (leaf)...')
    bst.delete(2)
    print([str(x) for x in bst.get_inorder_nodes()])
    bst.insert(2)
    print('Added back:', [str(x) for x in bst.get_inorder_nodes()])

    node11 = bst.search(11)
    print('Left child on node 11:', node11, node11.left, '(height: {})'.format(node11.height))
    print('Deleting 7 (one child)...')
    bst.delete(7)
    print([str(x) for x in bst.get_inorder_nodes()])
    bst.insert(7)
    print('Added back:', [str(x) for x in bst.get_inorder_nodes()])
    node11 = bst.search(11)
    print('Left child on node 11:', node11, node11.left, '(height: {})'.format(node11.height))

    print('Deleting 5 (root)...')
    bst.delete(5)
    print('Root:', bst.root)
    print([str(x) for x in bst.get_inorder_nodes()])

    bst.insert(5)
    bst.insert(10)
    bst.insert(12)
    bst.insert(3)
    bst.insert(13)
    bst.insert(14)
    bst.insert(15)

    bst.print_tree(bst.root)
    print()

    print('Now creating an AVL tree...')
    avl = AVLTree()
    for i in lst:
        avl.insert(i)
    avl.print_tree(avl.root)

    avl.delete(5)
    avl.insert(5)
    avl.insert(10)
    avl.insert(12)
    avl.insert(3)
    avl.insert(13)
    avl.print_tree(avl.root)
    print('Inserting 14, which should result in re-balance...')
    avl.insert(14)
    avl.print_tree(avl.root)
    print('Inserting 15, which should result in re-balance...')
    avl.insert(15)
    avl.print_tree(avl.root)
    print('Balance factor:', avl.get_balance(avl.root))


if __name__ == '__main__':
    main()


"""
$ python3 datastructures/binary_search_tree.py 
Building a binary search tree with this list: [5, 4, 7, 2, 11]
R----5
     L----4
     |    L----2
     R----7
          R----11
Inorder nodes: ['Node<2>', 'Node<4>', 'Node<5>', 'Node<7>', 'Node<11>']
Looking for 4: Node<4>
Looking for 14: None
Deleting 2 (leaf)...
['Node<4>', 'Node<5>', 'Node<7>', 'Node<11>']
Added back: ['Node<2>', 'Node<4>', 'Node<5>', 'Node<7>', 'Node<11>']
Left child on node 11: Node<11> None (height: 1)
Deleting 7 (one child)...
['Node<2>', 'Node<4>', 'Node<5>', 'Node<11>']
Added back: ['Node<2>', 'Node<4>', 'Node<5>', 'Node<7>', 'Node<11>']
Left child on node 11: Node<11> Node<7> (height: 2)
Deleting 5 (root)...
Root: Node<7>
['Node<2>', 'Node<4>', 'Node<7>', 'Node<11>']
R----7
     L----4
     |    L----2
     |    |    R----3
     |    R----5
     R----11
          L----10
          R----12
               R----13
                    R----14
                         R----15

Now creating an AVL tree...
R----5
     L----4
     |    L----2
     R----7
          R----11
R----7
     L----4
     |    L----2
     |    |    R----3
     |    R----5
     R----11
          L----10
          R----12
               R----13
Inserting 14, which should result in re-balance...
---Left rotating Node<12>
R----7
     L----4
     |    L----2
     |    |    R----3
     |    R----5
     R----11
          L----10
          R----13
               L----12
               R----14
Inserting 15, which should result in re-balance...
---Left rotating Node<11>
R----7
     L----4
     |    L----2
     |    |    R----3
     |    R----5
     R----13
          L----11
          |    L----10
          |    R----12
          R----14
               R----15
Balance factor: 0
"""
