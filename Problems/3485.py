"""รหัสต้องไม่ซ้ำกัน"""
N = int(input())
NUM = list(map(int, input().split()))[:N]
ANS = []

for i in NUM:
    if NUM.count(i) == 1:
        ANS.append(i)

ANS.sort()
print(*ANS)
