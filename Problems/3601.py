"""มากี่คน"""
MAN = 0
WOMAN = 0
TOTAL =0
while True:
    NUM = input()
    if NUM[0] == "-":
        break

    if NUM[-1] in ("1", "3", "5", "7", "9"):
        MAN += 1
    elif NUM[-1] in ("0", "2", "4", "6", "8"):
        WOMAN += 1

    TOTAL += 1
print(f"{MAN} {WOMAN} {TOTAL}")
