def solve(A: int, B: int) -> int:
    """
    Return the sum of A and B.
    
    A: a non-negative integer
    B: another non-negative integer
    """
    assert 1 <= A <= 1e12
    assert 1 <= B <= 1e12
    return 0


def main():
    T = int(input())
    assert T <= 100
    for _ in range(T):
        temp = input().split()
        A, B = int(temp[0]), int(temp[1])

if __name__ == '__main__':
    main()
