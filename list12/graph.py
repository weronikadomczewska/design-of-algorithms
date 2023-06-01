import networkx as nx
import matplotlib.pyplot as plt
import pickle

class Graph:
    def __init__(self):
        self.edges = {}

    def add_node(self, node):
        if node not in self.edges:
            self.edges[node] = []

    def add_edge(self, start_node, end_node):
        if start_node in self.edges and end_node in self.edges:
            self.edges[start_node].append(end_node)

    def get_neighbours(self, node):
        if node in self.edges:
            return self.edges[node]
        return []

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
                print(start_edge, end_edge)
                G.add_edge(start_edge, end_edge)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, arrows=True)
        plt.show()

    def __str__(self):
        return str(self.edges)


if __name__ == "__main__":
    my_graph = Graph()

    my_graph.add_node('A')
    my_graph.add_node('B')
    my_graph.add_node('C')

    my_graph.add_edge('A', 'B')
    my_graph.add_edge('B', 'C')
    my_graph.add_edge('C', 'A')

    my_graph.save_graph_to_file("testgraph.pickle")
    my_graph.visualize()
    graph_from_file = Graph.load_graph_from_file("testgraph.pickle")
    graph_from_file.visualize()
