import sys
import argparse
import mcb185

parser = argparse.ArgumentParser(
    description="mRNA translator",
    usage="65translate.py [-h] [-m MIN] [-a] file"
)
parser.add_argument("file", help="fasta file of mRNAs")
parser.add_argument("-m", "--min", type=int, default=100, 
                    help="minimum protein length [100]")
parser.add_argument("-a", "--anti", action="store_true", 
                    help="also examine the anti-parallel strand")
args = parser.parse_args()

def translate_sequence(seq, min_len=100, anti=False):
    proteins = []

    protein = mcb185.translate(seq, frame=0)
    if protein.count('*') <= 1 and len(protein.rstrip('*')) >= min_len:
        proteins.append(protein.rstrip('*'))

    if anti:
        anti_seq = mcb185.anti_seq(seq)
        anti_protein = mcb185.translate(anti_seq, frame=0)
        if anti_protein.count('*') <= 1 and len(anti_protein.rstrip('*')) >= min_len:
            proteins.append(anti_protein.rstrip('*'))
    
    return proteins

def process_fasta(fasta_file, min_len=100, anti=False):
    """Process FASTA file and output translated proteins."""
    for name, seq in mcb185.read_fasta(fasta_file):
        proteins = translate_sequence(seq, min_len, anti)
        for i, protein in enumerate(proteins):
            strand_suffix = "_anti" if anti and i == 1 else ""
            print(f">{name}{strand_suffix}")
            print(protein)

