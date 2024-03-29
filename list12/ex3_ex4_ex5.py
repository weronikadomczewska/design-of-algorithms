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

    # def get_augmenting_path(self, parent, source, sink):
    #     path = []
    #     v = sink
    #     while v != source:
    #         path.append(v)
    #         v = parent[v]
    #     path.append(source)
    #     return path[::-1]

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

            if x != y:
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
        plt.pause(2.0)
        # plt.clf()

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

    def bfs(self, source, sink, parent):
        visited = set()
        queue = [(source, float("inf"))]
        visited.add(source)
        while queue:
            node, flow = queue.pop(0)
            for neighbor, capacity in self.get_neighbors(node):
                if neighbor not in visited and capacity > 0:
                    visited.add(neighbor)
                    parent[neighbor] = (node, capacity)
                    min_flow = min(flow, capacity)
                    if neighbor == sink:
                        return min_flow
                    queue.append((neighbor, min_flow))
        return 0

    def edmonds_karp(self, source, sink):
        parent = {}
        max_flow = 0
        while True:
            min_flow = self.bfs(source, sink, parent)
            if min_flow == 0:
                break
            max_flow += min_flow
            node = sink
            while node != source:
                prev_node, capacity = parent[node]
                for i, (v, w) in enumerate(self.graph[prev_node]):
                    if v == node:
                        self.graph[prev_node][i] = (v, w - min_flow)
                        break
                for i, (v, w) in enumerate(self.graph[node]):
                    if v == prev_node:
                        self.graph[node][i] = (v, w + min_flow)
                        break
                node = prev_node
            self.visualize_edmonds_karp(source, sink, parent)
        return max_flow

    def visualize_edmonds_karp(self, source, sink, parent):
        G = nx.DiGraph()
        G.add_weighted_edges_from([(u, v, weight) for u, neighbors in self.graph.items() for v, weight in neighbors])

        node_colors = ['lightgray' for _ in G.nodes()]
        edge_colors = ['gray' for _ in G.edges()]
        edge_labels = {(u, v): str(w) for u, neighbors in self.graph.items() for v, w in neighbors}

        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, with_labels=True, node_color=node_colors, font_size=8, edge_color=edge_colors)
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v in parent.values()], edge_color='red', width=2)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

        # Highlight the flow path
        path_edges = []
        node = sink
        while node != source:
            prev_node, _ = parent[node]
            path_edges.append((prev_node, node))
            node = prev_node
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='blue', width=2)

        plt.axis('off')
        plt.show()

    # def edmonds_karp(self, source, sink):
    #     parent = {}
    #     max_flow = 0
    #     while True:
    #         min_flow = self.bfs(source, sink, parent)
    #         if min_flow == 0:
    #             break
    #         max_flow += min_flow
    #         node = sink
    #         while node != source:
    #             prev_node, capacity = parent[node]
    #             for i, (v, w) in enumerate(self.graph[prev_node]):
    #                 if v == node:
    #                     self.graph[prev_node][i] = (v, w - min_flow)
    #                     break
    #             for i, (v, w) in enumerate(self.graph[node]):
    #                 if v == prev_node:
    #                     self.graph[node][i] = (v, w + min_flow)
    #                     break
    #             node = prev_node
    #         self.visualize_edmonds_karp_step(source, sink, parent)
    #     return max_flow
    #
    # def visualize_edmonds_karp_step(self, source, sink, parent):
    #     G = nx.Graph()
    #     G.add_weighted_edges_from([(u, v, weight) for u, neighbors in self.graph.items() for v, weight in neighbors])
    #
    #     node_colors = ['lightgray' for _ in G.nodes()]
    #     edge_colors = ['gray' for _ in G.edges()]
    #     edge_labels = {(u, v): str(w) for u, neighbors in self.graph.items() for v, w in neighbors}
    #
    #     # Build the augmenting path
    #     augmenting_path = []
    #     node = sink
    #     while node != source:
    #         prev_node, _ = parent[node]
    #         augmenting_path.append((prev_node, node))
    #         node = prev_node
    #
    #     pos = nx.spring_layout(G)
    #     nx.draw_networkx(G, pos, with_labels=True, node_color=node_colors, font_size=8, edge_color=edge_colors)
    #     nx.draw_networkx_edges(G, pos, edgelist=augmenting_path, edge_color='red', width=2)
    #     nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)
    #
    #     plt.axis('off')
    #     plt.show()


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

    # ex3
    # graph.visualise_dijkstra(1, 10)

    # ex4
    # mst = graph.kruskal()
    # for u, v, weight in mst:
    #     graph.visualize_kruskal_step(u, v)
    # graph.visualize_minimum_spanning_tree(mst)

    # ex5
    max_flow = graph.edmonds_karp(1, 7)
    print("max flow: ", max_flow)






