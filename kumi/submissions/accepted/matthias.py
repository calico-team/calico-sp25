from math import ceil, sqrt

import sys

def solve(N):
    total_n = ceil((1+sqrt(1 + 8.0 * N)) / 2)
    too_much = (total_n * total_n - total_n) / 2 - N
    n4 = too_much // 6
    too_much = too_much % 6
    n3 = too_much // 3
    too_much = too_much % 3
    n2 = too_much
    n1 = total_n - (2 * n2 + 3 * n3 + 4 * n4)
    
    if n1 < 0:
        print("Bad n1")
        sys.exit(1)
    
    if N != ((4 * n4 + 3 * n3 + 2 * n2 + n1)** 2 - ((4 ** 2) * n4 + (3 ** 2) * n3 + (2 ** 2) * n2 + n1)) / 2:
        print("Not adding up")
        sys.exit(1)
        
    return 'w'.join(['o'] * int(n1) + ['oo'] * int(n2) + ['ooo'] * int(n3) + ['oooo'] * int(n4))

lines = list(sys.stdin)
T = int(lines[0])

for i in range(T):
    print(solve(int(lines[i+1])))

