"""Demo of Dijkstra's algorithm: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm """

from typing import Any, Dict, List


def dijkstra_shortest_paths(graph: Dict[Any, List[Any]], start_node: Any, print_distances: bool = False) -> Dict[Any, int]:
    all_shortest_paths = {start_node: 0}
    current_node = start_node

    # I use dicts here just to give a slight speed boost in finding nodes in the set
    visited_nodes = {}
    unvisited_nodes = {start_node: None}

    while unvisited_nodes:
        for neighbor_node in graph[current_node]:

            # skip node if already marked as visited
            if neighbor_node in visited_nodes:
                if neighbor_node in unvisited_nodes:
                    del unvisited_nodes[neighbor_node]
                continue

            # mark as unvisited so that we can process all neighbors
            unvisited_nodes[neighbor_node] = None

            # set distance if smaller than one previously set
            distance = all_shortest_paths[current_node] + 1
            if print_distances:
                print("Distance to {}: {}".format(neighbor_node, distance))
            if neighbor_node not in all_shortest_paths or all_shortest_paths[neighbor_node] > distance:
                all_shortest_paths[neighbor_node] = distance
        
        # mark as visited once all neighbors examined
        visited_nodes[current_node] = None
        del unvisited_nodes[current_node]

        # if there are nodes that haven't examined distances of all neighbors, look at the next one
        if unvisited_nodes:
            current_node = list(unvisited_nodes.keys())[0]

    return all_shortest_paths


def main() -> None:
    graph = {
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : [],
    }

    print("Graph: {}; to calculate all shortest lengths from A".format(graph))

    shortest_lengths = dijkstra_shortest_paths(graph, 'A', print_distances=True)
    print(shortest_lengths)

    graph2 = {'nyc': [], 'la': ['pdx'], 'seattle': ['pdx'], 'pdx': ['seattle'], 'denver': ['nyc', 'la']}
    print("\nSecond graph:", graph2)
    for starting_node in graph2.keys():
        print("Shortest paths from {}: {}".format(starting_node, dijkstra_shortest_paths(graph2, starting_node)))


if __name__ == '__main__':
    main()

"""
$ python3 algos/dijkstra.py 
Graph: {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}; to calculate all shortest lengths from A
Distance to B: 1
Distance to C: 1
Distance to D: 2
Distance to E: 2
Distance to F: 2
Distance to F: 3
{'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 2}

Second graph: {'nyc': [], 'la': ['pdx'], 'seattle': ['pdx'], 'pdx': ['seattle'], 'denver': ['nyc', 'la']}
Shortest paths from nyc: {'nyc': 0}
Shortest paths from la: {'la': 0, 'pdx': 1, 'seattle': 2}
Shortest paths from seattle: {'seattle': 0, 'pdx': 1}
Shortest paths from pdx: {'pdx': 0, 'seattle': 1}
Shortest paths from denver: {'denver': 0, 'nyc': 1, 'la': 1, 'pdx': 2, 'seattle': 3}
"""
