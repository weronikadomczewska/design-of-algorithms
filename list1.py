import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from math import sin, cos, radians

3.1
# creating a graph and adding edges with given weights
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)

# choosing 'prettier' graph visualisation- with as few as possible crossing edges and edges with similar length
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
plt.show()

# 3.2
# creating graph
G = nx.Graph()
# graph nodes
VV = [1, 2, 3, 4, 5]
# graph edges
WW = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (3, 5)]
# nodes' coords
Vx = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
Vy = {1: 0, 2: 1, 3: 0, 4: -1, 5: 0}

g = nx.Graph()
gpos = {}
# dictionary; keys: graph vertices, keys: list of coords for each vertex
for v in VV:
    g.add_node(v)
    gpos[v] = [Vx[v], Vy[v]]

# counting distance between every vertex with one other
for v1 in VV:
    for v2 in VV:
        if (v1, v2) in WW:
            label = str(np.sqrt((Vx[v1] - Vx[v2])**2 + (Vy[v1] - Vy[v2])**2))
            g.add_weighted_edges_from([(v1, v2, label)])

# drawing graph; vertices have given coords and
nx.draw(g, gpos, with_labels=True, node_color='yellow')
# pobranie wybranej właściwości grafu - tutaj jest to lista wag krawędzi
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, gpos, edge_labels=labels)
plt.show()

# 3.3 - with circular_layout
# number_of_vertices = int(input("Enter number of vertices: "))
# number_of_vertices = 5
# vertices = [x for x in range(1, number_of_vertices + 1)]
# edges = []
# x = 1
# y = 2
# for i in range(number_of_vertices):
#     if i == number_of_vertices - 1:
#         y = 1
#     edges.append((x, y))
#     x += 1
#     y += 1
#
# graph = nx.Graph()
# for edge in edges:
#     graph.add_edge(str(edge[0]), str(edge[1]))
#
# pos = nx.circular_layout(graph)
# nx.draw_networkx_nodes(graph, pos, node_size=500, node_color="pink")
# nx.draw_networkx_labels(graph, pos)
# nx.draw_networkx_edges(graph, pos)
# plt.show()

# 3.3 - with polar coordinates
radius = 3
number_of_vertices = int(input("Enter number of vertices: "))
vertices = [v for v in range(1, number_of_vertices+1)]
angle = 360 // number_of_vertices

graph = nx.Graph()
all_angles = [radians(a) for a in range(0, 360, angle)]
print(all_angles)
xs = [radius * cos(a) for a in all_angles]
ys = [radius * sin(a) for a in all_angles]

positions = {}
cnt = 0
for v in vertices:
    positions[v] = [xs[cnt], ys[cnt]]
    graph.add_node(v)
    cnt += 1

print(positions)

edges = []
for i in range(1, number_of_vertices + 1):
    for j in range(1, number_of_vertices + 1):
        if i != j:
            edges.append([i, j])
# print(edges)

for edge in edges:
    graph.add_edge(edge[0], edge[1])

nx.draw(graph, positions, with_labels=True, node_color='pink')
plt.show()

# 3.4
number_of_vertices = int(input("Enter number of vertices: "))
vertices = [v for v in range(1, number_of_vertices+1)]
low = -10
high = 10
xs = np.random.uniform(low, high, number_of_vertices)
ys = np.random.uniform(low, high, number_of_vertices)

positions = {}
idx = 0
for vertex in vertices:
    positions[vertex] = [xs[idx], ys[idx]]
    idx += 1

print(positions)

graph1 = nx.Graph()
for v in vertices:
    graph1.add_node(v)

number_of_edges = (number_of_vertices * (number_of_vertices - 1)) // 2
edges = [(random.choice(vertices), random.choice(vertices)) for n in range(number_of_vertices)]
print(edges)
for edge in edges:
    graph1.add_edge(edge[0], edge[1])
nx.draw(graph1, positions, with_labels=True, node_color='pink')
plt.show()

# 3.5
number_of_vertices = int(input("Enter number of vertices: "))
vertices = [v for v in range(1, number_of_vertices+1)]
radius = 0.1
low = 0
high = 1

# initial node
coords = np.random.uniform(low, high, 2)
positions = {1: [coords[0], coords[1]]}
circles_intersect = False
tries = 0

for vertex in vertices:
    tries = 0
    while vertex not in positions:
        coords = np.random.uniform(low, high, 2)
        circles_intersect = False
        x = coords[0]
        y = coords[1]
        for vertex_to_check in vertices:
            if vertex_to_check in positions:
                print(f"vertices to compare and try number: {vertex, vertex_to_check, tries}")
                x_to_check = positions[vertex_to_check][0]
                y_to_check = positions[vertex_to_check][1]
                centers_distance = ((x_to_check - x) ** 2 + (y_to_check - y) ** 2) ** (1 / 2)
                print(f"centers distance and double radius: {centers_distance, 2*radius}")
                if centers_distance < 2 * radius:
                    circles_intersect = True
                if tries >= 100:
                    break
        tries += 1
        if not circles_intersect:
            print(f"vertex {vertex} is placed")
            positions[vertex] = [x, y]
        if tries >= 100:
            break
    if tries >= 100:
        break

graph2 = nx.Graph()
for vertex in positions:
    graph2.add_node(vertex)
nx.draw(graph2, positions, with_labels=True, node_size=300+radius)
plt.show()


















