"""[LEARNING LOGS] จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
A =  int(input())
B =  int(input())
C =  int(input())
R =  int(input())
ANS = 0

for i in range(A,B+1):
    if (i % C) == R:
        ANS += 1

print(ANS)
