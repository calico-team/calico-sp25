#!/usr/bin/env python3

# Example add problem.
# Constraints:
#   main: T <= 100, A <= 100, B <= 100
#   bonus: T <= 1e5, A <= 1e12, B <= 1e12

import genericpath
from typing import override
from calico_lib import Problem, compile_all, cpp_runner, py_runner, TestFileBase, MulticaseTestFile, Subproblem, Runner
from collections.abc import Collection, Iterable
from typing import NamedTuple, override
import random
import os

from calico_lib.multicase import TestCaseBase

problem_dir = os.path.dirname(__file__)

p = Problem(
        'stable_blocks',
        problem_dir, # problem is in the same directory as the python source file
        test_sets=[
            Subproblem('main', rank=2),
            Subproblem('bonus', rank=3)
                       # , time_limit=4, mem_limit=1_000_000_000),
            ])

class TestCase(NamedTuple):
    X: int
    Y: int

solution = cpp_runner(
        os.path.join(problem_dir,
                     'submissions/accepted/stableblocks_bonus.cpp'),
        os.path.join(problem_dir,
                     'sol.bin'))
validator1 = py_runner(
        os.path.join(problem_dir,
                     'verify_data_in/stableblocks_verify_constraints.py'))
validator2 = cpp_runner(
        os.path.join(problem_dir,
                     'verify_data_in/stableblocks_verify_forest.cpp'),
        os.path.join(problem_dir,
                     'v2.bin'))
validator3 = cpp_runner(
        os.path.join(problem_dir,
                     'verify_data_in/stableblocks_verify_full_binary_tree.cpp'),
        os.path.join(problem_dir,
                     'v3.bin'))
validator4 = cpp_runner(
        os.path.join(problem_dir,
                     'verify_data_in/stableblocks_verify_min_dist.cpp'),
        os.path.join(problem_dir,
                     'v4.bin'))

p.add_raw_test_NO_VALIDATE('data/sample/sample_00_main', ['main', 'bonus'])
p.add_raw_test_NO_VALIDATE('data/sample/sample_00_bonus', ['bonus'])

p.add_raw_test_NO_VALIDATE('data/secret/main', ['main', 'bonus'])
p.add_raw_test_NO_VALIDATE('data/secret/main_curated', ['main', 'bonus'])

p.add_raw_test_NO_VALIDATE('data/secret/bonus', ['bonus'])
p.add_raw_test_NO_VALIDATE('data/secret/bonus_curated', ['bonus'])

# class TestFile(TestFileBase):
#     def __init__(self, gen_exe: Runner) -> None:
#         self.gen_exe = gen_exe
#         super().__init__()
#
#     @override
#     def write_test_in(self):
#         """Write the input file of this test case using print_test"""
#         p.print_test(self.gen_exe.exec())
#
#     @override
#     def validate_test_in(self, infile: str):
#         """Verify the test using an external validator."""
#         if 'main' in self.subproblems:
#             validator1.exec_file(infile)
#         validator2.exec_file(infile)
#
#     @override
#     def write_test_out(self, infile: str):
#         p.print_test(solution.exec_file(infile))

# p.add_hidden_test(
#         TestFile(
#             py_runner(
#                 os.path.join(problem_dir, 'make_data/main.py'))
#             ),
#         'main',
#         ['main']
#         )
#
# p.add_hidden_test(
#         TestFile(
#             py_runner(
#                 os.path.join(problem_dir, 'make_data/bonus.py'))
#             ),
#         'bonus',
#         ['main', 'bonus']
#         )

p.always_skip_test_gen = True
def main():
    # p.run_cli()

    # increase stack size for running solutions using heaving recursion
    # import resource
    # resource.setrlimit(resource.RLIMIT_STACK, (268435456, 268435456))

    # compile_all()
    p.init_problem()
    p.run_cli()

if __name__ == '__main__':
    main()
