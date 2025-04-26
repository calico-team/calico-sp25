from collections import deque
import math

def solve(N: int, K: int, A: list[int], B: list[int], C: list[int], D: list[int]) -> float:
    """
    Return the best score you can achieve in the Daily Run.
    
    N: number of stages
    K: number of turns each lure lasts
    A: list containing the health points of the first Pokémon in each stage
    B: list containing the turns it takes to beat each stage if it were a singles battle
    C: list containing the health points of the additional Pokémon in each stage
    D: list containing the turns it takes to beat each stage if it were a doubles battle
    """
    # Special case: only one stage => no lure decisions.
    if N == 1:
        return A[0] / B[0]
    
    # We'll use binary search on the candidate score R.
    # Set an initial high bound: no stage's ratio can exceed the best among singles and (for stages>=2) doubles.
    hi = 0.0
    for i in range(N):
        hi = max(hi, A[i] / B[i])
        if i >= 1:  # for stages 2..N, doubles option exists
            hi = max(hi, (A[i] + C[i]) / D[i])
    lo = 0.0

    m = N - 1  # number of stages from stage 2 to stage N

    def feasible(R: float) -> bool:
        # Compute base singles contribution for all stages.
        base = 0.0
        for i in range(N):
            base += A[i] - R * B[i]
        # For stages 2..N (we use 0-indexing for these m stages)
        # delta[i] = extra if forced doubles instead of singles for stage i+2.
        # (i=0 corresponds to original stage 2)
        delta = [0.0] * m
        for i in range(m):
            # For stage i+2:
            delta[i] = C[i+1] - R * (D[i+1] - B[i+1])
        # Build suffix sum array P: P[i] = delta[i] + delta[i+1] + ... + delta[m-1]
        P = [0.0] * (m + 1)
        P[m] = 0.0
        for i in range(m - 1, -1, -1):
            P[i] = P[i + 1] + delta[i]
        # dp[i] = maximum extra achievable from stages i+2 to N.
        dp = [0.0] * (m + 1)
        dp[m] = 0.0  # base: no stages left
        # We'll use a deque to quickly get:
        #   max_{j in [i+K, m]} (dp[j] - P[j])
        # Each element in the deque is a pair (j, Q[j]) with Q[j] = dp[j] - P[j].
        dq = deque()
        dq.append((m, dp[m] - P[m]))  # Q[m] = 0

        # Process dp backwards from i = m-1 downto 0.
        for i in range(m - 1, -1, -1):
            remaining = m - i  # number of stages available from index i
            if remaining < K:
                forced = P[i]  # if fewer than K stages remain, forcing means take them all.
            else:
                # We want: forced = P[i] + max_{j in [i+K, m]} (dp[j] - P[j])
                # Remove from the front any indices j that are out of range (j < i+K)
                while dq and dq[0][0] < i + K:
                    dq.popleft()
                bestQ = dq[0][1] if dq else float('-inf')
                forced = P[i] + bestQ
            # Option 1: do not force stage i (i.e. leave stage i+2 as singles)
            option1 = dp[i + 1] if i + 1 <= m else float('-inf')
            dp[i] = option1 if option1 > forced else forced
            # Compute Q[i] = dp[i] - P[i]
            Q_i = dp[i] - P[i]
            # Maintain dq in decreasing order of Q value.
            while dq and dq[-1][1] <= Q_i:
                dq.pop()
            dq.append((i, Q_i))
        extra = dp[0]
        return (base + extra) >= 0

    # Binary search for the maximum achievable R (to 1e-5 precision).
    for _ in range(50):
        mid = (lo + hi) / 2.0
        if feasible(mid):
            lo = mid
        else:
            hi = mid

    return lo


def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        C = list(map(int, input().split()))
        D = list(map(int, input().split()))
        print("{:.5f}".format(solve(N, K, A, B, C, D)))


if __name__ == '__main__':
    main()
