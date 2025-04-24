def solve(N: int, X: list[float], Y: list[float], Z: list[float]) -> int:
    return (max(X) - min(X)) * (max(Y) - min(Y)) * (max(Z) - min(Z))


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X, Y, Z = zip(*(map(int, input().split()) for _ in range(N)))
        print(solve(N, X, Y, Z))

if __name__ == '__main__':
    main()
