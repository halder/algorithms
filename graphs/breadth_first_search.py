import copy
from collections import defaultdict

def bfs(graph, s=0, shortest_path=False):
    """
    Breadth-first search.
    Returns either membership map (for shortest path distances)
    or layer map.
    """
    G = copy.deepcopy(graph)

    layers = defaultdict(list)
    membership = {s: 0}
    layers[0].append(s)
    
    queue = [s]
    while queue:
        node = queue.pop(0)
        layer = membership[node]

        for neighbor in G[node]:
            G[neighbor].remove(node)

            if neighbor not in layers[layer]:
                layers[layer + 1].append(neighbor)

                membership[neighbor] = layer + 1

            if neighbor not in queue:
                queue.append(neighbor)

    if shortest_path:
        return membership
    else:
        return {layer: set(members) for layer, members in layers.items()}


def shortest_path(graph, s=0, v=None):
    """
    Find shortest path on G from s to v using BFS.
    If v not specified compute distance to node explored last by BFS.
    """
    membership = bfs(graph, s=s, shortest_path=True)
    
    if not v:
        v = list(membership.keys())[-1]

    return membership[v] - membership[s]


def connected_components(graph):
    """
    Find connected components in an undirected graph using BFS.
    """
    components = defaultdict(list)
    explored_nodes = []
    cur_component = 0

    for node in graph:
        if node in explored_nodes:
            continue
        if node not in components[cur_component]:
            membership = bfs(graph, s=node, shortest_path=True)

            components[cur_component].extend(list(membership.keys()))
            explored_nodes.extend(list(membership.keys()))

            cur_component += 1

    return components

# test
if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3, 4],
        3: [1, 2, 4, 5],
        4: [2, 3, 5],
        5: [3, 4]
    }

    unconnected_graph = {
        1: [3, 5],
        2: [4],
        3: [1, 5],
        4: [2],
        5: [1, 3, 7, 9],
        6: [8, 10],
        7: [5],
        8: [6, 10],
        9: [5],
        10: [6, 8]
    }

    print(bfs(graph))
    print(shortest_path(graph))
    print(bfs(graph, s=1))
    print(shortest_path(graph, s=1, v=4))
    print(connected_components(unconnected_graph))