"""RectangleArea"""
X1, Y1, W1, H1 = map(int, input().split())
X2, Y2, W2, H2 = map(int, input().split())

LEFT1 = X1
RIGHT1 = X1 + W1
BOTTOM1 = Y1
TOP1 = Y1 + H1

LEFT2 = X2
RIGHT2 = X2 + W2
BOTTOM2 = Y2
TOP2 = Y2 + H2

OVER_W = min(RIGHT2, RIGHT1) - max(LEFT1, LEFT2)
OVER_H = min(TOP1, TOP2) - max(BOTTOM1, BOTTOM2)

if OVER_H > 0 and OVER_W > 0:
    AREA = OVER_H * OVER_W
    print(AREA)
else:
    print("no overlapping")
