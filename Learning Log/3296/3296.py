"""[LEARNING LOGS] RGB Mixed"""
R1, G1, B1 = map(int, input().split())
R2, G2, B2 = map(int, input().split())
R_A = (R1 + R2) // 2
G_A = (G1 + G2) // 2
B_A = (B1 + B2) // 2
print(f"{R_A} {G_A} {B_A}")
