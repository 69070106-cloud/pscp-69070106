"""ค่าน้อยที่สุด"""
NUM1 = int(input())
NUM2 = int(input())
NUM3 = int(input())
LIST = []
LIST.append(NUM1)
LIST.append(NUM2)
LIST.append(NUM1)
LIST.sort(reverse=False)
print(LIST[0])
