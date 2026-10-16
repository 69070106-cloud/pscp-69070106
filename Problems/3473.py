"""FourDirections"""
ARROWS = {
    'U': [
        "  *   ",
        " ***  ",
        "* * * ",
        "  *   ",
        "  *   "
    ],
    'D': [
        "  *   ",
        "  *   ",
        "* * * ",
        " ***  ",
        "  *   "
    ],
    'L': [
        "  *   ",
        " *    ",
        "***** ",
        " *    ",
        "  *   " 
    ],
    'R': [
        "  *   ",
        "   *  ",
        "***** ",
        "   *  ",
        "  *   "
    ]
}

TEXT = input()
SELECT_ARROW = []

for c in TEXT:
    SELECT_ARROW.append(ARROWS[c])

for i in range(5):
    ROWTEXT = ""

    for arrow in SELECT_ARROW:
        ROWTEXT += arrow[i]

    print(ROWTEXT)
