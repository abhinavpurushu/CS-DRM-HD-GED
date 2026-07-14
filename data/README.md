# Data

The dataset is not included in this repository because it is large and exceeds GitHub's file size limits.

## Raw Data

Run:

```bash
python src/download_data.py
```

This downloads and extracts the UCI Gene Expression Cancer RNA-Seq (TCGA PANCAN) dataset into `data/raw/`.

## Processed Data

After downloading the raw dataset, open and execute:

```text
notebooks/01_EDA&Preprocessing.ipynb
```

This generates the processed files in `data/processed/`:

- `X_processed.csv`
- `y_processed.csv`
