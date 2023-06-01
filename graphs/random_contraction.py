import copy
import random
from math import log as ln

def random_contraction(graph):
    """
    Contract a graph until only two nodes remain.
    Edges to contract on are chosen uniformly at random.

    Roughly O(n^2 * m) time complexity.
    """
    G = copy.deepcopy(graph)

    while len(G) > 2:
        # randomly choose node to start from, this will be the new super node
        super = random.choice(list(G.keys()))
        # randomly choose edge from starting node (in terms of target node)
        fuse = random.choice(G[super])
    
        # delete edge between 'super' and 'fuse'
        G[super].remove(fuse)
        G[fuse].remove(super)

        # absorb 'fuse' into super
        for edge in G[fuse]:
            if edge != super:
                G[super].append(edge)

        for node, edges in G.items():
            if node != fuse:
                # update old 'fuse' edge to new 'super' edge
                if fuse in edges:
                    edges = [super if edge == fuse else edge for edge in edges]
                    G[node] = edges.copy()

            # remove self loops
            if node in edges:
                G[node].remove(node)

        del G[fuse]

    return G


def min_cut(graph):
    """
    Returns the minimum cut (A, B) of a graph with probability 1/n,
    where n = number of nodes in the graph.
    """
    T = len(graph) ** 2 * ln(len(graph))

    min_cut = None
    for _ in range(int(T)):
        cut = len(list(random_contraction(graph).values())[0])

        if cut < min_cut or min_cut is None:
            min_cut = cut

    return min_cut

# test
if __name__ == "__main__":
    graph = {
        0: [1, 3],
        1: [0, 2, 3],
        2: [1, 3],
        3: [0, 1, 2]
    }

    print(min_cut(graph))