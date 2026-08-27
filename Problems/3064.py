"""Birthday"""
from datetime import date

Y1 = int(input())
M1 = int(input())
D1 = int(input())
Y2 = int(input())
M2 = int(input())
D2 = int(input())
G1 = date(Y1, M1, D1)
G2 = date(Y2, M2, D2)
DIFF = abs((G1 - G2).days)
if DIFF <= 7:
    print(0)
elif G1 < G2:
    print(1)
else:
    print(2)
