"""กองชาม"""
N = int(input())
CUP = {}

for _ in range(N):
    SIZE = int(input())

    if SIZE in CUP:
        CUP[SIZE] += 1
    else:
        CUP[SIZE] = 1

print(max(CUP.values()))
