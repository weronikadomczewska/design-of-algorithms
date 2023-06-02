from collections import defaultdict
import heapq
import networkx as nx
import matplotlib.pyplot as plt
import random

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

    graph.visualise_dijkstra(1, 10)



