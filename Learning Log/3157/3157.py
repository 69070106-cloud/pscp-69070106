"""[LEARNING LOGS] เกมสะสมแต้ม"""
NUM = int(input())
START = 0
for i in range(NUM):
    i += 1-1
    WHATs = input()
    if WHATs == "+":
        START += 10
    elif WHATs == "-":
        START -= 5

print(START)
