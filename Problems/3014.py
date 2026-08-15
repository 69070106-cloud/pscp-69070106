"""MILK"""
A = int(input())
B = int(input())
C = int(input())
D = int(input())
TOTAL = D // A
CAP = TOTAL

if B > 0:
    while CAP >= B:
        MILK_P = (CAP // B) * C
        CAP_L = CAP % B
        TOTAL += MILK_P
        CAP = MILK_P + CAP_L

print(TOTAL)
