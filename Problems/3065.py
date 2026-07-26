"""ตัวเลขโรมันแบบง่าย"""
NUM = int(input())

if 1 <= NUM <= 3 :
    print("I" * NUM)
elif NUM == 4 :
    print("IV")
elif  1 <= NUM < 9 :
    print("V" + "I" * (NUM - 5))
elif NUM == 9:
    print("IX")
elif NUM < 0:
    print("Error : Please input positive number")
elif NUM > 9 or not NUM:
    print("Error : Out of range")
