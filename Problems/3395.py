"""เข้าแถว"""
N = int(input().split()[0])
H = list(map(int, input().split()))
CUSTOMERS = list(map(int, input().split()))

PREFIX = [0] * N
CURRENT = 0

for i in range(N):
    PREFIX[i] = CURRENT

    if H[i] > CURRENT:
        CURRENT = H[i]

for pos in CUSTOMERS:
    IDX = pos - 1
    FRONT = PREFIX[IDX]

    CHAIR = FRONT - H[IDX] + 1

    if CHAIR < 0:
        CHAIR = 0

    print(CHAIR)
