"""บุพเพสันนิวาส"""
NAME_1 = input()
NAME_2 = input()

LEN_1 = len(NAME_1)
LEN_2 = len(NAME_2)

if LEN_1 < LEN_2:
    DIFF = LEN_2 - LEN_1
    for i in range(DIFF):
        NAME_1 += NAME_1[i % LEN_1]

elif LEN_2 < LEN_1:
    DIFF = LEN_1 - LEN_2
    for i in range(DIFF):
        NAME_2 += NAME_2[i % LEN_2]

LOVE = "loveLOVE"
TALISMAN = []

for i, c in enumerate(NAME_1):
    if c in LOVE or NAME_2[i] in LOVE:
        TALISMAN.append("w")
    else:
        TALISMAN.append("$")

RESULT = "".join(TALISMAN)
TOTAL_W = RESULT.count("w")

if TOTAL_W % 2:
    MAX_W = 0
    CURR_W = 0
    for c in RESULT:
        if c == "w":
            CURR_W += 1
            if CURR_W > MAX_W:
                MAX_W = CURR_W
        else:
            CURR_W = 0

    RESULT += str(MAX_W)
else:
    if "ww" not in RESULT:
        RESULT += "#"

print(RESULT)
