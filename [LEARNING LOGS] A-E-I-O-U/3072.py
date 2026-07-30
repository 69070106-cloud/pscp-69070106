"""[LEARNING LOGS] A-E-I-O-U"""
WORD = input().lower()
COUNT_A = WORD.count("a")
COUNT_E = WORD.count("e")
COUNT_I = WORD.count("i")
COUNT_O = WORD.count("o")
COUNT_U = WORD.count("u")

if COUNT_A:
    print(f"a : {COUNT_A}")

if COUNT_E:
    print(f"e : {COUNT_E}")

if COUNT_I:
    print(f"i : {COUNT_I}")

if COUNT_O:
    print(f"o : {COUNT_O}")

if COUNT_U:
    print(f"u : {COUNT_U}")
