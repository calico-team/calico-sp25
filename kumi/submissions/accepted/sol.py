"""
solution sketch:
    start with uwuwuwuwuwuwuw = "uw"*m
    answer is m*(m-1)//2
    find smallest m such that answer >= N

    remove 3 consecutive w's (uwuwuwuw ==> uuuuw): answer reduces by 6
    remove a single w (uwu ==> uu): answer reduces by 1

    does not work for small N
    (probably) works for large enough N
"""

T = int(input())
for _ in range(T):
    N = int(input())
    if N < 900000:
        print('ow' + 'o' * N)
        continue

    m = 2
    while m*m - m < 2*N:
        m += 1

    diff = (m*m-m) - 2*N

    d = diff // 12
    # print(f"m = {m}")
    # print(f"diff = {diff}")
    # print(f"d = {d}")
    # print(d*12)
    diff -= d*12
    b = diff // 2
    # print(b)

    a = m-d*4-b*2
    # print(f"{d} 4s; {b} 2s; {a} 1s;")
    print("ow"*a + "oow"*b + "oooow"*d)

    # arr = [1]*a + [2]*b + [4]*d
    # total = 0

    ## use formula to verify
    # total = a*(a-1)//2 + 4*b*(b-1)//2 + 16*d*(d-1)//2 + a*b*2 + a*d*4 + b*d*8

    # print(f"using formula,\n{total} should equal N: {N}")

    ## use double for loop to verify
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         total += arr[i]*arr[j]
    #
    # print(f"{total} should equal N: {N}")
