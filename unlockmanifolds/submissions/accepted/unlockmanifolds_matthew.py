def solve(N: int, M: int, G: list) -> int:
    """
    Return the minimum number of actions
    
    N: a non-negative integer representing the number of rows
    M: another non-negative integer representing the number of columns
    G: N x M array representing a grid
    """
    locations = {}
    actions = 0
    cursor = (0, 0)
    for i in range(N):
        for j in range(M):
            locations[G[i][j]] = (i, j)
    for b in range(1, N*M + 1):
        hor_left = (locations[b][1] - cursor[1]) % M
        hor_right = (cursor[1] - locations[b][1]) % M
        vert_up = (locations[b][0] - cursor[0]) % N
        vert_down = (cursor[0] - locations[b][0]) % N
        actions += 1 + min(hor_left, hor_right) + min(vert_up, vert_down)
        cursor = locations[b]
    return actions

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        G = []
        for _ in range(N): 
            row = list(map(int, input().split()))
            G.append(row)
        print(solve(N, M, G))      

if __name__ == '__main__':
    main()