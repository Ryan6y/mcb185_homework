import sys
import mcb185

k = 1
while True:
    k += 1
    kset = set()
    for defline, seq in mcb185.read_fasta(sys.argv[1]):
        for i in range(len(seq) -k +1):
            kset.add(seq[i : i + k])
    if len(kset) < (4 ** k):
            break
print(k)
print(len(kset))