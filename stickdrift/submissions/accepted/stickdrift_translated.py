maxn = 1010    # maximum for grid dimension allocation (n)
maxl = 10010   # maximum for path length allocation

def check(v, cx, cy, nx, ny, cm, n, m, move_len, prex, prey):
    ov = v  # original value of v
    if cm + v >= move_len:
        cx += prex[move_len] - prex[cm]
        cy += prey[move_len] - prey[cm]
        v -= (move_len - cm)
        cm = 0
        d = v // move_len
        cx += d * prex[move_len]
        cy += d * prey[move_len]
        v %= move_len
        cx = ((cx % n) + n) % n
        cy = ((cy % m) + m) % m
    cx += prex[cm + v] - prex[cm]
    cy += prey[cm + v] - prey[cm]
    dx = abs(cx - nx)
    dy = abs(cy - ny)
    dx = min(dx, n - dx)
    dy = min(dy, m - dy)
    return dx + dy <= ov

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        moves = input().strip()
        move_len = len(moves)
        
        # Preallocate array for positions using constant maxn
        arr = [None] * (maxn * maxn)
        # Fill the array with grid positions: x-1 is used as index to store (i, j)
        for i in range(n):
            row = list(map(int, input().split()))
            for j in range(m):
                x = row[j]
                arr[x - 1] = (i, j)
        
        # Preallocate movement accumulation arrays using constant maxl
        prex = [0] * maxl
        prey = [0] * maxl
        
        # Precompute movement effect accumulations for each prefix of moves.
        for i in range(move_len):
            prex[i + 1] = prex[i]
            prey[i + 1] = prey[i]
            if moves[i] == 'U':
                prex[i + 1] -= 1
            elif moves[i] == 'D':
                prex[i + 1] += 1
            elif moves[i] == 'L':
                prey[i + 1] -= 1
            elif moves[i] == 'R':
                prey[i + 1] += 1
        
        cx, cy, cm = 0, 0, 0
        ans = 0
        
        # Process positions in the order specified in arr
        for i in range(n * m):
            nx, ny = arr[i]
            if cx == nx and cy == ny:
                continue
            l, r = 0, n * m
            while l + 1 < r:
                mid = (l + r) // 2
                if check(mid, cx, cy, nx, ny, cm, n, m, move_len, prex, prey):
                    r = mid
                else:
                    l = mid
            cm = (cm + r) % move_len
            ans += r
            cx, cy = nx, ny
        
        print(ans)

if __name__ == "__main__":
    main()
