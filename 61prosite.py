import sys
import re
import mcb185


fasta_file = sys.argv[1]

# Define PROSITE patterns as regex
p_atpase_pattern = 'DKTGT[LIVM][TI]'  # D-K-T-G-T-[LIVM]-[TI]
zinc_finger_pattern = 'C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H'  # C-x(2,4)-C-x(3)-[LIVMFYWC]-x(8)-H-x(3,5)-H

# Iterate through FASTA file
for defline, seq in mcb185.read_fasta(fasta_file):
    # Check for P-type ATPase pattern
    if re.search(p_atpase_pattern, seq):
        print(f"{defline} [P-type ATPase]")
    
    # Check for C2H2 zinc-finger pattern
    if re.search(zinc_finger_pattern, seq):
        print(f"{defline} [C2H2 Zinc Finger]")
