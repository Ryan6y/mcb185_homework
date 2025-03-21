import sys
import mcb185

kd_scale = {
    'I': 4.5, 'V': 4.2, 'L': 3.8, 'F': 2.8, 'C': 2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P': -1.6,
    'H': -3.2, 'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_score(peptide):
    if len(peptide) == 0:
        return 0
    return sum(kd_scale.get(aa, 0) for aa in peptide) / len(peptide)

def has_signal_peptide(prot, window=8, threshold=2.5):
    if len(prot) < 30:
        return False
    for i in range(30 - window + 1):
        segment = prot[i:i+window]
        if 'P' not in segment and kd_score(segment) >= threshold:
            return True
    return False

def has_transmembrane_region(prot, window=11, threshold=2.0):
    if len(prot) < 30 + window:
        return False
    for i in range(30, len(prot) - window + 1):
        segment = prot[i:i+window]
        if 'P' not in segment and kd_score(segment) >= threshold:
            return True
    return False

for defline, prot in mcb185.read_fasta(sys.argv[1]):
        prot = prot.strip().upper()
        if has_signal_peptide(prot) and has_transmembrane_region(prot):
            print(defline)