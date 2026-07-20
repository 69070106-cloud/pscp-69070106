"""แลกเปลี่ยนเงิน"""
NUM = int(input())
TEN = 0
FIVE = 0
TWO = 0
ONE = 0

while True:
    if NUM >= 10:
        TEN = NUM // 10
        NUM -= TEN * 10
    elif NUM >= 5:
        FIVE = NUM // 5
        NUM -= FIVE * 5
    elif NUM >= 2:
        TWO = NUM // 2
        NUM -= TWO * 2
    elif NUM >= 1:
        ONE = NUM // 1
        NUM -= ONE
    elif not NUM:
        break

print(f"10 = {TEN}")
print(f"5 = {FIVE}")
print(f"2 = {TWO}")
print(f"1 = {ONE}")
