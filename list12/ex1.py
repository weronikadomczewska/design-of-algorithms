import networkx as nx
import matplotlib.pyplot as plt
import json
import random

class Graph:
    def __init__(self):
        self.edges = {}

    def add_node(self, node):
        if node not in self.edges:
            self.edges[node] = []

    def add_edge(self, start_node, end_node):
        if start_node in self.edges and end_node in self.edges:
            self.edges[start_node].append(end_node)

    def get_neighbors(self, node):
        if node in self.edges:
            return self.edges[node]
        return []

    def create_random_graph(self, num_nodes, num_edges):
        for vertex in range(num_nodes):
            self.add_node(vertex)

        available_edges = [(v1, v2) for v1 in range(num_nodes) for v2 in range(v1 + 1, num_nodes)]
        random.shuffle(available_edges)
        edges_to_add = available_edges[:num_edges]

        for edge in edges_to_add:
            self.add_edge(edge[0], edge[1])


    def save_graph_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file)

    def load_graph_from_file(self, filename):
        restored_graph = {}
        with open(filename, "r") as file:
            graph_dict = json.load(file)
            # self.from_dict(graph_dict)
        keys = graph_dict.keys()
        for k in keys:
            restored_graph[int(k)] = graph_dict[k]
        self.from_dict(restored_graph)

    def visualize(self):
        G = nx.DiGraph()
        for start_edge, end_edges in self.edges.items():
            for end_edge in end_edges:
                G.add_edge(start_edge, end_edge)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, arrows=True)
        plt.show()

    # def dfs(self, start_node):
    #     visited = set()
    #     self._dfs_recursive(start_node, visited)
    #
    # def _dfs_recursive(self, node, visited):
    #     visited.add(node)
    #     for neighbor in self.edges[node]:
    #         if neighbor not in visited:
    #             self._dfs_recursive(neighbor, visited)

    def visualize_dfs(self, start_vertex, nodes_pos):
        visited = set()
        self._visualize_dfs_recursive(start_vertex, visited, nodes_pos)

    def _visualize_dfs_recursive(self, node, visited, nodes_pos):
        visited.add(node)
        print(node, end=" ")

        G = nx.DiGraph(self.edges)
        plt.clf()

        nx.draw(G, nodes_pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
        nx.draw_networkx_nodes(G, nodes_pos, node_color='lightblue', node_size=500)
        nx.draw_networkx_nodes(G, nodes_pos, nodelist=[node], node_color='red', node_size=500)
        nx.draw_networkx_nodes(G, nodes_pos, nodelist=list(visited), node_color='green', node_size=500)

        nx.draw_networkx_edges(G, nodes_pos, edgelist=G.edges(), arrows=True)
        plt.pause(1)

        for neighbor in self.edges[node]:
            if neighbor not in visited:
                self._visualize_dfs_recursive(neighbor, visited, nodes_pos)
        plt.pause(0.5)

    def __str__(self):
        return str(self.edges)

    def to_dict(self):
        return self.edges

    def from_dict(self, graph_dict):
        self.edges = graph_dict


if __name__ == "__main__":
    graph = Graph()
    nodes = range(1, 13)
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

    fixed_layout = {
        1: (0, 0),
        2: (-1, -1),
        3: (-1, 1),
        4: (-2, -2),
        5: (-2, 0),
        6: (-2, 2),
        7: (-1, -3),
        8: (-3, -1),
        9: (-3, -3),
        10: (-4, -2),
        11: (-4, -4),
        12: (-4, 0)
    }
    for n in nodes:
        graph.add_node(n)

    for node, neighbors in edges.items():
        for neighbor in neighbors:
            graph.add_edge(node, neighbor)

    graph.save_graph_to_file("testgraph.json")
    graph_from_file = Graph()
    graph_from_file.load_graph_from_file("testgraph.json")
    print(graph_from_file.edges)
    graph_from_file.visualize_dfs(1, fixed_layout)
