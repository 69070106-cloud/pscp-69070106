"""คำนวณค่าแท็กซี่เบื้องต้น"""
LENGHT = int(input())
PRICE = 0

if LENGHT == 1:
    PRICE = 35
elif not LENGHT:
    PRICE = 0
elif LENGHT <= 10:
    PRICE = 35 + ((LENGHT - 1) * 5)
else:
    PRICE = 35 + (9 * 5) + ((LENGHT - 10) * 8)

print(PRICE)
