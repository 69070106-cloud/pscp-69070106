"""SAITAMA"""
PUSH_UP = int(input())
SIT_UP = int(input())
STAND_D = int(input())
RUN = int(input())
D_P = int(input())
D_SI = int(input())
D_R = int(input())
D_ST = int(input())
LIST = []

DAY_P = PUSH_UP / D_P
DAY_SI = SIT_UP / D_SI
DAY_ST = STAND_D / D_ST
DAY_RUN = RUN / D_R

LIST.append(DAY_P)
LIST.append(DAY_SI)
LIST.append(DAY_ST)
LIST.append(DAY_RUN)

print(f"{max(LIST):.0f}")
