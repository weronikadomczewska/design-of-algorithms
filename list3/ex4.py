from turing_machine import *

beginning_state = "q0"
acceptance_state = "qa"
rejection_state = "qr"

tape_alphabet = ["0", "1", "2", "3", "4", "[", "]", "(", ")", ",", "#", "blank_sign"]
transition_function_1 = {
    "0": {
        "q0": ("qr", None, "L"),
        "q1": ("qr", None, "L"),
        "q2": ("qa", None, "R")
    },
    "1": {
        "q0": ("qr", None, "L"),
        "q1": ("q2", None, "R"),
        "q2": ("qa", None, "R")
    },
    "2": {
        "q0": ("qr", None, "L"),
        "q1": ("q2", None, "R"),
        "q2": ("qa", None, "R")
    },

    "3": {
        "q0": ("qr", None, "L"),
        "q1": ("q2", None, "R"),
        "q2": ("qa", None, "R")
    },
    "4": {
        "q0": ("qr", None, "L"),
        "q1": ("q2", None, "R"),
        "q2": ("qa", None, "R")
    },
    "(": {
        "q0": ("qr", None, "L"),
        "q1": ("qr", None, "L"),
        "q2": ("qr", None, "R")
    },
    ")": {
        "q0": ("qr", None, "L"),
        "q1": ("qr", None, "L"),
        "q2": ("q1", None, "R")
    },

    "[": {
        "q0": ("q1", None, "R"),
        "q1": ("qr", None, "L"),
        "q2": ("qr", None, "L")
    },

    "]": {
        "q0": ("qr", None, "L"),
        "q1": ("qr", None, "L"),
        "q2": ("qr", None, "R")
    },
    ",": {
        "q0": ("qr", None, "L"),
        "q1": ("qr", None, "L"),
        "q2": ("qr", None, "L")
    },
    "#": {
        "q0": ("qr", None, "L"),
        "q1": ("qa", None, "L"),
        "q2": ("qr", None, "R")
    }

}

transition_function_2 = {
    "0": {
        "q0": ("q1", None, "R"),
        "q1": ("q1", None, "R"),
        "q2": ("qr", None, "L"),
        "q3": ("qr", None, "L"),
        "q4": ("q5", None, "R"),
        "q5": ("q4", None, "L"),
        "q6": ("qr", None, "R"),
        "q7": ("q6", None, "L")
    },
    "1": {
        "q0": ("q1", None, "R"),
        "q1": ("q1", None, "R"),
        "q2": ("qr", None, "L"),
        "q3": ("qr", None, "L"),
        "q4": ("q5", None, "R"),
        "q5": ("q4", None, "L"),
        "q6": ("q7", None, "R"),
        "q7": ("q6", None, "L")
    },
    "2": {
        "q0": ("q1", None, "R"),
        "q1": ("q1", None, "R"),
        "q2": ("qr", None, "L"),
        "q3": ("qr", None, "L"),
        "q4": ("q5", None, "R"),
        "q5": ("q4", None, "L"),
        "q6": ("q7", None, "R"),
        "q7": ("q6", None, "L")
    },

    "3": {
        "q0": ("q1", None, "R"),
        "q1": ("q1", None, "R"),
        "q2": ("qr", None, "L"),
        "q3": ("qr", None, "L"),
        "q4": ("q5", None, "R"),
        "q5": ("q4", None, "L"),
        "q6": ("q7", None, "R"),
        "q7": ("q6", None, "L")
    },
    "4": {
        "q0": ("q1", None, "R"),
        "q1": ("q1", None, "R"),
        "q2": ("qr", None, "L"),
        "q3": ("qr", None, "L"),
        "q4": ("q5", None, "R"),
        "q5": ("q4", None, "L"),
        "q6": ("q7", None, "R"),
        "q7": ("q6", None, "L")
    },
    "(": {
        "q0": ("q1", None, "R"),
        "q1": ("q1", None, "R"),
        "q2": ("qr", None, "R"),
        "q3": ("q4", None, "R"),
        "q4": ("qr", None, "L"),
        "q5": ("qr", None, "L"),
        "q6": ("qr", None, "L")
    },
    ")": {
        "q0": ("q1", None, "R"),
        "q1": ("q1", None, "R"),
        "q2": ("qr", None, "L"),
        "q3": ("qr", None, "L"),
        "q4": ("qr", None, "L"),
        "q5": ("q6", None, "R"),
        "q6": ("qr", None, "L"),
        "q7": ("q0", None, "L")
    },

    "[": {
        "q0": ("q1", None, "R"),
        "q1": ("q1", None, "R"),
        "q2": ("qr", None, "L"),
        "q3": ("qr", None, "L"),
        "q4": ("qr", None, "L"),
        "q5": ("qr", None, "L"),
        "q6": ("qr", None, "L"),
        "q7": ("qr", None, "L")
    },

    "]": {
        "q0": ("q1", None, "R"),
        "q1": ("q1", None, "R"),
        "q2": ("q3", None, "R"),
        "q3": ("qr", None, "L"),
        "q4": ("qr", None, "L"),
        "q5": ("qr", None, "L"),
        "q6": ("qr", None, "L"),
        "q7": ("qr", None, "L")
    },
    ",": {
        "q0": ("q1", None, "R"),
        "q1": ("q1", None, "R"),
        "q2": ("qr", None, "L"),
        "q3": ("qr", None, "L"),
        "q4": ("qr", None, "L"),
        "q5": ("q6", None, "R"),
        "q6": ("qr", None, "L"),
        "q7": ("qr", None, "L")
    },
    "#": {
        "q0": ("q2", None, "R"),
        "q2": ("qr", None, "L"),
        "q3": ("qr", None, "L"),
        "q4": ("qr", None, "L"),
        "q5": ("q6", None, "R"),
        "q6": ("qr", None, "L"),
        "q7": ("qr", None, "L")
    },

    "blank_sign": {
        "q1": ("q1", None, "R"),
        "q2": ("qa", None, "L")
    }
}

turing_machine1 = TuringMachine(beginning_state,
                               acceptance_state,
                               rejection_state,
                               tape_alphabet,
                               transition_function_1)

turing_machine2 = TuringMachine(beginning_state,
                               acceptance_state,
                               rejection_state,
                               tape_alphabet,
                               transition_function_2)

# text = input("insert text: ")
# while not TuringMachine.check_text(text, turing_machine1.tape_alphabet):
#     text = input("Insert text again: ")

text = input("insert text: ")
while not TuringMachine.check_text(text, turing_machine2.tape_alphabet):
    text = input("Insert text again: ")

# transitions1 = turing_machine1.simulate_turing_machine(text)
# for t in transitions1:
#     print(t)

transitions2 = turing_machine2.simulate_turing_machine(text)
for t in transitions2:
    print(t)

# test dla transition 1
# [ 2 3 , #

# test dla transition 2
# ( 2 3 , 4 ) ]
