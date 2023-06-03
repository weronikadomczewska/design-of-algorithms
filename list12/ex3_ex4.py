from collections import defaultdict
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class WeightedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def get_neighbors(self, node):
        return self.graph[node]

    def get_all_nodes(self):
        return list(self.graph.keys())

    def dijkstra(self, start):
        distances = {node: float("inf") for node in self.graph}
        distances[start] = 0
        visited = set()
        pq = [(0, start)]
        parent = {}
        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            for neighbor, weight in self.get_neighbors(curr_node):
                distance = curr_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parent[neighbor] = curr_node
                    heapq.heappush(pq, (distance, neighbor))
        return distances, parent

    def visualise_dijkstra(self, start, end):
        distances, parent = self.dijkstra(start)
        G = nx.DiGraph()
        G.add_weighted_edges_from([(u, v, weight) for u, neighbors in self.graph.items() for v, weight in neighbors])

        shortest_path = []
        node = end
        while node != start:
            shortest_path.insert(0, node)
            node = parent[node]
        shortest_path.insert(0, start)

        node_colors = ['lightblue' if n in shortest_path else 'lightgray' for n in G.nodes()]
        # node_sizes = [800 if n in shortest_path else 300 for n in G.nodes()]
        node_sizes = 800
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes, font_size=8)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'), font_size=6)

        path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

        plt.axis('off')
        plt.show()

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        minimum_spanning_tree = []
        parent = {}
        rank = {}

        for node in self.get_all_nodes():
            parent[node] = node
            rank[node] = 0

        edges = []

        for u, neighbors in self.graph.items():
            for v, weight in neighbors:
                edges.append((u, v, weight))

        edges.sort(key=lambda x: x[2])

        for u, v, weight in edges:
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x!= y:
                minimum_spanning_tree.append((u, v, weight))
                self.union(parent, rank, x, y)
                self.visualize_kruskal_step(u, v)

        return minimum_spanning_tree

    def visualize_kruskal_step(self, u, v):
        G = nx.Graph()
        G.add_weighted_edges_from([(u, v, weight) for u, neighbors in self.graph.items() for v, weight in neighbors])

        node_colors = ['lightgray' for _ in G.nodes()]
        edge_colors = ['gray' for _ in G.edges()]

        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, with_labels=True, node_color=node_colors, font_size=8, edge_color=edge_colors)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], edge_color='red', width=2)

        plt.axis('off')
        plt.pause(0.75)
        plt.clf()

    def visualize_minimum_spanning_tree(self, minimum_spanning_tree):
        G = nx.Graph()
        G.add_weighted_edges_from([(u, v, weight) for u, neighbors in self.graph.items() for v, weight in neighbors])

        node_colors = ['lightgray' for _ in G.nodes()]
        edge_colors = ['gray' for _ in G.edges()]

        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, with_labels=True, node_color=node_colors, font_size=8, edge_color=edge_colors)
        nx.draw_networkx_edges(G, pos, edgelist=minimum_spanning_tree, edge_color='red', width=2)

        plt.axis('off')
        plt.show()


if __name__ == "__main__":
    graph = WeightedGraph()
    nodes = [x for x in range(1, 13)]
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

    number_of_edges = 0
    for node in nodes:
        number_of_edges += len(edges[node])
    weights = [x for x in range(1, number_of_edges+1)]

    i = 0
    for node, neighbors in edges.items():
        for neighbor in neighbors:
            graph.add_edge(node, neighbor, weights[i])
            i += 1

    # graph.visualise_dijkstra(1, 10)
    mst = graph.kruskal()

    for u, v, weight in mst:
        graph.visualize_kruskal_step(u, v)
    graph.visualize_minimum_spanning_tree(mst)




