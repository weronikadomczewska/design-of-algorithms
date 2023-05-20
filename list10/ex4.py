import random
import numpy as np

def generate_random_graph(V, q):
    # max number of edges
    max_edges = (V * (V - 1)) // 2

    # chosen number of edges
    num_edges = int(q * max_edges)

    # creating incidence matrix
    incidence_matrix = np.zeros((V, num_edges), dtype=int)
    edge_count = 0
    while edge_count < num_edges:
        # choosing random pair of nodes
        v1, v2 = random.sample(range(V), 2)
        if incidence_matrix[v1, edge_count] == 0 and incidence_matrix[v2, edge_count] == 0:
            incidence_matrix[v1, edge_count] = 1
            incidence_matrix[v2, edge_count] = 1
            edge_count += 1

    # creating adjacency matrix
    adjacency_matrix = np.zeros((V, V), dtype=int)
    for edge in range(num_edges):
        v1 = np.argmax(incidence_matrix[:, edge])
        v2 = np.argmax(incidence_matrix[:, edge][v1+1:]) + v1 + 1
        adjacency_matrix[v1, v2] = 1
        adjacency_matrix[v2, v1] = 1

    return incidence_matrix, adjacency_matrix


if __name__ == "__main__":
    V = int(input("Insert number of nodes: "))
    q = float(input("Insert q: "))

    incidence_matrix, adjacency_matrix = generate_random_graph(V, q)

    print("Incidence matrix:")
    print(incidence_matrix)
    print("Incidence matrix size:", incidence_matrix.size)

    print("Adjacency matrix:")
    print(adjacency_matrix)
    print("Adjacency matrix size:", adjacency_matrix.size)
