import math


EPSILON = 10 ** -9


def equals_epsilon(a, b):
    return abs(a - b) < EPSILON


class Plane:
    """
    Represents a plane in 3D space using ax + by + cz + d = 0.
    Additionally guarantees that ||(a, b, c)|| = 1.
    """
    
    @staticmethod
    def from_points(p1, p2, p3):
        a = (p2[1] - p1[1]) * (p3[2] - p1[2]) - (p3[1] - p1[1]) * (p2[2] - p1[2])
        b = (p3[0] - p1[0]) * (p2[2] - p1[2]) - (p2[0] - p1[0]) * (p3[2] - p1[2])
        c = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
        d = (-a * p1[0] - b * p1[1] - c * p1[2])
        return Plane(a, b, c, d)
    
    def __init__(self, a, b, c, d):
        norm = math.sqrt(a * a + b * b + c * c)
        
        self.a = a / norm
        self.b = b / norm
        self.c = c / norm
        self.d = d / norm
    
    def signed_distance_to_point(self, p):
        return self.a * p[0] + self.b * p[1] + self.c * p[2] + self.d


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
    
    def signed_distance_to_point(self, p):
        return self.a * p[0] + self.b * p[1] + self.c
    
    def __eq__(self, other):
        return equals_epsilon(self.a, other.a) and equals_epsilon(self.b, other.b) and equals_epsilon(self.c, other.c)


def center(points):
    """TODO write docstring"""
    mu_X, mu_Y = sum(p[0] for p in points) / len(points), sum(p[1] for p in points) / len(points)
    return [[p[0] - mu_X, p[1] - mu_Y] for p in points]


def solve(N: int, X: list[float], Y: list[float], Z: list[float]) -> float:
    # reorganize as list of points for easier use
    points = list(zip(X, Y, Z))
    
    while True:
        sample = random.sample(points, 3)
        
        print(sample)
        visualize_debug(r, sample)
        
        first_plane = Plane.from_points(*sample)
        signed_distances = [first_plane.signed_distance_to_point(P) for P in points]
        max_signed_distance, min_signed_distance = max(signed_distances), min(signed_distances)
        if not equals_epsilon(max_signed_distance, 0) and not equals_epsilon(min_signed_distance, 0):
            continue # plane isn't tangent to the prism

        break


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X, Y, Z = zip(*(map(float, input().split()) for _ in range(N)))
        print(solve(N, X, Y, Z))


if __name__ == '__main__':
    main()
