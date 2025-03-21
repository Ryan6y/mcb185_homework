import sys
import mcb185
import math

def entropy(seq):
    nts = []
    counts = []
    for nt in seq:
        if nt not in nts:
            nts.append(nt)
            counts.append(0)
        idx = nts.index(nt)
        counts[idx] += 1
    
    ent = 0.0
    for count in counts:
        p = count / len(seq)
        ent = ent - (p * math.log(p, 2))
    return ent

window_size = int(sys.argv[2])
threshold = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    seq = seq.upper()
    mask = [0] * len(seq)  
    for i in range(0, len(seq) - window_size + 1):
        window = seq[i:i + window_size]
        if entropy(window) < threshold:
            for j in range(i, i + window_size):
                mask[j] = 1
    
    masked_seq = ''
    for i in range(len(seq)):
        if mask[i] == 1:
            masked_seq = masked_seq + 'N'
        else:
            masked_seq = masked_seq + seq[i]
    
    print('>' + defline)
    for i in range(0, len(masked_seq), 60):
        print(masked_seq[i:i + 60])