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
import os

problem_dir = os.path.dirname(__file__)

p = Problem["TestFile"](
        'stickdrift',
        os.path.dirname(__file__),
        test_sets=[
            Subproblem('main', rank=3),
            ])

class TestCase(NamedTuple):
    N: int
    M: int
    S: str
    G: list

solution = py_runner(os.path.join(problem_dir, 'submissions/accepted/stickdrift_translated.py'))
# validator1 = py_runner(os.path.join('scripts/validator_main.py'))
# validator2 = py_runner(os.path.join('scripts/validator.py'))

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
            p.print_test(case.S)
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
        p.print_test(solution.exec_file(infile), end='')

# adds to all subproblems by default
p.add_sample_test(TestFile([ #Todo actually make sample tests
    TestCase(2, 2, "UUD", [
        [1, 2],
        [3, 4]
    ]),
    TestCase(1, 4, "L", [
        [4, 1, 2, 3]
    ]),
    TestCase(2, 3, "UD", [
        [1, 3, 5],
        [2, 4, 6]
    ]),
    TestCase(3, 3, "RRLLUUDD", [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]),
    TestCase(1, 1, "UDLR", [
        [1]
    ])
    ]))

letters = ["U", "D", "L", "R"]
cases = []
total = 0
while (True):
    N = random.randint(1, 100)
    M = random.randint(1, 100)
    if (total + (N * M) > 180000):
        break
    numbers = list(range(1, N * M + 1))
    random.shuffle(numbers)
    G = []
    temp = []
    count = 0
    for num in numbers:
        temp.append(num)
        count += 1
        if (count == M):
            # print()
            G.append(temp)
            temp = []
            count = 0
    randSeq = [0, 1, 2, 3]
    random.shuffle(randSeq)
    S = ""
    for i in randSeq:
        S += letters[i]
    cases.append(TestCase(N, M, S, G))
    total += N * M

p.add_hidden_test(TestFile(cases), 'secret_01_main_random')
    
cases = []
temp = []
for i in range(1, 10001):
    temp.append(i)

cases.append(TestCase(1, 10000, "L", [temp]))

temp = []

for i in range(1, 10001):
    temp.append([i])

cases.append(TestCase(10000, 1, "U", temp))

p.add_hidden_test(TestFile(cases), 'secret_02_main_edge')

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