"""ใส่กล่อง"""
W ,L ,S ,T = map(int, input().split())
ANS = []
for i in range(S ,T+1):
    A = W % i
    B = L % i
    ANS.append(A * B)
print(min(ANS))
