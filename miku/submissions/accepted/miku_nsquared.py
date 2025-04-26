def solve(S):
    count = 0
    for i in range(0, len(S)):
        if (S[i] == 'o' and i + 1 <= len(S)):
            w = False
            for j in range(i + 1, len(S)):
                if (S[j] == 'w'):
                    w = True
                if (w and S[j] == 'o'):
                    count += 1

    for i in range(0, len(S)):
        if (S[i] == 'u' and i + 1 <= len(S)):
            w = False
            for j in range(i + 1, len(S)):
                if (S[j] == 'w'):
                    w = True
                if (w and S[j] == 'u'):
                    count += 1

    return count

def main():
    T = int(input())
    for _ in range(T):
        S = input()
        print(solve(S))
main()
