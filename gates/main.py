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

random.seed('123456')
p = Problem(
        'gates',
        problem_dir, # problem is in the same directory as the python source file
        test_sets=[
            Subproblem('main', rank=3),
            Subproblem('bonus', rank=3),
            ])

class TestCase(NamedTuple):
    N: int
    lst: list 

solution = py_runner(
        path.join(problem_dir, "submissions/accepted/solution.py"))
solution2 = py_runner(
        path.join(problem_dir, 'submissions/time_limit_exceeded/brute_force.py'))
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
            p.print_test(case.N)
            p.print_test(' '.join(str(x) for x in case.lst))

    @override
    def validate_test_in(self, infile: str):
        """Verify the test using an external validator."""
        if 'main' in self.subproblems:
            validator1.exec_file(infile)
        validator2.exec_file(infile)

    @override
    def write_test_out(self, infile: str):
        p.print_test(solution.exec_file(infile))

# adds to all subproblems by default
p.add_sample_test(TestFile([
    TestCase(2, [1, 1]),
    TestCase(3, [1, 0, 1]),
    ]))

cases = []
for i in range(10):
    lst = []
    for j in range(5):
        lst.append(random.randint(0, 1))
    cases.append(TestCase(5, lst))

p.add_hidden_test(TestFile(cases), 'small')
    
# more ways to add test cases
@p.hidden_test_generator(test_count=4)
def pure_random() -> TestFile:
    test = TestFile([])
    for i in range(1):
        n = random.randint(950, 1000)
        lst = []
        for j in range(n):
            lst.append(random.randint(0, 1))
        test.cases.append(TestCase(n, lst))
    return test

@p.hidden_test_generator(test_count=4, subproblems=['bonus'])
def pure_random2():
    test = TestFile([])
    for i in range(2):
        n = random.randint(80000, 100000)
        lst = []
        for j in range(n):
            lst.append(random.randint(0, 1))
        test.cases.append(TestCase(n, lst))
    return test

def main():
    # increase stack size for running solutions using heaving recursion
    # import resource
    # resource.setrlimit(resource.RLIMIT_STACK, (268435456, 268435456))

    # TODO: set seed
    p.run_cli()

    # p.init_problem()
    # p.create_all_tests()
    # p.create_zip()

if __name__ == '__main__':
    main()
