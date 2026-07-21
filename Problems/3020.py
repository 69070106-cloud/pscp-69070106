"""Coke"""
PRICE = int(input())
LID = int(input())
N_PRICE = int(input())
NUM = int(input())

if not NUM:
    TOTAL = 0
elif not LID:
    TOTAL = NUM * PRICE
else:
    PRO = (NUM - 1) // LID
    TOTAL = PRICE * (NUM - PRO) + (N_PRICE * PRO)


print(TOTAL)
