import math


EPSILON = 10 ** -8


def equals_epsilon(a, b):
    return abs(a - b) < EPSILON


class Line:
    """
    Represents a line in 2D space using ax + by + c = 0.
    Additionally guarantees that ||(a, b)|| = 1.
    """
    
    @staticmethod
    def from_points(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        
        a = y1 - y2
        b = x2 - x1
        c = x1 * y2 - x2 * y1
        
        return Line(a, b, c)
    
    def __init__(self, a, b, c):
        norm = math.sqrt(a * a + b * b)
        
        self.a = a / norm
        self.b = b / norm
        self.c = c / norm
    
    def signed_distance_to_point(self, point):
        return self.a * point[0] + self.b * point[1] + self.c
    
    def __eq__(self, other):
        return equals_epsilon(self.a, other.a) and equals_epsilon(self.b, other.b) and equals_epsilon(self.c, other.c)

        
def solve(N: int, X: list[float], Y: list[float]) -> int:
    assert 15 <= N <= 1000
    assert N == len(X) == len(Y)
    
    assert all(-1000 <= x <= 1000 for x in X)
    assert all(-1000 <= y <= 1000 for y in Y)
    
    # reorganize as list of points for easier use
    points = list(zip(X, Y))
    
    # radially sort points around the approximate center
    mu_X, mu_Y = sum(X) / N, sum(Y) / N
    points.sort(key=lambda p: math.atan2(p[1] - mu_Y, p[0] - mu_X))
    
    # collect all unique lines from radially adjacent points
    lines = []
    for i in range(-1, N - 1):
        l = Line.from_points(points[i], points[i + 1])
        if l not in lines:
            lines.append(l)
    
    # sanity check: points are from a rectangle, so we should at least 4 lines for each side, then at most another 4 for corner cutters
    assert 4 <= len(lines) <= 8
    
    answers = []
    unique_side_lengths = []
    
    # must be axis-aligned for main
    new_min_x, new_max_x = min(X), max(X)
    new_min_y, new_max_y = min(Y), max(Y)
    if all(equals_epsilon(p[0], new_min_x) or equals_epsilon(p[0], new_max_x) or equals_epsilon(p[1], new_min_y) or equals_epsilon(p[1], new_max_y) for p in points):
        width = (new_max_x - new_min_x)
        height = (new_max_y - new_min_y)
        curr_answer = width * height
        
        if not any(equals_epsilon(curr_answer, a) for a in answers):
            answers.append(curr_answer)
        if not any(equals_epsilon(width, s) for s in unique_side_lengths):
            unique_side_lengths.append(width)
        if not any(equals_epsilon(height, s) for s in unique_side_lengths):
            unique_side_lengths.append(height)
    
    # there should be exactly 1 answer
    assert len(answers) == 1
    assert len(unique_side_lengths) <= 2
    
    answer = answers[0]
    
    assert 1 <= answer <= 10 ** 6
    assert all(1 <= s <= 10 ** 3 for s in unique_side_lengths)


def main():
    T = int(input())
    assert 1 <= T <= 100
    for _ in range(T):
        N = int(input())
        X, Y = zip(*(map(float, input().split()) for _ in range(N)))
        solve(N, X, Y)


if __name__ == '__main__':
    main()
