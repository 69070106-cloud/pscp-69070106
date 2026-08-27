"""[LEARNING LOGS] สงคราม...ส่งด่วน"""
START ,END = input().split()
WEIGHT = float(input())
if START == "BKK" and END == "CNX":
    T = 10
    WEIGHT = WEIGHT * 30
    TOTAL = WEIGHT + T
    print(f"{TOTAL:.2f}")
elif START == "CNX" and END == "UBP":
    T = 15
    WEIGHT = WEIGHT * 40
    TOTAL = WEIGHT + T
    print(f"{TOTAL:.2f}")
elif START == "UBP" and END == "BKK":
    T = 20
    WEIGHT = WEIGHT * 40
    TOTAL = WEIGHT + T
    print(f"{TOTAL:.2f}")
elif START == "BKK" and END == "PKT":
    T = 25
    WEIGHT = WEIGHT * 50
    TOTAL = WEIGHT + T
    print(f"{TOTAL:.2f}")
elif START == "PKT" and END == "CNX":
    T = 30
    WEIGHT = WEIGHT * 60
    TOTAL = WEIGHT + T
    print(f"{TOTAL:.2f}")
elif START == "UBP" and END == "PKT":
    T = 40
    WEIGHT = WEIGHT * 70
    TOTAL = WEIGHT + T
    print(f"{TOTAL:.2f}")
else:
    print("Error")
