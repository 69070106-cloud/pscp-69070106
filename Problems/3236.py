"""รหัสแฝดเทค"""
LONG = int(input())
PASS1 = str(input())
PASS2 = str(input())
NOT9 = 0
ANS = 0
for i in range(LONG):
    P1 = int(PASS1[i])
    P2 = int(PASS2[i])
    if P1 + P2 != 9:
        ANS += 1
        NOT9 += 1

if not ANS:
    print("YES")
else:
    print(f"NO {NOT9}")
