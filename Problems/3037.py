"""ค่าสูงสุด"""
NUM1 = int(input())
NUM2 = int(input())
NUM3 = int(input())
LIST = []
LIST.append(NUM1)
LIST.append(NUM2)
LIST.append(NUM3)
LIST.sort(reverse=True)
print(LIST[0])
