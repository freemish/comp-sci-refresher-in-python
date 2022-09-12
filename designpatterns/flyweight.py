# Demonstrates flyweight design pattern.

from typing import Any, Dict, List, Optional


class TreeType:
    def __init__(self, name: str, color: str, texture: str):
        self.name = name
        self.color = color
        self.texture = texture

    @classmethod
    def generate_key(cls, name: str, color: str, texture: str) -> str:
        return '{}__{}__{}'.format(name, color, texture)

    def get_unique_key(self) -> str:
        return self.generate_key(self.name, self.color, self.texture)
    
    def draw(self, x: int, y: int) -> None:
        print(f'TreeType {self.name} drawn at x {x}, y {y}.')


class Tree:
    def __init__(self, tree_type: TreeType, x: int, y: int):
        self.tree_type = tree_type
        self.x = x
        self.y = y

    def draw(self) -> None:
        return self.tree_type.draw(self.x, self.y)


class TreeFactory:
    _tree_type_flyweights: Dict[str, TreeType] = {}

    def __init__(self, initial_flyweights_kwargs: Optional[List[Dict[str, Any]]] = None):
        if initial_flyweights_kwargs is None:
            initial_flyweights_kwargs = []
        
        flyweights = [self.get_tree_type(**init_kwargs) for init_kwargs in initial_flyweights_kwargs]
        self._tree_type_flyweights = {flyweight.get_unique_key(): flyweight for flyweight in flyweights}

    def list_generated_tree_types(self) -> List[str]:
        return list(self._tree_type_flyweights.keys())

    def get_tree_type(self, name: str, color: str, texture: str) -> TreeType:
        tree_type = self._tree_type_flyweights.get(TreeType.generate_key(name, color, texture))
        if tree_type:
            return tree_type

        tree_type = TreeType(name, color, texture)
        self._tree_type_flyweights[tree_type.get_unique_key()] = tree_type
        print('Created and cached new tree type:', tree_type.get_unique_key())
        return tree_type

    def create_tree(self, name: str, color: str, texture: str, x: int, y: int) -> Tree:
        tree_type = self.get_tree_type(name, color, texture)
        return Tree(tree_type, x, y)


def main() -> None:
    print("Demonstrating flyweight pattern...")

    print('Initializing 5 different tree types:')
    tree_factory = TreeFactory(
        [
            {'name': 'Cypress', 'color': 'beige-green', 'texture': 'softcypress.jpg'},
            {'name': 'Willow', 'color': 'sad-green', 'texture': 'wispywillow.jpg'},
            {'name': 'Gingko', 'color': 'yellow-green', 'texture': 'shinyginkgo.jpg'},
            {'name': 'Yew', 'color': 'warm-green', 'texture': 'yewknow.jpg'},
            {'name': 'Oak', 'color': 'dark-green', 'texture': 'crispyoak.jpg'},
        ],
    )
    print('All flyweights:', tree_factory.list_generated_tree_types())
    print('Initializing 1000 trees for a forest...')
    trees = []
    for x in range(100):
        for y in range(9):
            trees.append(tree_factory.create_tree('Imaginary', 'red', 'fairydust.jpg', x, y))
    for x in range(10):
        for y in range(10):
            trees.append(tree_factory.create_tree('Cypress', 'beige-green', 'softcypress.jpg', x, y))

    print('All flyweights:', tree_factory.list_generated_tree_types())
    print('Length of trees list:', len(trees))

if __name__ == '__main__':
    main()
