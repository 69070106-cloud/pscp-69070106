"""BIRD"""
N = int(input())
H = list(map(int, input().split()))
ANS = 0

for i in range(N):
    LEFT_OK = (not i or H[i] > H[i - 1])
    RIGHT_OK = (i == N - 1 or H[i] > H[i + 1])

    if LEFT_OK and RIGHT_OK:
        ANS += 1
print(ANS)
