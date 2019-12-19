# This program was not written by me, but this shows the implementation of Arbitrage well.

'''
Problem:

Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage.
Arbitrage: whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.
There are no transaction costs and you can trade fractional quantities.

Example:
Input = [[1, 2], 
        [0.5, 1]]
Output = False
'''

from math import log

# FUNCTION TO PERFORM THE OPERATION
def arbitrage(table):
    transformed_graph = [[-log(edge) for edge in row] for row in table]

    # Pick any source vertex -- we can run Bellman-Ford from any vertex and
    # get the right result
    source = 0
    n = len(transformed_graph)
    min_dist = [float('inf')] * n

    min_dist[source] = 0

    # Relax edges |V - 1| times
    for _ in range(n - 1):
        for v in range(n):
            for w in range(n):
                if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                    min_dist[w] = min_dist[v] + transformed_graph[v][w]

    # If we can still relax edges, then we have a negative cycle
    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                return True

    return False

# DRIVER CODE
print(arbitrage([[1, 2], [0.5, 1]]))
print(arbitrage([[1, 3, 4],
                [2, 1, 3], 
                [5, 2, 1]]))