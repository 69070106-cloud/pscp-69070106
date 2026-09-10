"""โรงแรมกลางกรุง ไม่มีชั้น 13"""
N = input()
ANS = ""
if int(N[0]) > 5:
    ANS += "9"
elif int(N[1]) > 5:
    ANS += "10"
elif int(N[2]) > 5:
    ANS += "11"
elif int(N[3]) > 5:
    ANS += "12"
elif int(N[4]) > 5:
    ANS += "14"
else:
    ANS += "13"

if N == N[::-1]:
    if int(N[0]) + int(N[4]) > 5:
        ANS += "1"
    elif int(N[1]) * int(N[3]) > 5:
        ANS += "2"
    else:
        ANS += "0"
else:
    if int(N[4]) and int(N[0]) // int(N[4]) > 5:
        ANS += "1"
    elif int(N[1]) - int(N[4]) > 5:
        ANS += "2"
    else:
        ANS += "0"

if int(N[0]) + int(N[1]) + int(N[2]) + int(N[3]) + int(N[4]) > 25:
    ANS += "1"
elif int(N[0]) * int(N[1]) * int(N[2]) * int(N[3]) * int(N[4]) > 55:
    ANS += "2"
else:
    ANS += "0"

print(ANS)
