"""SumOfNumber"""
N = int(input())
SUM = 0
while SUM != N:
    NUM = int(input())
    if NUM == -1:
        break
    SUM += NUM

print(SUM)
