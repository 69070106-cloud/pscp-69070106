"""กระต่ายอ้วน"""
TIME = int(input())
N_M = ""
MAX_W = 0
NUM_W = 0
for _ in range (TIME):
    NAME, W = map(str, input().split())
    WEIGH = int(W)
    if WEIGH > MAX_W:
        MAX_W = WEIGH
        N_M = NAME

    if WEIGH > 15:
        NUM_W += 1

print(NUM_W)
print(N_M)
