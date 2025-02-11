import random

def ds():
    success = 0
    failure = 0

    while success < 3 and failure < 3: 
        roll = random.randint(1, 21)
        if roll == 20:
            return "revived"
        elif roll <= 10:
            failure += 1
        elif roll == 1:
            failure += 2
        elif roll > 10:
            success += 1

    if success >= 3:
        return "stabilized"
    elif failure >= 3:
        return "died"
    
result = ds()

trials = 1000000
results = {"died": 0, "stabilized": 0, "revived": 0}

for _ in range(trials):
    results[ds()] += 1

for outcome in ["died", "stabilized", "revived"]:
    print(f"{results[outcome] / trials * 100:.2f}%")