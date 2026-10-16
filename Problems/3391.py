"""สะสมเหรียญเวทย์มนตร์"""
N = int(input())
TOTAL1F = 0
TOTAL1W = 0
TOTAL1E = 0

for _ in range(N):
    F1, W1, E1, F2, W2, E2 = map(int, input().split())
    TOTAL1F += max(F1, F2)
    TOTAL1W += max(W1, W2)
    TOTAL1E += max(E1, E2)

TOTAL = TOTAL1F + TOTAL1W + TOTAL1E
print(f"Total: {TOTAL}")
print(f"Fire: {TOTAL1F}")
print(f"Water: {TOTAL1W}")
print(f"Earth: {TOTAL1E}")

if TOTAL1F > TOTAL1W + TOTAL1E:
    print("Bonus: YES")
else:
    print("Bonus: NO")
