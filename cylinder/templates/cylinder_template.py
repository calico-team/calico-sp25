def solve(N: int, X: list[float], Y: list[float], Z: list[float]) -> int:
    """
    Return the volume of the rectangular prism described by the given points.
    
    N: the number of given points
    X: a list containing the x-coordinate of each point
    Y: a list containing the y-coordinate of each point
    Z: a list containing the z-coordinate of each point
    """
    # YOUR CODE HERE
    return 0


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X, Y, Z = zip(*(map(int, input().split()) for _ in range(N)))
        print(solve(N, X, Y, Z))

if __name__ == '__main__':
    main()
