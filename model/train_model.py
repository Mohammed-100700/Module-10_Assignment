"""
Train a simple classifier on the Heart Disease dataset and save to model/heart_model.joblib.
Run:
    python train_model.py
"""

import os
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib

CSV_PATH = os.environ.get("HEART_CSV", "heart.csv")

FEATURES = [
    "age","sex","cp","trestbps","chol","fbs","restecg",
    "thalach","exang","oldpeak","slope","ca","thal"
]
TARGET = "target"

def main():
    csv = Path(CSV_PATH)
    if not csv.exists():
        raise FileNotFoundError(
            f"Could not find dataset at {csv}. "
            "Place 'heart.csv' in project root or set HEART_CSV env var."
        )

    df = pd.read_csv(csv)
    df = df.dropna(subset=FEATURES + [TARGET])  # keep it simple

    X = df[FEATURES].astype(float).values
    y = df[TARGET].astype(int).values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000))
    ])

    pipe.fit(X_train, y_train)
    acc = accuracy_score(y_test, pipe.predict(X_test))
    print(f"Test Accuracy: {acc:.3f}")

    out = Path("model") / "heart_model.joblib"
    out.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipe, out)
    print(f"Saved model → {out}")

if __name__ == "__main__":
    main()