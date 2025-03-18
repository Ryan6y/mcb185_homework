import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    counts = [0, 0, 0, 0, 0] # A, C, G, T, N
    for nt in seq:
        if   nt == 'A': A += 1
        elif nt == 'C': C += 1
        elif nt == 'G': G += 1
        elif nt == 'T': T += 1
        else:           N += 1
    print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))