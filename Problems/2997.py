"""Elo"""
RA = int(input())
RB = int(input())
WHO = input()

if WHO == "A":
    CAL = 1 - (1/(1 + (10**((RA - RB)/400))))
    print(f"{CAL:.2f}")
elif WHO == "B":
    CAL = 1 - (1/(1 + (10**((RB - RA)/400))))
    print(f"{CAL:.2f}")
