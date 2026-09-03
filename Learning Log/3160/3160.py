"""[LEARNING LOGS] หาจำนวนเฉพาะ"""
START, END = map(int, input().split())
P_LIST = []
for n in range(START, END+1):
    if n > 1:
        PRIME = True
        for i in range(2, int(n**0.5) + 1):
            if not n % i:
                PRIME = False
                break
        if PRIME:
            P_LIST.append(n)

if P_LIST:
    print(*P_LIST)
print(f"Total primes: {len(P_LIST)}")
