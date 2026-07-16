"""STORE"""
NUM = float(input())
TA = (NUM /100) * 10
if TA < 50:
    TAX = ((50 + NUM) / 100) * 7
    TOTAL = NUM + 50 + TAX
    print(f"{TOTAL:.2f}")
elif TA > 1000:
    TAX = ((1000 + NUM) / 100) * 7
    TOTAL = NUM + 1000 + TAX
    print(f"{TOTAL:.2f}")
else:
    TAX = ((TA + NUM) / 100) * 7
    TOTAL = NUM + TA + TAX
    print(f"{TOTAL:.2f}")
