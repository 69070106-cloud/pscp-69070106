"""แซงรอบ"""
N, K = map(int, input().split())
TIME = []

for _ in range(N):
    TIME.append(int(input()))

MIN_TIME = min(TIME)

TARGET = K * MIN_TIME
FINALISTS = 0

for i in TIME:
    if (K - 1) * i < TARGET:
        FINALISTS += 1

print(FINALISTS)
