"""Day08-0_02-Backward"""
C_LIST = []
while True:
    CHR = input()
    if CHR == "NULL":
        break
    C_LIST.append(CHR)
for idx, _ in enumerate(C_LIST):
    print(C_LIST[(idx*-1)-1])
