"""NUMBER ABBREVIATION"""
NUMBERS = []
while True:
    VAL = int(input())
    if VAL == -1:
        break
    NUMBERS.append(VAL)

if len(NUMBERS) > 0:
    RESULT = []
    
    START = NUMBERS[0]
    PREV = NUMBERS[0]

    for i in range(1, len(NUMBERS)):
        CURRENT = NUMBERS[i]

        if CURRENT == PREV + 1:
            PREV = CURRENT
        else:
            if START == PREV:
                RESULT.append(str(START))
            else:
                RESULT.append(f"{START}-{PREV}")

            START = CURRENT
            PREV = CURRENT

    if START == PREV:
        RESULT.append(str(START))
    else:
        RESULT.append(f"{START}-{PREV}")

    print(", ".join(RESULT))
