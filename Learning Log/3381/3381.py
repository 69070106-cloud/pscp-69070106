"""[LEARNING LOGS] Point Sorting"""
T = int(input())

for _ in range(T):
    TIME = int(input())
    ANS = []

    for _ in range(TIME):
        N1, N2 = map(int, input().split())
        ANS.append([N1, N2])

    ANS.sort(key=lambda x: (x[0] + x[1], x[0]))

    for k in ANS:
        print(f"{k[0]} {k[1]}")
