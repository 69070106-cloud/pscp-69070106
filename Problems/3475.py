"""MUDDLED MENU"""
MENU = []

while True:
    TEXT = input()
    if TEXT == "DONE":
        break

    if TEXT == "CLOSED":
        MENU.clear()
        break

    if TEXT == "SOMETHING'S WRONG":
        MENU.clear()
        continue

    if TEXT == "Can't do":
        if len(MENU) > 0:
            MENU.pop()
        continue

    if TEXT.startswith("Can't do:"):
        FOOD = TEXT[10:]
        if FOOD in MENU:
            MENU.remove(FOOD)
        continue

    if " #" in TEXT:
        DATA = TEXT.rsplit(" #", 1)
        FOOD = DATA[0]
        ORDER = DATA[1]

        if ORDER == "N":
            MENU.append(FOOD)
        elif ORDER.isdigit():
            POS = int(ORDER) - 1

            if POS > len(MENU):
                POS = len(MENU)

            MENU.insert(POS, FOOD)

REVERSED_MENU = MENU[::-1]
print(f"Full Course: {MENU} Reversed: {REVERSED_MENU}")
