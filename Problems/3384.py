"""PickThem"""
N = input()
N_LIST = list(map(int, N.strip('[]').split(',')))
NOW_LIST = []
for i in N_LIST:
    if not i % 2 or not i:
        NOW_LIST.append(i)
if not NOW_LIST:
    print("Nope")
else:
    for r in NOW_LIST:
        print(r)
