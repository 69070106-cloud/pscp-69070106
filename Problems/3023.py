"""CALCULATOR"""
N = int(input())
STR = 0
for i in range(1, N+1):
    if N == 1:
        STR = 1
    else:
        STR += len(str(i))
        if i != N:
            STR += 1
        elif i == N:
            STR +=1

print(STR)
