import gzip
import argparse

parser = argparse.ArgumentParser(
    description="variant reporter",
    usage="66variants.py [-h] gff vcf"
)
parser.add_argument("gff", help="GFF file")
parser.add_argument("vcf", help="VCF file")
args = parser.parse_args()

def parse_gff(gff_file):
    """Parse GFF file into a list of features: (chrom, start, end, type)."""
    features = []
    opener = gzip.open if gff_file.endswith('.gz') else open
    mode = 'rt' if gff_file.endswith('.gz') else 'r'
    with opener(gff_file, mode) as fp:
        for line in fp:
            if line.startswith('#') or not line.strip():
                continue
            fields = line.strip().split('\t')
            if len(fields) < 9:
                continue
            chrom = fields[0]
            feat_type = fields[2]
            start = int(fields[3]) - 1  
            end = int(fields[4])        
            features.append((chrom, start, end, feat_type))
    return features

def parse_vcf(vcf_file):
    """Parse VCF file into a list of variants: (chrom, pos)."""
    variants = []
    opener = gzip.open if vcf_file.endswith('.gz') else open
    mode = 'rt' if vcf_file.endswith('.gz') else 'r'
    with opener(vcf_file, mode) as fp:
        for line in fp:
            if line.startswith('#'):
                continue
            fields = line.strip().split('\t')
            if len(fields) < 2:
                continue
            chrom = fields[0]
            pos = int(fields[1]) - 1 
            variants.append((chrom, pos))
    return variants

def compare_features(features, variants):
    """Compare variants to features and print overlapping types."""
    for v_chr, v_pos in variants:
        overlapping_types = set()
        for f_chr, f_start, f_end, f_type in features:
            if f_chr == v_chr and f_start <= v_pos <= f_end:
                overlapping_types.add(f_type)
        if overlapping_types:
            types_str = ','.join(sorted(overlapping_types))
            print(f"{v_chr}\t{v_pos + 1}\t{types_str}")

features = parse_gff(args.gff)
variants = parse_vcf(args.vcf)
compare_features(features, variants)