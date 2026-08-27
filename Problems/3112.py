"""ชานมไข่มุก"""
MOOK, NM = input().split()
TEA, SWEET, NT = input().split()

N_M = float(NM)
N_T = float(NT)
CAL = 0.0

if TEA == "R":
    if SWEET == "1":
        CAL += 12 * N_T
    elif SWEET == "2":
        CAL += 18 * N_T
    elif SWEET == "3":
        CAL += 25 * N_T
elif TEA == "T":
    if SWEET == "1":
        CAL += 15 * N_T
    elif SWEET == "2":
        CAL += 20 * N_T
    elif SWEET == "3":
        CAL += 30 * N_T
elif TEA == "M":
    if SWEET == "1":
        CAL += 10 * N_T
    elif SWEET == "2":
        CAL += 15 * N_T
    elif SWEET == "3":
        CAL += 20 * N_T

if MOOK == "H":
    CAL += 5 * N_M
elif MOOK == "O":
    CAL += 3 * N_M
elif MOOK == "J":
    CAL += 2 * N_M

if CAL.is_integer():
    print(int(CAL))
else:
    print(CAL)
