import networkx as nx
import matplotlib.pyplot as plt


def shortest_path(graph, start, end, path=[]):

    """
    Złożoność: O(V+E)
    """
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            new_path = shortest_path(graph, node, end, path)
            if new_path:
                if shortest is None or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest

g = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

graph = nx.Graph()
graph.add_nodes_from(g.keys())
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("E", "F")
graph.add_edge("C", "F")

print(shortest_path(graph, "F", "D"))

pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_color="pink")
plt.show()


