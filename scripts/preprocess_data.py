
def preprocess_ppin(ppin_file, output_file):
    """Preprocess the PPIN file for training."""
    ppin = load_ppin(ppin_file)
    with open(output_file, 'w') as f:
        for node, neighbors in ppin.items():
            f.write(f"{node}: {', '.join(neighbors)}\n")
