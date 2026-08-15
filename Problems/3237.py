"""[Recommend] สามเหลี่ยม"""
NUM = int(input())
A = "1"
if NUM <= 3:
    for i in range(1,NUM+1):
        print("0"*i)
else:
    for i in range(1,NUM+1):
        if i < 3 :
            print("0"*i)
        elif i == NUM:
            print("0"*i)
        elif i >= 3:
            print(f"0{A*(i-2)}0")
