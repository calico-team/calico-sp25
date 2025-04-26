def solve(N: int, C: list, P: list) -> str:
    def helper(number, competitors, powers):
        if (number == 1):
            return competitors[0]
        winners = []
        winnerPowers = []
        for i in range(0, number, 2):
            if (powers[i] > powers[i + 1]):
                winners.append(competitors[i])
            elif (powers[i] == powers[i + 1]):
                winners.append(competitors[i] + competitors[i + 1])
            else:    
                winners.append(competitors[i + 1])
            winnerPowers.append(powers[i] + powers[i + 1])
        return helper(number // 2, winners, winnerPowers)
    return helper(N, C, P)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = input().split(" ")
        P = list(map(lambda s: int(s), input().split(" ")))
        print(solve(N, C, P))

if __name__ == '__main__':
    main()
