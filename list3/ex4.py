from turing_machine import *

beginning_state = "q0"
acceptance_state = "qa"
rejection_state = "qr"

tape_alphabet = ["1", "2", "3", "4", "[", "]", "(", ")", ",", "#"]

transition_function = {

    "1": {
        "q0": ("qr", None, "R"),
        "q1": ("qr", None, "R"),
        "q2": ("q3", None, "R"),
        "q3": ("q3", None, "R"),
        "q4": ("q5", None, "R"),
        "q5": ("q5", None, "R"),
        "q6": ("qr", None, "R"),
        "q7": ("qr", None, "R"),
        "q8": ("q9", None, "R"),
        "q9": ("q9", None, "R"),
        "q10": ("q9", None, "R"),

    },
    "2": {
        "q0": ("qr", None, "R"),
        "q1": ("qr", None, "R"),
        "q2": ("q3", None, "R"),
        "q3": ("q3", None, "R"),
        "q4": ("q5", None, "R"),
        "q5": ("q5", None, "R"),
        "q6": ("qr", None, "R"),
        "q7": ("qr", None, "R"),
        "q8": ("q9", None, "R"),
        "q9": ("q9", None, "R"),
        "q10": ("q9", None, "R"),
    },

    "3": {

        "q0": ("qr", None, "R"),
        "q1": ("qr", None, "R"),
        "q2": ("q3", None, "R"),
        "q3": ("q3", None, "R"),
        "q4": ("q5", None, "R"),
        "q5": ("q5", None, "R"),
        "q6": ("qr", None, "R"),
        "q7": ("qr", None, "R"),
        "q8": ("q9", None, "R"),
        "q9": ("q9", None, "R"),
        "q10": ("q9", None, "R"),
    },
    "4": {

        "q0": ("qr", None, "R"),
        "q1": ("qr", None, "R"),
        "q2": ("q3", None, "R"),
        "q3": ("q3", None, "R"),
        "q4": ("q5", None, "R"),
        "q5": ("q5", None, "R"),
        "q6": ("qr", None, "R"),
        "q7": ("qr", None, "R"),
        "q8": ("q9", None, "R"),
        "q9": ("q9", None, "R"),
        "q10": ("q9", None, "R")
    },
    "(": {
        "q0": ("qr", None, "R"),
        "q1": ("q2", None, "R"),
        "q2": ("qr", None, "R"),
        "q3": ("qr", None, "R"),
        "q4": ("qr", None, "R"),
        "q5": ("qr", None, "R"),
        "q6": ("qr", None, "R"),
        "q7": ("q2", None, "R"),
        "q8": ("qr", None, "R"),
        "q9": ("qr", None, "R"),
        "q10": ("qr", None, "R")
    },
    ")": {
        "q0": ("qr", None, "R"),
        "q1": ("qr", None, "R"),
        "q2": ("qr", None, "R"),
        "q3": ("qr", None, "R"),
        "q4": ("qr", None, "R"),
        "q5": ("q6", None, "R"),
        "q6": ("qr", None, "R"),
        "q7": ("qr", None, "R"),
        "q8": ("qr", None, "R"),
        "q9": ("qr", None, "R"),
        "q10": ("qr", None, "R")
    },

    "[": {
        "q0": ("q1", None, "R"),
        "q1": ("qr", None, "R"),
        "q2": ("qr", None, "R"),
        "q3": ("qr", None, "R"),
        "q4": ("qr", None, "R"),
        "q5": ("qr", None, "R"),
        "q6": ("qr", None, "R"),
        "q7": ("q2", None, "R"),
        "q8": ("qr", None, "R"),
        "q9": ("qr", None, "R"),
        "q10": ("qr", None, "R")
    },

    "]": {
        "q0": ("qr", None, "R"),
        "q1": ("qr", None, "R"),
        "q2": ("qr", None, "R"),
        "q3": ("qr", None, "R"),
        "q4": ("qr", None, "R"),
        "q5": ("qr", None, "R"),
        "q6": ("qr", None, "R"),
        "q7": ("q2", None, "R"),
        "q8": ("qa", None, "R"),
        "q9": ("qa", None, "R"),
        "q10": ("qr", None, "R")
    },
    ",": {
        "q0": ("qr", None, "R"),
        "q1": ("qr", None, "R"),
        "q2": ("qr", None, "R"),
        "q3": ("q4", None, "R"),
        "q4": ("qr", None, "R"),
        "q5": ("qr", None, "R"),
        "q6": ("q7", None, "R"),
        "q7": ("qr", None, "R"),
        "q8": ("qr", None, "R"),
        "q9": ("q10", None, "R"),
        "q10": ("qr", None, "R")
    },
    "#": {
        "q0": ("qr", None, "R"),
        "q1": ("q8", None, "R"),
        "q2": ("qr", None, "R"),
        "q3": ("qr", None, "R"),
        "q4": ("qr", None, "R"),
        "q5": ("qr", None, "R"),
        "q6": ("q8", None, "R"),
        "q7": ("qr", None, "R"),
        "q8": ("qr", None, "R"),
        "q9": ("qr", None, "R"),
        "q10": ("qr", None, "R")
    },

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


