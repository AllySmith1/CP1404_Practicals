import random

num_quick_picks = int(input("How many quick picks? "))

quick_pick = []

for i in range(num_quick_picks):
    for j in range(6):
        quick_pick.append(random.randint(1, 45))
    quick_pick.sort()
    print(quick_pick)
    quick_pick.clear()




