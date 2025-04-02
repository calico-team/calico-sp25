def is_stable(blocks : list[tuple[tuple[int, int], tuple[int, int]]]) -> bool:
    # YOUR CODE HERE
    return True

def main():
    numCases = int(input())
    for i in range(numCases):
        numBlocks = int(input())
        blocks = []
        for b in range(numBlocks):
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
