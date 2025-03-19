def solve(P: str) -> int:
    '''
    Implements addition with Python's arbitary precision arithmetic.
    '''
    total_change = 0
    repetition = 0
    for action in P:
        if action == "T":
            total_change += 1 * 2**repetition 
            repetition = 0
        else:
            repetition += 1
    return total_change


def main():
    T = int(input())
    for _ in range(T):
        P = input()
        print(solve(P))


if __name__ == '__main__':
    main()
