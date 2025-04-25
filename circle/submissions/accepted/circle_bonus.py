import math


EPSILON = 10 ** -5


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


def solve(N: int, X: list[float], Y: list[float]) -> float:
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
    
    # sanity check: points are from a rectangle, so we should have at most 4 from sides and 4 from corner cutters
    assert len(lines) <= 8
    
    # try each line as hypothesis for a side of the rectangle
    for line in lines:
        new_x_axis = line
        new_y_axis = Line.from_points((0, 0), (new_x_axis.a, new_x_axis.b))
        new_points = [[new_y_axis.signed_distance_to_point(p), new_x_axis.signed_distance_to_point(p)] for p in points]
        
        new_X, new_Y = [p[0] for p in new_points], [p[1] for p in new_points]
        
        new_min_x, new_max_x = min(new_X), max(new_X)
        new_min_y, new_max_y = min(new_Y), max(new_Y)
        
        # if hypothesis works, we have our answer
        if all(equals_epsilon(p[0], new_min_x) or equals_epsilon(p[0], new_max_x) or equals_epsilon(p[1], new_min_y) or equals_epsilon(p[1], new_max_y) for p in new_points):
            return (new_max_x - new_min_x) * (new_max_y - new_min_y)
    
    # otherwise, we're screwed lol
    assert False


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X, Y = zip(*(map(float, input().split()) for _ in range(N)))
        print(solve(N, X, Y))


if __name__ == '__main__':
    main()
