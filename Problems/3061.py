"""ผ่าน/ไม่ผ่าน"""
NUM1 = int(input())
NUM2 = int(input())
TOTAL = NUM1 + NUM2
print(TOTAL)

if TOTAL < 50:
    print("fail")
else:
    print("pass")
