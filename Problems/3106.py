"""ATM"""
M = int(input())
T = 0
H = 0
R = 0

if M <= 0 or M % 100:
    print("ERROR")
elif M >= 100:
    T = M // 1000
    T1 = abs((T * 1000) - M)
    H = T1 // 500
    H1 = abs((H * 500) - T1)
    R = H1 // 100
    if T:
        print(f"1000 = {T}")
    if H:
        print(f"500 = {H}")
    if R:
        print(f"100 = {R}")
