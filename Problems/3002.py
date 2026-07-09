"""cyan"""
NAME = input()
SUR = input()
AGE = input()

if len(NAME) >= 5 and len(SUR) >= 5:
    print(NAME[0:2]+SUR[-1]+AGE[-1])
else:
    print(NAME[0]+AGE+SUR[-1])
