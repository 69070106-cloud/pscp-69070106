"""[LEARNING LOGS] Giraffe"""
N = int(input())
N_LIST = []
FULL = 0
for _ in range(N):
    HEGHT = int(input())
    N_LIST.append(HEGHT)
if N == 1:
    print('1')
else:
    if N_LIST[0] > N_LIST[1]:
        FULL += 1
    if N_LIST[-1] > N_LIST[-2]:
        FULL += 1
    for i in range(1,N-1):
        if N_LIST[i] > N_LIST[i-1] and N_LIST[i] > N_LIST[i+1]:
            FULL += 1
    print(FULL)
