#!/usr/bin/env python3

# Example add problem.
# Constraints:
#   main: T <= 100, A <= 100, B <= 100
#   bonus: T <= 1e5, A <= 1e12, B <= 1e12

from typing import override
from calico_lib import Problem, py_runner, TestFileBase, MulticaseTestFile, Subproblem
from collections.abc import Collection, Iterable
from typing import NamedTuple, override
import random
import os

from calico_lib.multicase import TestCaseBase

random.seed("or give it to the next person")
p = Problem(
        'doubleit',
        os.path.dirname(__file__),
        test_sets=[
            Subproblem('main', rank=1),
            ])

class TestCase(NamedTuple):
    L: int
    P: str

solution = py_runner('submissions/accepted/doubleit.py')
validator1 = py_runner('scripts/validator_main.py')
validator2 = py_runner('scripts/validator.py')

class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[TestCase]) -> None:
        self.cases = list(cases)
        super().__init__()

    @override
    def write_test_in(self):
        """Write the input file of this test case using print_test"""
        p.print_test(len(self.cases))
        for case in self.cases:
            p.print_test(case.L)
            p.print_test(case.P)

    @override
    def validate_test_in(self, infile: str):
        """Verify the test using an external validator."""
        #if 'main' in self.subproblems:
        #    validator1.exec_file(infile)
        #validator2.exec_file(infile)

    @override
    def write_test_out(self, infile: str):
        p.print_test(solution.exec_file(infile), end ="")

# adds to all subproblems by default
p.add_sample_test(TestFile([
    TestCase(5, "TTTTT"),
    TestCase(5, "DDDDT"),
    TestCase(5, "TDDDD"),
    TestCase(5, "TDTDT"),
    TestCase(1, "T")
    ]))

def randLetter():
    letter = ["T", "D"]
    return letter[random.randint(0, 1)]

cases = []
cases.append(TestCase(1000, "T"*1000))
cases.append(TestCase(1000, "D"*1000))
cases.append(TestCase(26, "D"*25 + "T"))
cases.append(TestCase(51, "D"*25 + "T" + "D"*25 ))
cases.append(TestCase(1, "D"))

p.add_hidden_test(TestFile(cases), 'main_edge')

cases = []
for i in range(90):
    S = ""
    counter = 0
    for j in range(1000):
        next = randLetter()
        if counter >= 25:
            next = "T"
            counter = 0
        S += next
    cases.append(TestCase(1000, S))

p.add_hidden_test(TestFile(cases), 'main_random')

# # more ways to add test cases
# @p.hidden_test_generator(test_count=4)
# def pure_random() -> TestFile:
#     test = TestFile([])
#     for i in range(10):
#         test.cases.append(TestCase(random.randint(1, 100), random.randint(1, 100)))
#     return test

# @p.hidden_test_generator(test_count=4, subproblems=['bonus'])
# def pure_random2():
#     cases = (TestCase(random.randint(70, int(1e12)), random.randint(70, int(1e12))) for _ in range(100))
#     return TestFile(cases)

def main():
    p.run_cli()
    # p.create_all_tests()
    # p.create_zip()

if __name__ == '__main__':
    main()
