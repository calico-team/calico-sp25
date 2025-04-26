import sys

def calc(a: int, op: int, b: int) -> int:
    if op == 0:
        return a & b
    elif op == 1:
        return a | b
    else:
        return a ^ b


def main():
    data = sys.stdin.read().split()
    it = iter(data)
    MOD = 10**9 + 7
    t = int(next(it))
    out = []

    for _ in range(t):
        n = int(next(it))
        arr = [int(next(it)) for _ in range(n)]

        # Precompute powers of 3 up to n-1
        pw = [1] * n
        for i in range(1, n):
            pw[i] = pw[i - 1] * 3

        ans = 0
        # Enumerate all operator assignments (3^(n-1))
        for mask in range(pw[n - 1]):
            x = mask
            ops = [0] * (n - 1)
            # Decode ternary representation
            for j in range(n - 2, -1, -1):
                ops[j] = x // pw[j]
                x %= pw[j]

            # Try every subarray [p1, p2]
            for p1 in range(n):
                for p2 in range(p1, n):
                    # Compute vp for segment [p1..p2]
                    vp = arr[p1]
                    for k in range(p1, p2):
                        vp = calc(vp, ops[k], arr[k + 1])

                    # Combine left side
                    if p1 != 0:
                        v = arr[0]
                        for k in range(p1 - 1):
                            v = calc(v, ops[k], arr[k + 1])
                        v = calc(v, ops[p1 - 1], vp)
                    else:
                        v = vp

                    # Combine right side
                    for k in range(p2, n - 1):
                        v = calc(v, ops[k], arr[k + 1])

                    # Count nonzero results
                    if v != 0:
                        ans += 1
                    ans %= MOD

        out.append(str(ans))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
