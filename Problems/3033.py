"""กระดาษห่อของขวัญ"""
R, H, T = map(float,input().split())
WIDE = (R * 2) + H
LONG = ((2* 3.14) * R) + T
print(f"{WIDE:.2f} {LONG:.2f}")
