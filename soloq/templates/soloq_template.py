MOD = 1000000007

def solve(N: int, K: int, X: int, Y: int, W1: int, W2: int, L1: int, L2: int, S: list[str]) -> int:
    """
    Return the sum of A and B.
    
    A: a non-negative integer
    B: another non-negative integer
    """
    # YOUR CODE HERE
    return 0


def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, list(input().split()))
        X, Y, W1, W2, L1, L2 = map(int, list(input().split()))
        S = [input() for _ in range(K)]
        print(solve(N, K, X, Y, W1, W2, L1, L2, S))

if __name__ == '__main__':
    main()
