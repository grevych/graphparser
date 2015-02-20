# -*- encoding:utf-8 -*-

from parser import Parser

#checamos que no empiece con gato
#checamos longitud
#checamos el split de espacios no me de 0
#   with open(file, 'r+') as f:
#         lineno = 0
#         # this reads in one line at a time from stdin
#         for line in f:
#             lineno += 1
#             print '{:>6} {}'.format(lineno, line[:-1])



def read_graph(file_name):
    parser = Parser()
    return parser(file_name)



if __name__ == '__main__':
    import sys

    commands = (
        ('read-graph', 'Read graph from file', ), )
    
    if len(sys.argv) < 2:
        print 'usage: search <command> [<args>]\n'
        print 'Search commands:'
        for command, description in commands:
            print '\t', command, '\t', description
        exit(0)
    
    graph = read_graph(sys.argv[1])

    for node in graph.nodes:
        print node
        for transition in node.transitions:
            print transition
