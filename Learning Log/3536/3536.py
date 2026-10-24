"""[LEARNING LOGS] isPrime_large"""
N = int(input())

if N <= 1:
    print("NO")
else:
    IS_PRIME = True

    LIMIT = int(N ** 0.5)

    for i in range(2, LIMIT + 1):
        if not N % i:
            IS_PRIME = False
            break

    if IS_PRIME:
        print("YES")
    else:
        print("NO")
