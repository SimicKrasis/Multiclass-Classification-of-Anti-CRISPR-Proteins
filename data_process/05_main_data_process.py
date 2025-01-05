import os
from entpacken import extract_gz_file
from fasta_to_csv import fasta_to_csv
from filter import filter_csv
from acr_classification import classify_acr

# 1. Entpacken der .gz-Datei
gz_file = "uniprotkb_Anti_CRISPR_protein_AcrIIA4_2025_01_02.fasta.gz"
fasta_file = "anti_crispr_proteins.fasta"
extract_gz_file(gz_file, fasta_file)

# 2. Konvertieren der FASTA-Datei in eine CSV-Datei
csv_file = "anti_crispr_proteins.csv"
fasta_to_csv(fasta_file, csv_file)

# 3. Filtern der CSV-Daten
filtered_csv = "filtered_anti_crispr_proteins.csv"
filter_csv(csv_file, filtered_csv, min_length=10)

# 4. Klassifizieren der Anti-CRISPR-Proteine
classified_csv = "classified_anti_crispr_proteins.csv"
classify_acr(filtered_csv, classified_csv)

print("✅ Workflow abgeschlossen!")