#!/usr/bin/env python3

# Example add problem.
# Constraints:
#   main: T <= 100, A <= 100, B <= 100
#   bonus: T <= 1e5, A <= 1e12, B <= 1e12

from typing import assert_type, override
from calico_lib import Problem, cpp_runner, py_runner, TestFileBase, MulticaseTestFile, Subproblem, Runner
from collections.abc import Collection, Iterable
from typing import NamedTuple, override
import random
import os
from os import path

from calico_lib.multicase import TestCaseBase

problem_dir = os.path.dirname(__file__)

random.seed('hiding_in_your_wifi')
p = Problem(
        'kumi',
        problem_dir, # problem is in the same directory as the python source file
        test_sets=[
            Subproblem('main', rank=3),
            ])

p.custom_checker = 'kumi_compare'
solution = py_runner(path.join(problem_dir, 'submissions/accepted/sol.py'))

class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[int]) -> None:
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
        assert len(self.cases) <= 30
        for i in self.cases:
            assert 1 <= i <= 1e9

    @override
    def write_test_out(self, infile: str):
        p.print_test(solution.exec_file(infile))

# adds to all subproblems by default
p.add_sample_test(TestFile([1, 2, 20]))
for i in range(1, 5):
    p.add_hidden_test(TestFile([i for i in range(i*30, i*30+30)]))

p.add_hidden_test(TestFile([1382, 19842, 38294, int(8e4 + 32)]))
p.add_hidden_test(TestFile([100000 + i for i in range(30)]))

# wolframalpha: prime numbers greater than 9e8
p.add_hidden_test(TestFile([900000011, 900000041, 900000053, 900000067, 900000083, 900000107, 900000131, 900000197, 900000209, 900000221]))

# more ways to add test cases
def pure_random(max_n: int) -> TestFile:
    cases = []
    for i in range(30):
        cases.append(random.randint(1, int(max_n)))
    return TestFile(cases)

for i in [200, 2000, 2e5, 2e6, 2e7]:
    p.add_hidden_test(pure_random(i))
    p.add_hidden_test(pure_random(i))
    p.add_hidden_test(pure_random(i))
    p.add_hidden_test(pure_random(i))

def main():
    # increase stack size for running solutions using heaving recursion
    # import resource
    # resource.setrlimit(resource.RLIMIT_STACK, (268435456, 268435456))

    # TODO: set seed
    solution.compile()
    p.init_problem()
    p.run_cli()

    # p.create_all_tests()
    # p.create_zip()

if __name__ == '__main__':
    main()
