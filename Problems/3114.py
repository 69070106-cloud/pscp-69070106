"""Suvarnabhumi Airport Parking"""
H_IN, M_IN = map(int, input().split('.'))
H_OUT, M_OUT = map(int, input().split('.'))
IN = (H_IN * 60) + M_IN
OUT = (H_OUT * 60) + M_OUT
DIFF = OUT - IN
CHECKT1 = (0 <= H_IN <= 23) and (0 <= M_IN <= 59)
CHECKT2 = (0 <= H_OUT <= 23) and (0 <= M_OUT <= 59)

if not CHECKT1 or not CHECKT2 or DIFF < 0:
    print("ERROR")
elif DIFF <= 15:
    print("FREE")
else:
    HOURS = DIFF // 60
    if DIFF % 60 > 0:
        HOURS += 1

    if HOURS == 1:
        print(25)
    elif HOURS == 2:
        print(50)
    elif HOURS == 3:
        print(80)
    elif HOURS == 4:
        print(110)
    elif HOURS == 5:
        print(145)
    elif HOURS == 6:
        print(180)
    elif 7 <= HOURS <= 24:
        print(250)
    else:
        print("ERROR")
