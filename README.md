# Comparative Evaluation of Dimension Reduction Methods for High-Dimensional Gene Expression Data

This repository contains the implementation and experimental workflow for a comparative study of dimension reduction methods on high-dimensional gene expression data. The study evaluates:

- Principal Component Analysis (**PCA**)
- Kernel PCA (**Polynomial** and **RBF** kernels)
- Gaussian Random Projection (**GRP**)
- Sparse Random Projection (**SRP**)

for multiclass cancer classification using the **TCGA Pan-Cancer RNA-Seq dataset**.

---

## Repository Structure

```text
.
├── data
│   ├── raw/          # Downloaded dataset
│   └── processed/    # Preprocessed dataset
├── figures
│   ├── comparison/
│   ├── eda/
│   ├── pca/
│   └── kpca/
├── manuscript/       # Internship report and related material
├── notebooks/        # Experiment notebooks
├── results
│   ├── metrics/
│   └── timings/
└── src/              # Python source files (scripts/utilities)
```

---

## Dataset

The dataset is **not included** in this repository due to GitHub file size limits.

To prepare data:

1. Run the dataset download script from `src/`.
2. The dataset will be saved to `data/raw/`.
3. Run the first preprocessing notebook to generate files in `data/processed/`.

---

## Requirements

Use Python **3.9+** (recommended). Install dependencies before running notebooks/scripts.

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available yet, create one from your environment:

```bash
pip freeze > requirements.txt
```

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/abhinavpurushu/CS-DRM-HD-GED.git
cd CS-DRM-HD-GED
```

2. Install required packages.

3. Run the dataset download script in `src/`.

4. Execute notebooks in sequence (recommended order):
   - Data preprocessing notebook
   - EDA notebook
   - PCA/KPCA/GRP/SRP experiment notebooks
   - Comparison and final results notebook

5. Check generated outputs in:
   - `results/metrics/`
   - `results/timings/`
   - `figures/`

---

## Outputs

This project generates:

- Classification performance metrics
- Computational timing results
- Reconstruction analysis
- Representation quality analysis
- Publication-quality figures
- Tables used in the internship report

---

## Reproducibility Notes

To improve reproducibility, keep track of:

- Python version
- Library versions (NumPy, pandas, scikit-learn, matplotlib, seaborn, etc.)
- Random seeds used in experiments
- Notebook execution order

---

## Report

The complete internship report is available in the **`manuscript/`** directory.

---

## Author

**Abhinav P**  
First-year M.Sc. Statistics student  
Department of Statistics & Applied Mathematics  
Central University of Tamil Nadu

Internship conducted at:

**Bioinformatics, Artificial Intelligence and Data Analytics (BAIDA) Research Group**  
Big Data & Biocomputing Laboratory (BDB Lab)  
Department of Computer Science & Engineering  
National Institute of Technology Calicut
