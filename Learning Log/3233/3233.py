"""[LEARNING LOGS] สลากกินแบ่ง"""
C1, N1 = input().split()
C2, N2 = input().split()
if C1 == C2 and N1 == N2:
    print("1000000")
elif N1 == N2:
    print("100000")
elif C1 == C2 and N1[2::1] == N2[2::1]:
    print("2000")
elif C1 == C2 and N1[3::1] == N2[3::1]:
    print("1000")
elif N1[2::1] == N2[2::1]:
    print("200")
elif N1[3::1] == N2[3::1]:
    print("100")
elif C1 == C2:
    print("20")
else:
    print("0")
