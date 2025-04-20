def solve(N: int, C: list, P: list) -> str:
    """
    Return a single string of the champion's name
    
    N: The length of C and P
    C: List of strings of the competitors
    P: List of integers of competitor's power
    """
    def helper(competitors, powers):
        if (len(competitors) == 1):
            return competitors[0]
        winners = []
        winnerPowers = []
        for i in range(len(competitors) // 2):
            if (powers[2 * i] >= powers[2 * i + 1]):
                winners.append(competitors[2 * i])
            else:
                winners.append(competitors[2 * i + 1])
            winnerPowers.append(powers[2 * i] + powers[2 * i + 1])
        if (len(competitors) % 2 == 1):
            winners.append(competitors[-1])
            winnerPowers.append(powers[-1])
        return helper(winners, winnerPowers)
    return helper(C, P)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = input().split(" ")
        P = list(map(lambda s: int(s), input().split(" ")))
        print(solve(N, C, P))

if __name__ == '__main__':
    main()
