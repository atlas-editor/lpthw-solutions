import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='?')
parser.add_argument('-d', '--delimiter')
parser.add_argument('-f', '--fields')

args = parser.parse_args()

def parse_field(f):
    res = []
    comma_separated = f.split(',')
    for i in comma_separated:
        if '-' in i:
            a, b = map(int, i.split('-', maxsplit=1))
            res += range(a,b+1)
        else:
            res.append(int(i))
    return res

if args.file is not None:
    with open(args.file) as f:
        raw_lines = f.readlines()
else:
    raw_lines = list(sys.stdin)

for raw_line in raw_lines:
    raw_line = raw_line.rstrip('\n')
    split_line = raw_line.split(args.delimiter)
    fields = parse_field(args.fields)
    for i in fields:
        if i<len(split_line):
            print(split_line[i], end=' ')
    print()
