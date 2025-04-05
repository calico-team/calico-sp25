MOD = 1000000007

def modinv(a: int, mod: int = MOD) -> int:
    return pow(a, mod - 2, mod)

def build_ac(patterns: list[str]):
    # Build Aho–Corasick automaton.
    ac_next = []   # list of dicts: for each node, mapping letter -> next node
    ac_fail = []   # failure link for each node
    ac_out = []    # out count (number of patterns ending here)
    ac_next.append({})  # root node, index 0
    ac_fail.append(0)
    ac_out.append(0)
    for pat in patterns:
        node = 0
        for ch in pat:
            if ch not in ac_next[node]:
                ac_next[node][ch] = len(ac_next)
                ac_next.append({})
                ac_fail.append(0)
                ac_out.append(0)
            node = ac_next[node][ch]
        ac_out[node] += 1
    # Build failure links using a BFS.
    from collections import deque
    q = deque()
    for ch, nxt in ac_next[0].items():
        q.append(nxt)
        ac_fail[nxt] = 0
    while q:
        node = q.popleft()
        for ch, nxt in ac_next[node].items():
            q.append(nxt)
            f = ac_fail[node]
            while f and ch not in ac_next[f]:
                f = ac_fail[f]
            ac_fail[nxt] = ac_next[f].get(ch, 0)
            ac_out[nxt] += ac_out[ac_fail[nxt]]
    return ac_next, ac_fail, ac_out

def ac_transition(node: int, ch: str, ac_next: list[dict], ac_fail: list[int]) -> int:
    # Follow transitions (using failure links if necessary).
    while node and ch not in ac_next[node]:
        node = ac_fail[node]
    return ac_next[node].get(ch, 0)

def identity_matrix(n: int) -> list[list[int]]:
    I = [[0] * n for _ in range(n)]
    for i in range(n):
        I[i][i] = 1
    return I

def mat_mult(A: list[list[int]], B: list[list[int]], mod: int = MOD) -> list[list[int]]:
    n = len(A)
    m = len(B)
    p = len(B[0])
    res = [[0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            if A[i][k]:
                for j in range(p):
                    res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % mod
    return res

def mat_vec_mult(A: list[list[int]], v: list[int], mod: int = MOD) -> list[int]:
    n = len(A)
    p = len(v)
    res = [0] * n
    for i in range(n):
        for j in range(p):
            res[i] = (res[i] + A[i][j] * v[j]) % mod
    return res

def pair_mult(pair1, pair2, mod: int = MOD):
    # Multiply two pairs (A, B) and (C, D):
    # (A, B) ∘ (C, D) = (A·C, B + A·D).
    A1, B1 = pair1
    A2, B2 = pair2
    A = mat_mult(A1, A2, mod)
    Av2 = mat_vec_mult(A1, B2, mod)
    B = [(B1[i] + Av2[i]) % mod for i in range(len(B1))]
    return (A, B)

def pair_pow(pair, power: int, mod: int = MOD):
    s = len(pair[0])
    I = identity_matrix(s)
    zero_vec = [0] * s
    result = (I, zero_vec)
    base = pair
    while power:
        if power & 1:
            result = pair_mult(result, base, mod)
        base = pair_mult(base, base, mod)
        power //= 2
    return result

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
    # Build the Aho–Corasick automaton.
    ac_next, ac_fail, ac_out = build_ac(S)
    num_nodes = len(ac_next)
    # Define swap_flag[node] = 1 if an odd number of streaks end at node, else 0.
    swap_flag = [ac_out[i] & 1 for i in range(num_nodes)]
    
    # Build combined state space: each state is (node, queue)
    # queue: 0 for Winners, 1 for Losers.
    state_index = {}
    states = []
    for node in range(num_nodes):
        for q in (0, 1):
            state_index[(node, q)] = len(states)
            states.append((node, q))
    s_size = len(states)
    
    # Precompute probabilities and immediate rewards.
    pW = (W1 * modinv(W2, MOD)) % MOD
    pL = (L1 * modinv(L2, MOD)) % MOD
    rW = (pW * X - ((1 - pW + MOD) % MOD) * Y) % MOD
    rL = (pL * X - ((1 - pL + MOD) % MOD) * Y) % MOD
    
    # Build transition matrix T (s_size x s_size) and reward vector r_vec (length s_size).
    T = [[0] * s_size for _ in range(s_size)]
    r_vec = [0] * s_size
    for (node, q), i in state_index.items():
        # Immediate reward depends only on the current queue.
        r_vec[i] = rW if q == 0 else rL
        # Determine the probability of a win/loss.
        if q == 0:
            prob_win = pW
            prob_loss = (1 - pW + MOD) % MOD
        else:
            prob_win = pL
            prob_loss = (1 - pL + MOD) % MOD
        # Outcome: win ('W')
        next_node = ac_transition(node, 'W', ac_next, ac_fail)
        new_q = q if swap_flag[next_node] == 0 else 1 - q
        j = state_index[(next_node, new_q)]
        T[i][j] = (T[i][j] + prob_win) % MOD
        # Outcome: loss ('L')
        next_node = ac_transition(node, 'L', ac_next, ac_fail)
        new_q = q if swap_flag[next_node] == 0 else 1 - q
        j = state_index[(next_node, new_q)]
        T[i][j] = (T[i][j] + prob_loss) % MOD

    # Package the pair (T, r_vec) where playing one game from a state gives reward r_vec and then
    # transitions according to T. Then (T, r_vec)^N = (T^N, sum_{i=0}^{N-1} T^i * r_vec).
    pair = (T, r_vec)
    _, S_vec = pair_pow(pair, N, MOD)
    # Big Ben starts at state (node 0, Winners Queue) i.e. (0, 0)
    start = state_index[(0, 0)]
    ans = S_vec[start] % MOD
    return ans

def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, list(input().split()))
        X, Y, W1, W2, L1, L2 = map(int, input().split())
        S = [input().strip() for _ in range(K)]
        print(solve(N, K, X, Y, W1, W2, L1, L2, S))

if __name__ == '__main__':
    main()
