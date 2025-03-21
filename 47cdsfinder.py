import sys
import mcb185
import sequence

min_length = int(sys.argv[2])
orf_counter = 0  

def find_orfs(prot, defline_prefix):
    global orf_counter
    i = 0
    while i < len(prot):
        if prot[i] == 'M':  
            j = i

            while j < len(prot) and prot[j] != '*':  
                j += 1
            
            if j < len(prot) and prot[j] == '*':
                orf = prot[i:j+1]  
                if len(orf) >= min_length:
                    orf_counter += 1
                    print(f">{defline_prefix}-prot-{orf_counter}")
                    print(orf)
            i = j + 1  
        else:
            i += 1


for defline, seq in mcb185.read_fasta(sys.argv[1]):
    seq = seq.upper().strip()  
    defline_prefix = defline.split()[0]  
    for frame in range(3):
        prot = mcb185.translate(seq[frame:])  
        find_orfs(prot, defline_prefix)
    
    rev_seq = sequence.revcomp(seq)
    for frame in range(3):
        prot = mcb185.translate(rev_seq[frame:])
        find_orfs(prot, defline_prefix)