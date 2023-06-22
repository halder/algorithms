from collections import defaultdict

def dfs(graph, s=0):
    discovered = [s]

    if s in graph:
        for neighbor in graph[s][::-1]:
            if neighbor not in discovered:
                unseen = [d for d in dfs(graph, neighbor) if d not in discovered]
                discovered.extend(unseen)

    return discovered


def topological_sort(graph):
    all_nodes = list(set(list(graph.keys()) + [v for val in graph.values() for v in val]))
    order = []

    def dfs(graph, s=0):
        if s in order:
            return
        
        if s in graph:
            for neighbor in graph[s]:
                dfs(graph, s=neighbor)
        
        order.append(s)

    for node in all_nodes:
        if node not in order:
            dfs(graph, s=node)

    return order[::-1]


def kosaraju(graph):
    """
    Calculates strongly connected components of a DAG.
    """
    def transpose_graph(graph):
        T = defaultdict(list)
        
        for node, edges in graph.items():
            for edge in edges:
                T[edge].append(node)
            
        return T
    
    def dfs_ord(graph, s=0):
        explored_ord.append(s)

        if s in graph:
            for neighbor in graph[s]:
                if neighbor not in explored_ord:
                    dfs_ord(graph, s=neighbor)
        
        stack.append(s)

    def dfs_scc(graph, s=0):
        scc[leader].append(s)
        explored_scc.append(s)

        if s in graph:
            for neighbor in graph[s]:
                if neighbor not in explored_scc:
                    dfs_scc(graph, s=neighbor)

    stack = []
    explored_ord = []
    explored_scc = []
    scc = defaultdict(list)
    nodes = list(graph.keys())

    for node in nodes:
        if node not in explored_ord:
            dfs_ord(graph, s=node)
    
    graph_t = transpose_graph(graph)

    while stack:
        leader = stack.pop()
        if leader not in explored_scc:
            dfs_scc(graph_t, s=leader)

    return scc

# test
if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [3],
        2: [3]
    }

    graph_abc = {
        "s": ["v", "w"],
        "v": ["t"],
        "w": ["t"]
    }
    
    graph_ssc = {
        1: [2],
        2: [3, 4],
        3: [1, 10, 11],
        4: [5, 6],
        5: [6],
        6: [7],
        7: [5],
        8: [7, 9],
        9: [10],
        10: [11],
        11: [5, 8, 9]
    }
    
    print(dfs(graph))
    print(dfs(graph_abc, s="s"))
    print(topological_sort(graph))
    print(kosaraju(graph_ssc))