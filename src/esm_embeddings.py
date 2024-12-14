
from fairseq.models.esm import esm1b_t33_650M_UR50S

def extract_esm_embeddings(sequence):
    """Extract ESM embeddings for a protein sequence."""
    model, alphabet = esm1b_t33_650M_UR50S()
    batch_converter = alphabet.get_batch_converter()
    batch_labels, batch_strs, batch_tokens = batch_converter([(None, sequence)])
    with torch.no_grad():
        results = model(batch_tokens, repr_layers=[33], return_contacts=True)
    return results["representations"][33]
