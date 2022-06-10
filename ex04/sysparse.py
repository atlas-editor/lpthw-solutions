import os
import sys

tokens = sys.argv[1:]

signs = {'add':'+', 'mul':'*', 'div': '/'}
names = {'add':'sum', 'mul':'product', 'div': 'quotient'}
ops = {'add':lambda x,y: x+y, 'mul':lambda x,y: x*y, 'div': lambda x,y: x/y}

def parse_input(tokens):
    op = tokens[0]
    sign = signs[op]
    name = names[op]
    fun = ops[op]
    res = None
    if tokens[1].isdigit() and tokens[2].isdigit():
        a = int(tokens[1])
        b = int(tokens[2])
        res = fun(a,b)
        print(f'{a}{sign}{b}={res}')
    elif tokens[1][0] == '-' and tokens[2].isdigit() and tokens[3].isdigit():
        a = int(tokens[2])
        b = int(tokens[3])
        res = fun(a,b)
        if tokens[1] == '-v':
            print(f'The {name} of {a} and {b} is: {res}')
        elif tokens[1] == '-q':
            print(res)
        elif tokens[1] == '-n':
            print(f'{a}{sign}{b}={res}')
        else:
            print(f'incorrect flag: {tokens[1]}')
    else:
        print(f'incorrect parameters for {op}: {" ".join(tokens[1:])}')

    if res is not None and os.path.isfile(tokens[-1]):
        with open(tokens[-1], 'w') as f:
            f.write(f'{a}{sign}{b}={res}')

if '-h' in tokens or '--help' in tokens:
    print('(help section)')
    sys.exit(0)

parse_input(tokens)