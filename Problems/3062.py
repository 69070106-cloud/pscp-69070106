"""ค่าตั๋ว"""
AGE = int(input())
STAT = input()

if AGE < 18 or STAT in ("s", "S"):
    print("20")
else:
    print("50")
