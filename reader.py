import sys
import gzip

filepath = sys.argv[1]
fp = gzip.open(filepath, 'rt')
for line in fp:
    cols = line.split()
    print(cols[0])

