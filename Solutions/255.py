"""
Problem:

The transitive closure of a graph is a measure of which vertices are reachable from other vertices. It can be represented as a matrix M, where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.

For example, suppose we are given the following graph in adjacency list form:

graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
The transitive closure of this graph would be:

[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
Given a graph, find its transitive closure.
"""


def get_transitive_helper(origin, curr_node, graph, transitive_matrix, visited):
    # helper function to generate the transitive matrix using dfs
    for node in graph[curr_node]:
        transitive_matrix[origin][node] = 1
        if node not in visited:
            visited.add(node)
            get_transitive_helper(origin, node, graph, transitive_matrix, visited)


def get_transitive(graph):
    num_nodes = len(graph)
    # creating and updating the transitive matrix
    transitive_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    for node in range(num_nodes):
        get_transitive_helper(node, node, graph, transitive_matrix, set([node]))
    return transitive_matrix


# DRIVER CODE
graph = [[0, 1, 3], [1, 2], [2], [3]]

for row in get_transitive(graph):
    print(*row)
