"""Tuple's Sad life"""
N = tuple(input().split())
M = input()
NUM = N.index(M)
SIDE = N.count(M)
for _ in range(SIDE):
    print(*(str(NUM)*SIDE))
