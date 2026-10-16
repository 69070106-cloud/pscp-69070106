"""Difference"""
A = int(input())
B = int(input())
SET_A = set()
SET_B = set()
for _ in range(A):
    SET_A.add(int(input()))

for _ in range(B):
    SET_B.add(int(input()))

ANS = sorted(SET_A - SET_B)
print(*ANS)
