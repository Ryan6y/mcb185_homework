import sys
import math

numbers = []
for arg in sys.argv[1:]:
    f = float(arg)
    numbers.append(f)

# The number of values
count = len(numbers)
print(f"The number of values: {count}")

# The minimum and maximum values
min = 0
for number in numbers:
    if number <= min:
        min = number
print(f"The minimum: {min}")

max = 0
for number in numbers:
    if number >= max:
        max = number
print(f"The maximum: {max}")

# The mean and standard deviation
total = 0
for number in numbers:
    total += number
mean = total / count
print(f"The mean: {mean}")

variance = 0
for number in numbers:
    variance += (number - mean)**2 / count
std_d = math.sqrt(variance)
print(f"Standard deviation: {std_d:.3f}")

# he median value
if count % 2 == 1:
    median = numbers[count // 2]
else:
    high = numbers[count // 2]
    low = numbers[count // 2 - 1]
    median = (high + low) / 2
print(f"The median: {median}")