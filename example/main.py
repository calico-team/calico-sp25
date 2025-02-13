#!/usr/bin/env python3

from collections.abc import Collection, Iterable
from typing import override
from calico_lib import Problem, py_runner, TestFileBase
import random

class TestCase():
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

solution = py_runner('submissions/accepted/add_sol.py')

# TODO: move this to library
class Test(TestFileBase):

    def __init__(self, cases: Iterable[TestCase]|None = None) -> None:
        if cases is None:
            self.cases: list[TestCase] = []
        else:
            self.cases = list(cases)
        super().__init__()

    # @override
    # def get_subproblems(self) -> list[str]:
    #     return ['bonus']

    @override
    def write_test_in(self):
        p.print_test(len(self.cases))
        for case in self.cases:
            case.write_test_in()
        return super().write_test_in()

    @override
    def write_test_out(self, infile: str):
        p.print_test(solution.exec_file(infile))

    @override
    def validate_test_in(self, infile: str):
        """Verify the test using assert (not recommended, consider properly
        verifying by reading the file)."""
        total = 0
        assert 1 <= len(self.cases) <= 100, f"Got {len(self.cases)} cases"
        for case in self.cases:
            case.verify_case(self.subproblems)
            total += case.X + case.Y
        assert total <= 1e6

p = Problem[Test](
        'add',
        test_sets=['main', 'bonus'])

p.add_sample_test(Test([
    TestCase(4, 7),
    TestCase(1, 23),
    TestCase(9, 8),
    TestCase(1, 1),
    ]))

@p.hidden_test_generator(test_count=5, subproblems=['main', 'bonus'])
def pure_random() -> Test:
    test = Test()
    for i in range(100):
        test.cases.append(TestCase(random.randint(1, 100), random.randint(1, 100)))
    return test

@p.hidden_test_generator(test_count=5, subproblems=['bonus'])
def pure_random2():
    cases = (TestCase(random.randint(70, 10000), random.randint(70, 10000)) for _ in range(5))
    return Test(cases)

def main():
    # p.run_cli()
    p.create_all_tests()
    # p.create_zip()

main()
