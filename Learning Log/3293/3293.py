"""[LEARNING LOGS] BigFrame"""
CHAR = []
NUM = []
P = "* "
for _ in range(5):
    C = input()
    CHAR.append(C.rstrip())
    NUM.append(len(C.rstrip()))
MAX = max(NUM)+4
TIME = len(CHAR)
print(MAX * "*")
for n in range(TIME):
    P += CHAR[n]
    P += ((MAX - len(P)) - 1) * " "
    P += "*"
    print(P)
    P = "* "
print(MAX * "*")
