"""นวัตกรรมงบประมาณโรงเรียน"""
SCHOOL = input()
F = ord(SCHOOL[0].upper())
L = ord(SCHOOL[-1].upper())
N = len(SCHOOL)

ANS = []

for i in range(10):
    if not i or not i % 2:
        ANS.append(((i + F) % N) % 10)
    else:
        ANS.append(((L - i) % N) % 10)

print(*ANS[2:8])
