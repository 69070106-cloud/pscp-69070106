"""Heron"""
A = float(input())
B = float(input())
C = float(input())
S = (A+B+C) / 2
AREA = (S*(S-A)*(S-B)*(S-C)) ** 0.5
print(f"{AREA:.3f}")
