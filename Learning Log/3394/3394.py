"""[LEARNING LOGS] ส่งต่อ"""
N, S = map(int, input().split())
FORWARD = [0] * (N + 1)

for i in range(1, N + 1):
    FORWARD[i] = int(input())

VISITED = [False] * (N + 1)

CURR = S
ANS = 0

while CURR and VISITED[CURR] is False:
    VISITED[CURR] = True
    ANS += 1
    CURR = FORWARD[CURR]

print(ANS)
