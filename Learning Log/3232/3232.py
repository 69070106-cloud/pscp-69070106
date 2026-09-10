"""[LEARNING LOGS] กบน้อยกระโดด"""
JUMP, GOAL = map(int, input().split())
NOW = 0
TIME = 0
while True:
    NOW += JUMP
    TIME += 1
    if NOW >= GOAL:
        print(TIME)
        break
    if NOW < GOAL and JUMP <= 0:
        print("-1")
        break
    JUMP -= 2
