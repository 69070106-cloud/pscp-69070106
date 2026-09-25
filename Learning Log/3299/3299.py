"""[LEARNING LOGS] แปลงดอกไม้"""
L, N = map(int, input().split())
K = 1
while True:
    MAX_C = (K * L) * (K * L + 1) // 2
    if MAX_C >= N:
        print(K)
        break
    K += 1
