"""Electric_Using"""
N = int(input())
B_COST = 0
TEMP = N

UNITE = min(TEMP, 10)
B_COST += UNITE * 5
TEMP -= UNITE

if TEMP > 0:
    UNITE = min(TEMP, 40)
    B_COST += UNITE * 7
    TEMP -= UNITE

if TEMP > 0:
    UNITE = min(TEMP, 50)
    B_COST += UNITE * 10
    TEMP -= UNITE

if TEMP > 0:
    UNITE = min(TEMP, 100)
    B_COST += UNITE * 12
    TEMP -= UNITE

if TEMP > 0:
    B_COST += TEMP * 15

TOTAL_S = (B_COST * 107) + (N * 50)

ANS = (TOTAL_S + 5) // 10

print(f"{ANS / 10:.1f}")
