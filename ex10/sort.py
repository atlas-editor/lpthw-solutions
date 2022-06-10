import argparse
import random
import sys

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='?')
parser.add_argument('-b', action='store_true')
parser.add_argument('-f', action='store_true')
parser.add_argument('-r', action='store_true')
parser.add_argument('-R', action='store_true')

args = parser.parse_args()

def rand_dict(lst):
    N = len(lst)
    lst = list(set(lst))
    M = len(lst)
    rands = random.sample(range(N), M)

    return {lst[i]:rands[i] for i in range(M)}

if args.file is not None:
    with open(args.file) as f:
        raw_lines = f.readlines()
else:
    raw_lines = list(sys.stdin)

lines = [(x.rstrip('\n'),x.rstrip('\n')) for x in raw_lines]
if args.b:
    lines = [(i,j.lstrip()) for i,j in lines]
if args.f:
    lines = [(i,j.lower()) for i,j in lines]
if args.R:
    random_function = rand_dict([j for _,j in lines])
    lines = [(i,random_function[j]) for i,j in lines]
sorted_lines = sorted(lines, key=lambda x: x[1], reverse=args.r)
for line in sorted_lines:
    print(line[0])
