import random

seq = []

for i in range(1000):
    nt = random.choice('ACGT')
    seq.append(nt)

dna = '-' . join(seq)

print(dna)