import pandas as pd
import re
import os

def classify_acr(input_csv, output_csv):
    """
    Klassifiziert Anti-CRISPR-Proteine und fügt die Typen hinzu.
    """
    if not os.path.exists(input_csv):
        print(f"❌ Datei {input_csv} nicht gefunden.")
        return

    df = pd.read_csv(input_csv)

    # Klassifiziere Anti-CRISPR-Proteine
    df["acr_type"] = "unknown"
    df["is_acr"] = 0
    for i, row in df.iterrows():
        desc = row["description"].lower()
        if "anti-crispr" in desc:
            df.at[i, "is_acr"] = 1
            type_match = re.search(r"type[- ]([IVX]+)", desc)
            if type_match:
                df.at[i, "acr_type"] = f"Type {type_match.group(1)}"

    df.to_csv(output_csv, index=False)
    print(f"✅ Klassifizierte CSV-Datei gespeichert: {output_csv}")
    print(f"📊 Anzahl der Anti-CRISPR-Proteine: {df['is_acr'].sum()}")

# Beispielaufruf
if __name__ == "__main__":
    input_csv = "/Users/maxi/Desktop/Hauptordner/Multiclass Classification of Anti-CRISPR Proteins/data/processed/combined_sequences.csv"  # Pfad zur Eingabe-CSV-Datei
    output_csv = "/Users/maxi/Desktop/Hauptordner/Multiclass Classification of Anti-CRISPR Proteins/data/processed/combined_sequences_classified.csv"  # Zielpfad für die klassifizierte CSV-Datei
    classify_acr(input_csv, output_csv)