#!/usr/bin/env python3

from collections.abc import Collection, Iterable
from typing import override
from calico_lib import Problem, py_runner, TestFileBase, MulticaseTestFile
import random

from calico_lib.multicase import TestCaseBase

p = Problem["TestFile"](
        'add',
        test_sets=['main', 'bonus'])

class TestCase(TestCaseBase):
    def __init__(self, X: int, Y: int) -> None:
        self.X = X
        self.Y = Y
        super().__init__()

    def write_test_in(self):
        """Write the input file of this test case using print_test"""
        p.print_test(self.X, self.Y)

    def verify_case(self, test_sets):
        assert 1 <= self.X <= 10000
        if 'main' in test_sets:
            assert self.X <= 100

solution = py_runner('submissions/accepted/add_arbitrary.py')

class TestFile(MulticaseTestFile):
    problem = p

    @override
    def validate_test_in(self, infile: str):
        """Verify the test using an external validator."""

        """Verify the test from test data (bad practice, prefer verifying the infile)."""
        total = 0
        assert 1 <= len(self.cases) <= 100, f"Got {len(self.cases)} cases"
        for case in self.cases:
            assert isinstance(case, TestCase)
            case.verify_case(self.subproblems)
            total += case.X + case.Y
        assert total <= 1e6

    @override
    def write_test_out(self, infile: str):
        p.print_test(solution.exec_file(infile))

p.add_sample_test(TestFile([
    TestCase(4, 7),
    TestCase(1, 23),
    TestCase(9, 8),
    TestCase(1, 1),
    ]))

@p.hidden_test_generator(test_count=5, subproblems=['main', 'bonus'])
def pure_random() -> TestFile:
    test = TestFile()
    for i in range(100):
        test.cases.append(TestCase(random.randint(1, 100), random.randint(1, 100)))
    return test

@p.hidden_test_generator(test_count=5, subproblems=['bonus'])
def pure_random2():
    cases = (TestCase(random.randint(70, 10000), random.randint(70, 10000)) for _ in range(5))
    return TestFile(cases)

def main():
    # p.run_cli()
    p.create_all_tests()
    # p.create_zip()

main()
