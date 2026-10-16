"""ขายรถยนต์"""
N = int(input())
CAR = []

for _ in range(N):
    P, V = map(int, input().split())
    CAR.append([P, V])

CAR.sort()

MAX_V = 0
ANS = 0

for _, v in CAR:
    if v < MAX_V:
        ANS += 1

    if v > MAX_V:
        MAX_V = v

print(ANS)
