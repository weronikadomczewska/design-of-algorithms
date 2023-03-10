from automata import *

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
print(automata.simulate_automata(text))
