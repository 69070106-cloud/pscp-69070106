"""COnan"""
CHAR = input().lower()
NUM = int(input())
for i in CHAR:
    A = ord(i)
    AN = A - ord("a")
    CH = (AN + NUM) % 26
    print(chr(CH + 97),end="")
