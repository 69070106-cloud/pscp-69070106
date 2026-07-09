"""Frame"""
WORD = input()
DOT = ""
LAST = f"*{WORD}*"
while len(DOT) != len(LAST):
    DOT += "*"

print(DOT)
print(LAST)
print(DOT)
