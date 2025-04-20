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

p = Problem(
        'tournament',
        problem_dir, # problem is in the same directory as the python source file
        test_sets=[
            Subproblem('main', rank=1),
            ])

class TestCase(NamedTuple):
    N: int
    C: list
    P: list

solution = py_runner(os.path.join(problem_dir, 'submissions/accepted/tournament.py'))
#solution2 = cpp_runner(os.path.join(problem_dir, 'submissions/accepted/add_int.cpp'), 'add_int')
#validator1 = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))
#validator2 = py_runner(os.path.join(problem_dir, 'scripts/validator.py'))

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
            temp = ""
            for s in case.C:
                temp = temp + " " + s
            p.print_test(temp.strip())
            temp = ""
            for num in case.P:
                temp = temp + " " + str(num)
            p.print_test(temp.strip())

    @override
    def validate_test_in(self, infile: str):
        """Verify the test using an external validator."""
        #if 'main' in self.subproblems:
        #    validator1.exec_file(infile)
        #validator2.exec_file(infile)

    @override
    def write_test_out(self, infile: str):
        p.print_test(solution.exec_file(infile), end='')

# adds to all subproblems by default
p.add_sample_test(TestFile([
    TestCase(4, 
             ["TralaleroTralala", "BombardiroCrocodilo", "BrrBrrPatapim", "LiriliLarila"],
             [42750, 31645, 12455, 12455]),
    TestCase(3,
             ["TungTungTungTungTungTungSahur", "CappuccinoAssassino", "BigBen"],
             [523530, 500250, 999999999]),
    TestCase(2, 
             ["TralaleroTralala", "TungTungTungTungTungTungSahur"],
             [100000, 100000]),
    TestCase(26, 
             ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
             [1, 26, 2, 25, 3, 24, 4, 23, 5, 22, 6, 21, 7, 20, 8, 19, 9, 18, 10, 17, 11, 16, 12, 15, 13, 14]),
    TestCase(1,
             ["LaVaccaSaturnoSaturnita"],
             [12510])
    ]))

Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
usedNames = {"A"}

def randName():
    while True:
        l = random.randint(1, 10)
        name = ""
        for _ in range(l):
            letter = random.randint(0, 25)
            name += Alphabet[letter]
        if (not name in usedNames):
            usedNames.add(name)
            return name
        

def randPower():
    return random.randint(0, 1000000)

cases = []
for i in range(95):
    N = 1000
    C = []
    P = []
    for _ in range(N):
        C.append(randName())
        P.append(randPower())
    cases.append(TestCase(N, C, P))


p.add_hidden_test(TestFile(cases), 'secret_01_main_random')
    
# more ways to add test cases
#@p.hidden_test_generator(test_count=4)
#def pure_random() -> TestFile:
#    test = TestFile([])
#    for i in range(10):
#       test.cases.append(TestCase(random.randint(1, 100), random.randint(1, 100)))
#    return test

#@p.hidden_test_generator(test_count=4, subproblems=['bonus'])
#def pure_random2():
#    cases = (TestCase(random.randint(70, int(1e12)), random.randint(70, int(1e12))) for _ in range(100))
#    return TestFile(cases)

def main():
    # p.run_cli()

    # increase stack size for running solutions using heaving recursion
    # import resource
    # resource.setrlimit(resource.RLIMIT_STACK, (268435456, 268435456))

    # TODO: set seed
    random.seed('tournament')
    p.init_problem()
    # p.create_all_tests()
    # p.create_zip()
    p.run_cli()

if __name__ == '__main__':
    main()
