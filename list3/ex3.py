from turing_machine import *

beginning_state = "q0"
acceptance_state = "qa"
rejection_state = "qr"
tape_alphabet = ["a", "b", "crossed_a", "crossed_b", "x", "blank_sign"]
transition_function = {
    "a": {
        "q0": ("q2", "crossed_a", "R"),
        "q1": ("qr", None, "L"),
        "q2": ("q2", None, "R"),
        "q3": ("q4", "crossed_a", "L"),
        "q4": ("q4", None, "L"),
        "q5": ("q0", None, None),
        "q6": ("qr", None, "L")
    },
    "b": {
        "q0": ("q2", "crossed_b", "R"),
        "q1": ("qr", None, "L"),
        "q2": ("q2", None, "R"),
        "q3": ("q4", "crossed_b", "L"),
        "q4": ("q4", None, "L"),
        "q5": ("q0", None, None),
        "q6": ("qr", None, "L")

    },
    "crossed_a": {
        "q1": ("qr", None, "L"),
        "q2": ("q2", None, "L"),
        "q3": ("qr", None, "L"),
        "q4": ("q5", None, "R"),
        "q5": ("qr", None, "L"),
        "q6": ("qa", None, "L")

    },
    "crossed_b": {
        "q1": ("qr", None, "L"),
        "q2": ("q3", None, "L"),
        "q3": ("qr", None, "L"),
        "q4": ("q5", None, "R"),
        "q5": ("qr", None, "L"),
        "q6": ("qa", None, "L")

    },
    "x": {
        "q0": ("q1", None, "R"),
        "q1": ("qr", None, "L"),
        "q2": ("q2", None, "R"),
        "q3": ("qr", None, "L"),
        "q4": ("q4", None, "L"),
        "q5": ("q6", None, "R")
    },

    "blank_sign": {
        "q1": ("qa", None, "L"),
        "q2": ("q3", None, "L")
    }
}


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
