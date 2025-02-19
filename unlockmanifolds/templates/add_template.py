def solve(N: int, M: int, G: list) -> int:
    """
    
    
    N: a non-negative integer representing the number of rows
    M: another non-negative integer representing the number of columns
    G: N x M array representing a grid
    """
    # YOUR CODE HERE
    return 0


def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        G = []
        for _ in range(N): 
            row = list(map(int, input().split()))
            G.append(row)      
if __name__ == '__main__':
    main()
