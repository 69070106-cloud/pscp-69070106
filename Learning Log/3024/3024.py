"""SurprisingVote"""
TOTAL = float(input())
MAX = float(input())

TWO = (TOTAL - MAX) / 2
#MID = TWO + ((TOTAL - MAX) % 2)
MIN = TWO - 1
if MIN < 0 :
    MIN = 0

if MAX - MIN <= 2:
    print("Not surprising")
elif MAX - MIN > 2:
    print("Surprising")
