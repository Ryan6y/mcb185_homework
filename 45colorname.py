import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

with open(colorfile) as fp:
    for line in fp:
        print(line)