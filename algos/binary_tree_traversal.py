# Demonstrates different binary tree traversal strategies.

from typing import List


class InvalidTraversalTypeError(Exception):
	pass

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key
	
	def __str__(self) -> str:
		return f'Node<{self.val}>'


def get_traversed_list(root: Node, traversal_type: str) -> List[Node]:
	"""
	Traverses a binary tree. Valid traversal types:
	["inorder", "preorder", "postorder"].
	"""
	valid_traversal_types = ["inorder", "preorder", "postorder"]
	if traversal_type not in valid_traversal_types:
		raise InvalidTraversalTypeError(f'Used invalid traversal type {traversal_type}; should be in {valid_traversal_types}')

	node_list = []
	if not root:
		return node_list

	left_list = get_traversed_list(root.left, traversal_type)
	root_list = [root.val]
	right_list = get_traversed_list(root.right, traversal_type)

	if traversal_type == valid_traversal_types[0]:
		return left_list + root_list + right_list
	if traversal_type == valid_traversal_types[1]:
		return root_list + left_list + right_list
	return left_list + right_list + root_list


def main():
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	print('Preorder list:', [x for x in get_traversed_list(root, "preorder")])
	print('Inorder list:', [x for x in get_traversed_list(root, "inorder")])
	print('Postorder list:', [x for x in get_traversed_list(root, "postorder")])

	try:
		get_traversed_list(root, "fakeorder")
	except InvalidTraversalTypeError as exc:
		print('Exception:', exc)

if __name__ == '__main__':
	main()
