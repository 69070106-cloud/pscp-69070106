"""[LEARNING LOGS] ไพ่ 44 ใบ"""
CHAR = input()
NUM = CHAR[:-1].upper()
TYPE = CHAR[-1].upper()

if TYPE == "D":
    if NUM in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
        print(f"{NUM} of diamonds")
    elif NUM == "A":
        print("ace of diamonds")
    elif NUM == "J":
        print("jack of diamonds")
    elif NUM == "Q":
        print("queen of diamonds")
    elif NUM == "K":
        print("king of diamonds")
elif TYPE == "H":
    if NUM in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
        print(f"{NUM} of hearts")
    elif NUM == "A":
        print("ace of hearts")
    elif NUM == "J":
        print("jack of hearts")
    elif NUM == "Q":
        print("queen of hearts")
    elif NUM == "K":
        print("king of hearts")
elif TYPE == "S":
    if NUM in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
        print(f"{NUM} of spades")
    elif NUM == "A":
        print("ace of spades")
    elif NUM == "J":
        print("jack of spades")
    elif NUM == "Q":
        print("queen of spades")
    elif NUM == "K":
        print("king of spades")
elif TYPE == "C":
    if NUM in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
        print(f"{NUM} of clubs")
    elif NUM == "A":
        print("ace of clubs")
    elif NUM == "J":
        print("jack of clubs")
    elif NUM == "Q":
        print("queen of clubs")
    elif NUM == "K":
        print("king of clubs")
