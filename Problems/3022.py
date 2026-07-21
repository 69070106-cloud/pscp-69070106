"""Temperature"""
NUM = float(input())
TEM1 = input()
TEM2 = input()
C = 0
ANS = 0
if TEM1 == "K":
    C = NUM - 273.15
elif TEM1 == "F":
    C = ((NUM - 32) * 5) / 9
elif TEM1 == "R":
    C = ((NUM * 5) / 9) -273.15
elif TEM1 == "C":
    C = NUM

if TEM2 == "K":
    ANS = C + 273.15
elif TEM2 == "F":
    ANS = ((C * 9) / 5) + 32
elif TEM2 == "R":
    ANS = ((C + 273.15) * 9) / 5
elif TEM2 == "C":
    ANS = C

print(f"{ANS:.2f}")
