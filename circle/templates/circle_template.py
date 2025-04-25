def solve(N: int, X: list[float], Y: list[float]) -> float:
    """
    Return the area of the rectangle described by the given points.
    
    N: the number of given points
    X: a list containing the x-coordinate of each point
    Y: a list containing the y-coordinate of each point
    """
    # YOUR CODE HERE
    return 0.0


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X, Y = zip(*(map(float, input().split()) for _ in range(N)))
        print(solve(N, X, Y))


if __name__ == '__main__':
    main()
