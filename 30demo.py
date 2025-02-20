import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0

for _ in range(trials):
    birthdays = []
    for _ in range(people):
        birthday = random.randint(0, days - 1)
        birthdays.append(birthday)
    if len(birthdays) != len(set(birthdays)):
        matches += 1
        print(f"{len(birthdays)}")
        print(f"{len(set(birthdays))}")
probability = matches / trials
print(f"Probability of at least two people sharing a birthday: {probability:.4f}")