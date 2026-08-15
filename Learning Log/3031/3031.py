"""[LEARNING LOGS] Ink"""
import math
S, N = map(int, input().split())
PIE = 3.1416
for _ in range(N):
    X, Y = map(float, input().split())
    TIME = (PIE * (X**2 + Y**2)) / S
    print(math.ceil(TIME))
