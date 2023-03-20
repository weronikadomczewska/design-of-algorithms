from turing_machine import *
import json

with open("ex3_config.json") as file:
    data = json.load(file)

tape_alphabet = data["tape_alphabet"]
beginning_state = data["beginning_state"]
acceptance_state = data["acceptance_state"]
rejection_state = data["rejection_state"]
transition_function = data["transition_function"]

turing_machine = TuringMachine(beginning_state,
                               acceptance_state,
                               rejection_state,
                               tape_alphabet,
                               transition_function)

text = input("insert text: ")
print(text)
while not TuringMachine.check_text(text, turing_machine.tape_alphabet):
    text = input("Insert text again: ")

transitions = turing_machine.simulate_turing_machine(text)
for t in transitions:
    print(t)
