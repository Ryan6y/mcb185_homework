import sys
import math

numbers = []
for arg in sys.argv[1:]:
    f = float(arg)
    numbers.append(f)

# Numbers of value
count = len(numbers)
print(f"number of values:{count}")

# Minium and Maximum values
min = numbers[0]
for number in numbers:
    if number <= min:
        min = number

print(f"minium values:{min}")
max = numbers[0]
for number in numbers:
    if number >= max:
        max = number
print(f"maxmium values:{max}")

# Mean and Standard deviation
total = 0
for number in numbers:
    total += number
mean = total / count
print(f"Mean:{mean}")

variance = 0
for number in numbers:
    variance += (number - mean)**2 / count
std_d = math.sqrt(variance)
print(f"Standard deviation:{std_d:.3f}")

# Median Value
numbers.sort()
if count % 2 == 1:
    median = numbers[count // 2]
else:
    high = numbers[count // 2]
    low = numbers[count // 2 - 1]
    median = (high + low) / 2
print(f"Median:{median}")