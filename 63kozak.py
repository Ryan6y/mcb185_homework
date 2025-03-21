import sys
import re
import gzip
import sequence

def parse_genbank(filepath):
    pwm = [[0, 0, 0, 0] for _ in range(15)]  
    sequence_data = ''
    cds_starts = []
    
    opener = gzip.open if filepath.endswith('.gz') else open
    mode = 'rt' if filepath.endswith('.gz') else 'r'
    
    with opener(filepath, mode) as fp:
        in_origin = False
        
        for line in fp:
            line = line.rstrip()
            if line.startswith('     CDS'):
                match = re.search(r'(\d+)\.\.', line)
                if match and 'complement' not in line:
                    cds_start = int(match.group(1)) - 1  
                    cds_starts.append(cds_start)
            elif line.startswith('ORIGIN'):
                in_origin = True
                sequence_data = ''
                continue
            elif line.startswith('//') and in_origin:
                in_origin = False
                sequence_data = sequence_data.upper()
                print(f"Sequence length: {len(sequence_data)}, CDS starts: {len(cds_starts)}")
                gc = sequence.gc_comp(sequence_data)
                print(f"GC composition: {gc:.2%}")
                
                for i, cds_start in enumerate(cds_starts[:5]):
                    if cds_start >= 7 and cds_start + 8 <= len(sequence_data):
                        kozak_seq = sequence_data[cds_start-7:cds_start+8]
                        print(f"CDS {i+1} at {cds_start+1}: {kozak_seq} (ATG at {kozak_seq[9:12]})")
                        if len(kozak_seq) == 15:  
                            for j, base in enumerate(kozak_seq):
                                if base == 'A':
                                    pwm[j][0] += 1
                                elif base == 'C':
                                    pwm[j][1] += 1
                                elif base == 'G':
                                    pwm[j][2] += 1
                                elif base == 'T':
                                    pwm[j][3] += 1
            elif in_origin:
                sequence_data += ''.join(c for c in line if c in 'acgtACGT')
    
    return pwm

def print_transfac(pwm):
    print("AC IMTSU001")
    print("XX")
    print("ID ECKOZ")
    print("XX")
    print("DE E.coli Kozak consensus PWM")
    print("PO      A       C       G       T")
    for i, counts in enumerate(pwm, 1):
        a, c, g, t = counts
        print(f"{i:<8}{a:<8}{c:<8}{g:<8}{t:<8}")
    print("XX")

filepath = sys.argv[1]
pwm = parse_genbank(filepath)
print_transfac(pwm)