"""[LEARNING LOGS] ของขวัญและขโมย"""
N, K, T = map(int, input().split())
if T == 1:
    print(1)
else:
    COUNT = 1
    THINK = 1
    while True:
        THINK = (THINK + K) % N
        if THINK == 1:
            break
        COUNT += 1

        if THINK == T:
            break
    print(COUNT)
