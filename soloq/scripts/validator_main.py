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
    assert 1 <= N <= 1e12
    assert 1 <= K <= 15
    assert 0 <= X <= 1e9
    assert 0 <= Y <= 1e9
    assert 0 <= W1 <= W2 <= 1e9
    assert W2 != 0
    assert 0 <= L1 <= L2 <= 1e9
    assert L2 != 0
    assert len(S) == K
    for s in S:
        assert 1 <= len(s) <= 15
        for c in s:
            assert (c in "WL")
    return 0



def main():
    T = int(input())
    assert T <= 10
    total_K = 0
    for _ in range(T):
        N, K = map(int, input().split())
        total_K += K
        X, Y, W1, W2, L1, L2 = map(int, input().split())
        S = [input() for _ in range(K)]
        solve(N, K, X, Y, W1, W2, L1, L2, S)
    assert total_K <= 15

if __name__ == '__main__':
    main()
