"""หาร 10"""
NUM = int(input())
LIST = []
for i in range(NUM + 1):
    if not i % 10:
        LIST.append(i)

print(*LIST[::-1])
