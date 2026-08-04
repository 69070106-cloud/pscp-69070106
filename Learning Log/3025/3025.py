"""SEASON"""
MONTH = int(input())
DAY = int(input())

if MONTH in (1, 2, 3):
    if MONTH == 3 and DAY >= 21:
        print("spring")
    else:
        print("winter")
elif MONTH in (4, 5, 6):
    if MONTH == 6 and DAY >= 21:
        print("summer")
    else:
        print("spring")
elif MONTH in (7, 8, 9):
    if MONTH == 9 and DAY >= 21:
        print("fall")
    else:
        print("summer")
elif MONTH in (10, 11, 12):
    if MONTH == 12 and DAY >= 21:
        print("winter")
    else:
        print("fall")
