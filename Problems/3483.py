"""มาเป็นทีม"""
N, M = map(int, input().split())
if N < 1 or N > 10 or M < 1 or M > 20:
    print("Data Incorrect")
else:
    TOTAL = 0
    TEAMS = []
    DATA_VALID = True

    for _ in range(N):
        SCORE = list(map(int, input().split()))

        if len(SCORE) != M:
            DATA_VALID = False

        for x in SCORE:
            if x < 0 or x > 100:
                DATA_VALID = False
                break

        if not DATA_VALID:
            print("Data Incorrect")
            break
            
        TEAMS.append(SCORE)

    if DATA_VALID:

        for i in range(N):
            TEAM_SCORE = TEAMS[i]
            
            TEAM_SUM = 0
            MAX_SCORE = -1

            for score in TEAM_SCORE:
                TEAM_SUM += score
                
                if score > MAX_SCORE:
                    MAX_SCORE = score
                    
            AVG = TEAM_SUM / M
            TOTAL += TEAM_SUM

            print(f"Team {i + 1}: Average = {AVG:.2f}, Max = {MAX_SCORE}")

        print(f"Total Score of All Teams = {TOTAL}")
