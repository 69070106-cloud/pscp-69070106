"""นับเลขคู่และเลขคี่"""
NUM1 = int(input())
NUM2 = int(input())
NUM3 = int(input())
KE = 0
KU = 0

if not NUM1 % 2:
    KU += 1
else:
    KE += 1

if not NUM2 % 2:
    KU += 1
else:
    KE += 1

if not NUM3 % 2:
    KU += 1
else:
    KE += 1

print(KU)
print(KE)
