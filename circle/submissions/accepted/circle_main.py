def solve(N: int, X: list[float], Y: list[float]) -> float:
    return (max(X) - min(X)) * (max(Y) - min(Y))


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X, Y = zip(*(map(float, input().split()) for _ in range(N)))
        print(solve(N, X, Y))


if __name__ == '__main__':
    main()
