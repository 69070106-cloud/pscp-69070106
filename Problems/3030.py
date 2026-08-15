"""SAITAMA"""
import math
PUSH_UP = int(input())
SIT_UP = int(input())
STAND_D = int(input())
RUN = int(input())
D_P = int(input())
D_SI = int(input())
D_R = int(input())
D_ST = int(input())

DAY_P = PUSH_UP / D_P
DAY_SI = SIT_UP / D_SI
DAY_ST = STAND_D / D_ST
DAY_RUN = RUN / D_R

MAX_D = max(DAY_P, DAY_SI, DAY_ST, DAY_RUN)

print(math.ceil(MAX_D))
