import math

vals = [7, 6, 5, 4, 3, 2, 1]

def entropy(probs):
    h = 0
    for p in probs:
        h -= p * math.log2(p)
    return h
print(entropy([0.2, 0.3, 0.5]))

print(vals[1:])
print(min(vals))