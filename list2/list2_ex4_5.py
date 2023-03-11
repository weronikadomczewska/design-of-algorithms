from automata import *
import json


alphabet = "abcd"
beginning_state = "q0"
acceptance_state = "q2"

transition_function = {
    "a": {"q0": "q0",
          "q1": "q3",
          "q2": "q3",
          "q3": "q3"},
    "b": {"q0": "q1",
          "q1": "q3",
          "q2": "q3",
          "q3": "q3"},
    "c": {"q0": "q3",
          "q1": "q2",
          "q2": "q3",
          "q3": "q3"},
    "d": {"q0": "q3",
          "q1": "q3",
          "q2": "q2",
          "q3": "q3"}
}

print("ex 4: ")
text = input("Enter text: ")
while not check_text(text, alphabet):
    print("Incorrect text, enter again: ")
    text = input("Enter text: ")

automata = Automata(alphabet, transition_function, beginning_state, acceptance_state)
transitions = automata.simulate_automata(text)
print(transitions)

print(100 * "-")
print("ex 5: ")

with open("automata_config.json") as file:
    data = json.load(file)

alphabet = data["alphabet"]
beginning_state = data["beginning_state"]
acceptance_state = data["acceptance_state"]
transition_function = data["transition_function"]

automata = Automata(alphabet, transition_function, beginning_state, acceptance_state)
transitions = automata.simulate_automata(text)
print(transitions)
