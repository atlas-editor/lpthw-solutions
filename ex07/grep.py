import argparse
import re
import glob
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument('pattern')
parser.add_argument('file', nargs='?')

args = parser.parse_args()

pattern = re.compile(args.pattern)
red_bold = '\033[1;31m'
magenta = '\033[;35m'
cyan = '\033[;36m'
reset = '\033[0m'

def grep_lines(raw_lines):
    for raw_line in raw_lines:
        line = raw_line.strip()
        print(f'{magenta}{i.split("/")[-1]}{cyan}:{reset}', end='')
        print(pattern.sub(lambda x: f'{red_bold}{x[0]}{reset}',line))

if args.file is not None:
    path = f'{os.getcwd()}/{args.file}'
    for i in glob.glob(path):
        with open(i) as f:
            raw_lines = f.readlines()
            grep_lines(raw_lines)
else:
    grep_lines(list(sys.stdin))
