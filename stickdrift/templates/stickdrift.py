def solve(N: int, M: int, S: str, G: list) -> int:
    """
    Return the minimum number of actions
    
    N: a non-negative integer representing the number of rows
    M: another non-negative integer representing the number of columns
    S: A string representing a sequence of drift inputs
    G: N x M array representing a grid
    """
    # YOUR CODE HERE
    return -1


def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        S =  input().strip()
        G = []
        for _ in range(N):
            row = list(map(int, input().split()))
            G.append(row)
        print(solve(N, M, S, G))


if __name__ == '__main__':
    main()