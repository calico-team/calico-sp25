def solve(N: int, C: list, P: list) -> str:
    """
    Return a single string of the champion's name
    
    N: The length of C and P
    C: List of strings of the competitors
    P: List of integers of competitor's power
    """
    # YOUR CODE HERE
    return ""


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = input().split(" ")
        P = list(map(lambda s: int(s), input().split(" ")))
        print(solve(N, C, P))

if __name__ == '__main__':
    main()
