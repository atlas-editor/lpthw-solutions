import argparse
import os


signs = {'add':'+', 'mul':'*', 'div': '/'}
names = {'add':'sum', 'mul':'product', 'div': 'quotient'}
ops = {'add':lambda x,y: x+y, 'mul':lambda x,y: x*y, 'div': lambda x,y: x/y}

parser = argparse.ArgumentParser()

parser.add_argument('op', choices=['add', 'mul', 'div'])
parser.add_argument('integer', nargs=2, type=int)
parser.add_argument('destination', nargs='?')

flags = parser.add_mutually_exclusive_group()
flags.add_argument('-v', '--verbose', action='store_true')
flags.add_argument('-q', '--quiet', action='store_true')
flags.add_argument('-n', '--normal', action='store_true')

args = parser.parse_args()
a = args.integer[0]
b = args.integer[1]
op = args.op
destination = args.destination
sign = signs[op]
name = names[op]
fun = ops[op]
res = fun(a,b)

if args.verbose:
    print(f'The {name} of {a} and {b} is: {res}')
elif args.quiet:
    print(res)
else:
    print(f'{a}{sign}{b}={res}')

if destination is not None and os.path.isfile(destination):
    with open(destination, 'w') as f:
            f.write(f'{a}{sign}{b}={res}')