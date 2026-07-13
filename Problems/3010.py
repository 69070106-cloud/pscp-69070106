"""QUADrant"""
X = float(input())
Y = float(input())
if X > 0 and Y > 0:
    print("Q1")
elif X < 0 < Y:
    print("Q2")
elif X < 0 and Y < 0:
    print("Q3")
elif X > 0 > Y:
    print("Q4")
elif not X and Y :
    print("Y")
elif not Y and X:
    print("X")
elif not X and not Y:
    print("O")
