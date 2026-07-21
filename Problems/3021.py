"""CIRCLE"""
import math
X1 = int(input())
Y1 = int(input())
R1 = int(input())
X2 = int(input())
Y2 = int(input())
R2 = int(input())

D = math.sqrt(((X2 - X1) ** 2) + ((Y2 - Y1) ** 2))

if R1+R2 > D:
    print("overlapping")
elif R1+R2 < D:
    print("no overlapping")
