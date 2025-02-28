#!/usr/bin/env python3

# Example add problem.
# Constraints:
#   main: T <= 100, A <= 100, B <= 100
#   bonus: T <= 1e5, A <= 1e12, B <= 1e12

from typing import override
from calico_lib import Problem, py_runner, TestFileBase, Subproblem
from collections.abc import Collection, Iterable
from typing import NamedTuple, override
import random

p = Problem["TestFile"](
        'unlockmanifolds',
        test_sets=[
            Subproblem('main', rank=2),
            ])

class TestCase(NamedTuple):
    N: int
    M: int
    G: list

solution = py_runner('unlockmanifolds/submissions/accepted/unlockmanifolds.py')
# validator1 = py_runner('scripts/validator_main.py')
# validator2 = py_runner('scripts/validator.py')

class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[TestCase]) -> None:
        self.cases = list(cases)
        super().__init__()

    @override
    def write_test_in(self):
        """Write the input file of this test case using print_test"""
        p.print_test(len(self.cases))
        for case in self.cases:
            p.print_test(case.N, case.M)
            for line in case.G:
                temp = ""
                for num in line:
                    temp = temp + " " + str(num)
                p.print_test(temp.strip())

    @override
    def validate_test_in(self, infile: str):
        """Verify the test using an external validator."""
        # if 'main' in self.subproblems:
        #     validator1.exec_file(infile)
        # validator2.exec_file(infile)

    @override
    def write_test_out(self, infile: str):
        p.print_test(solution.exec_file(infile))

# adds to all subproblems by default
p.add_sample_test(TestFile([
    TestCase(3, 3, [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]),
    TestCase(4, 2, [
        [1, 3],
        [5, 7],
        [2, 4],
        [6, 8]
    ]),
    ]))

cases = []
for i in range(10):
    N = random.randint(1, 200)
    M = random.randint(1, 200)
    numbers = list(range(1, N * M))
    random.shuffle(numbers)
    G = []
    temp = []
    count = 0
    for num in numbers:
        temp.append(num)
        if (count == M):
            G.append(temp)
            temp = []
            count = 0
    cases.append(TestCase(N, M, G))

p.add_hidden_test(TestFile(cases), 'secret_01_main_random.in')
    
#cases = []
#for i in range(100):
#    cases.append(TestCase(i+1, 10000-i))

#p.add_hidden_test(TestFile(cases), 'iota', subproblems=['bonus'])

# more ways to add test cases
#@p.hidden_test_generator(test_count=4)
#def pure_random() -> TestFile:
#    test = TestFile([])
#    for i in range(10):
#        test.cases.append(TestCase(random.randint(1, 100), random.randint(1, 100)))
#    return test

#@p.hidden_test_generator(test_count=4, subproblems=['bonus'])
#def pure_random2():
#    cases = (TestCase(random.randint(70, int(1e12)), random.randint(70, int(1e12))) for _ in range(100))
#    return TestFile(cases)

def main():
    # p.run_cli()
    p.create_all_tests()
    p.create_zip()

if __name__ == '__main__':
    main()
