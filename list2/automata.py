class Automata:

    def __init__(self, alphabet, transition_function, beginning_state, acceptance_state):
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.beginning_state = beginning_state
        self.acceptance_state = acceptance_state

    def simulate_automata(self, text):
        state = self.beginning_state
        transitions = []
        for sign in text:
            prev_state = state
            state = self.transition_function[sign][state]
            transitions.append((prev_state, state))
        if state == self.acceptance_state:
            print(f"Text {text} belongs to language described by automata ")
        else:
            print(f"Text {text} does not belong to language described by automata ")
        return transitions


def check_text(text, alphabet):
    for sign in text:
        if sign not in alphabet:
            return False
    return True
