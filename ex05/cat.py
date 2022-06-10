import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('files', metavar='FILE', nargs='*')
parser.add_argument('-b', '--number-nonblank', action='store_true', help='number nonempty output lines, overrides -n')
parser.add_argument('-E', '--show-ends', action='store_true', help='display $ at end of each line')
parser.add_argument('-n', '--number', action='store_true', help='number all output lines')
parser.add_argument('-s', '--squeeze-blank', action='store_true', help='suppress repeated empty output lines')

args = parser.parse_args()

i = 1
blank_above = False

def cat_print(raw_lines):
    for raw_line in raw_lines:
                line = raw_line.rstrip('\n')
                if args.squeeze_blank:
                    if line != '':
                        blank_above = False
                    elif blank_above:
                        continue
                    else:
                        blank_above = True
                if args.show_ends:
                    line += '$'
                if args.number or args.number_nonblank:
                    if not(args.number_nonblank and (line in ('', '$'))):
                        line = f'     {i}	{line}'
                        i += 1

                print(line)

if args.file is not None:
    for file in args.files:
        with open(file) as f:
            raw_lines = f.readlines()
            cat_print(raw_lines)
else:
    cat_print(list(sys.stdin))