
# GRL Project

This project implements graph-based methods for protein-protein interaction network (PPIN) analysis, including models such as GCN and GVP.

## Features

- Construct PPIN from input datasets.
- Extract embeddings using ESM and 3D structure data.
- Baseline implementation of GCN.
- Advanced implementation of GVP.

## Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Download the required datasets to the `data/` directory as per the notebook instructions.
2. Run the main notebook or the individual scripts in the `scripts/` directory for specific tasks.

## Repository Structure

- `src/`: Source code for PPIN construction, embedding extraction, and models.
- `notebooks/`: Jupyter notebooks for experimentation.
- `tests/`: Unit tests for project components.
- `data/`: Placeholder for datasets.
- `results/`: Placeholder for generated results.
- `scripts/`: Scripts for preprocessing, training, and evaluation.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
