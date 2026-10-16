"""[LEARNING LOGS] Pad Thai"""
VALID_INGREDIENTS = [
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", 
    "Bean Sprouts", "Noodle", "Chives", "Lime", "Egg", 
    "Oil", "Peanuts"
]

VALID_TASTES = ["Sweet", "Sour", "Salty"]

MY_INGREDIENT = []
while True:
    ITEM = input().strip()
    if ITEM == "Cook":
        break
    MY_INGREDIENT.append(ITEM)

MY_TASTE = []
while True:
    TASTE = input().strip()
    if TASTE == "End":
        break
    MY_TASTE.append(TASTE)

WORNG_INGREDIENT = False
for ITEM in MY_INGREDIENT:
    if ITEM not in VALID_INGREDIENTS:
        WORNG_INGREDIENT = True
        break

INGREDIENT_COMPLETE = True
for req in VALID_INGREDIENTS:
    if req not in MY_INGREDIENT:
        INGREDIENT_COMPLETE = False
        break

TASTE_PERFECT = True
for req in VALID_TASTES:
    if req not in MY_TASTE:
        TASTE_PERFECT = False
        break
for t in MY_TASTE:
    if t not in VALID_TASTES:
        TASTE_PERFECT = False
        break

if WORNG_INGREDIENT:
    print("This is not Pad Thai!")
elif INGREDIENT_COMPLETE == False:
    print("This is bad!")
elif TASTE_PERFECT == False:
    print("Not Bad...")
else:
    print("Delicious!")
