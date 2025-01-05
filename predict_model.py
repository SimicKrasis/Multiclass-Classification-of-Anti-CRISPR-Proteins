import pandas as pd
import joblib
import os

def apply_model(input_csv, output_csv, model_path, scaler_path):
    """
    Wendet ein trainiertes Modell auf neue Daten an und speichert die Vorhersagen.
    """
    # Überprüfe, ob alle Dateien existieren
    for file_path in [input_csv, model_path, scaler_path]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Die Datei {file_path} wurde nicht gefunden!")

    # 1. Neue Daten laden
    print("📂 Lade neue Daten...")
    data = pd.read_csv(input_csv)

    # Zeige Information über die geladenen Daten
    print(f"Anzahl der zu klassifizierenden Sequenzen: {len(data)}")
    print(f"Verfügbare Spalten: {', '.join(data.columns)}")

    # Trenne Features von der Zielvariable
    feature_columns = [col for col in data.columns if col != 'acr_type']
    X_new = data[feature_columns]

    # 2. Scaler laden und Daten skalieren
    print("🔄 Skaliere die Daten...")
    scaler = joblib.load(scaler_path)
    X_new_scaled = scaler.transform(X_new)  # Skaliere nur die Features

    # 3. Modell laden und Vorhersagen treffen
    print("🤖 Lade Modell und treffe Vorhersagen...")
    model = joblib.load(model_path)
    predictions = model.predict(X_new_scaled)  # Vorhersagen für die neuen Daten

    # Zeige Verteilung der Vorhersagen
    unique_predictions = pd.Series(predictions).value_counts()
    print("\nVerteilung der Vorhersagen:")
    for pred_class, count in unique_predictions.items():
        print(f"Klasse {pred_class}: {count} Sequenzen")

    # 4. Ergebnisse speichern
    print("\n💾 Speichere die Vorhersagen...")
    data["predicted_type"] = predictions  # Füge die Vorhersagen zu den Daten hinzu
    data.to_csv(output_csv, index=False)
    print(f"✅ Vorhersagen gespeichert in: {output_csv}")

if __name__ == "__main__":
    # Definiere die Pfade
    base_dir = "/Users/maxi/Desktop/Hauptordner/Multiclass Classification of Anti-CRISPR Proteins"
    input_csv = os.path.join(base_dir, "data/processed/combined_sequences_classified_numerical.csv")
    output_csv = os.path.join(base_dir, "combined_sequences_classified_numerical_predict.csv")
    model_path = os.path.join(base_dir, "acr_classifier_model.joblib")
    scaler_path = os.path.join(base_dir, "acr_classifier_scaler.joblib")

    try:
        apply_model(input_csv, output_csv, model_path, scaler_path)
    except Exception as e:
        print(f"❌ Fehler: {str(e)}")