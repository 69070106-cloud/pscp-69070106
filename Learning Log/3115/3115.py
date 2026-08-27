"""[LEARNING LOGS] Arcade of Time: Store Check"""
ALL = input().split()
STORE = int(ALL[0])
S_LIST = []
ANS = []
for _ in range(STORE):
    TO, TC = map(int, input().split())
    S_LIST.append([TO, TC])

NUM = input().split()
for i in NUM:
    TIME_V = int(i)
    COUNT = 0
    for r in S_LIST:
        if r[0] <= TIME_V < r[1]:
            COUNT += 1
    ANS.append(COUNT)

print(*ANS)
