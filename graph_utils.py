import networkx as nx

def path2graph(path:list):
    solution_edges = [()] * (len(path) - 1)

    for i in range(len(path) - 1):
        solution_edges[i] = (path[i], path[i + 1])

    solution = nx.Graph()
    solution.add_nodes_from(path)
    solution.add_edges_from(solution_edges)
    return solution
