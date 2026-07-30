"""วันเกิด"""
Y1 = int(input())
M1 = int(input())
D1 = int(input())
Y2 = int(input())
M2 = int(input())
D2 = int(input())
DM = 0
if D1 < D2:
     DM = D2 - D1
elif D1 > D2 and D1 == 31:
    DM = D2
elif D1 > D2 and D1 < 31 and M1 < M2:
    DM = (31 - D1) + D2
elif D1 > D2:
    DM = D1 - D2

#print(DM)

if (Y1 == Y2 and M1 == M2 and DM <= 7) or (Y1 == Y2 and M1 < M2 and DM <=7):
    print("0")
elif Y1 < Y2:
    print("1")
elif Y1 > Y2:
    print("2")
elif Y1 == Y2:
    if M1 < M2:
        print("1")
    elif M1 > M2:
        print("2")
    elif M1 == M2 and D1 < D2:
        print("1")
    elif M1 == M2 and D1 > D2:
            print("2")
