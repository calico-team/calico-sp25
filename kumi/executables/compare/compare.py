import sys

from solution import solve

def main():
    if len(sys.argv) != 3:
        print('Incorrect number of arguments')
        exit(1)
    _, test_in_path, test_out_path = sys.argv

    try:
        with open(test_in_path, 'r') as test_in:
            with open(test_out_path, 'r') as test_out:
                compare(test_in, test_out)
    except IOError:
        print('Failed to open test input')
        exit(1)


import string
def compare(test_in, test_out):
    T = int(read_file(test_in))
    for case in range(1, T + 1):

        judge_solution = int(read_file(test_in))

        # Read solution from the contestant
        contestant_solution = read()
        for x in contestant_solution:
            if x not in 'uw':
                print(f'Test #{case}: unexpected character "{x}"')

        if len(contestant_solution) > 1e5:
            print(f'Test #{case}: contestant solution longer than 1e5')

        x = solve(contestant_solution)
        if (x != judge_solution):
            print(f'WA at test #{case}: got {x}, expected {judge_solution}')
            break

    try:
        temp = ''
        while not temp:
            temp = input().strip()
        print('Trailing output when judge expected no more output')
    except:
        pass


def read_file(file):
    try:
        return file.readline().strip()
    except EOFError:
        print('End of test input while judge expected more input')
        exit(1)


def read():
    try:
        return input().strip()
    except EOFError:
        print('End of output while judge expected more output')
        exit()


if __name__ == '__main__':
    main()
