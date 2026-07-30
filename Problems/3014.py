"""MILK"""
A = int(input())
B = int(input())
C = int(input())
D = int(input())
NUM = D // A
NUM1 = (NUM // B) * C
NUM2 = NUM1 // B
if B > 0 and C >= 0 and C < B and NUM2 == 0:
    TOTAL = NUM1 + NUM
elif NUM2 > 0:
    TOTAL = (NUM2 * C) + NUM + NUM1
else:
    TOTAL = NUM
print(TOTAL)
