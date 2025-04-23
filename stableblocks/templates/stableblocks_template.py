def solve(N: int, X0: list[int], Y0: list[int], X1: list[int], Y1: list[int]) -> bool:
    """
    Return True if the configuration of blocks is stable, and False otherwise.
    
    N: the number of blocks
    X0: a list containing the X-coordinates of the lower left corner of each block
    Y0: a list containing the Y-coordinates of the lower left corner of each block
    X1: a list containing the X-coordinates of the upper right corner of each block
    Y1: a list containing the Y-coordinates of the upper right corner of each block
    """
    # YOUR CODE HERE
    return False


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        corners = []
        for _ in range(N):
            corners.append(list(map(int, input().split())))
        X0, Y0, X1, Y1 = zip(*corners)
        if solve(N, X0, Y0, X1, Y1):
            print('Stable')
        else:
            print('Unstable')


if __name__ == '__main__':
    main()