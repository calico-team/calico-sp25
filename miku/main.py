#!/usr/bin/env python3

# Example add problem.
# Constraints:
#   main: T <= 100, A <= 100, B <= 100
#   bonus: T <= 1e5, A <= 1e12, B <= 1e12

from typing import override
from calico_lib import Problem, cpp_runner, py_runner, TestFileBase, MulticaseTestFile, Subproblem, Runner
from collections.abc import Collection, Iterable
from typing import NamedTuple, override
import random
import os
from os import path

from calico_lib.multicase import TestCaseBase

problem_dir = os.path.dirname(__file__)

p = Problem(
        'miku',
        problem_dir, # problem is in the same directory as the python source file
        test_sets=[
            Subproblem('main', rank=2),
            ])

solution = cpp_runner(path.join(problem_dir, 'submissions/accepted/solution.cpp'), path.join(problem_dir, 'sol.bin'))

class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[str]) -> None:
        self.cases = list(cases)
        super().__init__()

    @override
    def write_test_in(self):
        """Write the input file of this test case using print_test"""
        p.print_test(len(self.cases))
        for case in self.cases:
            p.print_test(case)

    @override
    def validate_test_in(self, infile: str):
        """Verify the test using an external validator."""
        # validator1.exec_file(infile)

    @override
    def write_test_out(self, infile: str):
        p.print_test(solution.exec_file(infile))

# adds to all subproblems by default
p.add_sample_test(TestFile([
    "owwo",
    "oyowuoxuwo"
]))

import string

MAX_N = 1000

# more ways to add test cases
@p.hidden_test_generator(test_count=1)
def pure_random() -> TestFile:
    test = TestFile([])
    for i in range(10):
        test.cases.append(''.join(random.choice(string.ascii_lowercase) for i in range(MAX_N)))
    for i in range(10):
        test.cases.append(''.join(random.choice('ooouuuuwwxyz') for i in range(MAX_N)))
    for i in range(10):
        test.cases.append(''.join(random.choice('o'*100+'w') for i in range(MAX_N)))
    return test

def main():
    # increase stack size for running solutions using heaving recursion
    # import resource
    # resource.setrlimit(resource.RLIMIT_STACK, (268435456, 268435456))

    # TODO: set seed
    random.seed('teto_teto_teto_teto_teto_teto')
    solution.compile()
    p.init_problem()
    p.run_cli()

    # p.create_all_tests()
    # p.create_zip()

if __name__ == '__main__':
    main()
