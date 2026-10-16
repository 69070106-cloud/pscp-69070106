"""HINT"""
def check(v, op, k):
    """Check condition."""
    if op == "==":
        return v == k
    if op == "!=":
        return v != k
    if op == ">":
        return v > k
    if op == ">=":
        return v >= k
    if op == "<":
        return v < k
    if op == "<=":
        return v <= k
    return False

A, X = input().split()
B, Y = input().split()
C, Z = input().split()

X = int(X)
Y = int(Y)
Z = int(Z)

for i in range(1000):
    N = f"{i:03d}"

    H = int(N[0])
    T = int(N[1])
    U = int(N[2])

    if check(U, A, X) and check(T, B, Y) and check(H, C, Z):
        print(N)
