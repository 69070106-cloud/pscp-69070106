"""Bus Seat"""
N = int(input())
M = int(input())
X = int(input())

for r in range(N - 1, -1, -1):
    row = []
    for c in range(M):
        seat = (c * N) + r + 1

        if seat == X:
            row.append("XX")
        else:
            row.append(f"{seat:02d}")

    print(" ".join(row))

    if not r % 2 and r:
        print()
