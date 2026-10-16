"""นักสำรวจถ้ำ (Cave Explorer)"""
N = int(input())
CAVE = list(map(int, input().split()))
CMDS = input().strip()

CODE = CAVE.index(1)
CHEST = CAVE.index(2)

for i in CMDS:
    if i == "R":
        if CODE + 1 < N:
            CODE += 1
   
    elif i == "L":
        if CODE - 1 >= 0:
            CODE -= 1

    if CODE == CHEST:
        break

NEW_MAP = [0] * N
NEW_MAP[CODE] = 1

if CODE != CHEST:
    NEW_MAP[CHEST] = 2

print(*NEW_MAP)
