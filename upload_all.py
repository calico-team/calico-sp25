#!/usr/bin/env python

# from calico_lib import 
# from circle.main import problem as circle
# circle.create_all_tests()
# circle.create_zip()
#
# from doubleit.main import p as doubleit
# doubleit.create_all_tests()
# doubleit.create_zip()
#
# from kumi.main import p as kumi
# kumi.create_all_tests()
# kumi.create_zip()
#
# from miku.main import p as miku
# miku.create_all_tests()
# miku.create_zip()
#
# from pokerogue.main import p as pokerogue
# pokerogue.create_all_tests()
# pokerogue.create_zip()
#
# from soloq.main import p as soloq
# soloq.create_all_tests()
# soloq.create_zip()
#
# from stableblocks.main import p as stableblocks
# stableblocks.create_all_tests()
# stableblocks.create_zip()
#
# from stickdrift.main import p as stickdrift
# stickdrift.create_all_tests()
# stickdrift.create_zip()
#
# from tournament.main import p as tournament
# tournament.create_all_tests()
# tournament.create_zip()

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
all_branch = all_problems
all_branch.remove('kumi')
all_branch.remove('circle')
# skip_until = None
skip_until = 'cylinder'

import os
import sys
import subprocess

def check_branch_up_to_date(branch: str):
    diff = subprocess.check_output(['git', 'diff', f'origin/{branch}', branch, '--']).decode()
    return len(diff) == 0

def main():
    global skip_until
    subprocess.run(['git', 'fetch'], check=True)
    merged_branch = subprocess.check_output(['git', 'branch', '--merged']).decode().split('\n')

    merged_branch = [s.strip('*').strip(' ') for s in merged_branch]
    e = False

    if not check_branch_up_to_date('main'):
        print('main not up to date with origin!')
        e = True

    for p in all_problems:
        if p not in merged_branch:
            print(f'{p} not merged!')
            e = True
        if not check_branch_up_to_date(p):
            print(f'{p} not up to date with origin!')
            e = True
    if e:
        return

    CONTEST_ID = 35

    print(f'All branch up to date and merged, uploading to contest {CONTEST_ID}.')
    assert len(sys.argv) >= 2 and ':' in sys.argv[1], "Supply username:password"
    i = 0
    for p in all_problems:
        i = i + 1
        print(f"\n>> Uploading problem {i}, {p}")
        if p == skip_until:
            skip_until = None
        if skip_until is not None:
            continue
        os.chdir(p)
        subprocess.run(['python', 'main.py', '-f', f'{CONTEST_ID}', '-i', f'{i}', '-a', sys.argv[1]] + sys.argv[2:], check=True)
        os.chdir('..')


main()
