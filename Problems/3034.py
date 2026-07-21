"""PORT"""
PEOPLE, ROW = map(int, input().split())
K = 1
ANS = 0
for i in range(PEOPLE):
    NUM = int(input())
    if K > ROW:
        K = 1
    if NUM == K:
        K += 1
    else:
        ANS += 1
    i += 1

print(ANS)
