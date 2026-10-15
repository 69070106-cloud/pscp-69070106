"""Easy Histogram"""
CHR = input()
HISTROGRAM = {}

for char in CHR:
    if char.isalpha():
        HISTROGRAM[char] = HISTROGRAM.get(char, 0) + 1

S_HIS = sorted(HISTROGRAM.items(), key=lambda item: (item[0].lower(), item[0].isupper()))

for char, count in S_HIS:
    print(f"{char} = {count}")
