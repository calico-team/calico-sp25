MOD = 1000000007

def solve(N: int, K: int, X: int, Y: int, W1: int, W2: int, L1: int, L2: int, S: list[str]) -> int:
    """
    Return the LP gain mod 10^9 + 7.
    
    N: Number of games
    K: Number of special streaks
    X: LP won per win
    Y: LP lost per loss
    W1 / W2: Chance to win in the Winners Queue
    L1 / L2: Chance to win in the Losers Queue
    S: List containing the K special streaks
    """
    # YOUR CODE HERE
    return 0


def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, list(input().split()))
        X, Y, W1, W2, L1, L2 = map(int, input().split())
        S = [input() for _ in range(K)]
        print(solve(N, K, X, Y, W1, W2, L1, L2, S))

if __name__ == '__main__':
    main()
