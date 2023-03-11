from automata import *
import networkx as nx
import matplotlib.pyplot as plt
import imageio
import os


alphabet = "abc"
beginning_state = "q0"
acceptance_state = "q6"

transition_function = {
    "a": {"q0": "q2",
          "q1": "q4",
          "q2": "q1",
          "q3": "q3",
          "q4": "q0",
          "q5": "q4",
          "q6": "q3"},
    "b": {"q0": "q2",
          "q1": "q0",
          "q2": "q1",
          "q3": "q3",
          "q4": "q5",
          "q5": "q4",
          "q6": "q3"},
    "c": {"q0": "q2",
          "q1": "q3",
          "q2": "q6",
          "q3": "q3",
          "q4": "q5",
          "q5": "q4",
          "q6": "q3"}
}

print("ex 2: ")
text = input("Enter text: ")
while not check_text(text, alphabet):
    print("Incorrect text, enter again: ")
    text = input("Enter text: ")

automata = Automata(alphabet, transition_function, beginning_state, acceptance_state)
transitions = automata.simulate_automata(text)
print(transitions)

graph = nx.DiGraph()
for node in transition_function["a"].keys():
    graph.add_node(node)
graph.add_edge("q0", "q2")
graph.add_edge("q1", "q3")
graph.add_edge("q2", "q6")
graph.add_edge("q2", "q1")
graph.add_edge("q6", "q3")
graph.add_edge("q3", "q3")
graph.add_edge("q3", "q1")
graph.add_edge("q4", "q5")
graph.add_edge("q4", "q0")
graph.add_edge("q5", "q4")

edge_labels = {
    ("q0", "q2"): "a,b,c",
    ("q1", "q3"): "c",
    ("q2", "q6"): "c",
    ("q2", "q1"): "a,b",
    ("q6", "q3"): "a,b,c",
    ("q3", "q3"): "a,b,c",
    ("q3", "q1"): "a,b,c",
    ("q4", "q5"): "b,c",
    ("q4", "q0"): "a",
    ("q5", "q4"): "a,b,c"
}

pos = nx.spring_layout(graph)
all_states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6"]
chosen_states = []

for t in transitions:
    for state in t:
        chosen_states.append(state)

cnt = 0
color_map = []
for chosen_state in chosen_states:
    for state in all_states:
        if state == chosen_state:
            color_map.append("yellow")
        else:
            color_map.append("pink")
    # print(color_map)
    nx.draw(graph, pos, with_labels=True, node_color=color_map)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)
    plt.savefig(f"images/fig{cnt}.jpg")
    cnt += 1
    color_map = []




