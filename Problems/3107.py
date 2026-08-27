"""Bonus"""
STATS, AGE, MONEY = input().split()
A = int(AGE)
M = int(MONEY)
P_M = M / 100
BONUS = 0

if STATS == "M":
    BONUS += 1500
    if A <= 5:
        BONUS += P_M * 6
    elif A <= 10:
        BONUS += P_M * 8
    else:
        BONUS += P_M * 10

elif STATS == "B":
    BONUS += 1000
    if A <= 5:
        BONUS += P_M * 5
    elif A <= 10:
        BONUS += P_M * 6
    else:
        BONUS += P_M * 7

elif STATS == "G":
    BONUS += 500
    if A <= 5:
        BONUS += P_M * 4
    elif A <= 10:
        BONUS += P_M * 5
    else:
        BONUS += P_M * 6

print(f"{BONUS:.0f}")
