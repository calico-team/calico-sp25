def solve(N: int, C: list, P: list) -> str:
    assert 1 <= N <= 64
    assert len(C) == len(set(C))
    assert all(1 <= 10 ** 9 for p in P)
    assert sum(P) <= 2 ** 31 - 1 # overflow protection


def main():
    T = int(input())
    assert 1 <= T <= 100
    for _ in range(T):
        N = int(input())
        C = input().split(" ")
        P = list(map(lambda s: int(s), input().split(" ")))
        print(solve(N, C, P))

if __name__ == '__main__':
    main()
