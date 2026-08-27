"""COnan"""
CHAR = input().lower()
NUM = int(input())
ANS = ""
for i in CHAR:
    A = ord(i)
    AN = A + NUM
    if AN > 122:
        AN = (((AN - 97) + NUM) % 26) + 97
    ANS += chr(AN)

print(ANS)
