"""ไฟส่อง"""
N = int(input())
COVERED = [0] * 360

for _ in range(N):
    a, b = map(int, input().split())
    while a != b:
        COVERED[a] += 1
        a = (a + 1) % 360

if not COVERED.count(0):
    print(360)
else:
    ANS = 0
    CNT = 0

    for i in range(720):
        if COVERED[i % 360] > 0:
            CNT += 1

            if CNT > ANS:
                ANS = CNT
        else:
            CNT = 0

    if ANS > 360:
        ANS = 360

    print(ANS)
