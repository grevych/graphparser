# -*- encoding:utf-8 -*-


SETS = {
    'D': '01234456789',
    'L': 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ',
    'C': '01234456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ!"·#$%&/()=?¿¡ºª*+^`[]´Ç¨{}-_:.;,<>\'\\\t '
}


AUTOMATAS = (
    {'name': 'comment',
     'states': (
        ((('#', 1, ), ), False, ),
        (((SETS['C'], 1, ), ), True, ), )},
    {'name': 'digit',
     'states': ( 
        ((('+-' + SETS['D'], 1, ), ), False, ),
        (((SETS['D'], 1, ),
          ('.', 2, ), ),
         True, ),
        (((SETS['D'], 3, ), ),  False, ),
        (((SETS['D'], 3, ), ), True, ), )},
    {'name': 'reserved',
     'states': ( 
        (((SETS['L'], 1, ), ), False, ),
        (((SETS['L'], 1, ), ), True, ), )},
    {'name': 'variable',
     'states': ( 
        ((('_' + SETS['L'], 1, ), ), False, ),
        ((('_' + SETS['D'] + SETS['L'], 1, ), ), True, ), )},
)

LEXEMES = {
    'title': 'TITLE'
}

LEXEMES_AS_REGEXP = (
    (r'^\d+$', 'DIGIT'),
    (r'^\w+$', 'VARIABLE'),
    (r'^".*"', 'STRING'),
    (r'^#.*$', 'COMMENT'),  
)

ESCAPE_CHARACTERS = (' ', '\n', '\t', '\r', )
