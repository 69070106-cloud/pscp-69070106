"""Color"""
COL1 = input().lower()
COL2 = input().lower()
if (COL1 == "red" and COL2 == "yellow") or (COL2 == "red" and COL1 == "yellow"):
    print("Orange")
elif (COL1 == "red" and COL2 == "blue") or (COL2 == "red" and COL1 == "blue"):
    print("Violet")
elif (COL1 == "yellow" and COL2 == "blue") or (COL2 == "yellow" and COL1 == "blue"):
    print("Green")
elif COL1 == "red" and COL2 == "red":
    print("Red")
elif COL1 == "yellow" and COL2 == "yellow":
    print("Yellow")
elif COL1 == "blue" and COL2 == "blue":
    print("Blue")
else:
    print("Error")
