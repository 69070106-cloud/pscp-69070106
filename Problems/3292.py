"""Arrow"""
WAY = input().strip()
N = int(input())

for idx, ch in enumerate(WAY):
    if ch == "R":
        for i in range((N * 2) - 1):
            if i < (N - 1):
                print((i * 2) * " ", end="")
                print((N - i) * "*")
            elif i >= (N - 1):
                print(((((N * 2) - 2) - i) * 2) * " ", end="")
                print((N - (((N * 2) - 2) - i)) * "*")
    elif ch == "L":
        for i in range((N * 2) - 1):
            if i < (N - 1):
                print(((N - 1) - i) * " ", end="")
                print((N - i) * "*")
            elif i >= (N - 1):
                print((i - ((N - 1))) * " ", end="")
                print((i - (N - 2)) * "*")

    if idx < len(WAY) - 1:
        print()
