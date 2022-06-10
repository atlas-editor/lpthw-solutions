import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('input_file', nargs='?')
parser.add_argument('-i', action='store_true')

args = parser.parse_args()

if args.input_file is not None:
    with open(args.input_file) as f:
        raw_lines = [x.rstrip('\n') for x in f.readlines()]
else:
    raw_lines = [x.rstrip('\n') for x in list(sys.stdin)]

prev = None
comp = (lambda x,y: x.lower() == y.lower()) if args.i else lambda x,y: x == y
for i in raw_lines:
    if prev is not None and comp(i,prev):
        continue
    else:
        print(i)
        prev = i
