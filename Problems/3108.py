"""คำนวณราคาสินค้าโปรโมชั่น"""
A, B, C = map(int, input().split())
ALL = A+B+C
AP = A*25
BP = B*40
CP = C*55
TOTAL = AP+BP+CP
if ALL >= 3:
    TOTAL = TOTAL * 90 // 100
    print(f"{TOTAL:.0f}")
else:
    print(TOTAL)
