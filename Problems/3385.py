"""BusStop I"""
P = int(input())
N = int(input())
BUS = []
SIGN = {}
ANS = 0

for i in range(N):
    NUM = list(map(int, input().split()))
    SIGN[NUM[0]] = NUM[1:]

for i in range(1,N+1):
    NOW = BUS.count(i)
    ANS += NOW

    while i in BUS:
        BUS.remove(i)

    if i in SIGN:
        for n in SIGN[i]:
            if n > i:
                if len(BUS) < P:
                    BUS.append(n)
                else:
                    break

print(ANS)
