import random

rounds = 10000
die = 0
stable = 0
revive = 0

for i in range(rounds):
    f = 0
    s = 0
    rev = False

    for j in range(3):
        a = random.randint(1, 20)
        if a == 20:
            revive += 1
            rev = True
            break
        elif a == 1:
            f += 2
        elif a < 10:
            f += 1
        else:
            s += 1
        if f >= 3:
            die += 1
            break
        elif s >= 3:
            stable += 1
            break

total = (die + stable + revive)

print(die/total)
print(stable/total)
print(revive/total)