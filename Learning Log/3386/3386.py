"""[LEARNING LOGS] Duplicate I"""
M = int(input())
N = int(input())
GROUP1 = set()
GROUP2 = set()

for _ in range(M):
    GROUP1.add(int(input()))

for _ in range(N):
    GROUP2.add(int(input()))

SAME = GROUP1 & GROUP2

if not SAME:
    print("Nope")
else:
    ANS = sorted(SAME, reverse=True)
    for i in ANS:
        print(i)
