"""Array 2D ตรวจสอบ"""
ARRAY = []
ERROR_ROW = -1
ERROR_COL = -1
for _ in range(5):
    ARRAY.append(list(map(int, input().split())))

for i in range(5):
    if sum(ARRAY[i]) % 2:
        ERROR_ROW = i
        break

for r in range(5):
    COL_SUM = 0
    for n in range(5):
        COL_SUM += ARRAY[n][r]
    if COL_SUM % 2:
        ERROR_COL = r
        break

print(f"{ERROR_ROW} {ERROR_COL}")
