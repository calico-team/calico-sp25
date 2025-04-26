import random

T = random.randint(1, 100)
T = 1
print(T)

for i in range(T):
    # for bonus: should be 200000.
    N = random.randint(1, 1000)
    N = 10
    print(N)
    A = [random.randint(0, 1) for _ in range(N)]
    print(*A)
