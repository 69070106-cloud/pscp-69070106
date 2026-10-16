"""นักล่าอสูร"""
TEST = [["Spider Demon", 1], ["Swamp Demon", 2], ["Arrow Demon", 1], ["Hand Demon", 2],
    ["Drum Demon", 3], ["Mugen Train", 2], ["Upper Moon", 3],]

KILL = 0
T_ATTACK = 0

while KILL < 5:
    NAME, DEATH_SPOT = TEST.pop(0)
    print(NAME)
    KILLED_THIS_ROUND = False

    for _ in range(2):
        ATTACK = int(input())
        T_ATTACK += 1

        if ATTACK == DEATH_SPOT:
            print("kill")
            KILL += 1
            KILLED_THIS_ROUND = True
            break

    if not KILLED_THIS_ROUND:
        print("back")
        TEST.append([NAME, DEATH_SPOT])

print(T_ATTACK)
