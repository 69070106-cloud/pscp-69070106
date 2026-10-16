"""ตำบลกระสุนตก"""
N = int(input())
BULLET = []

for _ in range(N):
    x, y, d = map(int, input().split())
    BULLET.append([x, y, d])

FOUND = False

for tx in range(1000):
    for ty in range(1000):
        IS_MATH = True

        for bx, by, bd in BULLET:
            if (tx - bx)**2 + (ty - by)**2 != bd**2:
                IS_MATH = False
                break

        if IS_MATH:
            print(f"{tx} {ty}")
            FOUND = True
            break

    if FOUND:
        break
