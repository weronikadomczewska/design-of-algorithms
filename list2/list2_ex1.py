from automata import *

transition_function = {

    "0": {"q0": "q1",
          "q1": "q3",
          "q2": "q2",
          "q3": "q2"},
    "1": {"q0": "q0",
          "q1": "q2",
          "q2": "q0",
          "q3": "q2"},
}

alphabet = "01"
beginning_state = "q0"
acceptance_state = "q3"

print("ex 1: ")
text = input("Enter text: ")
while not check_text(text, alphabet):
    print("Incorrect text, enter again: ")
    text = input("Enter text: ")

automata = Automata(alphabet, transition_function, beginning_state, acceptance_state)
print(automata.simulate_automata(text))
