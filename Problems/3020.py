"""Coke"""
PRICE = int(input())
LID = int(input())
N_PRICE = int(input())
NUM = int(input())

if LID > 0:
    NUM_A = NUM - 1
    NUM_B = NUM_A // LID
    NUM_C = NUM_A - NUM_B
    TOTAL = ((NUM_B * N_PRICE) + (NUM_C * PRICE)) + PRICE
elif LID == 0 and N_PRICE > 0:
    TOTAL = NUM * N_PRICE
else:
    TOTAL = NUM * PRICE

print(TOTAL)
