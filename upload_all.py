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
    'stableblocks',
    # 'stickdrift',
    # 'kumi',
    # 'gates',
    # 'pokerogue',
    # 'cylinder',
    # 'soloq',
    ]
all_branch = all_problems
# all_branch.remove('kumi')
all_branch.remove('circle')

import os
import sys
def main():
    import subprocess
    subprocess.run(['git', 'fetch'], check=True)
    merged_branch = subprocess.check_output(['git', 'branch', '--merged']).decode().split('\n')

    merged_branch = [s.strip('*').strip(' ') for s in merged_branch]
    e = False
    for p in all_problems:
        origin_diff = subprocess.check_output(['git', 'diff', f'origin/{p}', p, '--']).decode()
        if p not in merged_branch:
            print(f'{p} not merged!')
            e = True
        if len(origin_diff) > 0:
            print(f'{p} not up to date with origin!')
    if e:
        return
    return

    assert len(sys.argv) >= 2 and ':' in sys.argv[1], "Supply username:password"
    i = 1
    for p in all_problems:
        os.chdir(p)
        subprocess.run(['python', 'main.py', '-f', '35', '-i', f'{i}', '-a', sys.argv[1]] + sys.argv[2:], check=True)
        os.chdir('..')
        i = i + 1


main()
