class TuringMachine:

    def __init__(self, beginning_state,
                 acceptance_state,
                 rejection_state,
                 tape_alphabet,
                 transition_function):
        self.tape = []
        self.head_idx = 0
        self.beginning_state = beginning_state
        self.acceptance_state = acceptance_state
        self.rejection_state = rejection_state
        self.tape_alphabet = tape_alphabet
        self.transition_function = transition_function

    def simulate_turing_machine(self, text):
        state = self.beginning_state
        self.tape = text.split() + ["blank_sign"]
        transitions = []
        while True:
            prev_state = state
            prev_tape = self.tape[:]
            prev_head_idx = self.head_idx
            current_sign = self.tape[self.head_idx]
            transition_details = self.transition_function[current_sign][prev_state]
            next_state = transition_details[0]
            next_sign = transition_details[1]
            next_move_direction = transition_details[2]
            if next_sign is not None:
                self.tape[self.head_idx] = next_sign
            if next_move_direction == "L":
                if self.head_idx >= 1:
                    self.head_idx -= 1
            elif next_move_direction == "R":
                self.head_idx += 1
            state = next_state
            transitions.append(f"transition: ({prev_state}, {current_sign})->({next_state}, {next_sign}, {next_move_direction}), \n"
                               f"previous tape: {prev_tape}, \nnew_tape: {self.tape}, \n"
                               f"previous head position: {prev_head_idx}, next head position: {self.head_idx}" + "\n")
            if state == self.acceptance_state:
                print(f"string {text} has been accepted")
                break
            elif state == self.rejection_state:
                print(f"string {text} has been rejected")
                break
        try:
            return transitions[:-1]
        except KeyError:
            print("Transitions is empty")

    @staticmethod
    def check_text(text, alphabet):
        for sign in text.split():
            if sign not in alphabet:
                return False
        return True

