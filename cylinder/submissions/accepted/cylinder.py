import math
import random


random.seed(1337)
EPSILON = 10 ** -5


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
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        
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
    mu_X, mu_Y, mu_Z = sum(p[0] for p in points) / len(points), sum(p[1] for p in points) / len(points), sum(p[2] for p in points) / len(points)
    return [[p[0] - mu_X, p[1] - mu_Y, p[2] - mu_Y] for p in points]


def project(points, plane):
    distances = [plane.signed_distance_to_point(p) for p in points]
    return [[p[0] - d * plane.a, p[1] - d * plane.b, p[2] - d * plane.c] for p, d in zip(points, distances)]


def rotate_plane_points_to_xy_plane(points):
    plane = Plane.from_points(*points[:3])

    a, b, c = plane.a, plane.b, plane.c

    # Rotation axis is cross product of (a,b,c) and (0,0,1)
    rx = b
    ry = -a
    rz = 0
    r_mag = math.sqrt(rx * rx + ry * ry)
    
    # ayo this shits alr rotated perfectly so we done
    if r_mag == 0:
        return points
    
    rx /= r_mag
    ry /= r_mag

    # Angle between (a,b,c) and (0,0,1)
    cos_theta = c
    sin_theta = math.sqrt(1 - c * c)

    # Rodrigues' rotation formula
    K = [
        [0, -rz, ry],
        [rz, 0, -rx],
        [-ry, rx, 0]
    ]

    def mat_mult(A, B):
        return [
            [
                sum(A[i][k] * B[k][j] for k in range(3))
                for j in range(3)
            ]
            for i in range(3)
        ]

    I = [[1 if i==j else 0 for j in range(3)] for i in range(3)]
    K2 = mat_mult(K, K)

    R = [
        [
            I[i][j] + sin_theta * K[i][j] + (1 - cos_theta) * K2[i][j]
            for j in range(3)
        ]
        for i in range(3)
    ]
    
    rotated_points = []
    for p in points:
        rx = R[0][0]*p[0] + R[0][1]*p[1] + R[0][2]*p[2]
        ry = R[1][0]*p[0] + R[1][1]*p[1] + R[1][2]*p[2]
        rz = R[2][0]*p[0] + R[2][1]*p[1] + R[2][2]*p[2]
        rotated_points.append((rx, ry, rz))
    return rotated_points


def rectangle_area(points):
    # radially sort points around the approximate center
    mu_X, mu_Y = sum(p[0] for p in points) / len(points), sum(p[1] for p in points) / len(points)
    points.sort(key=lambda p: math.atan2(p[1] - mu_Y, p[0] - mu_X))
    
    # collect all unique lines from radially adjacent points
    lines = []
    for i in range(-1, len(points) - 1):
        l = Line.from_points(points[i], points[i + 1])
        if l not in lines:
            lines.append(l)
    
    # try each line as hypothesis for a side of the rectangle
    for line in lines[:8]: # if it is from a rectangle, we should be able to identify it in 8 or less for sure
        new_x_axis = line
        new_y_axis = Line.from_points((0, 0), (new_x_axis.a, new_x_axis.b))
        new_points = [[new_y_axis.signed_distance_to_point(p), new_x_axis.signed_distance_to_point(p)] for p in points]
        
        new_X, new_Y = [p[0] for p in new_points], [p[1] for p in new_points]
        
        new_min_x, new_max_x = min(new_X), max(new_X)
        new_min_y, new_max_y = min(new_Y), max(new_Y)
        
        # if hypothesis works, we have our answer
        if all(equals_epsilon(p[0], new_min_x) or equals_epsilon(p[0], new_max_x) or equals_epsilon(p[1], new_min_y) or equals_epsilon(p[1], new_max_y) for p in new_points):
            return (new_max_x - new_min_x) * (new_max_y - new_min_y)
    
    # otherwise, this ain't it chief
    return None


def solve(N: int, X: list[float], Y: list[float], Z: list[float]) -> float:
    # reorganize as list of points for easier use
    points = list(zip(X, Y, Z))
    
    while True:
        # TODO optimize
        sample = random.sample(points, 3)
        
        # try to find a plane that goes through a face of the prism
        first_plane = Plane.from_points(*sample)
        
        signed_distances = [first_plane.signed_distance_to_point(p) for p in points]
        max_signed_distance, min_signed_distance = max(signed_distances), min(signed_distances)
        if not equals_epsilon(max_signed_distance, 0) and not equals_epsilon(min_signed_distance, 0):
            continue # plane definitely isn't tangent to the prism so it must not go through a face
        
        # categorize points relative to first_plane
        max_abs_distance = max(abs(max_signed_distance), abs(min_signed_distance))
        points_on_first_plane, points_on_second_plane, points_on_other_planes = [], [], []
        for p, d in zip(points, signed_distances):
            if equals_epsilon(d, 0):
                points_on_first_plane.append(p)
            elif equals_epsilon(abs(d), max_abs_distance):
                points_on_second_plane.append(p)
            else:
                points_on_other_planes.append(p)
        
        remaining_points = project(points_on_other_planes, first_plane)
        remaining_points = center(remaining_points)
        remaining_points = rotate_plane_points_to_xy_plane(remaining_points)
        
        area = rectangle_area([p[:2] for p in remaining_points])
        
        if area == None:
            continue # remaining points isn't a rectangle so this setup is wrong
        
        return area * max_abs_distance


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X, Y, Z = zip(*(map(float, input().split()) for _ in range(N)))
        print(solve(N, X, Y, Z))


if __name__ == '__main__':
    main()
