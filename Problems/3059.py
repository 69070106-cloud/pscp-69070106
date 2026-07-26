"""ผลการสอบ"""
FIST = int(input())
MID = int(input())
FINAL = int(input())
TOTAL = FINAL + MID + FIST
if TOTAL < 50 or FIST < 5 or MID < 20 or FINAL < 25:
    print("fail")
else:
    print("pass")
