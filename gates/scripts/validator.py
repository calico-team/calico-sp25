def main():
    T = int(input())
    assert T <= 100
    for _ in range(T):
        N = int(input())
        assert N <= 200000
        nums = list(map(int, input().split()))
        for x in nums:
            assert (x == 0 or x == 1)

if __name__ == '__main__':
    main()
