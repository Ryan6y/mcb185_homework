import sys
import sequence
import mcb185

g = 0
c = 0
w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    s = seq[:w]
g += s.count('G')
c += s.count('C')

for i in range(len(seq) - w + 1):
    base_out = seq[i - 1]
    base_in  = seq[i + w - 1]
    if   base_in == 'G':
        g += 1
    elif base_in == 'C':
        c += 1
    elif base_out == 'G':
        g -= 1
    elif base_out == 'C':
        c -= 1

skew = (g - c) / (g + c)

print(i,g,c, skew)
