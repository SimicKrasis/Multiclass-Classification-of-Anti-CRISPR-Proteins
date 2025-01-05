import pandas as pd

# Lade die Daten
df = pd.read_csv("/Users/maxi/Desktop/Hauptordner/Multiclass Classification of Anti-CRISPR Proteins/data/processed/numerical_features.csv")

# Labels vereinfachen
df['acr_type'] = df['acr_type'].apply(lambda x: 'I' if x.startswith('I-') else 'II' if x.startswith('II-') else None)

# Entferne alle anderen Klassen (z. B. III, V-A, etc.)
df = df[df['acr_type'].notnull()]

# Speichere die vereinfachten Daten
df.to_csv("/Users/maxi/Desktop/Hauptordner/Multiclass Classification of Anti-CRISPR Proteins/data/processed/simplified_numerical_features.csv", index=False)
# Features und Labels
X = df.drop(columns=['acr_type'])  # Alle Spalten außer 'acr_type'
y = df['acr_type']  # Zielvariable
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)