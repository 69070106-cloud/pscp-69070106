"""กระต่ายน้อยกินราเมน"""
SIZE, TYPE = map(str, input().split())
TOPPING = input()
TOP = TOPPING[0]
COST = 0
NUM = 0
if len(TOPPING) > 1:
    NUM = int(TOPPING[2::1])
if SIZE == "S" and TYPE == "R":
    COST += 60
    if TOP == "P":
        COST += 15 * NUM
    elif TOP == "E":
        COST += 10 * NUM
    elif TOP == "N":
        COST += 0
elif SIZE == "S" and TYPE == "T":
    COST += 80
    if TOP == "P":
        COST += 15 * NUM
    elif TOP == "E":
        COST += 10 * NUM
    elif TOP == "N":
        COST += 0
elif SIZE == "M" and TYPE == "R":
    COST += 80
    if TOP == "P":
        COST += 15 * NUM
    elif TOP == "E":
        COST += 10 * NUM
    elif TOP == "N":
        COST += 0
elif SIZE == "M" and TYPE == "T":
    COST += 100
    if TOP == "P":
        COST += 15 * NUM
    elif TOP == "E":
        COST += 10 * NUM
    elif TOP == "N":
        COST += 0
elif SIZE == "L" and TYPE == "R":
    COST += 100
    if TOP == "P":
        COST += 15 * NUM
    elif TOP == "E":
        COST += 10 * NUM
    elif TOP == "N":
        COST += 0
elif SIZE == "L" and TYPE == "T":
    COST += 120
    if TOP == "P":
        COST += 15 * NUM
    elif TOP == "E":
        COST += 10 * NUM
    elif TOP == "N":
        COST += 0

print(COST)
