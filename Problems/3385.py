"""BusStop I"""
P = int(input())
N = int(input())
BUS = []
SIGN = {}
for i in range(N):
    N = list(map(int, input().split()))
    SIGN[N[0]] = N[1:]
for sign, people in SIGN:
    print(people)
