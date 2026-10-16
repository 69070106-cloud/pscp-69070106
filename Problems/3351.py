"""พูดจาภาษากระต่าย"""
TEXT = input().upper()
N = len(TEXT)
ALL_IT = True
for c in TEXT:
    if c not in "IT":
        ALL_IT = False
        break

if ALL_IT:
    print(f"unknown {N}")
else:
    BEST = 0
    COUNT = 0
    ERROR = -1

    for i in range(N):
        c = TEXT[i]

        if c not in "RABIT":
            ERROR = i
            break

        if c == "A":
            if not i or TEXT[i-1] not in "RA":
                ERROR = i
                break

            COUNT += 1

            if COUNT > BEST:
                BEST = COUNT
        else:
            COUNT = 0

        if c == "R" and (i == N - 1 or TEXT[i+1] != "A"):
            if i + 1 < N:
                ERROR = i + 1
            else:
                ERROR = i
            break

        if c == "B" and (i == N - 1 or TEXT[i+1] not in "IT"):
            if i + 1 < N:
                ERROR = i + 1
            else:
                ERROR = i
            break

    if ERROR != -1:
        print(f"no {ERROR}")
    else:
        print(f"yes {BEST}")
