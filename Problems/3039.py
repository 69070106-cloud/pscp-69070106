"""ค่าน้อยที่สุด (4 ค่า)"""
NUM = int(input())
TOT = 0
LIST = []
while TOT != NUM:
    NUM_1 = int(input())
    TOT += 1
    LIST.append(NUM_1)

LIST.sort(reverse=False)
print(LIST[0])
