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
            G[super].append(edge)
        
        # remove self loops
        super_edges = [node for node in G[super] if node not in (super, fuse)]
        G[super] = super_edges.copy()

        for node in G[super]:
            if node != fuse:
                edges = [super if edge == fuse else edge for edge in G[node].copy()]
                G[node] = edges.copy()

        del G[fuse]

    return G


def min_cut(graph, runs=None):
    """
    Returns the minimum cut (A, B) of a graph with probability 1/n,
    where n = number of nodes in the graph.

    Set `runs` manually for large graphs since T will grow large quickly.
    """
    runs = runs if runs else int(len(graph) ** 2 * ln(len(graph))) # T

    min_cut = None
    for _ in range(runs):
        cut = len(list(random_contraction(graph).values())[0])

        if min_cut is None or cut < min_cut:
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

    print(random_contraction(graph))
    print(min_cut(graph))