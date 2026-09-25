"""กระต่ายน้อยรัก BUU"""
S = input().strip()
S_UPPER = S.upper()

MAX_U = 0
for i, char in enumerate(S_UPPER):
    if char == 'B':
        COUNT = 0
        j = i + 1
        while j < len(S_UPPER) and S_UPPER[j] == 'U':
            COUNT += 1
            j += 1
        if COUNT > MAX_U:
            MAX_U = COUNT

if MAX_U >= 2:
    print(f"Yes {MAX_U}")
elif 'B' in S_UPPER:
    F_B_INDEX = -1
    for i, char in enumerate(S):
        if char in ('B', 'b'):
            F_B_INDEX = i
            break
    PREFIX = S[:F_B_INDEX + 1]
    REMAIN_LENGHT = len(S) - len(PREFIX)
    print(PREFIX + ('U' * REMAIN_LENGHT))

else:
    PATTERN = "BUU" * len(S)
    print(PATTERN[:len(S)])
