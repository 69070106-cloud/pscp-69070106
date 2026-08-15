"""[LEARNING LOGS] ปราสาท"""
import math
N = int(input())
if N == 1:
    print("0")
else:
    ROW = math.ceil(math.sqrt(N))
    COL = N - ((ROW-1)**2)
    COL2 = COL % 2

    if COL2:
        print(2 * (ROW - 1))
    else:
        print((2 * ROW) - 3)
