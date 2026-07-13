"""CALCULATOR"""
N = int(input())
I = 1
STR = "1"
while True:
    if I < N:
        I += 1
        STR += (f"+{I}")
        if I == N:
            STR += "="
            break
    elif N == 1:
        break

print(len(STR))
