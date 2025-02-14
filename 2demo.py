import random
import math

def dis(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)** 2 + (y1 - y2)** 2) 

inside = 0
outside = 0

for i in range(100000000):
    x = random.random()
    y = random.random()
    d = dis(0, 0, x, y)

    if d <= 1:
        inside += 1
    else:
        outside += 1
    p = (inside/(inside+outside)*4)
    
print(p)
