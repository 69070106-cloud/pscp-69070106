"""[LEARNING LOGS] BrickBridge"""
A = int(input())
B = int(input())
GOAL = int(input())
TOTAL_A = A
TOTAL_B = B * 5
GOAL_B = GOAL % 5
if TOTAL_B >= GOAL and not GOAL_B:
    print("0")
elif TOTAL_B >= GOAL and GOAL_B and GOAL_B <= TOTAL_A:
    print(GOAL % 5)
elif TOTAL_B + TOTAL_A >= GOAL and GOAL - TOTAL_B > 0:
    print(GOAL - TOTAL_B)
else:
    print("-1")
