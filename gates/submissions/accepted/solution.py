import sys

def main():
    MOD = 10**9 + 7
    data = sys.stdin.read().split()
    it = iter(data)
    t = int(next(it))
    out = []

    for _ in range(t):
        n = int(next(it))
        arr = [int(next(it)) for _ in range(n)]

        # dp[i][state][bit]
        dp = [[[0, 0] for _ in range(4)] for _ in range(n)]
        dp[0][0][arr[0]] = 1

        for i in range(n - 1):
            # process next element
            if arr[i + 1] == 1:
                for j in range(4):
                    s0, s1 = dp[i][j]
                    dp[i + 1][j][0] = (dp[i + 1][j][0] + s0 + s1) % MOD
                    dp[i + 1][j][1] = (dp[i + 1][j][1] + 2 * (s0 + s1)) % MOD

                dp[i + 1][1][1] = (dp[i + 1][1][1] + dp[i][0][0]) % MOD
                dp[i + 1][2][1] = (dp[i + 1][2][1] + dp[i][0][1]) % MOD
            else:
                for j in range(4):
                    s0, s1 = dp[i][j]
                    dp[i + 1][j][0] = (dp[i + 1][j][0] + 3 * s0 + s1) % MOD
                    dp[i + 1][j][1] = (dp[i + 1][j][1] + 2 * s1) % MOD

                dp[i + 1][1][0] = (dp[i + 1][1][0] + dp[i][0][0]) % MOD
                dp[i + 1][2][0] = (dp[i + 1][2][0] + dp[i][0][1]) % MOD

            # finalize state 3 for i+1
            dp3_0 = (3 * dp[i + 1][1][0] + dp[i + 1][1][1] + dp[i + 1][2][0] + dp[i + 1][2][1]) % MOD
            dp3_1 = (2 * dp[i + 1][1][1] + 2 * dp[i + 1][2][0] + 2 * dp[i + 1][2][1]) % MOD
            dp[i + 1][3][0] = (dp[i + 1][3][0] + dp3_0) % MOD
            dp[i + 1][3][1] = (dp[i + 1][3][1] + dp3_1) % MOD

        # compute result
        last = dp[n - 1]
        num0 = (last[3][0] + n * last[0][0]) % MOD
        num1 = (last[3][1] + n * last[0][1]) % MOD
        out.append(str(num1))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
