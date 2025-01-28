# Function to find the DNA complement
def dna_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}  # Mapping of DNA bases
    complement_sequence = ''.join([complement[base] for base in sequence.upper()])
    return complement_sequence

# Main program
def main():
    print("Welcome to the DNA Complement Calculator!")
    dna_sequence = input("Enter the DNA sequence (e.g., ATGC): ").strip().upper()

    # Validate input (ensure only A, T, C, G are used)
    valid_bases = {'A', 'T', 'C', 'G'}
    if not all(base in valid_bases for base in dna_sequence):
        print("Invalid DNA sequence! Please only use A, T, C, or G.")
        return

    # Calculate and display the complement
    complement = dna_complement(dna_sequence)
    print(f"The complement of the DNA sequence '{dna_sequence}' is: {complement}")

# Run the program
if __name__ == "__main__":
    main()
