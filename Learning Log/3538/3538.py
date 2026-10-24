"""B-Fully"""
PAIR = input()
NO_PAIR = ""
TEXT_C = []

for char in PAIR:
    if char not in TEXT_C:
        TEXT_C.append(char)
        count = PAIR.count(char)
        if count % 2:
            NO_PAIR += char

if not NO_PAIR:
    print("fully paired")
else:
    print(NO_PAIR)
