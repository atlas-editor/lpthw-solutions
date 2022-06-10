import argparse
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument('script')
parser.add_argument('input_file', nargs='?')

args = parser.parse_args()

def parse_script(s):
    split_script = s.split('/')
    if split_script[0] == 's':
        if split_script[-1] == 'g':
            count = 0
        elif split_script[-1] == '':
            count = 1
        else:
            count = int(split_script[-1])
        return 's', split_script[1], split_script[2], count
    elif split_script[0] == '' and split_script[-1].startswith('a'):
        return 'a', split_script[1], split_script[2].split(' ', maxsplit=1)[1]

if args.input_file is not None:
    with open(args.input_file) as f:
        raw_lines = f.readlines()
else:
    raw_lines = list(sys.stdin)

for raw_line in raw_lines:
    line = raw_line.rstrip('\n')
    parsed = parse_script(args.script)
    if parsed[0] == 's':
        pattern, repl, count = parsed[1:]
        print(re.sub(pattern, repl, line, count))
    if parsed[0] == 'a':
        print(line)
        pattern, append = parsed[1:]
        if re.search(pattern, line) is not None:
            print(append)