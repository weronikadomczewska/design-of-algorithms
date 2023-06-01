from graph import *

graph = Graph()
nodes = range(1, 12)
edges = {
    1: [2, 7, 8],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [9, 12],
    9: [10, 11],
    10: [],
    11: [],
    12: []
}
for n in nodes:
    graph.add_node(n)

for node, neighbors in edges.items():
    for neighbor in neighbors:
        graph.add_edge(node, neighbor)

# graph.edges = edges
# graph.visualize()
graph.visualize_dfs(1)

