import os
import random
from collections.abc import Collection, Iterable
from typing import assert_type, override, NamedTuple
from pathlib import Path

import numpy as np

from calico_lib import Problem, cpp_runner, py_runner, TestFileBase, MulticaseTestFile, Subproblem, Runner
from calico_lib.multicase import TestCaseBase
import scripts.validator_both
import submissions.accepted.circle_bonus

random.seed('asdf sure about what no what what random number generator ok CHICKEN JOCKEYYYY WATER BUCKET i dont know any brainrot um ummmmmmm umm ok so turns out you can\'t export slack data unless you\'re an admin')
np.random.seed(178236)

problem_path = Path(__file__).resolve().parent

problem = Problem(
    'circle',
    problem_path, # problem is in the same directory as the python source file
    test_sets=[
        Subproblem('main', rank=1),
        Subproblem('bonus', rank=3),
    ]
)

problem.custom_checker = 'circle_compare'
solution = py_runner(problem_path / 'submissions/accepted/circle_bonus.py')

validator_both = py_runner(os.path.join(problem_path, 'scripts/validator_both.py'))
validator_main = py_runner(os.path.join(problem_path, 'scripts/validator_main.py'))

class TestCase:
    def __init__(self, rectangle, points):
        self.rectangle = rectangle
        self.points = points

class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[TestCase]) -> None:
        self.cases = list(cases)
        super().__init__()

    @override
    def write_test_in(self):
        """Write the input file of this test case using print_test"""
        problem.print_test(len(self.cases))
        for case in self.cases:
            problem.print_test(len(case.points))
            for p in case.points:
                problem.print_test(f'{p[0]} {p[1]}')

    @override
    def validate_test_in(self, infile: str):
        validator_both.exec_file(infile)
        if 'main' in self.subproblems:
            validator_main.exec_file(infile)

    @override
    def write_test_out(self, infile: str):
        for case in self.cases:
            solver_ans = submissions.accepted.circle_bonus.solve(len(case.points), *list(zip(*case.points)))
            assert equals_epsilon(solver_ans, case.rectangle.area()), 'ur solution is wrong, idiot'
            problem.print_test(case.rectangle.area())


EPSILON = 10 ** -5


def equals_epsilon(a, b):
    return abs(a - b) < EPSILON


class Rectangle:
    def __init__(self, width, height, translation=(0, 0), rotation=0):
        self.width = width
        self.height = height
        
        self.translation_vector = np.array(translation)
        
        rotation_rad = np.radians(rotation)
        self.rotation_matrix = np.array([
            [np.cos(rotation_rad), -np.sin(rotation_rad)],
            [np.sin(rotation_rad), np.cos(rotation_rad)]
        ])

    def get_corners(self):
        corners = np.array([
            [-self.width / 2, -self.height / 2],
            [-self.width / 2,  self.height / 2],
            [ self.width / 2, -self.height / 2],
            [ self.width / 2,  self.height / 2]
        ])
        
        return corners @ self.rotation_matrix.T + self.translation_vector

    def area(self):
        return self.width * self.height

    def sample_perimeter_point(self):
        perimeter = 2 * (self.width + self.height)
        prob = random.uniform(0, perimeter)
        
        if prob < 2 * self.width:
            y = random.choice([-self.height / 2, self.height / 2])
            point = np.array([random.uniform(-self.width / 2, self.width / 2), y])
        else:
            x = random.choice([-self.width / 2, self.width / 2])
            point = np.array([x, random.uniform(-self.height / 2, self.height / 2)])
    
        # Apply rotation and translation to the sampled point
        return point @ self.rotation_matrix.T + self.translation_vector

# main samples
main_sample_test_cases = []

r = Rectangle(25, 50)
points = [[round(c, 2) if equals_epsilon(c, round(c, 2)) else c for c in r.sample_perimeter_point()] for _ in range(15)]
main_sample_test_cases.append(TestCase(r, points))

r = Rectangle(133.7 + 42.42, 777 - 69.69, ((-133.7 + 42.42) / 2, (69.69 + 777) / 2))
points = [[round(c, 2) if equals_epsilon(c, round(c, 2)) else c for c in r.sample_perimeter_point()] for _ in range(20)]
main_sample_test_cases.append(TestCase(r, points))

problem.add_sample_test(TestFile(main_sample_test_cases))


# bonus samples
bonus_sample_test_cases = []
r = Rectangle(123, 456, (789, 101), 123)
points = [r.sample_perimeter_point() for _ in range(15)]
bonus_sample_test_cases.append(TestCase(r, points))
problem.add_sample_test(TestFile(bonus_sample_test_cases), subproblems=['bonus'])


# main secret
@problem.hidden_test_generator(test_count=5)
def pure_random() -> TestFile:
    print('generating pure random hidden test for main')
    test = TestFile([])
    for _ in range(100):
        valid = False
        while not valid:
            r = Rectangle(random.uniform(1, 1000), random.uniform(1, 1000), (random.uniform(-500, 500), random.uniform(-500, 500)))
            points = [r.sample_perimeter_point() for _ in range(random.randrange(15, 1001))]

            try:
                scripts.validator_both.solve(len(points), *list(zip(*points)))
                valid = True
            except Exception as e:
                valid = False
        test.cases.append(TestCase(r, points))
    return test

@problem.hidden_test_generator(test_count=5)
def stress() -> TestFile:
    print('generating stress hidden test for main')
    test = TestFile([])
    for _ in range(100):
        valid = False
        while not valid:
            r = Rectangle(random.uniform(1, 1000), random.uniform(1, 1000), (random.uniform(-500, 500), random.uniform(-500, 500)))
            points = [r.sample_perimeter_point() for _ in range(1000)]

            try:
                scripts.validator_both.solve(len(points), *list(zip(*points)))
                valid = True
            except Exception as e:
                valid = False
        test.cases.append(TestCase(r, points))
    return test


# bonus secret
@problem.hidden_test_generator(test_count=5, subproblems=['bonus'])
def pure_random2() -> TestFile:
    print('generating pure random hidden test for bonus')
    test = TestFile([])
    for _ in range(100):
        valid = False
        while not valid:
            r = Rectangle(random.uniform(1, 1000), random.uniform(1, 1000), (random.uniform(-500, 500), random.uniform(-500, 500)), random.uniform(0, 360))
            points = [r.sample_perimeter_point() for _ in range(random.randrange(15, 1001))]

            try:
                scripts.validator_both.solve(len(points), *list(zip(*points)))
                valid = True
            except Exception as e:
                valid = False
        test.cases.append(TestCase(r, points))
    return test

@problem.hidden_test_generator(test_count=5, subproblems=['bonus'])
def stress2() -> TestFile:
    print('generating stress hidden test for bonus')
    test = TestFile([])
    for _ in range(100):
        valid = False
        while not valid:
            r = Rectangle(random.uniform(1, 1000), random.uniform(1, 1000), (random.uniform(-500, 500), random.uniform(-500, 500)), random.uniform(0, 360))
            points = [r.sample_perimeter_point() for _ in range(1000)]
            
            try:
                scripts.validator_both.solve(len(points), *list(zip(*points)))
                valid = True
            except Exception as e:
                # print(e)
                valid = False
        test.cases.append(TestCase(r, points))
    return test


def main():
    # increase stack size for running solutions using heaving recursion
    # import resource
    # resource.setrlimit(resource.RLIMIT_STACK, (268435456, 268435456))
    
    problem.init_problem()
    problem.run_cli()

    problem.create_all_tests()
    problem.create_zip()

if __name__ == '__main__':
    main()
