"""สหกรณ์โรงเรียน"""
from decimal import Decimal, ROUND_HALF_UP
STATS = input()
N = int(input())
TOTAL = Decimal("0")
for _ in range(N):
    COST = Decimal(input())
    TOTAL += COST
if STATS == "Y":
    TOTAL =TOTAL * Decimal("95") / Decimal("100")
elif STATS == "N":
    if TOTAL >= Decimal("500"):
        TOTAL = TOTAL * Decimal("97") / Decimal("100")
TOTAL  = TOTAL.quantize(Decimal('0.00'), rounding = ROUND_HALF_UP)
print(f"{TOTAL:.2f}")
