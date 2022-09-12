# Demonstrates different binary tree traversal strategies.

from enum import Enum
from typing import Any, List, Optional, Tuple


class TraversalType(Enum):
	PREORDER = 0
	INORDER = 1
	POSTORDER = 2


class InvalidTraversalTypeError(Exception):
	pass


class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

	def __str__(self) -> str:
		return f'Node<{self.val}>'


def build_bt_from_level_order(level_order_list: List[Any], i: int = 0) -> Optional[Node]:
	"""Assumes binary tree is "complete" (filled from left to right)"""
	root = None

	if i < len(level_order_list):
		root = Node(level_order_list[i])
		root.left = build_bt_from_level_order(level_order_list, 2 * i + 1)
		root.right = build_bt_from_level_order(level_order_list, 2 * i + 2)
		  
	return root


def get_traversed_list(root: Node, traversal_type: TraversalType) -> List[Any]:
	"""
	Traverses a binary tree. Valid traversal types: inorder, preorder, postorder.
	"""
	if traversal_type not in list(TraversalType):
		raise InvalidTraversalTypeError(
			'Used invalid traversal type {}; should be in list {}'.format(
				traversal_type,
				list(TraversalType.__members__.keys())
			)
		)

	node_list = []
	if not root:
		return node_list

	left_list = get_traversed_list(root.left, traversal_type)
	root_list = [root.val]
	right_list = get_traversed_list(root.right, traversal_type)

	if traversal_type == TraversalType.INORDER:
		return left_list + root_list + right_list
	if traversal_type == TraversalType.PREORDER:
		return root_list + left_list + right_list
	return left_list + right_list + root_list


def get_depth_and_capacity_of_left_loaded_binary_tree(items_count: int) -> Tuple[int, int]:
	depth = 0
	capacity_of_depth = 0
	while capacity_of_depth < items_count:
		capacity_of_depth += 2**depth
		depth += 1
	return depth, capacity_of_depth


def get_binary_tree_level_order_from_inorder(val_list: List[Any]) -> List[Any]:
	"""Assumes that tree is filled from left to right."""

	def get_last_row():
		last_row = []
		depth, max_capacity = get_depth_and_capacity_of_left_loaded_binary_tree(len(val_list))
		len_last_row = 2**(depth-1) if len(val_list) == max_capacity else len(val_list) - (2**(depth-1) - 1)
		if len_last_row < 1:
			return []

		for i in range(len_last_row):
			last_row.append(val_list[i])
			val_list.pop(i)

		return last_row

	depth, _ = get_depth_and_capacity_of_left_loaded_binary_tree(len(val_list))
	matrix = []
	if len(val_list):
		for _ in range(depth):
			last_row = get_last_row()
			matrix.append(last_row)

	matrix = matrix[::-1]
	loadorder_list = []
	for row in matrix:
		loadorder_list += row
	return loadorder_list


def main():
	root = build_bt_from_level_order([x+1 for x in range(10)])

	print('Preorder list:', [x for x in get_traversed_list(root, TraversalType.PREORDER)])
	print('Inorder list:', [x for x in get_traversed_list(root, TraversalType.INORDER)])
	print('Postorder list:', [x for x in get_traversed_list(root, TraversalType.POSTORDER)])

	level_order = get_binary_tree_level_order_from_inorder(get_traversed_list(root, TraversalType.INORDER))
	print("Level order:", level_order)
	recon_bt = build_bt_from_level_order(level_order)
	print('Preorder list from reconstructed bt:', [x for x in get_traversed_list(recon_bt, TraversalType.PREORDER)])


if __name__ == '__main__':
	main()
