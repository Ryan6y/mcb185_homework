import random

rounds = 10
fail = 0
suc = 0
die = 0
stabilize = 0
revived = 0


for i in range(rounds):
    for i in range(3):
        a = random.randint(0, 20)
        if a < 10:
            fail += 1
        elif a >= 10:
            suc += 1
        elif a == 1:
            fail += 2
        elif a == 20:
            suc += 5

    if fail == 3:
        die += 1
    elif suc == 3:
        stabilize += 1
    elif suc >= 3:
        revived += 1

total = (die + stabilize + revived)
print(die/total, stabilize/total, revived/total)
    
