import random

def death_save_simulation():
    successes = 0
    failures = 0

    while True:
        roll = random.randint(1, 20)
        if roll == 1:
            failures += 2
        elif roll == 20:
            return "revived"
        elif roll < 10:
            failures += 1
        else:
            successes += 1

        if failures >= 3:
            return "died"
        if successes >= 3:
            return "stabilized"
