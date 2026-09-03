"""ผลรวมของค่าที่มากกว่า"""
N = int(input())
if N == 1:
    NUM1 = int(input())
    NUM2 = int(input())
    print(max(NUM1, NUM2))
else:
    SUM = 0
    ANS = ""
    for i in range(N):
        NUM1 = int(input())
        NUM2 = int(input())
        if i != N-1:
            if i:
                ANS += ' '
            if NUM1 > NUM2:
                SUM += NUM1
                ANS += f"{str(NUM1)} +"
            else:
                SUM += NUM2
                ANS += f"{str(NUM2)} +"
        else:
            if NUM1 > NUM2:
                SUM += NUM1
                ANS += f" {str(NUM1)} ="
            else:
                SUM += NUM2
                ANS += f" {str(NUM2)} ="
    print(f"{ANS} {SUM}")
