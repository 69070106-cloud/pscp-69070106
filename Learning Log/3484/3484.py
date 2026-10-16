"""[LEARNING LOGS] หุ่นยนต์เคาะเสียงกระเบื้อง"""
INPUT_DATA = input().split()
N = int(INPUT_DATA[0])
P = float(INPUT_DATA[1])

GRID = []

for _ in range(N):
    row = list(map(int, input().split()))
    GRID.append(row)

COL_TILES = [0] * N
COL_POINTS = [0] * N

TOTAL_TILES = 0
TOTAL_POINTS = 0

for r in range(N):
    ROW_TITLE = 0
    ROW_POINT = 0
    
    for c in range(N):
        VAL = GRID[r][c]

        if VAL > 0:
            ROW_TITLE += 1
            ROW_POINT += VAL
            
            COL_TILES[c] += 1
            COL_POINTS[c] += VAL
            
            TOTAL_TILES += 1
            TOTAL_POINTS += VAL

    print(*GRID[r], ROW_TITLE, ROW_POINT)

print(*COL_TILES)

print(*COL_POINTS)

TOTAL_PENALTY = TOTAL_POINTS * P
print(f"{TOTAL_TILES} {TOTAL_POINTS} {TOTAL_PENALTY:.2f}")
