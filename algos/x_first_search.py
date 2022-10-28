"""Demo of breadth-first search and depth-first search."""

from typing import Any, Dict, List


class NodeScroller:
    @staticmethod
    def simplified_breadth_first_search(
            simplified_graph_or_tree: Dict[Any, List[Any]],
            starting_node: Any,
        ) -> List[Any]:
        """Accepts a graph or tree in simplified dict form and returns a list of nodes in breadth-first order."""
        visited = [starting_node]
        queue = [starting_node]

        while queue:
            dequeued_node = queue.pop(0)
            for neighbor in simplified_graph_or_tree[dequeued_node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

        return visited

    @staticmethod
    def simplified_depth_first_search(
            simplified_graph_or_tree: Dict[Any, List[Any]],
            starting_node: Any,
            visited: List[Any] = [],
        ) -> List[Any]:
        """Accepts a graph or tree in simplified dict form and returns a list of nodes in depth-first order."""
        visited.append(starting_node)
        for neighbor in simplified_graph_or_tree[starting_node]:
            if neighbor not in visited:
                NodeScroller.simplified_depth_first_search(simplified_graph_or_tree, neighbor)
        return visited


def main() -> None:
    graph = {
        'A' : ['B','C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : [],
    }

    print("Graph: {}; Starting at A".format(graph))

    visited_breadth = NodeScroller.simplified_breadth_first_search(graph, 'A')
    assert visited_breadth == [x for x in 'ABCDEF']
    visited_depth = NodeScroller.simplified_depth_first_search(graph, 'A')
    assert visited_depth == [x for x in 'ABDEFC']

    print("breadth-first: {}\ndepth-first: {}".format(visited_breadth, visited_depth))


if __name__ == '__main__':
    main()


"""
$ python3 algos/x_first_search.py 
Graph: {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}; Starting at A
breadth-first: ['A', 'B', 'C', 'D', 'E', 'F']
depth-first: ['A', 'B', 'D', 'E', 'F', 'C']
"""
