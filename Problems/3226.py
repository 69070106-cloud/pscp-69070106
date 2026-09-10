"""Inflation"""
N = int(float(input()) * 100)
K = int(input())
for _ in range(K):
    N += (N * 381) // 10000

print(f"{N // 100}.{N % 100:02d}")
