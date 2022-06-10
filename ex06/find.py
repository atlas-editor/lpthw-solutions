import argparse
import subprocess
import glob
import os

parser = argparse.ArgumentParser()
parser.add_argument('path')
parser.add_argument('-name')
parser.add_argument('-type', choices=['d', 'f'])
parser.add_argument('-print', action='store_true')
parser.add_argument('-exec')

args = parser.parse_args()

exec = 'echo' if args.exec is None else args.exec
check = lambda _: True
if args.type == 'd':
    check = os.path.isdir
elif args.type == 'f':
    check = os.path.isfile

def search(path, name):
    for i in glob.glob(f'{path}/{name}'):
        if check(i):
            subprocess.run([exec, i])
    try:
        ls = os.listdir(path)
    except PermissionError:
        return
    for entry in ls:
        if os.path.isdir(f'{path}/{entry}'):
            search(f'{path}/{entry}', name)

search(args.path, args.name)