
def load_ppin(file_path):
    """Load PPIN from the given file."""
    ppin = {}
    with open(file_path, 'r') as f:
        for line in f:
            protein_a, protein_b, _ = line.strip().split()
            ppin.setdefault(protein_a, []).append(protein_b)
            ppin.setdefault(protein_b, []).append(protein_a)
    return ppin
