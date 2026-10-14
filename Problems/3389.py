"""Smart Trash Collector"""
TIME = int(input())
for _ in range(TIME):
    PLASTIC, CAN, GLASS = map(float, input().split())
    TOTAL = PLASTIC + CAN + GLASS
    if TOTAL > 50:
        ANS = f"{TOTAL:.1f}, Overloaded"
        if PLASTIC > 20:
            ANS += ", Check Type Plastic"
        if CAN > 20:
            ANS += ", Check Type Can"
        if GLASS > 20:
            ANS += ", Check Type Glass"
        print(ANS)
    else:
        ANS = f"{TOTAL:.1f}"
        if PLASTIC > 20:
            ANS += ", Check Type Plastic"
        if CAN > 20:
            ANS += ", Check Type Can"
        if GLASS > 20:
            ANS += ", Check Type Glass"
        print(ANS)
