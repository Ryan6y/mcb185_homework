import random
import sys

trials = int(sys.argv[1])
days = 365
student = int(sys.argv[2])

def birthday_simulation(trials, days, students):
    shared_count = 0
    for _ in range(trials):
        calendar = [0] * days 
        for _ in range(students):
            bday = random.randint(0, days - 1)
            calendar[bday] += 1
        if any(day > 1 for day in calendar):
            shared_count += 1
    
    probability = (shared_count / trials) * 100
    return probability

probability = birthday_simulation(trials, days, student)

print(f"{student} {probability:.2f}%")    