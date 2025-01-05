import pandas as pd

# Liste der Aminosäuren
AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"

# Funktion zur Berechnung der Features
def extract_features(sequence):
    features = {}
    # Länge der Sequenz
    features["length"] = len(sequence)
    # Anteil hydrophober Aminosäuren
    hydrophobic = "AILMFVW"
    features["hydrophobic_ratio"] = sum(sequence.count(aa) for aa in hydrophobic) / len(sequence)
    # Anteil polarer Aminosäuren
    polar = "STYNQ"
    features["polar_ratio"] = sum(sequence.count(aa) for aa in polar) / len(sequence)
    # Anteil jeder einzelnen Aminosäure
    for aa in AMINO_ACIDS:
        features[f"aa_{aa}"] = sequence.count(aa) / len(sequence)
    return features

# Hauptfunktion
def main(input_csv, output_csv):
    # Lese die CSV-Datei
    df = pd.read_csv(input_csv)

    # Extrahiere Features für jede Sequenz
    feature_list = []
    for _, row in df.iterrows():
        sequence = row["sequence"]
        features = extract_features(sequence)
        features["acr_type"] = row["acr_type"]  # Zielvariable hinzufügen
        feature_list.append(features)

    # Erstelle ein DataFrame mit den Features
    feature_df = pd.DataFrame(feature_list)

    # Speichere die Features in einer neuen CSV-Datei
    feature_df.to_csv(output_csv, index=False)
    print(f"Features wurden in '{output_csv}' gespeichert.")

# Aufruf der Hauptfunktion
if __name__ == "__main__":
    input_csv = "/Users/maxi/Desktop/Hauptordner/Multiclass Classification of Anti-CRISPR Proteins/data/processed/combined_sequences_classified.csv"  # Eingabedatei
    output_csv = "/Users/maxi/Desktop/Hauptordner/Multiclass Classification of Anti-CRISPR Proteins/data/processed/combined_sequences_classified_numerical.csv"   # Ausgabedatei
    main(input_csv, output_csv)