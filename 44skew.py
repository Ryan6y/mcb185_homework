import sys
import gzip

g = 0
c = 0
w = 5000 #windowsize

with gzip.open(sys.argv[1],'rt') as fp:
    seq = ''.join(line.strip() for line in fp)

#first window
initial_gc=seq[:w]
g = initial_gc.upper().count('G')
c = initial_gc.upper().count('C')

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

print(i, f'skew = {(g - c) / (g + c)}', g, c)
