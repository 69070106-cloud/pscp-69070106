"""วิเคราะห์ยอดขายร้านกาแฟ"""
N = int(input())
SELL1 = int(input())
SUM = SELL1
MAX = SELL1
MIN = SELL1
for _ in range(N-1):
    SELL = int(input())
    SUM += SELL
    if  MAX < SELL:
        MAX = SELL
    if MIN > SELL:
        MIN = SELL
AVG = round(SUM / N, 1)
print(SUM)
print(MAX)
print(MIN)
print(f"{AVG:.1f}")
