"""safe"""
WORD = input()
NUM = input()
if WORD == "H" and NUM == "4567":
    print("safe unlocked")
elif WORD == "H":
    print("safe locked - change digit")
elif NUM == "4567":
    print("safe locked - change char")
else:
    print("safe locked")
