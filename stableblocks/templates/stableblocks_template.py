def is_stable(blocks : list[tuple[tuple[int, int], tuple[int, int]]]) -> bool:
    # YOUR CODE HERE
    return True

def main():
    T = int(input())
    for j in range(T):
        N = int(input())
        blocks = []
        for i in range(N):
            lowerLeftX, lowerLeftY, upperRightX, upperRightY = input().split()
            blocks.append(
                ((int(lowerLeftX),  int(lowerLeftY)),
                 (int(upperRightX), int(upperRightY))))
        if is_stable(blocks):
            print("Stable")
        else:
            print("Unstable")

if __name__ == '__main__':
    main()
