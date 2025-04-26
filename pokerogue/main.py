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

from calico_lib.multicase import TestCaseBase

problem_dir = os.path.dirname(__file__)

MAXTURNS = 1000
MAXHP = 1000000


random.seed('pokepokeroguerogue')
p = Problem(
        'pokerogue',
        problem_dir, # problem is in the same directory as the python source file
        test_sets=[
            Subproblem('main', rank=3, time_limit=4),
            ])

p.custom_checker = 'pachinko_compare'

class TestCase(NamedTuple):
    N: int
    K: int
    A: list[int]
    B: list[int]
    C: list[int]
    D: list[int]

# solution = py_runner(os.path.join(problem_dir, 'submissions/accepted/pokerogue.py'))
solution2 = cpp_runner(os.path.join(problem_dir, 'submissions/accepted/pokerogue.cpp'),
                       os.path.join(problem_dir, 'pokerogue'))
validator = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

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
            p.print_test(*case.A)
            p.print_test(*case.B)
            p.print_test(*case.C)
            p.print_test(*case.D)

    @override
    def validate_test_in(self, infile: str):
        """Verify the test using an external validator."""
        validator.exec_file(infile)

    @override
    def write_test_out(self, infile: str):
        p.print_test(solution2.exec_file(infile))

# adds to all subproblems by default
p.add_sample_test(TestFile([
    TestCase(4,1,[7,2,3,8],[1,2,3,4],[5,4,6,29],[1,2,3,14]),
    TestCase(4,2,[2,20,200,6],[1,2,2,1],[1,40,40,6],[1,1,20,1]),
    ]))

def random_case(N: int):
    K = random.randint(1, N)
    A = [random.randint(1, MAXHP) for _ in range(N)]
    B = [random.randint(1, MAXTURNS) for _ in range(N)]
    C = [random.randint(1, MAXHP) for _ in range(N)]
    D = [random.randint(1, MAXTURNS) for _ in range(N)]
    return TestCase(N, K, A, B, C, D)

def random_case_little_difference(N: int):
    K = random.randint(1, N)
    A = [random.randint(1, MAXHP) for _ in range(N)]
    B = [random.randint(1, MAXTURNS) for _ in range(N)]
    C = [random.randint(1, 10) for i in range(N)]
    D = [B[i] + random.randint(-10,10) for i in range(N)]
    for i in range(N):
        if not 1 <= D[i] <= MAXTURNS:
            D[i] = B[i]
    return TestCase(N, K, A, B, C, D)

def random_case_bigger_answer(N: int):
    K = random.randint(1, N)
    A = [random.randint(1, MAXHP) for _ in range(N)]
    B = [random.randint(1, 10) for _ in range(N)]
    C = [random.randint(1, MAXHP) for _ in range(N)]
    D = [random.randint(1, 10) for _ in range(N)]
    return TestCase(N, K, A, B, C, D)

def random_case_small_answer(N: int):
    K = random.randint(1, N)
    A = [random.randint(1, 10) for _ in range(N)]
    B = [random.randint(1, MAXTURNS) for _ in range(N)]
    C = [random.randint(1, 10) for _ in range(N)]
    D = [random.randint(1, MAXTURNS) for _ in range(N)]
    return TestCase(N, K, A, B, C, D)

def random_test_file(fun):
    total_N = 0
    cases = []
    while len(cases) < 10 and total_N < 100000:
        N = random.randint(1, 100000 - total_N)
        total_N += N
        cases.append(fun(N))
    return TestFile(cases)

def big_test_file(fun):
    return TestFile([fun(random.randint(90000, 100000))])

for _ in range(3):
    p.add_hidden_test(random_test_file(random_case), 'random_small_cases')

for _ in range(3):
    p.add_hidden_test(random_test_file(random_case_little_difference), 'little_difference_small_cases')

for _ in range(3):
    p.add_hidden_test(random_test_file(random_case_bigger_answer), 'big_answer_small_cases')

for _ in range(3):
    p.add_hidden_test(random_test_file(random_case_small_answer), 'small_answer_small_cases')

for _ in range(3):
    p.add_hidden_test(big_test_file(random_case), 'random_one_case')

for _ in range(3):
    p.add_hidden_test(big_test_file(random_case_little_difference), 'little_difference_one_case')

for _ in range(3):
    p.add_hidden_test(big_test_file(random_case_bigger_answer), 'big_answer_one_case')

for _ in range(3):
    p.add_hidden_test(big_test_file(random_case_small_answer), 'small_answer_one_case')


def main():

    # increase stack size for running solutions using heaving recursion
    # import resource
    # resource.setrlimit(resource.RLIMIT_STACK, (268435456, 268435456))

    solution2.compile()
    p.init_problem()
    # p.create_all_tests()
    # p.create_zip()
    p.run_cli()

if __name__ == '__main__':
    main()
