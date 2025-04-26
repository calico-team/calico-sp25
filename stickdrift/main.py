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

random.seed('tokyo drift~~')
p = Problem(
        'stickdrift',
        os.path.dirname(__file__),
        test_sets=[
            Subproblem('main', rank=2),
            Subproblem('bonus', rank=3),
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

# Python program to create a spiral matrix from given array
# Credit to https://www.geeksforgeeks.org/form-a-spiral-matrix-from-the-given-array/
def spiralFill(n, m, arr):
    res = [[-1] * m for _ in range(n)]

    # Change in row index for each direction
    dr = [0, 1, 0, -1]

    # Change in column index for each direction
    dc = [1, 0, -1, 0]

    # Initial direction index (0 corresponds to 'right')
    dirIdx = 0

    index = 0
    r, c = 0, 0

    while index < len(arr):
        res[r][c] = arr[index]
        index += 1

        # The next cell indices
        newR = r + dr[dirIdx]
        newC = c + dc[dirIdx]

        # Check if the next cell is out of bounds or
        # it is already filled, then update the direction
        if newR < 0 or newR == n or newC < 0 or newC == m \
        						 or res[newR][newC] != -1:
            dirIdx = (dirIdx + 1) % 4

            newR = r + dr[dirIdx]
            newC = c + dc[dirIdx]

        # Update the cells
        r = newR
        c = newC

    return res

#Main Tests

cases = []
total = 0
while (True):
    N = random.randint(5, 20)
    M = random.randint(5, 20)
    if (total + (N * M) > 1000):
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
for i in range(1, 501):
    temp.append(i)

cases.append(TestCase(1, 500, "L", [temp]))

temp = []

for i in range(1, 501):
    temp.append([i])

cases.append(TestCase(500, 1, "U", temp))

p.add_hidden_test(TestFile(cases), 'secret_02_main_edgeLine')

cases = []

N = 30
M = 30
numbers = list(range(1, N * M + 1))
temp = spiralFill(N, M, numbers)

cases.append(TestCase(N, M, "UDLR", temp))

N = 10
M = 10
numbers = list(range(1, N * M + 1))
temp = spiralFill(N, M, numbers)

cases.append(TestCase(N, M, "UDLR", temp))

p.add_hidden_test(TestFile(cases), 'secret_03_main_edgeSpiral')

#Bonus Tests


total = 0
cases = []
while (True):
    N = random.randint(50, 200)
    M = random.randint(50, 200)
    if (total + (N * M) > 200000):
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

p.add_hidden_test(TestFile(cases), 'secret_01_bonus_random', ['bonus'])
    
cases = []
temp = []
for i in range(1, 100001):
    temp.append(i)

cases.append(TestCase(1, 100000, "L", [temp]))

temp = []

for i in range(1, 100001):
    temp.append([i])

cases.append(TestCase(100000, 1, "U", temp))

p.add_hidden_test(TestFile(cases), 'secret_02_bonus_edgeLine', ['bonus'])

cases = []

N = 1000
M = 100
numbers = list(range(1, N * M + 1))
temp = spiralFill(N, M, numbers)

cases.append(TestCase(N, M, "UDLR", temp))

N = 10000
M = 10
numbers = list(range(1, N * M + 1))
temp = spiralFill(N, M, numbers)

cases.append(TestCase(N, M, "UDLR", temp))

p.add_hidden_test(TestFile(cases), 'secret_03_bonus_edgeSpiral', ['bonus'])

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
    p.run_cli()
    # p.create_all_tests()
    # p.create_zip()

if __name__ == '__main__':
    main()
