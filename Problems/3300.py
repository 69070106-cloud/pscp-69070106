"""สมดุลย์ชีวิต"""
N = int(input())
LIST = []
for _ in range(N):
    NUM = int(input())
    LIST.append(NUM)
DAY = 0
H_WORK = 0
L_WORK = 0

for k in range(N):
    NEW = LIST[k]
    if NEW > 18:
        H_WORK += 1
    else:
        L_WORK += 1

NOW = ""
while H_WORK or L_WORK:
    DAY += 1
    if NOW == "H":
        if L_WORK:
            L_WORK -= 1
            NOW = "L"
        else:
            NOW = "R"
    else:
        if H_WORK:
            H_WORK -= 1
            NOW = "H"
        else:
            L_WORK -= 1
            NOW = "L"

print(DAY)
