MAXHP = 1000000
MAXTURNS = 1000

def solve(N: int, K: int, A: list[int], B: list[int], C: list[int], D: list[int]) -> float:
    """
    Return the best score you can achieve in the Daily Run.
    
    N: number of stages
    K: number of turns each lure lasts
    A: list containing the health points of the first Pokemon in each stage
    B: list containing the turns it takes to beat each stage if it were a singles battle
    C: list containing the health points of the additional Pokemon in each stage
    D: list containing the turns it takes to beat each stage if it were a doubles battle
    """
    # YOUR CODE HERE
    assert 1 <= K <= N <= 50000
    assert len(A) == len(B) == len(C) == len(D) == N
    for a in A:
        assert 1 <= a <= MAXHP
    for b in B:
        assert 1 <= b <= MAXTURNS
    for c in C:
        assert 1 <= c <= MAXHP
    for d in D:
        assert 1 <= d <= MAXTURNS



def main():
    T = int(input())
    assert 1 <= T <= 10
    for _ in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        C = list(map(int, input().split()))
        D = list(map(int, input().split()))
        solve(N, K, A, B, C, D)

if __name__ == '__main__':
    main()
