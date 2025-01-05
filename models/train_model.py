import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

def load_data(file_path):
    """Load and prepare the data."""
    df = pd.read_csv(file_path)
    X = df.drop(columns=['acr_type'])
    y = df['acr_type']
    return X, y

def train_and_evaluate_model(X, y):
    """Train the model and evaluate its performance."""
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Initialize and train the model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight='balanced'
    )
    model.fit(X_train_scaled, y_train)

    # Make predictions
    y_pred = model.predict(X_test_scaled)

    # Calculate cross-validation score
    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)

    return model, scaler, y_test, y_pred, cv_scores

def plot_confusion_matrix(y_test, y_pred, save_path='confusion_matrix.png'):
    """Plot and save the confusion matrix."""
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Type I', 'Type II'],
                yticklabels=['Type I', 'Type II'])
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def save_model(model, scaler, model_path='acr_classifier_model.joblib', 
               scaler_path='acr_classifier_scaler.joblib'):
    """Save the model and scaler."""
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)

def main():
    # File paths
    input_file = '/Users/maxi/Desktop/Hauptordner/Multiclass Classification of Anti-CRISPR Proteins/data/processed/simplified_numerical_features.csv'

    # Load data
    print("Loading data...")
    X, y = load_data(input_file)

    # Train and evaluate model
    print("Training model...")
    model, scaler, y_test, y_pred, cv_scores = train_and_evaluate_model(X, y)

    # Print results
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print("\nCross-validation scores:", cv_scores)
    print("Average CV score:", cv_scores.mean())

    # Plot confusion matrix
    print("\nGenerating confusion matrix...")
    plot_confusion_matrix(y_test, y_pred)

    # Save model and scaler
    print("\nSaving model and scaler...")
    save_model(model, scaler)

    print("\nTraining complete! Model and scaler have been saved.")

if __name__ == "__main__":
    main()