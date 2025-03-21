import sys
import mcb185
import sequence

def process_frame(seq, frame, min_len):
    results = []
    L = len(seq)
    stop_codons = {"TAA", "TAG", "TGA"}
    i = frame
    while i <= L - 3:
        codon = seq[i:i+3]
        if codon == "ATG":
            start = i
            j = i
            found_stop = False
            while j <= L - 3:
                curr_codon = seq[j:j+3]
                if curr_codon in stop_codons:
                    found_stop = True
                    break
                j += 3
            if found_stop:
                end = j + 3  
                if end - start >= min_len:
                    results.append((start, end))
                i = j + 3
            else:
                break
        else:
            i += 3
    return results

def convert_minus_coords(r_start, r_end, L):
    original_start = L - r_end + 1
    original_end   = L - r_start
    return (original_start, original_end)

min_len = int(sys.argv[2])
gene_id = 1

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    seq = seq.upper().strip()
    seqid = defline.split()[0] 
    L = len(seq)
    
    for frame in range(3):
        orfs = process_frame(seq, frame, min_len)
        for start, end in orfs:
            gff_start = start + 1
            gff_end = end
            print(f"{seqid}\t55genefinder\tCDS\t{gff_start}\t{gff_end}\t.\t+\t0\tID=gene{gene_id}")
            gene_id += 1

    rev = sequence.revcomp(seq)
    for frame in range(3):
        orfs_rev = process_frame(rev, frame, min_len)
        for r_start, r_end in orfs_rev:
            original_start, original_end = convert_minus_coords(r_start, r_end, L)
            if original_start > original_end:
                original_start, original_end = original_end, original_start
            print(f"{seqid}\t55genefinder\tCDS\t{original_start}\t{original_end}\t.\t-\t0\tID=gene{gene_id}")
            gene_id += 1
