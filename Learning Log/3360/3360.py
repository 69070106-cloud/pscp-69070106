"""[LEARNING LOGS] หั่นขนมปัง"""
DATA = input().split()
W = int(DATA[0])
H = int(DATA[1])
_ = int(DATA[2])
_ = int(DATA[3])

X_INPUT = list(map(int, input().split()))
Y_INPUT = list(map(int, input().split()))

X_CUTS = [0]
for x in X_INPUT:
    X_CUTS.append(x)
X_CUTS.append(W)

Y_CUTS = [0]
for y in Y_INPUT:
    Y_CUTS.append(y)
Y_CUTS.append(H)

WIDTHS = []
for i in range(1, len(X_CUTS)):
    w = X_CUTS[i] - X_CUTS[i - 1]
    WIDTHS.append(w)

HEIGHTS = []
for i in range(1, len(Y_CUTS)):
    h = Y_CUTS[i] - Y_CUTS[i - 1]
    HEIGHTS.append(h)

AREAS = []
for w in WIDTHS:
    for h in HEIGHTS:
        AREAS.append(w * h)

AREAS.sort(reverse=True)

print(f"{AREAS[0]} {AREAS[1]}")
