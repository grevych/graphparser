# -*- encoding:utf-8 -*-

import re

import utils
import error

from lexical import Automata
from graph import Graph, Node


class Parser(object):

    def __init__(self):
        self.tokens = []
        self.file = None
        self.line = 1
        self.sets = utils.SETS
        self.automatas = [Automata(automata) for automata in utils.AUTOMATAS]
        self.lexemes = utils.LEXEMES
        self.lexemes_as_regexp = utils.LEXEMES_AS_REGEXP
        self.escape_characters = utils.ESCAPE_CHARACTERS

    def __call__(self, file_name):
        with open(file_name, 'r') as graph_file:
            self.file = graph_file
            self.get_tokens()
        return self.parse()
    
    def get_tokens(self):
        token = self.next_token()
        while token:
            lexeme = self.is_lexeme(token)
            if not lexeme:
                raise error.NotLexeme(token) #, line)
            self.tokens.append((self.line, lexeme, token, ))
            token = self.next_token()
        print self.tokens

    def parse(self):
        table = {
            'graph': None,
            'line_buffer': None,
            'column': None
        }

        def set_graph(line, token):
            table['graph'] = Graph()
            table['line_buffer'] = line + 1
            table['column'] = 0

        def set_node(line, token):
            print '->', line - table['line_buffer']

            if table['graph'].nodes.__len__() <= line - table['line_buffer']:
                node = Node()
                table['graph'].nodes.append(node)
                table['column'] = 0

            if token == '0':
                table['column'] = table['column'] + 1
                return
                
            set_transition(table['graph'].nodes[-1], token)
            table['column'] = table['column'] + 1

        def set_transition(node, token):
            node.transitions.append((table['column'], token, ))

        funcs = {
            'TITLE': set_graph,
            'DIGIT': set_node
        }

        for line, lexeme, token in self.tokens:
            print line, lexeme, token
            if funcs.has_key(lexeme):
                funcs[lexeme](line, token)

        return table['graph']

    def next_token(self):
        token = None

        print '','_______INIT______',''

        for automata in self.automatas:
            token = ''
            character = self.file.read(1)
            counter = 1
            index = 0
            state = automata.states[index]
            has_transition = True

            print 'AUTOMATA: ', automata.name

            while character in self.escape_characters:
                if character == '\n':
                    self.line = self.line + 1
                    print self.line
                character = self.file.read(1)

            while has_transition and character:

                print '\tCHARACTER: ', character
                print '\tSTATE', index

                has_transition = False
                for charset in state.transitions.keys():

                    print '\t\tCHARSET:', charset

                    if character in charset:

                        print '______ACEPTED______'
                        print '\t\tMOVE_TO: ', state.transitions[charset]

                        token = token + character
                        index = state.transitions[charset]
                        state = automata.states[index]
                        character = self.file.read(1)
                        counter = counter + 1
                        has_transition = True
                        break
            print '_______OUT_______'
            print 'TOKEN: ', token

            if state.final:
                print '______FINAL______'
                if character:
                    self.file.seek(-1, 1)
                return token

            if not character:
                return False

            print 'COUNTER: ', counter
            self.file.seek(-counter, 1)

        #regresar TODO EL TOKEN mal escrito read until special character
        a = self.file.readline()
        print a
        return a


    def is_lexeme(self, token):
        if self.lexemes.has_key(token):
            return self.lexemes[token]

        for regexp, lexeme in self.lexemes_as_regexp:
            if re.match(regexp, token):
                return lexeme

        return False


