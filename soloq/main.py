#!/usr/bin/env python3

# Example add problem.
# Constraints:
#   main: T <= 100, A <= 100, B <= 100
#   bonus: T <= 1e5, A <= 1e12, B <= 1e12

MAXWORDS = 10
MAXWORDSIZE = 10

from typing import override
from calico_lib import Problem, cpp_runner, py_runner, TestFileBase, MulticaseTestFile, Subproblem, Runner
from collections.abc import Collection, Iterable
from typing import NamedTuple, override
import random
import os

from calico_lib.multicase import TestCaseBase

problem_dir = os.path.dirname(__file__)

p = Problem(
        'soloq',
        problem_dir, # problem is in the same directory as the python source file
        test_sets=[
            Subproblem('main', rank=4),
        ])

class TestCase(NamedTuple):
    N: int
    K: int
    X: int
    Y: int
    W1: int
    W2: int
    L1: int
    L2: int
    S: list[str]

solution = py_runner(os.path.join(problem_dir, 'submissions/accepted/soloq.py'))
solution2 = cpp_runner(os.path.join(problem_dir, 'submissions/accepted/soloq.cpp'), 'soloq')
validator1 = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[TestCase]) -> None:
        self.cases = list(cases)
        super().__init__()

    @override
    def write_test_in(self):
        """Write the input file of this test case using print_test"""
        p.print_test(len(self.cases))
        for case in self.cases:
            p.print_test(case.N, case.K)
            p.print_test(case.X, case.Y, case.W1, case.W2, case.L1, case.L2)
            for s in case.S:
                p.print_test(s)

    @override
    def validate_test_in(self, infile: str):
        """Verify the test using an external validator."""
        if 'main' in self.subproblems:
            validator1.exec_file(infile)

    @override
    def write_test_out(self, infile: str):
        p.print_test(solution2.exec_file(infile))

# adds to all subproblems by default
p.add_sample_test(TestFile([
    TestCase(10, 2, 30, 28, 1, 2, 1, 2, ["L", "W"]),
    TestCase(int(1e9 + 8), 6, 36, 34, 4, 7, 29, 351, ["L", "W", "LL", "LW", "WL", "WW"]),
    # TestCase(5,3,10,5,1,2,1,2,["WWLW", "LW", "LWLW"]),
    ]))



def generate_random_string(l: int):
    return ''.join(['W' if random.randint(0,1) == 0 else 'L' for _ in range(l)])

def generate_random_case(k: int):
    N = random.randint(int(1e10), int(1e12))
    X = random.randint(0, int(1e9))
    Y = random.randint(0, int(1e9))
    W1 = random.randint(0, int(1e9))
    W2 = random.randint(W1 if W1 != 0 else 1, int(1e9))
    L1 = random.randint(0, int(1e9))
    L2 = random.randint(L1 if L1 != 0 else 1, int(1e9))
    S = [generate_random_string(random.randint(1, MAXWORDSIZE)) for _ in range(k)]
    return TestCase(N, k, X, Y, W1, W2, L1, L2, S)

def generate_small_random_test_file():
    nums, s = [], 0
    while s < MAXWORDS and len(nums) < 10:
        nums.append(random.randint(1, MAXWORDS - s))
        s += nums[-1]
    return TestFile([generate_random_case(k) for k in nums])

def generate_big_random_test_file():
    return TestFile([generate_random_case(MAXWORDS)])

for _ in range(5):
    p.add_hidden_test(generate_small_random_test_file(), 'small_random')

for _ in range(5):
    p.add_hidden_test(generate_big_random_test_file(), 'big_random')

# todo: edge the cases

def main():
    # p.run_cli()

    # increase stack size for running solutions using heaving recursion
    # import resource
    # resource.setrlimit(resource.RLIMIT_STACK, (268435456, 268435456))

    # TODO: set seed
    random.seed('add_seed_600')
    solution2.compile()
    p.init_problem()
    p.create_all_tests()
    p.create_zip()

if __name__ == '__main__':
    main()
