def solve(N: int, K: int, A: list[int], B: list[int], C: list[int], D: list[int]) -> float:
    """
    Return the best score you can achieve in the Daily Run.
    
    N: number of stages
    K: number of turns each lure lasts
    A: list containing the health points of the first Pokemon in each stage
    B: list containing the turns it takes to beat each stage if it were a singles battle
    C: list containing the health points of the additional Pokemon in each stage
    D: list containing the turns it takes to beat each stage if it were a doubles battle
    """
    # YOUR CODE HERE
    return 0.0


def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        C = list(map(int, input().split()))
        D = list(map(int, input().split()))
        print(solve(N, K, A, B, C, D))

if __name__ == '__main__':
    main()
