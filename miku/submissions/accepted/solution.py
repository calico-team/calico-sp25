import sys

def solve(s: str) -> int:
    # curw tracks the most recent 'w' index to the right
    n = len(s)
    curw = -1
    nxtw = [-1] * n
    sufu = [0] * n  # suffix count of 'u'

    # build suffix arrays and next-'w' indices
    for i in range(n - 1, -1, -1):
        if i < n - 1:
            sufu[i] = sufu[i + 1]

        if s[i] == 'w':
            curw = i
        elif s[i] == 'u':
            sufu[i] += 1

        nxtw[i] = curw

    ans = 0
    # for each 'o' or 'u', add contributions based on the next 'w'
    for i, ch in enumerate(s):
        j = nxtw[i]
        if j != -1:
            if ch == 'u':
                ans += sufu[j]

    return ans

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(solve(s))

if __name__ == "__main__":
    main()
