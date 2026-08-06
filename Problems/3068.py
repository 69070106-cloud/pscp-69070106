"""ปีอธิกสุรทิน"""
YEAR = int(input())
HUN = YEAR % 100
HUN_F = YEAR % 400
FOUR = YEAR % 4

if not HUN_F or (not FOUR and HUN) or (YEAR < 1582 and not FOUR):
    print("yes")
else:
    print("no")
