import pandas as pd
import os

def filter_csv(input_csv, output_csv, min_length=10):
    """
    Filtert eine CSV-Datei basierend auf der Mindestlänge und entfernt Duplikate.
    """
    if not os.path.exists(input_csv):
        print(f"❌ Datei {input_csv} nicht gefunden.")
        return

    df = pd.read_csv(input_csv)

    # Entferne Duplikate
    df = df.drop_duplicates(subset="sequence")

    # Filtere nach Mindestlänge
    df = df[df["length"] >= min_length]

    df.to_csv(output_csv, index=False)
    print(f"✅ Gefilterte CSV-Datei gespeichert: {output_csv}")
    print(f"📊 Anzahl der Sequenzen nach Filterung: {len(df)}")

# Beispielaufruf
if __name__ == "__main__":
    input_csv = "example.csv"  # Pfad zur Eingabe-CSV-Datei
    output_csv = "filtered_example.csv"  # Zielpfad für die gefilterte CSV-Datei
    filter_csv(input_csv, output_csv, min_length=10)