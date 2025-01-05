from Bio import SeqIO
import pandas as pd
import os

def fasta_to_csv(fasta_file, output_csv):
    """
    Konvertiert eine FASTA-Datei in eine CSV-Datei.
    """
    if not os.path.exists(fasta_file):
        print(f"❌ Datei {fasta_file} nicht gefunden.")
        return

    sequences = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequences.append({
            "id": record.id,
            "description": record.description,
            "sequence": str(record.seq),
            "length": len(record.seq)
        })

    df = pd.DataFrame(sequences)
    df.to_csv(output_csv, index=False)
    print(f"✅ CSV-Datei gespeichert: {output_csv}")

# Beispielaufruf
if __name__ == "__main__":
    fasta_file = "example.fasta"  # Pfad zur FASTA-Datei
    output_csv = "example.csv"  # Zielpfad für die CSV-Datei
    fasta_to_csv(fasta_file, output_csv)