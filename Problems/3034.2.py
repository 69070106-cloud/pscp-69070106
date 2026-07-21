"""PORT"""
PEOPLE, ROW = map(int, input().split())
LIST = []
N_LIST = []
ANS = 0

for i in range(PEOPLE):
    i = i + 1 - 1
    NUM = int(input())
    if NUM > ROW:
        ANS += 1
    else:
        LIST.append(NUM)

for p in range(ROW):
    p += 1
    COUNT_N = LIST.count(p)
    N_LIST.append(COUNT_N)

for m in range(ROW):
    A = N_LIST[m]
    ANS += A - min(N_LIST)

print(ANS)
