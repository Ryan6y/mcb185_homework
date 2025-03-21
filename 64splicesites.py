import sys
import gzip
import mcb185
import sequence

def parse_gff(gff_file, sequences):
    donor_pwm = [[0, 0, 0, 0] for _ in range(6)]  # -2 to +3
    acceptor_pwm = [[0, 0, 0, 0] for _ in range(7)]  # -4 to +2
    splice_count = 0
    
    opener = gzip.open if gff_file.endswith('.gz') else open
    mode = 'rt' if gff_file.endswith('.gz') else 'r'
    with opener(gff_file, mode) as fp:
        for line in fp:
            if line.startswith('#') or not line.strip():
                continue
            fields = line.strip().split('\t')
            if len(fields) < 9 or fields[2] != 'intron' or fields[1] != 'RNASeq_splice':
                continue
            
            seqid = fields[0]
            if seqid not in sequences:
                print(f"Warning: Sequence ID {seqid} not found in FASTA")
                continue
            
            sequence = sequences[seqid]
            start = int(fields[3]) - 1  # 0-based
            end = int(fields[4]) - 1    # 0-based, inclusive
            strand = fields[6]
            splice_count += 1
            
            if strand == '+':
                donor_start = start - 2
                donor_seq = sequence[donor_start:donor_start + 6] if donor_start >= 0 and donor_start + 6 <= len(sequence) else ''
                acceptor_start = end - 4
                acceptor_seq = sequence[acceptor_start:acceptor_start + 7] if acceptor_start >= 0 and acceptor_start + 7 <= len(sequence) else ''
                print(f"{seqid} Forward: Donor at {start+1}: {donor_seq}, Acceptor at {end+1}: {acceptor_seq}")
            
            elif strand == '-':
                donor_start = end - 3
                donor_seq = sequence.revcomp(sequence[donor_start:donor_start + 6]) if donor_start >= 0 and donor_start + 6 <= len(sequence) else ''
                acceptor_start = start - 2
                acceptor_seq = sequence.revcomp(sequence[acceptor_start:acceptor_start + 7]) if acceptor_start >= 0 and acceptor_start + 7 <= len(sequence) else ''
                print(f"{seqid} Reverse: Donor at {end+1}: {donor_seq}, Acceptor at {start+1}: {acceptor_seq}")
            
            else:
                continue
            
            if len(donor_seq) == 6:
                for i, base in enumerate(donor_seq):
                    if base == 'A':
                        donor_pwm[i][0] += 1
                    elif base == 'C':
                        donor_pwm[i][1] += 1
                    elif base == 'G':
                        donor_pwm[i][2] += 1
                    elif base == 'T':
                        donor_pwm[i][3] += 1
            
            if len(acceptor_seq) == 7:
                for i, base in enumerate(acceptor_seq):
                    if base == 'A':
                        acceptor_pwm[i][0] += 1
                    elif base == 'C':
                        acceptor_pwm[i][1] += 1
                    elif base == 'G':
                        acceptor_pwm[i][2] += 1
                    elif base == 'T':
                        acceptor_pwm[i][3] += 1
    
    print(f"Found {splice_count} RNASeq_splice introns")
    return donor_pwm, acceptor_pwm

def print_transfac(donor_pwm, acceptor_pwm):
    print("AC DEMO1")
    print("XX")
    print("ID ACC")
    print("XX")
    print("DE splice acceptor")
    print("PO      A       C       G       T")
    for i, counts in enumerate(acceptor_pwm, 1):
        a, c, g, t = counts
        print(f"{i:<8}{a:<8}{c:<8}{g:<8}{t:<8}")
    print("XX")
    print("//")
    
    print("AC DEMO2")
    print("XX")
    print("ID DON")
    print("XX")
    print("DE splice donor")
    print("PO      A       C       G       T")
    for i, counts in enumerate(donor_pwm, 1):
        a, c, g, t = counts
        print(f"{i:<8}{a:<8}{c:<8}{g:<8}{t:<8}")
    print("XX")
    print("//")

# Check command-line arguments
if len(sys.argv) != 3:
    print("Usage: python3 64splicesites.py <fasta_file> <gff_file>")
    sys.exit(1)

fasta_file = sys.argv[1]
gff_file = sys.argv[2]

# Validate FASTA file
if not fasta_file.endswith(('.fa', '.fasta', '.fa.gz', '.fasta.gz')):
    print(f"Error: {fasta_file} does not appear to be a FASTA file")
    sys.exit(1)

# Load all sequences from FASTA into a dictionary
sequences = {}
try:
    for name, seq in mcb185.read_fasta(fasta_file):
        if name is None:
            print(f"Error: Failed to parse FASTA file {fasta_file}")
            sys.exit(1)
        chrom = name.split()[0]  # Take first word of defline
        sequences[chrom] = seq.upper()
        print(f"Loaded {chrom} with length {len(seq)}")
except Exception as e:
    print(f"Error reading FASTA file {fasta_file}: {e}")
    sys.exit(1)

if not sequences:
    print(f"Error: No sequences loaded from {fasta_file}")
    sys.exit(1)

donor_pwm, acceptor_pwm = parse_gff(gff_file, sequences)
print_transfac(donor_pwm, acceptor_pwm)