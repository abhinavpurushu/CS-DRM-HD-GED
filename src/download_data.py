"""Download and extract the UCI Gene Expression Cancer RNA-Seq (TCGA PANCAN) dataset."""

from pathlib import Path
import urllib.request
import zipfile
import tarfile


def main():
    url = "https://archive.ics.uci.edu/static/public/401/gene+expression+cancer+rna+seq.zip"

    zip_name = "gene_expression_cancer_rna_seq.zip"
    tar_name = "TCGA-PANCAN-HiSeq-801x20531.tar.gz"

    # Project directories
    project_root = Path(__file__).resolve().parents[1]

    raw_dir = project_root / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    zip_file = raw_dir / zip_name
    tar_file = raw_dir / tar_name
    data_file = raw_dir / "data.csv"
    labels_file = raw_dir / "labels.csv"

    # Download the file
    if not zip_file.exists():
        urllib.request.urlretrieve(url, zip_file)
        print("Download complete.")
    else:
        print("ZIP file already exists. Skipping download.")

    # Extract ZIP
    if not tar_file.exists():
        print("Extracting ZIP")
        with zipfile.ZipFile(zip_file, "r") as z:
            z.extractall(raw_dir)
    else:
        print("TAR archive already exists. Skipping ZIP extraction.")

    # Extract TAR.GZ
    if not (data_file.exists() and labels_file.exists()):
        print("Extracting TAR.GZ")
        with tarfile.open(tar_file, "r:gz") as tar:
            tar.extractall(raw_dir)
    else:
        print("Dataset already extracted.")

    print("Dataset setup is complete.")


if __name__ == "__main__":
    main()



