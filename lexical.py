# -*- encoding:utf-8 -*-



class State(object):

    def __init__(self):
        self.final = False
        self.transitions = {}


class Automata(object):
    
    def __init__(self, automata):
        self.states = []
        self.name = automata['name']

        for transitions, final in automata['states']:
            state = State()
            state.final = final

            for charset, forward in transitions:
                state.transitions[charset] = forward
            self.states.append(state)
            





