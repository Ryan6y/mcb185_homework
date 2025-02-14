import random
import math

def dis(x1, y1, x2, y2):
    d = math.sqrt((x1 - x2)** 2 + (y1 - y2)** 2)
    return d 

inside = 0
outside = 0

for i in range(100000):
    x = random.random()
    y = random.random()
    d = dis(0, 0, x, y)

    if d <= 1:
        inside += 1
    else:
        outside += 1

    print(inside/(outside+inside)*4)