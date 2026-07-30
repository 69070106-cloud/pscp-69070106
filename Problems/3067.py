"""การเพิ่ม/ลด"""
NUM1 = float(input())
NUM2 = float(input())
NUM3 = float(input())

if NUM1 > NUM2 > NUM3 :
    print("decreasing")
elif NUM1 < NUM2 < NUM3 :
    print("increasing")
else:
    print("neither")
