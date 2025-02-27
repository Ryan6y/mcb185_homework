import sys
import gzip

filepath = sys.argv[1]

exons= 0
total = 0

with gzip.open(filepath, 'rt') as fp:
    for line in fp:
        f = line.split()
        beg = int(f[3])
        end = int(f[4])
        total += end - beg + 1
        exons += 1
print(total/exons)