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

random.seed('add_seed_600')
p = Problem(
        'add',
        problem_dir, # problem is in the same directory as the python source file
        test_sets=[
            Subproblem('main', rank=1),
            Subproblem('bonus', rank=2, time_limit=4, mem_limit=1_000_000_000),
            ])

class TestCase(NamedTuple):
    X: int
    Y: int

solution = py_runner(path.join(problem_dir, 'submissions/accepted/add_arbitrary.py'))
solution2 = cpp_runner(
        path.join(problem_dir, 'submissions/accepted/add_int.cpp'),
        path.join(problem_dir, 'add_int.bin'))
validator1 = py_runner(path.join(problem_dir, 'scripts/validator_main.py'))
validator2 = py_runner(path.join(problem_dir, 'scripts/validator.py'))

class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[TestCase]) -> None:
        self.cases = list(cases)
        super().__init__()

    @override
    def write_test_in(self):
        """Write the input file of this test case using print_test"""
        p.print_test(len(self.cases))
        for case in self.cases:
            p.print_test(case.X, case.Y)

    @override
    def validate_test_in(self, infile: str):
        """Verify the test using an external validator."""
        if 'main' in self.subproblems:
            validator1.exec_file(infile)
        validator2.exec_file(infile)

    @override
    def write_test_out(self, infile: str):
        p.print_test(solution2.exec_file(infile))

# adds to all subproblems by default
p.add_sample_test(TestFile([
    TestCase(4, 7),
    TestCase(1, 23),
    TestCase(9, 8),
    TestCase(1, 1),
    ]))

cases = []
for i in range(80):
    cases.append(TestCase(i+1, 80-i))

p.add_hidden_test(TestFile(cases), 'iota')
    
cases = []
for i in range(100):
    cases.append(TestCase(i+1, 10000-i))

p.add_hidden_test(TestFile(cases), 'iota', subproblems=['bonus'])

# more ways to add test cases
@p.hidden_test_generator(test_count=4)
def pure_random() -> TestFile:
    test = TestFile([])
    for i in range(10):
        test.cases.append(TestCase(random.randint(1, 100), random.randint(1, 100)))
    return test

@p.hidden_test_generator(test_count=4, subproblems=['bonus'])
def pure_random2():
    cases = (TestCase(random.randint(70, int(1e12)), random.randint(70, int(1e12))) for _ in range(100))
    return TestFile(cases)

def main():
    # increase stack size for running solutions using heaving recursion
    # import resource
    # resource.setrlimit(resource.RLIMIT_STACK, (268435456, 268435456))

    # TODO: set seed
    solution2.compile()
    p.run_cli()

    # p.init_problem()
    # p.create_all_tests()
    # p.create_zip()

if __name__ == '__main__':
    main()
