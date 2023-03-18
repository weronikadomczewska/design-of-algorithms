from turing_machine import *

beginning_state = "q0"
acceptance_state = "qa"
rejection_state = "qr"
tape_alphabet = ["0", "1", "crossed_zero", "crossed_one", "b", "blank_sign"]
transition_function = {
    "0": {
        "q0": ("q2", "crossed_zero", "R"),
        "q1": ("q1", None, "L"),
        "q2": ("q2", None, "R"),
        "q3": ("q3", None, "R"),
        "q4": ("q6", "crossed_zero", "L"),
        "q5": ("qr", None, "R"),
        "q7": ("q7", None, "L"),
        "qa": ("qa", None, None),
        "qr": ("qr", None, None)
    },
    "1": {
        "q0": ("q3", "crossed_one", "R"),
        "q1": ("q1", None, "L"),
        "q2": ("q2", None, "R"),
        "q3": ("q3", None, "R"),
        "q4": ("qr", None, "R"),
        "q5": ("q6", "crossed_one", "L"),
        "q7": ("q7", None, "L"),
        "qa": ("qa", None, None),
        "qr": ("qr", None, None)
    },
    "crossed_zero": {
        "q1": ("q1", None, "R"),
        "q4": ("q4", None, "R"),
        "q5": ("q5", None, "R"),
        "q6": ("q6", None, "L"),
        "q7": ("q0", None, "R"),
        "qa": ("qa", None, None),
        "qr": ("qr", None, None)
    },
    "crossed_one": {
        "q1": ("q1", None, "R"),
        "q4": ("q4", None, "R"),
        "q5": ("q5", None, "R"),
        "q6": ("q6", None, "L"),
        "q7": ("q0", None, "R"),
        "qa": ("qa", None, None),
        "qr": ("qr", None, None)
    },
    "b": {
        "q0": ("q1", None, "R"),
        "q2": ("q4", None, "R"),
        "q3": ("q5", None, "R"),
        "q6": ("q7", None, "L"),
        "qa": ("qa", None, None),
        "qr": ("qr", None, None)
    },
    "blank_sign": {
        "q1": ("qa", None, "L"),
        "q2": ("qr", None, "R"),
        "q3": ("qr", None, "R"),
        "q4": ("qr", None, "R"),
        "q5": ("qr", None, "R"),
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
print(text)
while not TuringMachine.check_text(text, turing_machine.tape_alphabet):
    text = input("Insert text again: ")

transitions = turing_machine.simulate_turing_machine(text)
for t in transitions:
    print(t)
