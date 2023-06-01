import networkx as nx
import matplotlib.pyplot as plt
import pickle
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
        with open(filename, "wb") as file:
            pickle.dump(self.edges, file)

    @classmethod
    def load_graph_from_file(cls, filename):
        graph = cls()
        with open(filename, "rb") as file:
            graph.edges = pickle.load(file)
        return graph

    def visualize(self):
        G = nx.DiGraph()
        for start_edge, end_edges in self.edges.items():
            for end_edge in end_edges:
                G.add_edge(start_edge, end_edge)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, arrows=True)
        plt.show()

    def dfs(self, start_node):
        visited = set()
        self._dfs_recursive(start_node, visited)

    def _dfs_recursive(self, node, visited):
        visited.add(node)
        for neighbor in self.edges[node]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def visualize_dfs(self, start_vertex):
        visited = set()
        self._visualize_dfs_recursive(start_vertex, visited)

    def _visualize_dfs_recursive(self, node, visited):
        visited.add(node)
        print(node, end=" ")

        G = nx.DiGraph(self.edges)
        pos = nx.spring_layout(G)
        plt.clf()

        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
        nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color='red', node_size=500)
        nx.draw_networkx_nodes(G, pos, nodelist=list(visited), node_color='green', node_size=500)

        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrows=True)
        plt.pause(1)

        for neighbor in self.edges[node]:
            if neighbor not in visited:
                self._visualize_dfs_recursive(neighbor, visited)

        plt.pause(0.5)

    def __str__(self):
        return str(self.edges)


if __name__ == "__main__":
    my_graph = Graph()
    my_graph.create_random_graph(10, 20)

    # my_graph.add_node(1)
    # my_graph.add_node(2)
    # my_graph.add_node(3)
    #
    # my_graph.add_edge(1, 2)
    # my_graph.add_edge(2, 3)
    # my_graph.add_edge(3, 1)

    my_graph.save_graph_to_file("testgraph.pickle")
    my_graph.visualize()
    graph_from_file = Graph.load_graph_from_file("testgraph.pickle")
    # graph_from_file.visualize()
