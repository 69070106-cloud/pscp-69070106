"""[LEARNING LOGS] Impostor"""
from ast import literal_eval
ALIVE = {}
DEAD = {}

while True:
    LINE = input().strip()
    if LINE == "Start":
        break
    if LINE:
        ALIVE.update(literal_eval(LINE))

while True:
    VOTE_NAME = input().strip()
    if VOTE_NAME == "End":
        break
    if VOTE_NAME in ALIVE:
        DEAD[VOTE_NAME] = ALIVE.pop(VOTE_NAME)

IMPOSTER_REMAIN = list(ALIVE.values()).count("Impostor")

print(f"{IMPOSTER_REMAIN} Impostor Remains")
print("***Alive***")

for name in sorted(ALIVE):
    print(f"{name} : {ALIVE[name]}")

print("***Dead***")
for name in sorted(DEAD):
    print(f"{name} : {DEAD[name]}")
