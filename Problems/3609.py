"""[Recommend] 3nPlus1"""
while True:
    N = int(input())
    if not N:
        break
    TIME = 1
    while N != 1:
        if not N % 2:
            N = N / 2
        else:
            N = (N * 3) + 1
        TIME += 1

    print(TIME)
