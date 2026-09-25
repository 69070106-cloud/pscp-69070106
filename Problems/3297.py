"""ตั๋วหนังสุดป่วน"""
TICKET = int(input())
T_LIST = []
while TICKET > 0 :
    AGE, WANT = map(int, input().split())
    if AGE < 15:
        T_LIST.append(-1)
    elif TICKET < WANT:
        T_LIST.append(-2)
    elif 15 <= AGE <= 22:
        TICKET -= WANT
        T_LIST.append((f"{(WANT*((150/100)*80)):.0f}", TICKET))
    elif AGE >= 60:
        TICKET -= WANT
        T_LIST.append((f"{(WANT*((150/100)*50)):.0f}", TICKET))
    else:
        TICKET -= WANT
        T_LIST.append(((WANT*150), TICKET))

for i in T_LIST:
    if isinstance(i, tuple):
        print(*i)
    else:
        print(i)
