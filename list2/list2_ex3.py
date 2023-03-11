from automata import *

alphabet = "a01"
beginning_state = "q0"
acceptance_state = "q2"

transition_function = {
    "a": {"q0": "q1",
          "q1": "q2",
          "q2": "q3",
          "q3": "q3"},
    "0": {"q0": "q3",
          "q1": "q1",
          "q2": "q2",
          "q3": "q3"},
    "1": {"q0": "q3",
          "q1": "q1",
          "q2": "q2",
          "q3": "q3"}
}

print("ex 3: ")
text = input("Enter text: ")
while not check_text(text, alphabet):
    print("Incorrect text, enter again: ")
    text = input("Enter text: ")

automata = Automata(alphabet, transition_function, beginning_state, acceptance_state)
transitions = automata.simulate_automata(text)
print(transitions)

# graph = nx.DiGraph()
# for node in transition_function["a"].keys():
#     graph.add_node(node)
# graph.add_edge("q0", "q1")
# graph.add_edge("q0", "q3")
# graph.add_edge("q1", "q2")
# graph.add_edge("q1", "q1")
# graph.add_edge("q2", "q3")
# graph.add_edge("q2", "q2")
# graph.add_edge("q3", "q3")
#
# edge_labels = {
#     ("q0", "q1"): "a",
#     ("q1", "q1"): "0,1",
#     ("q1", "q2"): "a",
#     ("q2", "q2"): "0,1",
#     ("q2", "q3"): "a",
#     ("q3", "q3"): "0,1,a"
# }
#
# pos = nx.spring_layout(graph)
# nx.draw(graph, pos, with_labels=True, node_color="pink")
# nx.draw_networkx_edge_labels(graph, pos, edge_labels)
# plt.show()
