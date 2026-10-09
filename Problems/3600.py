"""แคลอรี่"""
TOTAL = 0
while True:
    NUM = int(input())
    if NUM == 1:
        TOTAL += 100
    elif NUM == 2:
        TOTAL += 120
    elif NUM == 3:
        TOTAL += 200
    elif NUM == 4:
        TOTAL += 60
    elif NUM == 5:
        break
print("Bye Bye")
print(f"Total Calories: {TOTAL}")
