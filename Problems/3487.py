"""ติดตั้งหลอดไฟ"""
N = int(input())
HEIGHT = []

for _ in range(N):
    HEIGHT.append(int(input()))

HEIGHT.sort()

TOTAL = 0
LEFT = 0

for h in HEIGHT:
    LEFT += h
    TOTAL += LEFT * 2

print(TOTAL)
