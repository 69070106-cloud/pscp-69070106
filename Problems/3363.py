"""ไข้หวัดกระต่ายสายพันธุ์ใหม่"""
ROW, COL = map(int, input().split())
RAB_R, RAB_C = map(int, input().split())
N = int(input())

NOTSAFE_PLACE = [[0] * COL for _ in range(ROW)]

for _ in range(N):
    INF_R, INF_C = map(int, input().split())
    for i in range(max(0, INF_R - 2), min(ROW, INF_R + 3)):
        for n in range(max(0, INF_C - 2), min(COL, INF_C + 3)):
            DIST = max(abs(i - INF_R), abs(n - INF_C))
            if not DIST:
                RISK = 100
            elif DIST == 1:
                RISK = 60
            else:
                RISK = 20
            if RISK > NOTSAFE_PLACE[i][n]:
                NOTSAFE_PLACE[i][n] = RISK

SAFE_COUNT = 0
for r in range(ROW):
    for c in range(COL):
        if not NOTSAFE_PLACE[r][c]:
            SAFE_COUNT += 1

print(SAFE_COUNT)
print(f"{NOTSAFE_PLACE[RAB_R][RAB_C]}%")
