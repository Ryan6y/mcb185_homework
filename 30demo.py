import random

shared = 0
trials = 1
days = 365
students = 23

calender = []
for i in range(days):
    calender.append(0)

for i in range(students):
    bday = random.randint(0, days)
    calender[bday] += 1

for i in range(calender):
    if calender[bday] > 1 : print('found')
print()

print(f"{shared/trials*100}"'%')