"""Name of Card"""
CHAR = input()
NUM = CHAR[:-1].upper()
TYPE = CHAR[-1].upper()

if TYPE == "D":
    if NUM in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
        print(f"{NUM} of Diamonds")
    elif NUM == "A":
        print("Ace of Diamonds")
    elif NUM == "J":
        print("Jack of Diamonds")
    elif NUM == "Q":
        print("Queen of Diamonds")
    elif NUM == "K":
        print("King of Diamonds")
elif TYPE == "H":
    if NUM in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
        print(f"{NUM} of Hearts")
    elif NUM == "A":
        print("Ace of Hearts")
    elif NUM == "J":
        print("Jack of Hearts")
    elif NUM == "Q":
        print("Queen of Hearts")
    elif NUM == "K":
        print("King of Hearts")
elif TYPE == "S":
    if NUM in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
        print(f"{NUM} of Spades")
    elif NUM == "A":
        print("Ace of Spades")
    elif NUM == "J":
        print("Jack of Spades")
    elif NUM == "Q":
        print("Queen of Spades")
    elif NUM == "K":
        print("King of Spades")
elif TYPE == "C":
    if NUM in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
        print(f"{NUM} of Clubs")
    elif NUM == "A":
        print("Ace of Clubs")
    elif NUM == "J":
        print("Jack of Clubs")
    elif NUM == "Q":
        print("Queen of Clubs")
    elif NUM == "K":
        print("King of Clubs")
