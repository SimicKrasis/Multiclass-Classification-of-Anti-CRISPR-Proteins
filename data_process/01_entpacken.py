import gzip
import shutil
import os

def extract_gz_file(gz_file, output_file):
    """
    Entpackt eine .gz-Datei und speichert den Inhalt in einer neuen Datei.
    """
    if not os.path.exists(gz_file):
        print(f"❌ Datei {gz_file} nicht gefunden.")
        return

    with gzip.open(gz_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"✅ Datei entpackt: {output_file}")

# Beispielaufruf
if __name__ == "__main__":
    gz_file = "example.fasta.gz"  # Pfad zur .gz-Datei
    output_file = "example.fasta"  # Zielpfad für die entpackte Datei
    extract_gz_file(gz_file, output_file)