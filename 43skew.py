import sequence
import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
    seq = ''.join(line.strip() for line in fp)

w = 5000
c = seq.count('C')
g = seq.count('G')
for i in range(len(seq) -w +1):
   s = seq[i:i+w]

print(i, sequence.gc_comp(s), sequence.gc_skew(s), g, c)

