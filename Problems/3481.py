"""ลอดสะพาน"""
_, N = map(int, input().split())
EVENT = []

for _ in range(N):
    a, b = map(int, input().split())
    EVENT.append([a, 1])
    EVENT.append([b, -1])

EVENT.sort()

CURRENT = 0
ANS = 0

for _, c in EVENT:
    CURRENT += c

    if CURRENT > ANS:
        ANS = CURRENT

print(ANS)
