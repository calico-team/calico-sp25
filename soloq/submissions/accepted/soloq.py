from collections import deque

MOD = 1000000007

class AhoCorasick:
    class Node:
        def __init__(self):
            self.to = [-1,-1]
            self.link = -1
            self.endsHere = []
            self.end = False
            self.terminal = 0
        
    def __init__(self):
        self.d = [self.Node()]
        self.bfs = []

    def ins(self, s, i):
        v = 0
        for C in s:
            c = 0 if C == 'W' else 1
            if self.d[v].to[c] == -1:
                self.d[v].to[c] = len(self.d)
            v = self.d[v].to[c]
        self.d[v].end = True
        self.d[v].endsHere.append((i, len(s)))

    def push_links(self):
        self.d[0].link = -1
        q = deque()
        while q:
            v = q.popleft()
            self.bfs.append(v)
            self.d[v].terminal = 0 if self.d[v].link == -1 else self.d[v].link if self.d[self.d[v].link].end else self.d[self.d[v].link].terminal
            for x in self.d[self.d[v].terminal].endsHere:
                self.d[v].endsHere.append(x)
            for c in range(2):
                u = self.d[v].to[c]
                if u == 0:
                    continue
                self.d[u].link = 0 if self.d[v].link == -1 else self.d[self.d[v].link].to[c]
                q.append(u)
            if v != 0:
                for c in range(2):
                    if self.d[v].to[c] != 0:
                        self.d[v].to[c] = self.d[self.d[v].link].to[c]


def matMul(A, B):
    N, L, M = len(A), len(A[0]), len(B[0])
    res = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for k in range(L):
                res[i][j] += A[i][k] * B[k][j]
                res[i][j] %= MOD
    return res

def matSum(A, B):
    return [[(A[i][j] + B[i][j]) % MOD for j in range(len(A[0]))] for i in range(len(A))]

def eye(n):
    return [[0 if j != i else 1 for j in range(n)] for i in range(n)]

def matPow(A, b):
    res = eye(len(A))
    while b != 0:
        if b % 2 == 1:
            res = matMul(res, A)
        A = matMul(A, A)
        b //= 2
    return res
    

def solve(N: int, K: int, X: int, W1: int, W2: int, L1: int, L2: int, S: list[str]) -> int:

    # Transform the chances to Fp
    W1 *= pow(W2, MOD - 2, MOD)
    L1 *= pow(L2, MOD - 2, MOD)


    # Construct graph
    AC = AhoCorasick()

    for i in range(len(S)):
        AC.ins(S[i], i)
    
    AC.push_links()

    num_states = len(AC.d)

    # Construct transition matrix
    A = [[0 for _ in range(2 * num_states)] for _ in range(2 * num_states)]
    
    for i in range(num_states):
        j_win = AC.d[i].to[0]
        swap_win = len(AC.d[j_win].endsHere) % 2 == 1
        if swap_win:
            A[i][j_win + num_states] = W1
            A[i + num_states][j_win] = L1
        else:
            A[i][j_win] = W1
            A[i + num_states][j_win + num_states] = L1
        
        j_lose = AC.d[i].to[1]
        swap_lose = len(AC.d[j_lose].endsHere) % 2 == 1
        if swap_lose:
            A[i][j_lose + num_states] = MOD - W1
            A[i + num_states][j_lose] = MOD - L1
        else:
            A[i][j_lose] = MOD - W1
            A[i + num_states][j_lose + num_states] = MOD - L2
    
    d0 = [[0 if i != 0 else 1 for i in range(2 * num_states)]]
    mu = [[X * (2 * W1 - MOD) if i < num_states else X * (2 * L1 - MOD)] for i in range(2 * num_states)]
    for v in mu:
        if v[0] < 0:
            v[0] += MOD
    
    # Returns sum from i = 1 to n of A^i
    def fun(n):
        if n == 1:
            return eye(len(A))
        elif n % 2 == 1:
            return matSum(matPow(A, n), fun(n - 1))
        else:
            return matMul(matSum(eye(len(A)), matPow(A, n // 2)), fun(n // 2))
    
    return matMul(d0, matMul(matSum(eye(len(A)), fun(N - 1)), mu))[0][0]


def main():
    T = int(input())
    for _ in range(T):
        N, K, W1, W2, L1, L2 = map(int, list(input().split()))
        S = [input() for _ in range(K)]
        print(solve(N, K, W1, W2, L1, L2, S))

if __name__ == '__main__':
    main()
