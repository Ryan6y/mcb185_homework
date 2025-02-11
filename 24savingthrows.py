import random

def advantage:
    roll1 = random.randint(1, 20)
    roll2 = random.randint(1, 20)
    if roll1 > roll2: return roll1
    return roll2

trials = 1000000
dc = 5
for dc in range(5, 16, 5):
        success = 0
        for i in range(trials):
            roll advantage()
            if roll >= dc: success += 1
        print(dc, success/tirals)