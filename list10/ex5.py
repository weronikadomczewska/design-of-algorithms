from ex4 import generate_random_graph


class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


def get_connected_components(adjacency_matrix):
    V = adjacency_matrix.shape[0]
    ds = DisjointSet(V)

    for v in range(V):
        for neighbor in range(V):
            if adjacency_matrix[v, neighbor] == 1:
                ds.union(v, neighbor)

    components = {}
    for v in range(V):
        root = ds.find(v)
        if root in components:
            components[root].append(v)
        else:
            components[root] = [v]

    return components


if __name__ == "__main__":
    V = int(input("Enter number of nodes: "))
    q = float(input("Enter q: "))

    _, adjacency_matrix = generate_random_graph(V, q)
    print("Incidence matrix: ")
    print(_)
    connected_components = get_connected_components(adjacency_matrix)
    print(connected_components)
