#!/usr/bin/env python

all_problems = [
    'doubleit',
    'circle',
    'tournament',
    'unlockmanifolds',
    'miku',
    'stickdrift',
    'stableblocks',
    'kumi',
    'gates',
    'pokerogue',
    'cylinder',
    'soloq',
    ]
all_branch = all_problems[:]
all_branch.remove('kumi')
all_branch.remove('circle')

skip_until = None
# skip_until = 'cylinder'

skip_problems = ['cylinder']

import os
import sys
import subprocess
import concurrent.futures

def check_branch_up_to_date(branch: str):
    diff = subprocess.check_output(['git', 'diff', f'origin/{branch}', branch, '--']).decode()
    return len(diff) == 0

def process_problem(p, i):
    print(f"\n>> Running command for problem {i}, {p}")
    os.chdir(p)
    # subprocess.run(['python', 'main.py', '-f', f'{CONTEST_ID}', '-i', f'{i}', '-a', sys.argv[1]] + sys.argv[2:], check=True)
    subprocess.run(['python', 'main.py', '-i', f'{i}'] + sys.argv[1:], check=True)
    os.chdir('..')

def main():
    global skip_until
    subprocess.run(['git', 'fetch'], check=True)
    merged_branch = subprocess.check_output(['git', 'branch', '--merged']).decode().split('\n')

    merged_branch = [s.strip('*').strip(' ') for s in merged_branch]
    e = False

    if not check_branch_up_to_date('main'):
        print('main not up to date with origin!')
        e = True

    for p in all_branch:
        if p not in merged_branch:
            print(f'{p} not merged!')
            e = True
        if not check_branch_up_to_date(p):
            print(f'{p} not up to date with origin!')
            e = True
    if e:
        return

    # CONTEST_ID = 35

    print(f'All branch up to date and merged, running commands for each problem.')
    i = 0

    arg1 = []
    arg2 = []
    for p in all_problems:
        i = i + 1
        if p == skip_until:
            skip_until = None
        if skip_until is not None or p in skip_problems:
            print(f"\n>> Skipping problem {i}, {p}")
            continue
        arg1.append(p)
        arg2.append(i)

    print(arg1, arg2)
    [x for x in map(process_problem, arg1, arg2)]

    # with concurrent.futures.ProcessPoolExecutor() as exe:
    #     exe.map(process_problem, arg1, arg2)


main()
