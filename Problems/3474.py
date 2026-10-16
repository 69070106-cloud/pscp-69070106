"""RESISTOR"""
MEAN_NUM = {
    "Black": 0,
    "Brown": 1,
    "Red": 2,
    "Orange": 3,
    "Yellow": 4,
    "Green": 5,
    "Blue": 6,
    "Purple": 7,
    "Grey": 8,
    "White": 9,
}

MULTIPLIER = {
    "Black": 1,
    "Brown": 10,
    "Red": 100,
    "Orange": 1000,
    "Yellow": 10000,
    "Green": 100000,
    "Blue": 1000000,
    "Purple": 10000000,
    "Gold": 0.1,
    "Silver": 0.01,
}

TOLERANCE = {
    "Brown": 0.01,
    "Red": 0.02,
    "Green": 0.005,
    "Blue": 0.0025,
    "Purple": 0.0010,
    "Grey": 0.0005,
    "Gold": 0.05,
    "Silver": 0.10,
}

B1 = input()
B2 = input()
B3 = input()
B4 = input()

if (B1 in MEAN_NUM and B2 in MEAN_NUM and B3 in MULTIPLIER and B4 in TOLERANCE):
    BASE = (MEAN_NUM[B1] * 10 + MEAN_NUM[B2]) * MULTIPLIER[B3]
    LOWER = BASE * (1 - TOLERANCE[B4])
    UPPER = BASE * (1 + TOLERANCE[B4])
    print(f"{LOWER:.4f}")
    print(f"{UPPER:.4f}")
else:
    print("Error")
