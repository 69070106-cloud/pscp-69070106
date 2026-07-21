"""TIKTOK"""
R, X, Y = map(int,input().split())
TOTAL = (X ** 2) + (Y ** 2)
RAD = R ** 2
if TOTAL == RAD:
    print("ON")
elif TOTAL > RAD :
    print("OUT")
else:
    print("IN")
