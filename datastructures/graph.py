"""Demo for directed graphs."""

from typing import Any, Dict, List, Optional


class Graph:
    def __init__(self, nodes: Optional[List['GraphNode']] = None):
        self._nodes: Dict[Any, 'GraphNode'] = {}
        self.directed_vertices: Dict['GraphNode', List['GraphNode']] = {}
        for n in nodes:
            self.add_node(n)

    def get_node_by_value(self, value: Any) -> 'GraphNode':
        return self._nodes.get(value)

    def add_node(self, node: 'GraphNode') -> None:
        node.add_to_graph(self)
        self._nodes[node.val] = node
        self.directed_vertices[node] = node.connections

    def has_cycle(self) -> bool:
        visited = {x: False for x in self.directed_vertices.keys()}
        recursion_stack = {x: False for x in self.directed_vertices.keys()}
        for node in self.directed_vertices.keys():
            if not visited[node]:
                if self._has_cycle_helper(node, visited, recursion_stack):
                    return True
        return False

    def _has_cycle_helper(self, node: 'GraphNode', visited: Dict['GraphNode', bool], rec_stack: Dict['GraphNode', bool]) -> bool:
        visited[node] = True
        rec_stack[node] = True

        print("visiting {}".format(node))

        for connection in self.directed_vertices[node]:
            if visited[connection] and rec_stack[connection]:
                print("cycle found on {}".format(connection))
                return True

            if not visited[connection]:
                print("visiting {} through helper".format(connection))
                if self._has_cycle_helper(connection, visited, rec_stack):
                    return True

        rec_stack[node] = False
        return False


class GraphNode:
    def __init__(self, value: Any, connections: Optional[List['GraphNode']] = None):
        self.val = value
        self.connections = connections or []
        self._graph = None

    def __str__(self) -> str:
        return "{} <{}>".format(type(self).__name__, self.val)

    def add_to_graph(self, graph: Graph) -> None:
        self._graph = graph

    def add_connection(self, new_connection: 'GraphNode', link_back: bool = False):
        self.connections.append(new_connection)
        if link_back:
            new_connection.add_connection(self)
        if self._graph:
            self._graph.add_node(self)


def main() -> None:
    graph_nodes_map = {
        "nyc": GraphNode("nyc"),
        "la": GraphNode("la"),
        "seattle": GraphNode("seattle"),
        "pdx": GraphNode("pdx"),
        "denver": GraphNode("denver"),
    }

    graph_nodes_map["denver"].add_connection(graph_nodes_map["nyc"])
    graph_nodes_map["denver"].add_connection(graph_nodes_map["la"])
    graph_nodes_map["la"].add_connection(graph_nodes_map["pdx"])
    graph_nodes_map["pdx"].add_connection(graph_nodes_map["seattle"])

    graph = Graph(list(graph_nodes_map.values()))
    print("Does graph have cycle?", graph.has_cycle())

    graph_nodes_map["seattle"].add_connection(graph_nodes_map["pdx"])
    print("Does graph have cycle?", graph.has_cycle())


if __name__ == "__main__":
    main()


"""
$ python3 datastructures/graph.py
visiting GraphNode <nyc>
visiting GraphNode <la>
visiting GraphNode <pdx> through helper
visiting GraphNode <pdx>
visiting GraphNode <seattle> through helper
visiting GraphNode <seattle>
visiting GraphNode <denver>
Does graph have cycle? False
visiting GraphNode <nyc>
visiting GraphNode <la>
visiting GraphNode <pdx> through helper
visiting GraphNode <pdx>
visiting GraphNode <seattle> through helper
visiting GraphNode <seattle>
cycle found on GraphNode <pdx>
Does graph have cycle? True
"""