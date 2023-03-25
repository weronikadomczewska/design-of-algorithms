from turing_machine import *

beginning_state = "q0"
acceptance_state = "qa"
rejection_state = "qr"
tape_alphabet = ["a", "crossed_a", "a_with_dot", "blank_sign"]
transition_function = {
    "a": {
        "q0": ("q1", "a_with_dot", "R"),
        "q1": ("q2", None, "L"),
        "q3": ("q4", None, "R"),
        "q4": ("q5", "crossed_a", "R"),
        "q5": ("q3", "crossed_a", "R"),
        "q6": ("q6", None, "L"),
        "qa": ("qa", None, None),
        "qr": ("qr", None, None)
    },
    "a_with_dot": {
        "q2": ("q3", None, "L"),
        "q3": ("q4", None, "R"),
        "q6": ("q1", None, "R"),
        "qa": ("qa", None, None),
        "qr": ("qr", None, None)
    },
    "crossed_a": {
        "q1": ("q1", None, "R"),
        "q2": ("q2", None, "L"),
        "q3": ("q3", None, "R"),
        "q4": ("q4", None, "R"),
        "q5": ("q5", None, "R"),
        "q6": ("q6", None, "L"),
        "qa": ("qa", None, None),
        "qr": ("qr", None, None)
    },
    "blank_sign": {
        "q0": ("qr", None, "L"),
        "q1": ("qa", None, "L"),
        "q3": ("q6", None, "L"),
        "q4": ("qr", None, "L"),
        "q5": ("qr", None, "L"),
        "qa": ("qa", None, None),
        "qr": ("qr", None, None)
    }
}

turing_machine = TuringMachine(beginning_state,
                               acceptance_state,
                               rejection_state,
                               tape_alphabet,
                               transition_function)

text = input("insert text: ")
while not TuringMachine.check_text(text, turing_machine.tape_alphabet):
    text = input("Insert text again: ")

transitions = turing_machine.simulate_turing_machine(text)
for t in transitions:
    print(t)
